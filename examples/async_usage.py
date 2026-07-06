"""Example: Async usage of SocialMedia-Hub."""

import asyncio


async def main():
    """Demo: Async usage."""
    # from socialmedia_hub import AsyncSocialMediaHub
    #
    # async with AsyncSocialMediaHub(
    #     api_key="YOUR_API_KEY",
    #     base_url="http://127.0.0.1:8000",
    # ) as client:
    #     # Fetch multiple videos concurrently
    #     video1 = await client.douyin.fetch_video(video_id="123")
    #     video2 = await client.tiktok.fetch_video(video_id="456")
    #     print(f"Video 1: {video1.get('desc')}")
    #     print(f"Video 2: {video2.get('desc')}")
    print("Async usage example - uncomment the code to run.")


if __name__ == "__main__":
    asyncio.run(main())
