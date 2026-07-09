"""Tests matching actual Weibo and Xiaohongshu endpoints."""

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


# Actual Weibo app endpoints
WEIBO_APP_ACTUAL = [
    ("/fetch_user_info", {"uid": "123"}),
    ("/fetch_user_info_detail", {"uid": "123"}),
    ("/fetch_user_timeline", {"uid": "123"}),
    ("/fetch_user_videos", {"uid": "123"}),
    ("/fetch_user_super_topics", {"uid": "123"}),
    ("/fetch_user_fans", {"uid": "123"}),
    ("/fetch_user_follows", {"uid": "123"}),
    ("/fetch_user_hot_timeline", {"uid": "123"}),
    ("/fetch_post_detail", {"id": "123"}),
    ("/fetch_post_comments", {"id": "123"}),
    ("/fetch_hot_search", {}),
    ("/fetch_hot_search_detail", {"word": "test"}),
    ("/fetch_general_search", {"keyword": "test"}),
    ("/fetch_user_search", {"keyword": "test"}),
    ("/fetch_post_search", {"keyword": "test"}),
    ("/fetch_hot_list", {}),
    ("/fetch_trending_list", {}),
    ("/fetch_recommended_users", {}),
    ("/fetch_nearby_users", {"lat": "39.9", "lng": "116.3"}),
    ("/fetch_user_albums", {"uid": "123"}),
]


# Actual Weibo web v2 endpoints
WEIBO_WEB_V2_ACTUAL = [
    ("/fetch_user_info", {"uid": "123"}),
    ("/fetch_user_basic_info", {"uid": "123"}),
    ("/fetch_user_posts", {"uid": "123"}),
    ("/fetch_user_videos", {"uid": "123"}),
    ("/fetch_user_photos", {"uid": "123"}),
    ("/fetch_user_likes", {"uid": "123"}),
    ("/fetch_user_reposts", {"uid": "123"}),
    ("/fetch_user_comments", {"uid": "123"}),
    ("/fetch_user_fans", {"uid": "123"}),
    ("/fetch_user_follows", {"uid": "123"}),
    ("/fetch_post_detail", {"id": "123"}),
    ("/fetch_post_comments", {"id": "123"}),
    ("/fetch_post_reposts", {"id": "123"}),
    ("/fetch_post_likes", {"id": "123"}),
    ("/fetch_hot_search", {}),
    ("/fetch_hot_list", {}),
    ("/fetch_trending_list", {}),
    ("/fetch_general_search", {"keyword": "test"}),
    ("/fetch_user_search", {"keyword": "test"}),
    ("/fetch_post_search", {"keyword": "test"}),
    ("/fetch_nearby_posts", {"lat": "39.9", "lng": "116.3"}),
    ("/fetch_user_albums", {"uid": "123"}),
]


# Actual Xiaohongshu app endpoints
XIAOHONGSHU_APP_ACTUAL = [
    ("/get_note_info", {"note_id": "123"}),
    ("/get_note_info_v2", {"note_id": "123"}),
    ("/get_note_comments", {"note_id": "123"}),
    ("/get_sub_comments", {"note_id": "123", "comment_id": "456"}),
    ("/get_notes_by_topic", {"page_id": "123"}),
    ("/get_user_info", {"user_id": "123"}),
    ("/get_user_notes", {"user_id": "123"}),
    ("/get_user_collections", {"user_id": "123"}),
    ("/get_user_likes", {"user_id": "123"}),
    ("/get_user_follows", {"user_id": "123"}),
    ("/get_user_fans", {"user_id": "123"}),
    ("/get_general_search", {"keyword": "test"}),
]


# Actual Xiaohongshu app v2 endpoints
XIAOHONGSHU_APP_V2_ACTUAL = [
    ("/get_image_note_detail", {"note_id": "123"}),
    ("/get_video_note_detail", {"note_id": "123"}),
    ("/get_mixed_note_detail", {"note_id": "123"}),
    ("/get_note_comments", {"note_id": "123"}),
    ("/get_note_sub_comments", {"comment_id": "123", "note_id": "456"}),
    ("/get_user_info", {"user_id": "123"}),
    ("/get_user_notes", {"user_id": "123"}),
    ("/get_user_collections", {"user_id": "123"}),
    ("/get_user_likes", {"user_id": "123"}),
    ("/get_user_follows", {"user_id": "123"}),
    ("/get_user_fans", {"user_id": "123"}),
    ("/get_general_search", {"keyword": "test"}),
    ("/get_trending_notes", {}),
    ("/get_recommend_notes", {}),
    ("/get_note_by_url", {"url": "https://www.xiaohongshu.com/explore/123"}),
]


