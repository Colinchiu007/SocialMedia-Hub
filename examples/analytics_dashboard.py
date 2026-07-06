"""Example: Social Media Analytics Dashboard.

This example demonstrates how to build a social media analytics dashboard
using SocialMedia-Hub SDK.
"""

import asyncio
from collections import Counter
from datetime import datetime
from typing import Any

from socialmedia_hub import AsyncSocialMediaHub


class SocialMediaAnalytics:
    """Social media analytics dashboard."""

    def __init__(self, api_key: str):
        self.api_key = api_key
        self.client = None

    async def __aenter__(self):
        self.client = AsyncSocialMediaHub(api_key=self.api_key)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.client:
            await self.client.aclose()

    async def get_tiktok_analytics(self, username: str) -> dict[str, Any]:
        """Get TikTok user analytics."""
        # Fetch user profile
        profile = await self.client.tiktok_web.fetch_user_profile(uniqueId=username)
        user_data = profile.get("data", {})

        # Fetch user posts
        posts = await self.client.tiktok_web.fetch_user_post(
            secUid=user_data.get("secUid", ""),
            count=50
        )
        post_list = posts.get("data", {}).get("itemList", [])

        # Calculate analytics
        total_likes = sum(
            post.get("stats", {}).get("diggCount", 0) for post in post_list
        )
        total_comments = sum(
            post.get("stats", {}).get("commentCount", 0) for post in post_list
        )
        total_shares = sum(
            post.get("stats", {}).get("shareCount", 0) for post in post_list
        )

        return {
            "username": username,
            "followers": user_data.get("followers", 0),
            "following": user_data.get("following", 0),
            "likes": user_data.get("heart", 0),
            "videos_count": len(post_list),
            "total_likes": total_likes,
            "total_comments": total_comments,
            "total_shares": total_shares,
            "engagement_rate": (total_likes + total_comments + total_shares) / max(len(post_list), 1),
        }

    async def get_douyin_analytics(self, uid: str) -> dict[str, Any]:
        """Get Douyin user analytics."""
        # Fetch user profile
        profile = await self.client.douyin_web.fetch_user_profile_by_uid(uid=uid)
        user_data = profile.get("data", {}).get("user", {})

        # Fetch user posts
        posts = await self.client.douyin_web.fetch_user_post_videos(
            sec_user_id=user_data.get("sec_uid", ""),
            count=50
        )
        post_list = posts.get("data", {}).get("aweme_list", [])

        # Calculate analytics
        total_likes = sum(
            post.get("statistics", {}).get("digg_count", 0) for post in post_list
        )
        total_comments = sum(
            post.get("statistics", {}).get("comment_count", 0) for post in post_list
        )

        return {
            "uid": uid,
            "nickname": user_data.get("nickname", ""),
            "followers": user_data.get("follower_count", 0),
            "following": user_data.get("following_count", 0),
            "likes": user_data.get("total_favorited", 0),
            "videos_count": len(post_list),
            "total_likes": total_likes,
            "total_comments": total_comments,
        }

    async def get_cross_platform_analytics(self, usernames: dict[str, str]) -> dict[str, Any]:
        """Get analytics across multiple platforms."""
        results = {}

        if "tiktok" in usernames:
            try:
                results["tiktok"] = await self.get_tiktok_analytics(usernames["tiktok"])
            except Exception as e:
                results["tiktok"] = {"error": str(e)}

        if "douyin" in usernames:
            try:
                results["douyin"] = await self.get_douyin_analytics(usernames["douyin"])
            except Exception as e:
                results["douyin"] = {"error": str(e)}

        return results


async def main():
    """Main function."""
    api_key = "YOUR_API_KEY"

    async with SocialMediaAnalytics(api_key) as analytics:
        # Get TikTok analytics
        print("=== TikTok Analytics ===")
        tiktok_data = await analytics.get_tiktok_analytics("tiktok")
        print(f"Followers: {tiktok_data.get('followers', 'N/A')}")
        print(f"Engagement Rate: {tiktok_data.get('engagement_rate', 'N/A'):.2f}")

        # Get cross-platform analytics
        print("\n=== Cross-Platform Analytics ===")
        cross_data = await analytics.get_cross_platform_analytics({
            "tiktok": "tiktok",
            "douyin": "123456789",
        })
        for platform, data in cross_data.items():
            print(f"\n{platform.upper()}:")
            if "error" in data:
                print(f"  Error: {data['error']}")
            else:
                print(f"  Followers: {data.get('followers', 'N/A')}")


if __name__ == "__main__":
    asyncio.run(main())
