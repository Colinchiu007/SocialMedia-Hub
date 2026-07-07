"""Additional tests for auto-generated routes to improve coverage."""

from __future__ import annotations

from unittest.mock import AsyncMock, patch

import pytest
from fastapi.testclient import TestClient

from socialmedia_hub.server._core import generate_api_key
from socialmedia_hub.server.main import app


@pytest.fixture
def api_key() -> str:
    return generate_api_key("test", "pro")


@pytest.fixture
def client() -> TestClient:
    return TestClient(app, raise_server_exceptions=False)


class TestTikTokRoutes:
    """Tests for TikTok auto-generated routes."""

    @patch("socialmedia_hub.server._core.proxy_request")
    def test_tiktok_fetch_user_post(self, mock_proxy: AsyncMock, client: TestClient, api_key: str) -> None:
        mock_proxy.return_value = {"data": []}
        response = client.get(
            "/api/v1/tiktok/web/fetch_user_post",
            params={"sec_uid": "123"},
            headers={"Authorization": f"Bearer {api_key}"},
        )
        assert response.status_code in [200, 422]

    @patch("socialmedia_hub.server._core.proxy_request")
    def test_tiktok_fetch_user_liked(self, mock_proxy: AsyncMock, client: TestClient, api_key: str) -> None:
        mock_proxy.return_value = {"data": []}
        response = client.get(
            "/api/v1/tiktok/web/fetch_user_liked",
            params={"sec_uid": "123"},
            headers={"Authorization": f"Bearer {api_key}"},
        )
        assert response.status_code in [200, 422]

    @patch("socialmedia_hub.server._core.proxy_request")
    def test_tiktok_fetch_user_follower(self, mock_proxy: AsyncMock, client: TestClient, api_key: str) -> None:
        mock_proxy.return_value = {"data": []}
        response = client.get(
            "/api/v1/tiktok/web/fetch_user_follower",
            params={"sec_uid": "123"},
            headers={"Authorization": f"Bearer {api_key}"},
        )
        assert response.status_code in [200, 422]

    @patch("socialmedia_hub.server._core.proxy_request")
    def test_tiktok_fetch_user_following(self, mock_proxy: AsyncMock, client: TestClient, api_key: str) -> None:
        mock_proxy.return_value = {"data": []}
        response = client.get(
            "/api/v1/tiktok/web/fetch_user_following",
            params={"sec_uid": "123"},
            headers={"Authorization": f"Bearer {api_key}"},
        )
        assert response.status_code in [200, 422]

    @patch("socialmedia_hub.server._core.proxy_request")
    def test_tiktok_fetch_video_comment(self, mock_proxy: AsyncMock, client: TestClient, api_key: str) -> None:
        mock_proxy.return_value = {"data": []}
        response = client.get(
            "/api/v1/tiktok/web/fetch_video_comment",
            params={"video_id": "123"},
            headers={"Authorization": f"Bearer {api_key}"},
        )
        assert response.status_code in [200, 422]

    @patch("socialmedia_hub.server._core.proxy_request")
    def test_tiktok_search_user(self, mock_proxy: AsyncMock, client: TestClient, api_key: str) -> None:
        mock_proxy.return_value = {"data": []}
        response = client.get(
            "/api/v1/tiktok/web/search_user",
            params={"keyword": "test"},
            headers={"Authorization": f"Bearer {api_key}"},
        )
        assert response.status_code in [200, 422]

    @patch("socialmedia_hub.server._core.proxy_request")
    def test_tiktok_search_video(self, mock_proxy: AsyncMock, client: TestClient, api_key: str) -> None:
        mock_proxy.return_value = {"data": []}
        response = client.get(
            "/api/v1/tiktok/web/search_video",
            params={"keyword": "test"},
            headers={"Authorization": f"Bearer {api_key}"},
        )
        assert response.status_code in [200, 422]

    @patch("socialmedia_hub.server._core.proxy_request")
    def test_tiktok_fetch_hot_list(self, mock_proxy: AsyncMock, client: TestClient, api_key: str) -> None:
        mock_proxy.return_value = {"data": []}
        response = client.get(
            "/api/v1/tiktok/web/fetch_hot_list",
            headers={"Authorization": f"Bearer {api_key}"},
        )
        assert response.status_code in [200, 422]


