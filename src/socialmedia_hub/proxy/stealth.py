"""Enhanced anti-detection techniques for web scraping."""

from __future__ import annotations

import logging
import random
from typing import Any

logger = logging.getLogger("socialmedia_hub.proxy.stealth")

# User-Agent pool for randomization
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2 Safari/605.1.15",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.0.0",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
]


class StealthFetcher:
    """Enhanced fetcher with anti-detection capabilities.

    Features:
    - TLS fingerprint impersonation (curl_cffi)
    - Randomized browser headers
    - Smart request intervals
    - Cookie rotation support
    """

    def __init__(
        self,
        impersonate: str = "edge",
        min_delay: float = 2.0,
        max_delay: float = 5.0,
    ) -> None:
        """Initialize stealth fetcher.

        Args:
            impersonate: Browser to impersonate ('chrome', 'edge', 'safari', etc.)
            min_delay: Minimum delay between requests (seconds)
            max_delay: Maximum delay between requests (seconds)
        """
        self.impersonate = impersonate
        self.min_delay = min_delay
        self.max_delay = max_delay
        self._last_request_time = 0
        self._check_curl_cffi()

    def _check_curl_cffi(self) -> None:
        """Check if curl_cffi is installed."""
        try:
            import curl_cffi.requests
            logger.info("curl_cffi available for stealth fetching")
        except ImportError:
            logger.warning("curl_cffi not installed. Install with: pip install curl-cffi")

    def _get_random_user_agent(self) -> str:
        """Get a random User-Agent from the pool."""
        return random.choice(USER_AGENTS)

    def _get_smart_delay(self) -> float:
        """Get smart delay between requests.

        - 90% chance: 2-5 seconds (normal)
        - 10% chance: 10-30 seconds (long pause, simulates human behavior)
        """
        if random.random() < 0.1:  # 10% chance for long delay
            return random.uniform(10.0, 30.0)
        return random.uniform(self.min_delay, self.max_delay)

    def _wait_if_needed(self) -> None:
        """Wait if needed based on smart delay."""
        import time
        now = time.time()
        elapsed = now - self._last_request_time
        delay = self._get_smart_delay()

        if elapsed < delay:
            wait_time = delay - elapsed
            logger.debug(f"Waiting {wait_time:.2f}s for smart delay")
            time.sleep(wait_time)

        self._last_request_time = time.time()

    def fetch(
        self,
        url: str,
        method: str = "GET",
        headers: dict[str, str] | None = None,
        cookies: dict[str, str] | None = None,
        json_data: Any = None,
        timeout: int = 30,
    ) -> dict[str, Any]:
        """Fetch URL with anti-detection.

        Args:
            url: Target URL
            method: HTTP method
            headers: Additional headers
            cookies: Cookies to send
            json_data: JSON body for POST
            timeout: Request timeout

        Returns:
            Response dictionary
        """
        try:
            from curl_cffi import requests as curl_requests

            # Smart delay before request
            self._wait_if_needed()

            # Merge headers with random User-Agent
            final_headers = {
                "User-Agent": self._get_random_user_agent(),
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
                "Accept-Language": "en-US,en;q=0.9",
                "Accept-Encoding": "gzip, deflate, br",
                "Cache-Control": "no-cache",
                "Pragma": "no-cache",
                "Sec-Ch-Ua": '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
                "Sec-Ch-Ua-Mobile": "?0",
                "Sec-Ch-Ua-Platform": '"Windows"',
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "none",
                "Sec-Fetch-User": "?1",
                "Upgrade-Insecure-Requests": "1",
            }
            if headers:
                final_headers.update(headers)

            # Make request with browser impersonation
            response = curl_requests.request(
                method=method,
                url=url,
                headers=final_headers,
                cookies=cookies,
                json=json_data,
                timeout=timeout,
                impersonate=self.impersonate,
            )

            return {
                "status_code": response.status_code,
                "text": response.text,
                "headers": dict(response.headers),
                "cookies": dict(response.cookies),
            }

        except ImportError:
            logger.error("curl_cffi not installed")
            return {"status_code": 0, "error": "curl_cffi not installed"}

        except Exception as e:
            logger.error(f"Stealth fetch failed: {e}")
            return {"status_code": 0, "error": str(e)}

    def fetch_json(
        self,
        url: str,
        headers: dict[str, str] | None = None,
        cookies: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        """Fetch JSON data with anti-detection.

        Args:
            url: Target URL
            headers: Additional headers
            cookies: Cookies to send

        Returns:
            Parsed JSON response
        """
        result = self.fetch(url, headers=headers, cookies=cookies)

        if result["status_code"] == 200:
            try:
                import json
                return json.loads(result["text"])
            except Exception:
                return {"error": "Failed to parse JSON", "raw": result["text"][:500]}

        return result


class BrowserStealth:
    """Browser-based stealth using Playwright."""

    def __init__(self, headless: bool = True) -> None:
        """Initialize browser stealth.

        Args:
            headless: Run browser in headless mode
        """
        self.headless = headless
        self._browser = None
        self._context = None

    async def start(self) -> None:
        """Start the browser."""
        try:
            from playwright.async_api import async_playwright

            self._playwright = await async_playwright().start()
            self._browser = await self._playwright.chromium.launch(headless=self.headless)
            self._context = await self._browser.new_context(
                viewport={"width": 1920, "height": 1080},
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            )
            logger.info("Browser started")

        except ImportError:
            logger.error("playwright not installed")
            raise

    async def stop(self) -> None:
        """Stop the browser."""
        if self._browser:
            await self._browser.close()
        if self._playwright:
            await self._playwright.stop()
        logger.info("Browser stopped")

    async def fetch_page(self, url: str, wait_for: str = "networkidle") -> dict[str, Any]:
        """Fetch page content with browser.

        Args:
            url: Page URL
            wait_for: Wait condition ('load', 'domcontentloaded', 'networkidle')

        Returns:
            Page content dictionary
        """
        if not self._context:
            await self.start()

        try:
            page = await self._context.new_page()
            await page.goto(url, wait_until=wait_for)

            # Get page content
            content = await page.content()
            title = await page.title()

            # Try to get JSON data (for SPA)
            json_data = None
            try:
                json_data = await page.evaluate("() => window.__NEXT_DATA__")
            except Exception:
                pass

            await page.close()

            return {
                "title": title,
                "content": content[:5000],  # First 5000 chars
                "json_data": json_data,
                "url": url,
            }

        except Exception as e:
            logger.error(f"Browser fetch failed: {e}")
            return {"error": str(e), "url": url}

    async def fetch_with_cookies(self, url: str, cookies: list[dict]) -> dict[str, Any]:
        """Fetch page with cookies.

        Args:
            url: Page URL
            cookies: List of cookie dictionaries

        Returns:
            Page content dictionary
        """
        if not self._context:
            await self.start()

        # Add cookies
        await self._context.add_cookies(cookies)

        return await self.fetch_page(url)


# Global instances
stealth_fetcher = StealthFetcher()
browser_stealth = BrowserStealth()