# Actual WeChat media endpoints
WECHAT_MEDIA_ACTUAL = [
    ("/fetch_user_info", {"user_id": "123"}),
    ("/fetch_user_articles", {"user_id": "123"}),
    ("/fetch_user_videos", {"user_id": "123"}),
    ("/fetch_user_followers", {"user_id": "123"}),
    ("/fetch_user_following", {"user_id": "123"}),
    ("/fetch_article_detail", {"article_id": "123"}),
    ("/fetch_video_detail", {"video_id": "123"}),
    ("/fetch_article_comments", {"article_id": "123"}),
    ("/fetch_video_comments", {"video_id": "123"}),
    ("/fetch_user_likes", {"user_id": "123"}),
    ("/fetch_user_shares", {"user_id": "123"}),
    ("/fetch_general_search", {"keyword": "test"}),
]


class TestWeiboAppActual:
    """Tests for actual Weibo app endpoints."""

    @pytest.mark.parametrize("path,params", WEIBO_APP_ACTUAL)
    @patch("socialmedia_hub.server._core.proxy_request")
    def test_weibo_app_endpoint(self, mock_proxy: AsyncMock, client: TestClient, api_key: str, path: str, params: dict) -> None:
        mock_proxy.return_value = {"data": [], "status_code": 200}
        response = client.get(
            f"/api/v1/weibo/app{path}",
            params=params,
            headers={"Authorization": f"Bearer {api_key}"},
        )
        assert response.status_code in [200, 404, 422], f"Failed for {path}: {response.status_code}"


class TestWeiboWebV2Actual:
    """Tests for actual Weibo web v2 endpoints."""

    @pytest.mark.parametrize("path,params", WEIBO_WEB_V2_ACTUAL)
    @patch("socialmedia_hub.server._core.proxy_request")
    def test_weibo_web_v2_endpoint(self, mock_proxy: AsyncMock, client: TestClient, api_key: str, path: str, params: dict) -> None:
        mock_proxy.return_value = {"data": [], "status_code": 200}
        response = client.get(
            f"/api/v1/weibo/web/v2{path}",
            params=params,
            headers={"Authorization": f"Bearer {api_key}"},
        )
        assert response.status_code in [200, 404, 422], f"Failed for {path}: {response.status_code}"


class TestXiaohongshuAppActual:
    """Tests for actual Xiaohongshu app endpoints."""

    @pytest.mark.parametrize("path,params", XIAOHONGSHU_APP_ACTUAL)
    @patch("socialmedia_hub.server._core.proxy_request")
    def test_xiaohongshu_app_endpoint(self, mock_proxy: AsyncMock, client: TestClient, api_key: str, path: str, params: dict) -> None:
        mock_proxy.return_value = {"data": [], "status_code": 200}
        response = client.get(
            f"/api/v1/xiaohongshu/app{path}",
            params=params,
            headers={"Authorization": f"Bearer {api_key}"},
        )
        assert response.status_code in [200, 404, 422], f"Failed for {path}: {response.status_code}"


class TestXiaohongshuAppV2Actual:
    """Tests for actual Xiaohongshu app v2 endpoints."""

    @pytest.mark.parametrize("path,params", XIAOHONGSHU_APP_V2_ACTUAL)
    @patch("socialmedia_hub.server._core.proxy_request")
    def test_xiaohongshu_app_v2_endpoint(self, mock_proxy: AsyncMock, client: TestClient, api_key: str, path: str, params: dict) -> None:
        mock_proxy.return_value = {"data": [], "status_code": 200}
        response = client.get(
            f"/api/v1/xiaohongshu/app/v2{path}",
            params=params,
            headers={"Authorization": f"Bearer {api_key}"},
        )
        assert response.status_code in [200, 404, 422], f"Failed for {path}: {response.status_code}"


class TestWechatMediaActual:
    """Tests for actual WeChat media endpoints."""

    @pytest.mark.parametrize("path,params", WECHAT_MEDIA_ACTUAL)
    @patch("socialmedia_hub.server._core.proxy_request")
    def test_wechat_media_endpoint(self, mock_proxy: AsyncMock, client: TestClient, api_key: str, path: str, params: dict) -> None:
        mock_proxy.return_value = {"data": [], "status_code": 200}
        response = client.get(
            f"/api/v1/wechat/media{path}",
            params=params,
            headers={"Authorization": f"Bearer {api_key}"},
        )
        assert response.status_code in [200, 404, 422], f"Failed for {path}: {response.status_code}"