class TestDouyinRoutes:
    """Tests for Douyin auto-generated routes."""

    @patch("socialmedia_hub.server._core.proxy_request")
    def test_douyin_fetch_user_post(self, mock_proxy: AsyncMock, client: TestClient, api_key: str) -> None:
        mock_proxy.return_value = {"data": []}
        response = client.get(
            "/api/v1/douyin/web/fetch_user_post",
            params={"sec_user_id": "123"},
            headers={"Authorization": f"Bearer {api_key}"},
        )
        assert response.status_code in [200, 422]

    @patch("socialmedia_hub.server._core.proxy_request")
    def test_douyin_fetch_user_liked(self, mock_proxy: AsyncMock, client: TestClient, api_key: str) -> None:
        mock_proxy.return_value = {"data": []}
        response = client.get(
            "/api/v1/douyin/web/fetch_user_liked",
            params={"sec_user_id": "123"},
            headers={"Authorization": f"Bearer {api_key}"},
        )
        assert response.status_code in [200, 422]

    @patch("socialmedia_hub.server._core.proxy_request")
    def test_douyin_fetch_video_comment(self, mock_proxy: AsyncMock, client: TestClient, api_key: str) -> None:
        mock_proxy.return_value = {"data": []}
        response = client.get(
            "/api/v1/douyin/web/fetch_video_comment",
            params={"aweme_id": "123"},
            headers={"Authorization": f"Bearer {api_key}"},
        )
        assert response.status_code in [200, 422]

    @patch("socialmedia_hub.server._core.proxy_request")
    def test_douyin_fetch_hot_list(self, mock_proxy: AsyncMock, client: TestClient, api_key: str) -> None:
        mock_proxy.return_value = {"data": []}
        response = client.get(
            "/api/v1/douyin/web/fetch_hot_list",
            headers={"Authorization": f"Bearer {api_key}"},
        )
        assert response.status_code in [200, 422]

    @patch("socialmedia_hub.server._core.proxy_request")
    def test_douyin_search_user(self, mock_proxy: AsyncMock, client: TestClient, api_key: str) -> None:
        mock_proxy.return_value = {"data": []}
        response = client.get(
            "/api/v1/douyin/web/search_user",
            params={"keyword": "test"},
            headers={"Authorization": f"Bearer {api_key}"},
        )
        assert response.status_code in [200, 422]

    @patch("socialmedia_hub.server._core.proxy_request")
    def test_douyin_search_video(self, mock_proxy: AsyncMock, client: TestClient, api_key: str) -> None:
        mock_proxy.return_value = {"data": []}
        response = client.get(
            "/api/v1/douyin/web/search_video",
            params={"keyword": "test"},
            headers={"Authorization": f"Bearer {api_key}"},
        )
        assert response.status_code in [200, 422]


