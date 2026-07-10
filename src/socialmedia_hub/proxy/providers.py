"""Proxy service providers integration."""

from __future__ import annotations

import logging
import time
from abc import ABC, abstractmethod
from typing import Any

import httpx

logger = logging.getLogger("socialmedia_hub.proxy.providers")


class ProxyProvider(ABC):
    """Abstract base class for proxy providers."""

    @abstractmethod
    def get_proxies(self, count: int = 10) -> list[dict[str, Any]]:
        """Get a list of proxies from the provider.

        Args:
            count: Number of proxies to fetch

        Returns:
            List of proxy dictionaries with host, port, username, password
        """
        pass

    @abstractmethod
    def report_proxy(self, proxy: dict[str, Any], success: bool) -> None:
        """Report proxy status back to provider.

        Args:
            proxy: Proxy that was used
            success: Whether the request was successful
        """
        pass


class KuaiDaiLiProvider(ProxyProvider):
    """快代理 (KuaiDaiLi) proxy provider.

    Website: https://www.kuaidaili.com/
    """

    def __init__(self, api_key: str) -> None:
        """Initialize KuaiDaiLi provider.

        Args:
            api_key: KuaiDaiLi API key
        """
        self.api_key = api_key
        self.base_url = "https://dps.kuaidaili.com/api/dps/get"

    def get_proxies(self, count: int = 10) -> list[dict[str, Any]]:
        """Get proxies from KuaiDaiLi."""
        try:
            with httpx.Client(timeout=10) as client:
                resp = client.get(
                    self.base_url,
                    params={
                        "api_key": self.api_key,
                        "num": count,
                        "pt": 1,  # 1=HTTP, 2=HTTPS, 3=SOCKS5
                        "sep": 1,  # 1=txt
                    },
                )

                if resp.status_code == 200:
                    proxies = []
                    for line in resp.text.strip().split("\n"):
                        if ":" in line:
                            host, port = line.split(":")
                            proxies.append({
                                "host": host,
                                "port": int(port),
                                "protocol": "http",
                            })
                    return proxies
                else:
                    logger.error(f"KuaiDaiLi API error: {resp.status_code}")
                    return []

        except Exception as e:
            logger.error(f"KuaiDaiLi request failed: {e}")
            return []

    def report_proxy(self, proxy: dict[str, Any], success: bool) -> None:
        """Report proxy status (not supported by KuaiDaiLi)."""
        pass


class ZhiMaProvider(ProxyProvider):
    """芝麻代理 (ZhiMa) proxy provider.

    Website: https://www.zhimaruanjian.com/
    """

    def __init__(self, api_key: str) -> None:
        """Initialize ZhiMa provider.

        Args:
            api_key: ZhiMa API key
        """
        self.api_key = api_key
        self.base_url = "https://api.zhimaruanjian.com/get"

    def get_proxies(self, count: int = 10) -> list[dict[str, Any]]:
        """Get proxies from ZhiMa."""
        try:
            with httpx.Client(timeout=10) as client:
                resp = client.get(
                    self.base_url,
                    params={
                        "api_key": self.api_key,
                        "num": count,
                        "type": "2",  # HTTP
                        "country": "cn",
                    },
                )

                if resp.status_code == 200:
                    data = resp.json()
                    proxies = []
                    for item in data.get("data", []):
                        proxies.append({
                            "host": item["ip"],
                            "port": item["port"],
                            "protocol": "http",
                        })
                    return proxies
                else:
                    logger.error(f"ZhiMa API error: {resp.status_code}")
                    return []

        except Exception as e:
            logger.error(f"ZhiMa request failed: {e}")
            return []

    def report_proxy(self, proxy: dict[str, Any], success: bool) -> None:
        """Report proxy status (not supported by ZhiMa)."""
        pass


class BrightDataProvider(ProxyProvider):
    """Bright Data (Luminati) residential proxy provider.

    Website: https://brightdata.com/
    """

    def __init__(self, api_key: str, zone: str = "residential") -> None:
        """Initialize Bright Data provider.

        Args:
            api_key: Bright Data API key
            zone: Proxy zone (residential, datacenter, etc.)
        """
        self.api_key = api_key
        self.zone = zone
        self.base_url = f"https://brd.superproxy.io:33335"

    def get_proxies(self, count: int = 10) -> list[dict[str, Any]]:
        """Get proxies from Bright Data (brd proxy format)."""
        # Bright Data uses a different approach - connection through their proxy server
        # Each request goes through their proxy, IP rotates automatically
        return [{
            "host": "brd.superproxy.io",
            "port": 33335,
            "protocol": "http",
            "username": f"brd-customer-{self.api_key}-zone-{self.zone}",
            "password": "brd_password",
        }]

    def report_proxy(self, proxy: dict[str, Any], success: bool) -> None:
        """Report proxy status."""
        pass


