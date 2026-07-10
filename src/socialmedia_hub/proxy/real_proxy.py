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
from socialmedia_hub.proxy.stealth import StealthFetcher, stealth_fetcher
from socialmedia_hub.proxy.ytdlp_extractor import YTDLExtractor, ytdlp_extractor
from socialmedia_hub.transcription.whisper import WhisperTranscriber, whisper_transcriber

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
        ytdlp_extractor: YTDLExtractor | None = None,
        whisper_transcriber: Any | None = None,
        min_delay: float = 1.0,
        max_delay: float = 3.0,
        use_proxy_cache: bool = True,
    ) -> None:
        """Initialize the proxy layer.

        Args:
            cookie_manager: Cookie manager instance
            signature_manager: Signature manager instance
            proxy_pool: Proxy pool instance
            ytdlp_extractor: yt-dlp extractor instance
            whisper_transcriber: Whisper transcriber instance
            min_delay: Minimum delay between requests (seconds)
            max_delay: Maximum delay between requests (seconds)
            use_proxy_cache: Whether to use smart proxy caching
        """
        self.cookie_manager = cookie_manager or cookie_manager_global
        self.signature_manager = signature_manager or signature_manager_global
        self.proxy_pool = proxy_pool or proxy_pool_global
        self.ytdlp_extractor = ytdlp_extractor or ytdlp_extractor_global
        self.whisper_transcriber = whisper_transcriber or whisper_transcriber_global

        # Request rate control
        self._request_times: dict[str, list[float]] = {}
        self._min_interval: float = 1.0  # Minimum seconds between requests to same domain
        self._min_delay = min_delay
        self._max_delay = max_delay

        # Smart proxy cache
        self._use_proxy_cache = use_proxy_cache
        if use_proxy_cache and len(self.proxy_pool.proxies) == 0:
            self._load_proxy_cache()

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

        # Note: Signatures are handled by yt-dlp when using smart_fetch
        # For direct API calls, most platforms don't need signatures for public data

        # Get proxy
        proxy_url = None
        if use_proxy:
            proxy_url = self.proxy_pool.get_proxy_url()

        # Make request - try stealth first, fallback to httpx
        try:
            # Try stealth fetch (curl_cffi with browser fingerprint)
            result = await self._stealth_request(url, method, headers, cookies, json_body)
            if result.get("status_code") == 200:
                return result

            # Fallback to httpx if stealth fails
            logger.warning("Stealth fetch failed, falling back to httpx")

        except Exception as e:
            logger.warning(f"Stealth fetch error: {e}, falling back to httpx")

        # Fallback: httpx
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

    async def _stealth_request(
        self,
        url: str,
        method: str,
        headers: dict[str, str],
        cookies: dict[str, str] | None,
        json_body: Any = None,
    ) -> dict[str, Any]:
        """Internal stealth request using curl_cffi."""
        result = self.stalth_fetcher.fetch(
            url=url,
            method=method,
            headers=headers,
            cookies=cookies,
            json_data=json_body,
        )

        if result.get("status_code") == 200:
            try:
                import json
                data = json.loads(result.get("text", "{}"))
            except Exception:
                data = {"raw": result.get("text", "")[:2000]}

            return {
                "status_code": result["status_code"],
                "data": data,
                "headers": result.get("headers", {}),
            }

        return {"status_code": result.get("status_code", 0), "error": result.get("error", "")}

    def _load_proxy_cache(self) -> None:
        """Load proxies from smart cache."""
        try:
            from socialmedia_hub.proxy.providers import FreeProxyProvider
            provider = FreeProxyProvider()
            proxies = provider.get_proxies(count=5)
            if proxies:
                self.proxy_pool.add_proxies(proxies)
                logger.info(f"Loaded {len(proxies)} proxies from cache")
        except Exception as e:
            logger.warning(f"Failed to load proxy cache: {e}")

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

    async def stealth_fetch(
        self,
        url: str,
        headers: dict[str, str] | None = None,
        cookies: dict[str, str] | None = None,
    ) -> dict[str, Any]:
        """Fetch URL with enhanced anti-detection (curl_cffi).

        Uses real browser TLS fingerprint to avoid detection.

        Args:
            url: Target URL
            headers: Additional headers
            cookies: Cookies to send

        Returns:
            Response dictionary
        """
        # Rate control
        await self._rate_control("stealth")

        # Random delay
        delay = random.uniform(self._min_delay, self._max_delay)
        await asyncio.sleep(delay)

        # Use stealth fetcher
        result = self.stalth_fetcher.fetch(
            url=url,
            headers=headers,
            cookies=cookies,
        )

        return result

    async def smart_fetch(self, url: str, platform: str | None = None) -> dict[str, Any]:
        """Smart fetch video info - try yt-dlp first, fallback to API.

        Args:
            url: Video URL
            platform: Platform name (auto-detected if None)

        Returns:
            Video information dictionary
        """
        # Auto-detect platform from URL
        if platform is None:
            platform = self._detect_platform(url)

        # 1. Try yt-dlp first (recommended)
        try:
            result = await self.extract_video_info(url)
            if result and result.get("status_code") == 200:
                result["method"] = "yt-dlp"
                return result
        except Exception as e:
            logger.warning(f"yt-dlp failed: {e}")

        # 2. Fallback to API
        if platform:
            try:
                result = await self.fetch(
                    platform=platform,
                    url=url,
                    use_signature=True,
                )
                result["method"] = "api"
                return result
            except Exception as e:
                logger.warning(f"API fallback failed: {e}")

        return {"status_code": 404, "error": "Could not fetch video info"}

    def _detect_platform(self, url: str) -> str | None:
        """Auto-detect platform from URL.

        Args:
            url: Video URL

        Returns:
            Platform name or None
        """
        url_lower = url.lower()
        platform_patterns = {
            "tiktok": ["tiktok.com"],
            "douyin": ["douyin.com", "v.douyin.com"],
            "instagram": ["instagram.com"],
            "youtube": ["youtube.com", "youtu.be"],
            "bilibili": ["bilibili.com"],
            "twitter": ["twitter.com", "x.com"],
            "xiaohongshu": ["xiaohongshu.com", "xhslink.com"],
            "weibo": ["weibo.com", "m.weibo.cn"],
            "kuaishou": ["kuaishou.com"],
            "reddit": ["reddit.com"],
            "linkedin": ["linkedin.com"],
            "zhihu": ["zhihu.com"],
            "threads": ["threads.net"],
            "wechat": ["mp.weixin.qq.com", "channels.weixin.qq.com"],
            "lemon8": ["lemon8-app.com"],
        }

        for platform, patterns in platform_patterns.items():
            for pattern in patterns:
                if pattern in url_lower:
                    return platform
        return None

    async def transcribe_video(self, url: str, language: str | None = None) -> dict[str, Any]:
        """Transcribe video audio to text using Whisper.

        Args:
            url: Video URL to transcribe
            language: Language code (e.g., 'en', 'zh') or None for auto-detect

        Returns:
            Transcription result with text, segments, and metadata
        """
        try:
            result = self.ytdlp_extractor.extract_info(url)
            if not result:
                return {"status_code": 404, "error": "Video not found"}

            # Download and transcribe
            import yt_dlp
            import tempfile
            from pathlib import Path

            with tempfile.TemporaryDirectory() as temp_dir:
                output_path = Path(temp_dir) / "video.%(ext)s"

                ydl_opts = {
                    "format": "bestaudio/best",
                    "outtmpl": str(output_path),
                    "quiet": True,
                }

                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    info = ydl.extract_info(url, download=True)
                    filename = ydl.prepare_filename(info)

                # Transcribe
                transcription = self.whisper_transcriber.transcribe_file(
                    filename, language
                )

                return {
                    "status_code": 200,
                    "data": {
                        "title": info.get("title"),
                        "description": info.get("description"),
                        "transcription": transcription["text"],
                        "segments": transcription["segments"],
                        "language": transcription.get("language"),
                        "duration": info.get("duration"),
                    },
                    "source": "whisper",
                }

        except Exception as e:
            logger.error(f"Transcription failed: {e}")
            return {"status_code": 500, "error": str(e)}

    async def smart_fetch(self, url: str, platform: str | None = None) -> dict[str, Any]:
        """Smart fetch video info - try yt-dlp first, fallback to API.

        Args:
            url: Video URL
            platform: Platform name (auto-detected if None)

        Returns:
            Video information dictionary
        """
        # Auto-detect platform from URL
        if platform is None:
            platform = self._detect_platform(url)

        # 1. Try yt-dlp first (recommended)
        try:
            result = await self.extract_video_info(url)
            if result and result.get("status_code") == 200:
                result["method"] = "yt-dlp"
                return result
        except Exception as e:
            logger.warning(f"yt-dlp failed: {e}")

        # 2. Fallback to API
        if platform:
            try:
                result = await self.fetch(
                    platform=platform,
                    url=url,
                    use_signature=True,
                )
                result["method"] = "api"
                return result
            except Exception as e:
                logger.warning(f"API fallback failed: {e}")

        return {"status_code": 404, "error": "Could not fetch video info"}

    def _detect_platform(self, url: str) -> str | None:
        """Auto-detect platform from URL.

        Args:
            url: Video URL

        Returns:
            Platform name or None
        """
        url_lower = url.lower()
        platform_patterns = {
            "tiktok": ["tiktok.com"],
            "douyin": ["douyin.com", "v.douyin.com"],
            "instagram": ["instagram.com"],
            "youtube": ["youtube.com", "youtu.be"],
            "bilibili": ["bilibili.com"],
            "twitter": ["twitter.com", "x.com"],
            "xiaohongshu": ["xiaohongshu.com", "xhslink.com"],
            "weibo": ["weibo.com", "m.weibo.cn"],
            "kuaishou": ["kuaishou.com"],
            "reddit": ["reddit.com"],
            "linkedin": ["linkedin.com"],
            "zhihu": ["zhihu.com"],
            "threads": ["threads.net"],
            "wechat": ["mp.weixin.qq.com", "channels.weixin.qq.com"],
            "lemon8": ["lemon8-app.com"],
        }

        for platform, patterns in platform_patterns.items():
            for pattern in patterns:
                if pattern in url_lower:
                    return platform
        return None

    async def extract_video_info(self, url: str) -> dict[str, Any] | None:
        """Extract video information using yt-dlp.

        Args:
            url: Video URL to extract information from

        Returns:
            Video information dictionary or None
        """
        try:
            info = self.ytdlp_extractor.extract_info(url)
            if info:
                return {
                    "status_code": 200,
                    "data": {
                        "title": info.get("title"),
                        "description": info.get("description"),
                        "duration": info.get("duration"),
                        "uploader": info.get("uploader"),
                        "upload_date": info.get("upload_date"),
                        "view_count": info.get("view_count"),
                        "like_count": info.get("like_count"),
                        "comment_count": info.get("comment_count"),
                        "thumbnail": info.get("thumbnail"),
                        "webpage_url": info.get("webpage_url"),
                        "formats": info.get("formats", []),
                    },
                    "source": "yt-dlp",
                }
            return {"status_code": 404, "error": "Video not found"}
        except Exception as e:
            logger.error(f"yt-dlp extraction failed: {e}")
            return {"status_code": 500, "error": str(e)}


# Global instances
cookie_manager_global = CookieManager()
signature_manager_global = SignatureManager()
proxy_pool_global = ProxyPool()
ytdlp_extractor_global = YTDLExtractor()
whisper_transcriber_global = WhisperTranscriber()
stalth_fetcher_global = StealthFetcher()

# Global proxy layer
real_proxy = RealProxyLayer()