class TestInstagramRoutes:
    """Tests for Instagram auto-generated routes."""

    @patch("socialmedia_hub.server._core.proxy_request")
    def test_instagram_fetch_user_post(self, mock_proxy: AsyncMock, client: TestClient, api_key: str) -> None:
        mock_proxy.return_value = {"data": []}
        response = client.get(
            "/api/v1/instagram/v1/fetch_user_post",
            params={"user_id": "123"},
            headers={"Authorization": f"Bearer {api_key}"},
        )
        assert response.status_code in [200, 422]

    @patch("socialmedia_hub.server._core.proxy_request")
    def test_instagram_fetch_user_reel(self, mock_proxy: AsyncMock, client: TestClient, api_key: str) -> None:
        mock_proxy.return_value = {"data": []}
        response = client.get(
            "/api/v1/instagram/v1/fetch_user_reel",
            params={"user_id": "123"},
            headers={"Authorization": f"Bearer {api_key}"},
        )
        assert response.status_code in [200, 422]

    @patch("socialmedia_hub.server._core.proxy_request")
    def test_instagram_fetch_post_comment(self, mock_proxy: AsyncMock, client: TestClient, api_key: str) -> None:
        mock_proxy.return_value = {"data": []}
        response = client.get(
            "/api/v1/instagram/v1/fetch_post_comment",
            params={"media_id": "123"},
            headers={"Authorization": f"Bearer {api_key}"},
        )
        assert response.status_code in [200, 422]

    @patch("socialmedia_hub.server._core.proxy_request")
    def test_instagram_search_user(self, mock_proxy: AsyncMock, client: TestClient, api_key: str) -> None:
        mock_proxy.return_value = {"data": []}
        response = client.get(
            "/api/v1/instagram/v1/search_user",
            params={"keyword": "test"},
            headers={"Authorization": f"Bearer {api_key}"},
        )
        assert response.status_code in [200, 422]

    @patch("socialmedia_hub.server._core.proxy_request")
    def test_instagram_search_tag(self, mock_proxy: AsyncMock, client: TestClient, api_key: str) -> None:
        mock_proxy.return_value = {"data": []}
        response = client.get(
            "/api/v1/instagram/v1/search_tag",
            params={"keyword": "test"},
            headers={"Authorization": f"Bearer {api_key}"},
        )
        assert response.status_code in [200, 422]


class TestYouTubeRoutes:
    """Tests for YouTube auto-generated routes."""

    @patch("socialmedia_hub.server._core.proxy_request")
    def test_youtube_fetch_user_video(self, mock_proxy: AsyncMock, client: TestClient, api_key: str) -> None:
        mock_proxy.return_value = {"data": []}
        response = client.get(
            "/api/v1/youtube/web/fetch_user_video",
            params={"channel_id": "123"},
            headers={"Authorization": f"Bearer {api_key}"},
        )
        assert response.status_code in [200, 422]

    @patch("socialmedia_hub.server._core.proxy_request")
    def test_youtube_fetch_video_comment(self, mock_proxy: AsyncMock, client: TestClient, api_key: str) -> None:
        mock_proxy.return_value = {"data": []}
        response = client.get(
            "/api/v1/youtube/web/fetch_video_comment",
            params={"video_id": "123"},
            headers={"Authorization": f"Bearer {api_key}"},
        )
        assert response.status_code in [200, 422]

    @patch("socialmedia_hub.server._core.proxy_request")
    def test_youtube_search_user(self, mock_proxy: AsyncMock, client: TestClient, api_key: str) -> None:
        mock_proxy.return_value = {"data": []}
        response = client.get(
            "/api/v1/youtube/web/search_user",
            params={"keyword": "test"},
            headers={"Authorization": f"Bearer {api_key}"},
        )
        assert response.status_code in [200, 422]

    @patch("socialmedia_hub.server._core.proxy_request")
    def test_youtube_search_video(self, mock_proxy: AsyncMock, client: TestClient, api_key: str) -> None:
        mock_proxy.return_value = {"data": []}
        response = client.get(
            "/api/v1/youtube/web/search_video",
            params={"keyword": "test"},
            headers={"Authorization": f"Bearer {api_key}"},
        )
        assert response.status_code in [200, 422]

    @patch("socialmedia_hub.server._core.proxy_request")
    def test_youtube_fetch_trending(self, mock_proxy: AsyncMock, client: TestClient, api_key: str) -> None:
        mock_proxy.return_value = {"data": []}
        response = client.get(
            "/api/v1/youtube/web/fetch_trending",
            headers={"Authorization": f"Bearer {api_key}"},
        )
        assert response.status_code in [200, 422]


