"""Example: Server setup and API key management."""

import httpx


def main():
    """Demo: Server setup."""
    base_url = "http://127.0.0.1:8000"

    with httpx.Client(timeout=10) as client:
        # 1. Check server health
        print("=== Health Check ===")
        resp = client.get(f"{base_url}/api/v1/health/check")
        print(resp.json())

        # 2. Create an API key
        print("\n=== Create API Key ===")
        resp = client.post(
            f"{base_url}/api/v1/auth/create_key",
            params={"name": "demo", "tier": "pro"},
        )
        key_data = resp.json()
        api_key = key_data["api_key"]
        print(f"Created key: {api_key[:20]}...")

        # 3. Verify the key
        print("\n=== Verify Key ===")
        resp = client.get(
            f"{base_url}/api/v1/auth/verify",
            headers={"Authorization": f"Bearer {api_key}"},
        )
        print(resp.json())

        # 4. List platforms
        print("\n=== Platforms ===")
        resp = client.get(f"{base_url}/api/v1/health/platforms")
        print(resp.json())

        # 5. Fetch a video (example)
        print("\n=== Fetch Douyin Video ===")
        resp = client.get(
            f"{base_url}/api/v1/douyin/web/fetch_video",
            params={"video_id": "7251234567890123456"},
            headers={"Authorization": f"Bearer {api_key}"},
        )
        print(resp.status_code, resp.json().get("code"))


if __name__ == "__main__":
    main()