class FreeProxyProvider(ProxyProvider):
    """Free proxy provider with smart caching.

    Features:
    - Caches working proxies to file
    - Tests proxies before using
    - Auto-refreshes stale cache
    - Removes failed proxies
    """

    def __init__(self, cache_file: str = "free_proxies.json", cache_ttl: int = 3600) -> None:
        """Initialize free proxy provider.

        Args:
            cache_file: Path to cache file for working proxies
            cache_ttl: Cache TTL in seconds (default: 1 hour)
        """
        self._cache_file = cache_file
        self._cache_ttl = cache_ttl
        self._proxy_cache: list[dict[str, Any]] = []
        self._last_refresh: float = 0
        self._working_proxies: list[dict[str, Any]] = []
        self._load_cache()

    def _load_cache(self) -> None:
        """Load cached proxies from file."""
        try:
            import json
            from pathlib import Path

            cache_path = Path(self._cache_file)
            if cache_path.exists():
                data = json.loads(cache_path.read_text())
                self._working_proxies = data.get("proxies", [])
                self._last_refresh = data.get("last_refresh", 0)
                logger.info(f"Loaded {len(self._working_proxies)} cached proxies")
        except Exception as e:
            logger.warning(f"Failed to load proxy cache: {e}")

    def _save_cache(self) -> None:
        """Save working proxies to file."""
        try:
            import json
            from pathlib import Path

            cache_path = Path(self._cache_file)
            data = {
                "proxies": self._working_proxies,
                "last_refresh": self._last_refresh,
                "count": len(self._working_proxies),
            }
            cache_path.write_text(json.dumps(data, indent=2))
            logger.info(f"Saved {len(self._working_proxies)} proxies to cache")
        except Exception as e:
            logger.warning(f"Failed to save proxy cache: {e}")

    def _test_proxy(self, proxy: dict[str, Any], timeout: int = 5) -> bool:
        """Test if a proxy is working.

        Args:
            proxy: Proxy dictionary with host and port
            timeout: Timeout in seconds

        Returns:
            True if proxy is working
        """
        try:
            proxy_url = f"http://{proxy['host']}:{proxy['port']}"
            with httpx.Client(timeout=timeout, proxy=proxy_url) as client:
                resp = client.get("https://api.ipify.org?format=json")
                return resp.status_code == 200
        except Exception:
            return False

    def _refresh_proxies(self, count: int = 20) -> None:
        """Refresh proxy list from sources and test them."""
        logger.info("Refreshing proxy list...")

        # Fetch new proxies
        new_proxies = self._fetch_from_sources(count * 3)  # Fetch more to filter

        # Test each proxy
        working = []
        for proxy in new_proxies[:count * 2]:  # Test up to 2x needed
            if self._test_proxy(proxy):
                working.append(proxy)
                if len(working) >= count:
                    break

        # Update cache
        self._working_proxies = working
        self._last_refresh = time.time()
        self._save_cache()

        logger.info(f"Refreshed: {len(working)} working proxies out of {len(new_proxies[:count * 2])} tested")

    def _fetch_from_sources(self, count: int) -> list[dict[str, Any]]:
        """Fetch proxies from public sources."""
        sources = [
            "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt",
            "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt",
            "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt",
        ]

        proxies = []
        for url in sources:
            try:
                with httpx.Client(timeout=5) as client:
                    resp = client.get(url)
                    if resp.status_code == 200:
                        for line in resp.text.strip().split("\n"):
                            if ":" in line and not line.startswith("#"):
                                parts = line.strip().split(":")
                                if len(parts) == 2:
                                    host, port = parts
                                    try:
                                        proxies.append({
                                            "host": host.strip(),
                                            "port": int(port.strip()),
                                            "protocol": "http",
                                        })
                                    except ValueError:
                                        continue
            except Exception:
                continue

        return proxies[:count]

    def get_proxies(self, count: int = 10) -> list[dict[str, Any]]:
        """Get working proxies.

        Args:
            count: Number of proxies needed

        Returns:
            List of working proxies
        """
        # Check if cache needs refresh
        now = time.time()
        if now - self._last_refresh > self._cache_ttl:
            self._refresh_proxies(count)

        # Return cached working proxies
        if self._working_proxies:
            return self._working_proxies[:count]

        # If no cached proxies, fetch and test
        self._refresh_proxies(count)
        return self._working_proxies[:count]

    def report_proxy(self, proxy: dict[str, Any], success: bool) -> None:
        """Report proxy status.

        Args:
            proxy: Proxy that was used
            success: Whether the request was successful
        """
        if not success:
            # Remove failed proxy from working list
            self._working_proxies = [
                p for p in self._working_proxies
                if not (p["host"] == proxy["host"] and p["port"] == proxy["port"])
            ]
            self._save_cache()
            logger.info(f"Removed failed proxy: {proxy['host']}:{proxy['port']}")

    def test_all_proxies(self) -> dict[str, Any]:
        """Test all cached proxies and return results.

        Returns:
            Dictionary with test results
        """
        results = {"working": [], "failed": [], "total": len(self._working_proxies)}

        for proxy in self._working_proxies:
            if self._test_proxy(proxy):
                results["working"].append(proxy)
            else:
                results["failed"].append(proxy)

        # Update cache with only working proxies
        self._working_proxies = results["working"]
        self._save_cache()

        return results


# Provider registry
PROVIDERS: dict[str, type[ProxyProvider]] = {
    "kuaidaili": KuaiDaiLiProvider,
    "zhima": ZhiMaProvider,
    "brightdata": BrightDataProvider,
    "free": FreeProxyProvider,
}


def create_provider(provider_name: str, **kwargs: Any) -> ProxyProvider:
    """Create a proxy provider by name.

    Args:
        provider_name: Provider name (kuaidaili, zhimma, brightdata, free)
        **kwargs: Provider-specific arguments

    Returns:
        ProxyProvider instance
    """
    if provider_name not in PROVIDERS:
        raise ValueError(f"Unknown provider: {provider_name}. Available: {list(PROVIDERS.keys())}")

    return PROVIDERS[provider_name](**kwargs)