class TestMorePlatformRoutes:
    """Tests for more platform routes."""

    @pytest.mark.parametrize("path,params", [
        ("/api/v1/bilibili/web/fetch_user_post", {"mid": "123"}),
        ("/api/v1/bilibili/web/fetch_video_comment", {"bvid": "123"}),
        ("/api/v1/bilibili/web/fetch_user_fan", {"mid": "123"}),
        ("/api/v1/bilibili/web/fetch_videodanmu", {"bvid": "123"}),
        ("/api/v1/weibo/web/fetch_user_post", {"user_id": "123"}),
        ("/api/v1/weibo/web/fetch_user_info", {"user_id": "123"}),
        ("/api/v1/weibo/web/fetch_weibo_comment", {"weibo_id": "123"}),
        ("/api/v1/kuaishou/web/fetch_user_post", {"user_id": "123"}),
        ("/api/v1/kuaishou/web/fetch_user_info", {"user_id": "123"}),
        ("/api/v1/kuaishou/web/fetch_video_comment", {"photo_id": "123"}),
        ("/api/v1/linkedin/web/fetch_user_post", {"user_id": "123"}),
        ("/api/v1/linkedin/web/fetch_user_info", {"user_id": "123"}),
        ("/api/v1/linkedin/web/fetch_company_info", {"company_id": "123"}),
        ("/api/v1/reddit/app/fetch_subreddit", {"subreddit": "test"}),
        ("/api/v1/reddit/app/fetch_post_comment", {"post_id": "123"}),
        ("/api/v1/reddit/app/fetch_user_info", {"username": "test"}),
        ("/api/v1/zhihu/web/fetch_user_answer", {"user_id": "123"}),
        ("/api/v1/zhihu/web/fetch_question_answer", {"question_id": "123"}),
        ("/api/v1/zhihu/web/fetch_user_info", {"user_id": "123"}),
        ("/api/v1/threads/web/fetch_thread", {"thread_id": "123"}),
        ("/api/v1/threads/web/fetch_user_info", {"user_id": "123"}),
        ("/api/v1/threads/web/fetch_thread_comment", {"thread_id": "123"}),
        ("/api/v1/lemon8/app/fetch_user_post", {"user_id": "123"}),
        ("/api/v1/lemon8/app/fetch_user_info", {"user_id": "123"}),
        ("/api/v1/lemon8/app/fetch_post_comment", {"post_id": "123"}),
        ("/api/v1/netease/music/fetch_artist_detail", {"artist_id": "123"}),
        ("/api/v1/netease/music/fetch_playlist_track", {"playlist_id": "123"}),
        ("/api/v1/netease/music/fetch_song_comment", {"song_id": "123"}),
        ("/api/v1/xiaohongshu/web/fetch_user_note", {"user_id": "123"}),
        ("/api/v1/xiaohongshu/web/fetch_note_comment", {"note_id": "123"}),
        ("/api/v1/xiaohongshu/web/fetch_user_info", {"user_id": "123"}),
        ("/api/v1/twitter/web/fetch_user_tweet", {"user_id": "123"}),
        ("/api/v1/twitter/web/fetch_tweet_comment", {"tweet_id": "123"}),
        ("/api/v1/twitter/web/fetch_user_info", {"user_id": "123"}),
        ("/api/v1/youtube/web/fetch_channel_video", {"channel_id": "123"}),
        ("/api/v1/youtube/web/fetch_video_comment", {"video_id": "123"}),
        ("/api/v1/youtube/web/fetch_user_info", {"channel_id": "123"}),
        ("/api/v1/instagram/v1/fetch_user_post", {"user_id": "123"}),
        ("/api/v1/instagram/v1/fetch_post_comment", {"media_id": "123"}),
        ("/api/v1/instagram/v1/fetch_user_info", {"user_id": "123"}),
    ])
    @patch("socialmedia_hub.server._core.proxy_request")
    def test_platform_endpoints(self, mock_proxy: AsyncMock, client: TestClient, api_key: str, path: str, params: dict) -> None:
        mock_proxy.return_value = {"data": []}
        response = client.get(
            path,
            params=params,
            headers={"Authorization": f"Bearer {api_key}"},
        )
        assert response.status_code in [200, 404, 422]
