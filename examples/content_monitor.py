"""Example: Social Media Content Monitor.

This example demonstrates how to monitor social media content
for specific keywords or topics using SocialMedia-Hub SDK.
"""

import asyncio
from datetime import datetime
from typing import Any

from socialmedia_hub import AsyncSocialMediaHub


class ContentMonitor:
    """Social media content monitor."""

    def __init__(self, api_key: str):
        self.api_key = api_key
        self.client = None
        self.keywords = []
        self.platforms = []

    async def __aenter__(self):
        self.client = AsyncSocialMediaHub(api_key=self.api_key)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.client:
            await self.client.aclose()

    def add_keyword(self, keyword: str) -> None:
        """Add a keyword to monitor."""
        self.keywords.append(keyword)

    def add_platform(self, platform: str) -> None:
        """Add a platform to monitor."""
        self.platforms.append(platform)

    async def search_tiktok(self, keyword: str, count: int = 20) -> list[dict]:
        """Search TikTok for keyword."""
        try:
            results = await self.client.tiktok_web.fetch_general_search(
                keyword=keyword,
                count=count
            )
            return results.get("data", {}).get("data", [])
        except Exception as e:
            print(f"Error searching TikTok: {e}")
            return []

    async def search_douyin(self, keyword: str, count: int = 20) -> list[dict]:
        """Search Douyin for keyword."""
        try:
            results = await self.client.douyin_search.fetch_general_search_result(
                keyword=keyword,
                count=count
            )
            return results.get("data", {}).get("data", [])
        except Exception as e:
            print(f"Error searching Douyin: {e}")
            return []

    async def search_instagram(self, hashtag: str) -> list[dict]:
        """Search Instagram for hashtag."""
        try:
            results = await self.client.instagram_v1.fetch_hashtag_posts(
                hashtag=hashtag
            )
            return results.get("data", {}).get("data", [])
        except Exception as e:
            print(f"Error searching Instagram: {e}")
            return []

    async def search_youtube(self, keyword: str, count: int = 20) -> list[dict]:
        """Search YouTube for keyword."""
        try:
            results = await self.client.youtube_web.search_video(
                search_query=keyword,
                count=count
            )
            return results.get("data", {}).get("data", [])
        except Exception as e:
            print(f"Error searching YouTube: {e}")
            return []

    async def search_twitter(self, keyword: str) -> list[dict]:
        """Search Twitter for keyword."""
        try:
            results = await self.client.twitter_web.fetch_search_timeline(
                keyword=keyword
            )
            return results.get("data", {}).get("entries", [])
        except Exception as e:
            print(f"Error searching Twitter: {e}")
            return []

    async def monitor_keyword(self, keyword: str) -> dict[str, Any]:
        """Monitor a keyword across all platforms."""
        results = {
            "keyword": keyword,
            "timestamp": datetime.now().isoformat(),
            "platforms": {},
        }

        if "tiktok" in self.platforms:
            results["platforms"]["tiktok"] = await self.search_tiktok(keyword)

        if "douyin" in self.platforms:
            results["platforms"]["douyin"] = await self.search_douyin(keyword)

        if "instagram" in self.platforms:
            results["platforms"]["instagram"] = await self.search_instagram(keyword)

        if "youtube" in self.platforms:
            results["platforms"]["youtube"] = await self.search_youtube(keyword)

        if "twitter" in self.platforms:
            results["platforms"]["twitter"] = await self.search_twitter(keyword)

        return results

    async def monitor_all(self) -> list[dict[str, Any]]:
        """Monitor all keywords across all platforms."""
        results = []
        for keyword in self.keywords:
            result = await self.monitor_keyword(keyword)
            results.append(result)
        return results


async def main():
    """Main function."""
    api_key = "YOUR_API_KEY"

    async with ContentMonitor(api_key) as monitor:
        # Add keywords to monitor
        monitor.add_keyword("Python")
        monitor.add_keyword("AI")
        monitor.add_keyword("Machine Learning")

        # Add platforms to monitor
        monitor.add_platform("tiktok")
        monitor.add_platform("youtube")
        monitor.add_platform("twitter")

        # Monitor all keywords
        print("=== Monitoring Keywords ===")
        results = await monitor.monitor_all()

        for result in results:
            print(f"\nKeyword: {result['keyword']}")
            print(f"Timestamp: {result['timestamp']}")
            for platform, data in result["platforms"].items():
                print(f"  {platform}: {len(data)} results")


if __name__ == "__main__":
    asyncio.run(main())
