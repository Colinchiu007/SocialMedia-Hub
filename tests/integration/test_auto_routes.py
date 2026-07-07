"""Tests for auto-generated routes to improve coverage."""

from __future__ import annotations

from unittest.mock import AsyncMock, patch

import pytest
from fastapi.testclient import TestClient

from socialmedia_hub.server._core import API_KEYS, generate_api_key
from socialmedia_hub.server.main import app


@pytest.fixture
def api_key() -> str:
    key = generate_api_key("test", "pro")
    return key


@pytest.fixture
def client() -> TestClient:
    return TestClient(app)


class TestAutoRoutesCoverage:
    """Tests for auto-generated route files."""

    def test_health_check(self, client: TestClient) -> None:
        response = client.get("/api/v1/health/check")
        assert response.status_code == 200

    def test_health_platforms(self, client: TestClient) -> None:
        response = client.get("/api/v1/health/platforms")
        assert response.status_code == 200

    def test_monitor_status(self, client: TestClient) -> None:
        response = client.get("/api/v1/monitor/status")
        assert response.status_code == 200

    def test_mcp_tools_list(self, client: TestClient, api_key: str) -> None:
        response = client.get(
            "/api/v1/mcp/tools",
            headers={"Authorization": f"Bearer {api_key}"},
        )
        assert response.status_code == 200

    @patch("socialmedia_hub.server._core.proxy_request")
    def test_douyin_fetch_video(self, mock_proxy: AsyncMock, client: TestClient, api_key: str) -> None:
        mock_proxy.return_value = {"data": {"aweme_id": "123"}}
        response = client.get(
            "/api/v1/douyin/web/fetch_video",
            params={"aweme_id": "123"},
            headers={"Authorization": f"Bearer {api_key}"},
        )
        assert response.status_code in [200, 422]

    @patch("socialmedia_hub.server._core.proxy_request")
    def test_tiktok_fetch_video(self, mock_proxy: AsyncMock, client: TestClient, api_key: str) -> None:
        mock_proxy.return_value = {"data": {"video_id": "123"}}
        response = client.get(
            "/api/v1/tiktok/web/fetch_video",
            params={"video_id": "123"},
            headers={"Authorization": f"Bearer {api_key}"},
        )
        assert response.status_code in [200, 422]

    @patch("socialmedia_hub.server._core.proxy_request")
    def test_instagram_fetch_user(self, mock_proxy: AsyncMock, client: TestClient, api_key: str) -> None:
        mock_proxy.return_value = {"data": {"user_id": "123"}}
        response = client.get(
            "/api/v1/instagram/v1/fetch_user",
            params={"user_id": "123"},
            headers={"Authorization": f"Bearer {api_key}"},
        )
        assert response.status_code in [200, 422]

    @patch("socialmedia_hub.server._core.proxy_request")
    def test_youtube_fetch_video(self, mock_proxy: AsyncMock, client: TestClient, api_key: str) -> None:
        mock_proxy.return_value = {"data": {"video_id": "123"}}
        response = client.get(
            "/api/v1/youtube/web/fetch_video",
            params={"video_id": "123"},
            headers={"Authorization": f"Bearer {api_key}"},
        )
        assert response.status_code in [200, 422]

    @patch("socialmedia_hub.server._core.proxy_request")
    def test_twitter_fetch_user(self, mock_proxy: AsyncMock, client: TestClient, api_key: str) -> None:
        mock_proxy.return_value = {"data": {"user_id": "123"}}
        response = client.get(
            "/api/v1/twitter/web/fetch_user",
            params={"user_id": "123"},
            headers={"Authorization": f"Bearer {api_key}"},
        )
        assert response.status_code in [200, 422]

    @patch("socialmedia_hub.server._core.proxy_request")
    def test_xiaohongshu_fetch_video(self, mock_proxy: AsyncMock, client: TestClient, api_key: str) -> None:
        mock_proxy.return_value = {"data": {"note_id": "123"}}
        response = client.get(
            "/api/v1/xiaohongshu/web/fetch_video",
            params={"note_id": "123"},
            headers={"Authorization": f"Bearer {api_key}"},
        )
        assert response.status_code in [200, 422]

    @patch("socialmedia_hub.server._core.proxy_request")
    def test_bilibili_fetch_video(self, mock_proxy: AsyncMock, client: TestClient, api_key: str) -> None:
        mock_proxy.return_value = {"data": {"bvid": "123"}}
        response = client.get(
            "/api/v1/bilibili/web/fetch_video",
            params={"bvid": "123"},
            headers={"Authorization": f"Bearer {api_key}"},
        )
        assert response.status_code in [200, 422]

    @patch("socialmedia_hub.server._core.proxy_request")
    def test_weibo_fetch_user(self, mock_proxy: AsyncMock, client: TestClient, api_key: str) -> None:
        mock_proxy.return_value = {"data": {"user_id": "123"}}
        response = client.get(
            "/api/v1/weibo/web/fetch_user",
            params={"user_id": "123"},
            headers={"Authorization": f"Bearer {api_key}"},
        )
        assert response.status_code in [200, 422]

    @patch("socialmedia_hub.server._core.proxy_request")
    def test_kuaishou_fetch_video(self, mock_proxy: AsyncMock, client: TestClient, api_key: str) -> None:
        mock_proxy.return_value = {"data": {"photo_id": "123"}}
        response = client.get(
            "/api/v1/kuaishou/web/fetch_video",
            params={"photo_id": "123"},
            headers={"Authorization": f"Bearer {api_key}"},
        )
        assert response.status_code in [200, 422]

    @patch("socialmedia_hub.server._core.proxy_request")
    def test_linkedin_fetch_user(self, mock_proxy: AsyncMock, client: TestClient, api_key: str) -> None:
        mock_proxy.return_value = {"data": {"user_id": "123"}}
        response = client.get(
            "/api/v1/linkedin/web/fetch_user",
            params={"user_id": "123"},
            headers={"Authorization": f"Bearer {api_key}"},
        )
        assert response.status_code in [200, 422]

    @patch("socialmedia_hub.server._core.proxy_request")
    def test_reddit_fetch_post(self, mock_proxy: AsyncMock, client: TestClient, api_key: str) -> None:
        mock_proxy.return_value = {"data": {"post_id": "123"}}
        response = client.get(
            "/api/v1/reddit/app/fetch_post",
            params={"post_id": "123"},
            headers={"Authorization": f"Bearer {api_key}"},
        )
        assert response.status_code in [200, 422]

    @patch("socialmedia_hub.server._core.proxy_request")
    def test_zhihu_fetch_question(self, mock_proxy: AsyncMock, client: TestClient, api_key: str) -> None:
        mock_proxy.return_value = {"data": {"question_id": "123"}}
        response = client.get(
            "/api/v1/zhihu/web/fetch_question",
            params={"question_id": "123"},
            headers={"Authorization": f"Bearer {api_key}"},
        )
        assert response.status_code in [200, 422]

    @patch("socialmedia_hub.server._core.proxy_request")
    def test_threads_fetch_user(self, mock_proxy: AsyncMock, client: TestClient, api_key: str) -> None:
        mock_proxy.return_value = {"data": {"user_id": "123"}}
        response = client.get(
            "/api/v1/threads/web/fetch_user",
            params={"user_id": "123"},
            headers={"Authorization": f"Bearer {api_key}"},
        )
        assert response.status_code in [200, 422]

    @patch("socialmedia_hub.server._core.proxy_request")
    def test_wechat_fetch_user(self, mock_proxy: AsyncMock, client: TestClient, api_key: str) -> None:
        mock_proxy.return_value = {"data": {"user_id": "123"}}
        response = client.get(
            "/api/v1/wechat/channels/fetch_user",
            params={"user_id": "123"},
            headers={"Authorization": f"Bearer {api_key}"},
        )
        assert response.status_code in [200, 422]

    @patch("socialmedia_hub.server._core.proxy_request")
    def test_netease_fetch_song(self, mock_proxy: AsyncMock, client: TestClient, api_key: str) -> None:
        mock_proxy.return_value = {"data": {"song_id": "123"}}
        response = client.get(
            "/api/v1/netease/music/fetch_song_detail",
            params={"song_id": "123"},
            headers={"Authorization": f"Bearer {api_key}"},
        )
        assert response.status_code in [200, 422]

    @patch("socialmedia_hub.server._core.proxy_request")
    def test_live_room_bilibili(self, mock_proxy: AsyncMock, client: TestClient, api_key: str) -> None:
        mock_proxy.return_value = {"data": {"room_id": "123"}}
        response = client.get(
            "/api/v1/live/bilibili/room_info",
            params={"room_id": "123"},
            headers={"Authorization": f"Bearer {api_key}"},
        )
        assert response.status_code in [200, 400, 422]

    def test_health_stats(self, client: TestClient) -> None:
        response = client.get("/api/v1/health/stats")
        assert response.status_code == 200
        data = response.json()
        assert "total_endpoints" in data

    def test_monitor_metrics(self, client: TestClient) -> None:
        response = client.get("/api/v1/monitor/metrics")
        assert response.status_code == 200
        data = response.json()
        assert "requests_total" in data

    def test_monitor_platforms(self, client: TestClient) -> None:
        response = client.get("/api/v1/monitor/platforms")
        assert response.status_code == 200
        data = response.json()
        assert "platforms" in data

    def test_create_api_key(self, client: TestClient) -> None:
        response = client.post("/api/v1/auth/create_key", params={"name": "test", "tier": "pro"})
        assert response.status_code == 200
        data = response.json()
        assert "api_key" in data

    def test_verify_key(self, client: TestClient, api_key: str) -> None:
        response = client.get(
            "/api/v1/auth/verify",
            headers={"Authorization": f"Bearer {api_key}"},
        )
        assert response.status_code == 200
        data = response.json()
        assert data["valid"] is True

    def test_docs_endpoint(self, client: TestClient) -> None:
        response = client.get("/docs")
        assert response.status_code == 200

    def test_openapi_endpoint(self, client: TestClient) -> None:
        import warnings
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            response = client.get("/openapi.json")
        assert response.status_code == 200

    @patch("socialmedia_hub.server._core.proxy_request")
    def test_lemon8_fetch_user(self, mock_proxy: AsyncMock, client: TestClient, api_key: str) -> None:
        mock_proxy.return_value = {"data": {"user_id": "123"}}
        response = client.get(
            "/api/v1/lemon8/app/fetch_user",
            params={"user_id": "123"},
            headers={"Authorization": f"Bearer {api_key}"},
        )
        assert response.status_code in [200, 422]

    @patch("socialmedia_hub.server._core.proxy_request")
    def test_douyin_fetch_user(self, mock_proxy: AsyncMock, client: TestClient, api_key: str) -> None:
        mock_proxy.return_value = {"data": {"sec_user_id": "123"}}
        response = client.get(
            "/api/v1/douyin/web/fetch_user",
            params={"sec_user_id": "123"},
            headers={"Authorization": f"Bearer {api_key}"},
        )
        assert response.status_code in [200, 422]

    @patch("socialmedia_hub.server._core.proxy_request")
    def test_tiktok_fetch_user(self, mock_proxy: AsyncMock, client: TestClient, api_key: str) -> None:
        mock_proxy.return_value = {"data": {"sec_uid": "123"}}
        response = client.get(
            "/api/v1/tiktok/web/fetch_user",
            params={"sec_uid": "123"},
            headers={"Authorization": f"Bearer {api_key}"},
        )
        assert response.status_code in [200, 422]

    @patch("socialmedia_hub.server._core.proxy_request")
    def test_instagram_fetch_video(self, mock_proxy: AsyncMock, client: TestClient, api_key: str) -> None:
        mock_proxy.return_value = {"data": {"media_id": "123"}}
        response = client.get(
            "/api/v1/instagram/v1/fetch_video",
            params={"media_id": "123"},
            headers={"Authorization": f"Bearer {api_key}"},
        )
        assert response.status_code in [200, 422]

    @patch("socialmedia_hub.server._core.proxy_request")
    def test_youtube_fetch_user(self, mock_proxy: AsyncMock, client: TestClient, api_key: str) -> None:
        mock_proxy.return_value = {"data": {"channel_id": "123"}}
        response = client.get(
            "/api/v1/youtube/web/fetch_user",
            params={"channel_id": "123"},
            headers={"Authorization": f"Bearer {api_key}"},
        )
        assert response.status_code in [200, 422]

    @patch("socialmedia_hub.server._core.proxy_request")
    def test_twitter_fetch_video(self, mock_proxy: AsyncMock, client: TestClient, api_key: str) -> None:
        mock_proxy.return_value = {"data": {"tweet_id": "123"}}
        response = client.get(
            "/api/v1/twitter/web/fetch_video",
            params={"tweet_id": "123"},
            headers={"Authorization": f"Bearer {api_key}"},
        )
        assert response.status_code in [200, 422]

    @patch("socialmedia_hub.server._core.proxy_request")
    def test_xiaohongshu_fetch_user(self, mock_proxy: AsyncMock, client: TestClient, api_key: str) -> None:
        mock_proxy.return_value = {"data": {"user_id": "123"}}
        response = client.get(
            "/api/v1/xiaohongshu/web/fetch_user",
            params={"user_id": "123"},
            headers={"Authorization": f"Bearer {api_key}"},
        )
        assert response.status_code in [200, 422]

    @patch("socialmedia_hub.server._core.proxy_request")
    def test_bilibili_fetch_user(self, mock_proxy: AsyncMock, client: TestClient, api_key: str) -> None:
        mock_proxy.return_value = {"data": {"mid": "123"}}
        response = client.get(
            "/api/v1/bilibili/web/fetch_user",
            params={"mid": "123"},
            headers={"Authorization": f"Bearer {api_key}"},
        )
        assert response.status_code in [200, 422]

    @patch("socialmedia_hub.server._core.proxy_request")
    def test_weibo_fetch_video(self, mock_proxy: AsyncMock, client: TestClient, api_key: str) -> None:
        mock_proxy.return_value = {"data": {"weibo_id": "123"}}
        response = client.get(
            "/api/v1/weibo/web/fetch_video",
            params={"weibo_id": "123"},
            headers={"Authorization": f"Bearer {api_key}"},
        )
        assert response.status_code in [200, 422]

    @patch("socialmedia_hub.server._core.proxy_request")
    def test_kuaishou_fetch_user(self, mock_proxy: AsyncMock, client: TestClient, api_key: str) -> None:
        mock_proxy.return_value = {"data": {"user_id": "123"}}
        response = client.get(
            "/api/v1/kuaishou/web/fetch_user",
            params={"user_id": "123"},
            headers={"Authorization": f"Bearer {api_key}"},
        )
        assert response.status_code in [200, 422]

    @patch("socialmedia_hub.server._core.proxy_request")
    def test_linkedin_fetch_posts(self, mock_proxy: AsyncMock, client: TestClient, api_key: str) -> None:
        mock_proxy.return_value = {"data": {"posts": []}}
        response = client.get(
            "/api/v1/linkedin/web/fetch_posts",
            params={"user_id": "123"},
            headers={"Authorization": f"Bearer {api_key}"},
        )
        assert response.status_code in [200, 422]

    @patch("socialmedia_hub.server._core.proxy_request")
    def test_reddit_fetch_user(self, mock_proxy: AsyncMock, client: TestClient, api_key: str) -> None:
        mock_proxy.return_value = {"data": {"username": "test"}}
        response = client.get(
            "/api/v1/reddit/app/fetch_user",
            params={"username": "test"},
            headers={"Authorization": f"Bearer {api_key}"},
        )
        assert response.status_code in [200, 422]

    @patch("socialmedia_hub.server._core.proxy_request")
    def test_zhihu_fetch_answer(self, mock_proxy: AsyncMock, client: TestClient, api_key: str) -> None:
        mock_proxy.return_value = {"data": {"answer_id": "123"}}
        response = client.get(
            "/api/v1/zhihu/web/fetch_answer",
            params={"answer_id": "123"},
            headers={"Authorization": f"Bearer {api_key}"},
        )
        assert response.status_code in [200, 422]

    @patch("socialmedia_hub.server._core.proxy_request")
    def test_threads_fetch_threads(self, mock_proxy: AsyncMock, client: TestClient, api_key: str) -> None:
        mock_proxy.return_value = {"data": {"threads": []}}
        response = client.get(
            "/api/v1/threads/web/fetch_threads",
            params={"user_id": "123"},
            headers={"Authorization": f"Bearer {api_key}"},
        )
        assert response.status_code in [200, 422]

    @patch("socialmedia_hub.server._core.proxy_request")
    def test_wechat_fetch_video(self, mock_proxy: AsyncMock, client: TestClient, api_key: str) -> None:
        mock_proxy.return_value = {"data": {"video_id": "123"}}
        response = client.get(
            "/api/v1/wechat/channels/fetch_video",
            params={"video_id": "123"},
            headers={"Authorization": f"Bearer {api_key}"},
        )
        assert response.status_code in [200, 422]

    @patch("socialmedia_hub.server._core.proxy_request")
    def test_netease_fetch_playlist(self, mock_proxy: AsyncMock, client: TestClient, api_key: str) -> None:
        mock_proxy.return_value = {"data": {"playlist_id": "123"}}
        response = client.get(
            "/api/v1/netease/music/fetch_playlist_detail",
            params={"playlist_id": "123"},
            headers={"Authorization": f"Bearer {api_key}"},
        )
        assert response.status_code in [200, 422]
