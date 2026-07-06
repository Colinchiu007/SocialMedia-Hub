"""Example: Social Media Competitor Analysis.

This example demonstrates how to analyze competitors on social media
using SocialMedia-Hub SDK.
"""

import asyncio
from datetime import datetime
from typing import Any

from socialmedia_hub import AsyncSocialMediaHub


class CompetitorAnalyzer:
    """Social media competitor analyzer."""

    def __init__(self, api_key: str):
        self.api_key = api_key
        self.client = None

    async def __aenter__(self):
        self.client = AsyncSocialMediaHub(api_key=self.api_key)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.client:
            await self.client.aclose()

    async def analyze_tiktok_user(self, username: str) -> dict[str, Any]:
        """Analyze a TikTok user's performance."""
        try:
            # Get user profile
            profile = await self.client.tiktok_web.fetch_user_profile(uniqueId=username)
            user_data = profile.get("data", {})

            # Get user posts
            posts = await self.client.tiktok_web.fetch_user_post(
                secUid=user_data.get("secUid", ""),
                count=50
            )
            post_list = posts.get("data", {}).get("itemList", [])

            # Calculate metrics
            total_likes = sum(
                post.get("stats", {}).get("diggCount", 0) for post in post_list
            )
            total_comments = sum(
                post.get("stats", {}).get("commentCount", 0) for post in post_list
            )
            total_shares = sum(
                post.get("stats", {}).get("shareCount", 0) for post in post_list
            )

            avg_likes = total_likes / max(len(post_list), 1)
            avg_comments = total_comments / max(len(post_list), 1)
            avg_shares = total_shares / max(len(post_list), 1)

            # Find top performing videos
            sorted_posts = sorted(
                post_list,
                key=lambda x: x.get("stats", {}).get("diggCount", 0),
                reverse=True
            )
            top_videos = sorted_posts[:5]

            return {
                "username": username,
                "followers": user_data.get("followers", 0),
                "following": user_data.get("following", 0),
                "likes": user_data.get("heart", 0),
                "videos_count": len(post_list),
                "total_likes": total_likes,
                "total_comments": total_comments,
                "total_shares": total_shares,
                "avg_likes": avg_likes,
                "avg_comments": avg_comments,
                "avg_shares": avg_shares,
                "engagement_rate": (total_likes + total_comments + total_shares) / max(len(post_list), 1),
                "top_videos": [
                    {
                        "id": v.get("id"),
                        "description": v.get("desc", "")[:100],
                        "likes": v.get("stats", {}).get("diggCount", 0),
                        "comments": v.get("stats", {}).get("commentCount", 0),
                    }
                    for v in top_videos
                ],
            }
        except Exception as e:
            return {"username": username, "error": str(e)}

    async def analyze_douyin_user(self, uid: str) -> dict[str, Any]:
        """Analyze a Douyin user's performance."""
        try:
            # Get user profile
            profile = await self.client.douyin_web.fetch_user_profile_by_uid(uid=uid)
            user_data = profile.get("data", {}).get("user", {})

            # Get user posts
            posts = await self.client.douyin_web.fetch_user_post_videos(
                sec_user_id=user_data.get("sec_uid", ""),
                count=50
            )
            post_list = posts.get("data", {}).get("aweme_list", [])

            # Calculate metrics
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
                "avg_likes": total_likes / max(len(post_list), 1),
                "avg_comments": total_comments / max(len(post_list), 1),
            }
        except Exception as e:
            return {"uid": uid, "error": str(e)}

    async def compare_competitors(self, competitors: dict[str, str]) -> dict[str, Any]:
        """Compare multiple competitors."""
        results = {}

        for platform, username in competitors.items():
            if platform == "tiktok":
                results[platform] = await self.analyze_tiktok_user(username)
            elif platform == "douyin":
                results[platform] = await self.analyze_douyin_user(username)

        # Calculate comparison metrics
        comparison = {
            "timestamp": datetime.now().isoformat(),
            "competitors": results,
            "summary": self._calculate_comparison(results),
        }

        return comparison

    def _calculate_comparison(self, results: dict[str, Any]) -> dict[str, Any]:
        """Calculate comparison summary."""
        summary = {
            "total_competitors": len(results),
            "platforms": list(results.keys()),
        }

        # Find best performer for each metric
        for metric in ["followers", "total_likes", "engagement_rate"]:
            best_platform = None
            best_value = 0
            for platform, data in results.items():
                if "error" not in data:
                    value = data.get(metric, 0)
                    if value > best_value:
                        best_value = value
                        best_platform = platform
            summary[f"best_{metric}"] = {
                "platform": best_platform,
                "value": best_value,
            }

        return summary


async def main():
    """Main function."""
    api_key = "YOUR_API_KEY"

    async with CompetitorAnalyzer(api_key) as analyzer:
        # Compare competitors
        print("=== Competitor Analysis ===")
        comparison = await analyzer.compare_competitors({
            "tiktok": "tiktok",
            "douyin": "123456789",
        })

        print(f"\nTimestamp: {comparison['timestamp']}")
        print(f"Competitors: {comparison['summary']['total_competitors']}")

        for platform, data in comparison["competitors"].items():
            print(f"\n{platform.upper()}:")
            if "error" in data:
                print(f"  Error: {data['error']}")
            else:
                print(f"  Followers: {data.get('followers', 'N/A')}")
                print(f"  Engagement Rate: {data.get('engagement_rate', 'N/A'):.2f}")

        print("\n=== Summary ===")
        for metric, value in comparison["summary"].items():
            if isinstance(value, dict):
                print(f"{metric}: {value.get('platform', 'N/A')} ({value.get('value', 'N/A')})")
            else:
                print(f"{metric}: {value}")


if __name__ == "__main__":
    asyncio.run(main())
