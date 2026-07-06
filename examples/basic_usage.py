"""Example: Using SocialMedia-Hub to fetch social media data."""

from socialmedia_hub import SocialMediaHub


def main():
    """Demo: Connect to SocialMedia-Hub server and fetch data."""

    # Connect to local server
    client = SocialMediaHub(
        api_key="YOUR_API_KEY",
        base_url="http://127.0.0.1:8000",
    )

    try:
        # Health check
        print("=== Health Check ===")
        # result = client.health_check()
        # print(result)

        # Example: Fetch a Douyin video
        print("\n=== Douyin Video ===")
        # video = client.douyin.fetch_video(video_id="7251234567890123456")
        # print(f"Title: {video.get('desc', 'N/A')}")

        # Example: Fetch a TikTok video
        print("\n=== TikTok Video ===")
        # video = client.tiktok.fetch_video(video_id="7251234567890123456")
        # print(f"Title: {video.get('desc', 'N/A')}")

        # Example: Fetch Instagram user
        print("\n=== Instagram User ===")
        # user = client.instagram.fetch_user(username="instagram")
        # print(f"Followers: {user.get('edge_followed_by', {}).get('count', 'N/A')}")

        # Example: Search Douyin
        print("\n=== Search Douyin ===")
        # results = client.douyin.search(keyword="python")
        # print(f"Found {len(results.get('data', []))} results")

        print("\nNote: Uncomment the actual API calls above to run them.")

    finally:
        client.close()


if __name__ == "__main__":
    main()
