"""Proxy service providers integration."""

from __future__ import annotations

import logging
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
    """Free proxy provider - scrapes free proxy lists.

    WARNING: Free proxies are unstable and may be slow.
    """

    def __init__(self) -> None:
        self._proxy_cache: list[dict[str, Any]] = []

    def get_proxies(self, count: int = 10) -> list[dict[str, Any]]:
        """Get free proxies from public lists."""
        if self._proxy_cache:
            return self._proxy_cache[:count]

        try:
            # Try multiple free proxy sources
            sources = [
                "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt",
                "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt",
            ]

            proxies = []
            for url in sources:
                try:
                    with httpx.Client(timeout=5) as client:
                        resp = client.get(url)
                        if resp.status_code == 200:
                            for line in resp.text.strip().split("\n"):
                                if ":" in line:
                                    host, port = line.split(":")
                                    proxies.append({
                                        "host": host.strip(),
                                        "port": int(port.strip()),
                                        "protocol": "http",
                                    })
                except Exception:
                    continue

            self._proxy_cache = proxies[:100]  # Cache up to 100 proxies
            return proxies[:count]

        except Exception as e:
            logger.error(f"Free proxy fetch failed: {e}")
            return []

    def report_proxy(self, proxy: dict[str, Any], success: bool) -> None:
        """Report proxy status (remove bad proxies)."""
        if not success:
            # Remove failed proxy from cache
            self._proxy_cache = [
                p for p in self._proxy_cache
                if not (p["host"] == proxy["host"] and p["port"] == proxy["port"])
            ]


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
