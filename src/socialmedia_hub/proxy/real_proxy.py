"""Real proxy layer for social media platform authentication."""

from __future__ import annotations

import asyncio
import logging
import random
import time
from typing import Any

import httpx

from socialmedia_hub.proxy.cookies import CookieManager
from socialmedia_hub.proxy.pool import ProxyPool
from socialmedia_hub.proxy.signatures import SignatureManager

logger = logging.getLogger("socialmedia_hub.proxy")


class RealProxyLayer:
    """Real proxy layer for connecting to social media platforms.

    This layer handles:
    - Cookie management for authentication
    - Signature generation for anti-crawl
    - Proxy rotation for IP diversity
    - Request rate control with random delays
    - Cookie rotation for multiple accounts
    - Session management
    """

    def __init__(
        self,
        cookie_manager: CookieManager | None = None,
        signature_manager: SignatureManager | None = None,
        proxy_pool: ProxyPool | None = None,
        min_delay: float = 1.0,
        max_delay: float = 3.0,
    ) -> None:
        """Initialize the proxy layer.

        Args:
            cookie_manager: Cookie manager instance
            signature_manager: Signature manager instance
            proxy_pool: Proxy pool instance
            min_delay: Minimum delay between requests (seconds)
            max_delay: Maximum delay between requests (seconds)
        """
        self.cookie_manager = cookie_manager or cookie_manager_global
        self.signature_manager = signature_manager or signature_manager_global
        self.proxy_pool = proxy_pool or proxy_pool_global

        # Request rate control
        self._request_times: dict[str, list[float]] = {}
        self._min_interval: float = 1.0  # Minimum seconds between requests to same domain
        self._min_delay = min_delay
        self._max_delay = max_delay

    async def fetch(
        self,
        platform: str,
        url: str,
        method: str = "GET",
        params: dict[str, Any] | None = None,
        json_body: Any = None,
        cookies: dict[str, str] | None = None,
        use_proxy: bool = True,
        use_signature: bool = True,
    ) -> dict[str, Any]:
        """Fetch data from a social media platform.

        Args:
            platform: Platform name (douyin, tiktok, etc.)
            url: Target URL
            method: HTTP method
            params: Query parameters
            json_body: JSON body for POST requests
            cookies: Additional cookies
            use_proxy: Whether to use proxy
            use_signature: Whether to generate signature

        Returns:
            Response data as dictionary
        """
        # Rate control with random delay
        await self._rate_control(platform)

        # Random delay between requests (anti-crawl)
        delay = random.uniform(self._min_delay, self._max_delay)
        await asyncio.sleep(delay)

        # Get cookies for domain with rotation
        from urllib.parse import urlparse
        parsed = urlparse(url)
        domain = parsed.hostname or ""
        cookie_header = self._get_rotating_cookie(domain)

        # Merge with provided cookies
        if cookies:
            extra_cookies = "; ".join(f"{k}={v}" for k, v in cookies.items())
            if cookie_header:
                cookie_header = f"{cookie_header}; {extra_cookies}"
            else:
                cookie_header = extra_cookies

        # Build headers
        headers: dict[str, str] = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Accept": "application/json",
            "Accept-Language": "en-US,en;q=0.9",
        }

        if cookie_header:
            headers["Cookie"] = cookie_header

        # Add signature if needed
        if use_signature:
            sig_headers = self.signature_manager.generate_signature(platform, url=url)
            headers.update(sig_headers)

        # Get proxy
        proxy_url = None
        if use_proxy:
            proxy_url = self.proxy_pool.get_proxy_url()

        # Make request
        try:
            async with httpx.AsyncClient(
                timeout=30.0,
                proxy=proxy_url,
                follow_redirects=True,
            ) as client:
                if method.upper() == "GET":
                    response = await client.get(url, params=params, headers=headers)
                elif method.upper() == "POST":
                    response = await client.post(url, json=json_body, headers=headers)
                else:
                    response = await client.request(method, url, params=params, headers=headers)

                # Record success
                if proxy_url:
                    proxy = self.proxy_pool.get_proxy()
                    if proxy:
                        self.proxy_pool.record_success(proxy)

                # Parse response
                try:
                    data = response.json()
                except Exception:
                    data = {"raw": response.text[:2000]}

                return {
                    "status_code": response.status_code,
                    "data": data,
                    "headers": dict(response.headers),
                }

        except httpx.RequestError as e:
            # Record failure
            if proxy_url:
                proxy = self.proxy_pool.get_proxy()
                if proxy:
                    self.proxy_pool.record_failure(proxy)

            logger.error(f"Request failed: {e}")
            return {"status_code": 0, "error": str(e)}

    def _get_rotating_cookie(self, domain: str) -> str:
        """Get cookie header with rotation for multiple accounts."""
        cookies = self.cookie_manager.get_cookies_for_domain(domain)
        if not cookies:
            return ""

        # If multiple cookies, rotate randomly
        if len(cookies) > 1:
            cookie_name = random.choice(list(cookies.keys()))
            return f"{cookie_name}={cookies[cookie_name]}"

        # Single cookie
        cookie_name = list(cookies.keys())[0]
        return f"{cookie_name}={cookies[cookie_name]}"

    async def _rate_control(self, platform: str) -> None:
        """Control request rate per platform."""
        now = time.time()
        if platform not in self._request_times:
            self._request_times[platform] = []

        # Clean old timestamps
        self._request_times[platform] = [
            t for t in self._request_times[platform] if now - t < 60
        ]

        # Check rate limit (max 10 requests per minute per platform)
        if len(self._request_times[platform]) >= 10:
            wait_time = 60 - (now - self._request_times[platform][0])
            if wait_time > 0:
                logger.info(f"Rate limited for {platform}, waiting {wait_time:.1f}s")
                await asyncio.sleep(wait_time)

        self._request_times[platform].append(now)

    def get_stats(self) -> dict[str, Any]:
        """Get proxy layer statistics."""
        return {
            "cookie_stats": self.cookie_manager.get_stats(),
            "proxy_stats": self.proxy_pool.get_stats(),
            "request_counts": {
                platform: len(times)
                for platform, times in self._request_times.items()
            },
        }


# Global instances
cookie_manager_global = CookieManager()
signature_manager_global = SignatureManager()
proxy_pool_global = ProxyPool()

# Global proxy layer
real_proxy = RealProxyLayer()
