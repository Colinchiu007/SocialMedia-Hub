"""yt-dlp based extractor for signature generation and video info."""

from __future__ import annotations

import json
import logging
import subprocess
from typing import Any

logger = logging.getLogger("socialmedia_hub.proxy.ytdlp")


class YTDLExtractor:
    """Extract video information using yt-dlp.

    This class uses yt-dlp to extract video information and signatures
    from various social media platforms.
    """

    def __init__(self, timeout: int = 30) -> None:
        """Initialize the extractor.

        Args:
            timeout: Timeout in seconds for yt-dlp operations
        """
        self.timeout = timeout
        self._check_ytdlp()

    def _check_ytdlp(self) -> None:
        """Check if yt-dlp is installed."""
        try:
            result = subprocess.run(
                ["yt-dlp", "--version"],
                capture_output=True,
                text=True,
                timeout=5,
            )
            if result.returncode == 0:
                logger.info(f"yt-dlp version: {result.stdout.strip()}")
            else:
                logger.warning("yt-dlp not found or not working properly")
        except FileNotFoundError:
            logger.warning("yt-dlp not installed. Install with: pip install yt-dlp")
        except Exception as e:
            logger.warning(f"Error checking yt-dlp: {e}")

    def extract_info(self, url: str, no_download: bool = True) -> dict[str, Any] | None:
        """Extract video information from URL.

        Args:
            url: Video URL to extract information from
            no_download: If True, only extract info without downloading

        Returns:
            Video information dictionary or None if extraction fails
        """
        try:
            cmd = ["yt-dlp", "--dump-json"]
            if no_download:
                cmd.append("--no-download")
            cmd.append(url)

            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=self.timeout,
            )

            if result.returncode == 0:
                return json.loads(result.stdout)
            else:
                logger.error(f"yt-dlp error: {result.stderr}")
                return None

        except subprocess.TimeoutExpired:
            logger.error(f"yt-dlp timeout after {self.timeout}s")
            return None
        except json.JSONDecodeError as e:
            logger.error(f"Failed to parse yt-dlp output: {e}")
            return None
        except Exception as e:
            logger.error(f"yt-dlp extraction failed: {e}")
            return None

    def get_video_url(self, url: str, quality: str = "best") -> str | None:
        """Get direct video URL.

        Args:
            url: Video URL
            quality: Video quality (best, 720p, 480p, etc.)

        Returns:
            Direct video URL or None
        """
        try:
            cmd = ["yt-dlp", "-g", "-f", quality, url]
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=self.timeout,
            )

            if result.returncode == 0:
                return result.stdout.strip()
            else:
                logger.error(f"Failed to get video URL: {result.stderr}")
                return None

        except Exception as e:
            logger.error(f"Failed to get video URL: {e}")
            return None

    def get_video_title(self, url: str) -> str | None:
        """Get video title.

        Args:
            url: Video URL

        Returns:
            Video title or None
        """
        info = self.extract_info(url)
        if info:
            return info.get("title")
        return None

    def get_video_metadata(self, url: str) -> dict[str, Any] | None:
        """Get video metadata.

        Args:
            url: Video URL

        Returns:
            Video metadata dictionary or None
        """
        info = self.extract_info(url)
        if info:
            return {
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
            }
        return None

    def extract_tiktok(self, url: str) -> dict[str, Any] | None:
        """Extract TikTok video information.

        Args:
            url: TikTok video URL

        Returns:
            Video information dictionary
        """
        return self.extract_info(url)

    def extract_douyin(self, url: str) -> dict[str, Any] | None:
        """Extract Douyin video information.

        Args:
            url: Douyin video URL

        Returns:
            Video information dictionary
        """
        return self.extract_info(url)

    def extract_youtube(self, url: str) -> dict[str, Any] | None:
        """Extract YouTube video information.

        Args:
            url: YouTube video URL

        Returns:
            Video information dictionary
        """
        return self.extract_info(url)

    def extract_instagram(self, url: str) -> dict[str, Any] | None:
        """Extract Instagram video information.

        Args:
            url: Instagram video URL

        Returns:
            Video information dictionary
        """
        return self.extract_info(url)

    def extract_bilibili(self, url: str) -> dict[str, Any] | None:
        """Extract Bilibili video information.

        Args:
            url: Bilibili video URL

        Returns:
            Video information dictionary
        """
        return self.extract_info(url)


# Global extractor instance
ytdlp_extractor = YTDLExtractor()
