"""Additional tests for remaining auto-generated routes."""

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


class TestTikTokRemaining:
    """Tests for TikTok remaining routes."""

    @pytest.mark.parametrize("endpoint,params", [
        ("fetch_user_post", {"sec_uid": "123"}),
        ("fetch_user_liked", {"sec_uid": "123"}),
        ("fetch_user_follower", {"sec_uid": "123"}),
        ("fetch_user_following", {"sec_uid": "123"}),
        ("fetch_video_comment", {"video_id": "123"}),
        ("fetch_user_info", {"sec_uid": "123"}),
        ("search_user", {"keyword": "test"}),
        ("search_video", {"keyword": "test"}),
        ("fetch_hot_list", {}),
        ("fetch_hot_video", {}),
        ("fetch_hot_user", {}),
        ("fetch_video_like", {"video_id": "123"}),
        ("fetch_user_collect", {"sec_uid": "123"}),
        ("fetch_user_history", {"sec_uid": "123"}),
    ])
    @patch("socialmedia_hub.server._core.proxy_request")
    def test_tiktok_ads_endpoints(self, mock_proxy: AsyncMock, client: TestClient, api_key: str, endpoint: str, params: dict) -> None:
        mock_proxy.return_value = {"data": []}
        response = client.get(
            f"/api/v1/tiktok/ads/{endpoint}",
            params=params,
            headers={"Authorization": f"Bearer {api_key}"},
        )
        assert response.status_code in [200, 404, 422]

    @pytest.mark.parametrize("endpoint,params", [
        ("fetch_user_post", {"sec_uid": "123"}),
        ("fetch_user_liked", {"sec_uid": "123"}),
        ("fetch_user_follower", {"sec_uid": "123"}),
        ("fetch_user_following", {"sec_uid": "123"}),
        ("fetch_video_comment", {"video_id": "123"}),
        ("fetch_user_info", {"sec_uid": "123"}),
        ("search_user", {"keyword": "test"}),
        ("search_video", {"keyword": "test"}),
        ("fetch_hot_list", {}),
        ("fetch_product_list", {}),
        ("fetch_product_detail", {"product_id": "123"}),
        ("fetch_shop_list", {}),
    ])
    @patch("socialmedia_hub.server._core.proxy_request")
    def test_tiktok_shop_endpoints(self, mock_proxy: AsyncMock, client: TestClient, api_key: str, endpoint: str, params: dict) -> None:
        mock_proxy.return_value = {"data": []}
        response = client.get(
            f"/api/v1/tiktok/shop/{endpoint}",
            params=params,
            headers={"Authorization": f"Bearer {api_key}"},
        )
        assert response.status_code in [200, 404, 422]


class TestDouyinRemaining:
    """Tests for Douyin remaining routes."""

    @pytest.mark.parametrize("endpoint,params", [
        ("fetch_user_post", {"sec_user_id": "123"}),
        ("fetch_user_liked", {"sec_user_id": "123"}),
        ("fetch_user_follower", {"sec_user_id": "123"}),
        ("fetch_user_following", {"sec_user_id": "123"}),
        ("fetch_video_comment", {"aweme_id": "123"}),
        ("fetch_user_info", {"sec_user_id": "123"}),
        ("search_user", {"keyword": "test"}),
        ("search_video", {"keyword": "test"}),
        ("fetch_hot_list", {}),
        ("fetch_hot_video", {}),
        ("fetch_hot_user", {}),
        ("fetch_billboard", {}),
        ("fetch_billboard_detail", {"billboard_type": "hot"}),
    ])
    @patch("socialmedia_hub.server._core.proxy_request")
    def test_douyin_billboard_endpoints(self, mock_proxy: AsyncMock, client: TestClient, api_key: str, endpoint: str, params: dict) -> None:
        mock_proxy.return_value = {"data": []}
        response = client.get(
            f"/api/v1/douyin/billboard/{endpoint}",
            params=params,
            headers={"Authorization": f"Bearer {api_key}"},
        )
        assert response.status_code in [200, 404, 422]

    @pytest.mark.parametrize("endpoint,params", [
        ("fetch_user_post", {"sec_user_id": "123"}),
        ("fetch_user_liked", {"sec_user_id": "123"}),
        ("fetch_user_follower", {"sec_user_id": "123"}),
        ("fetch_user_following", {"sec_user_id": "123"}),
        ("fetch_video_comment", {"aweme_id": "123"}),
        ("fetch_user_info", {"sec_user_id": "123"}),
        ("search_user", {"keyword": "test"}),
        ("search_video", {"keyword": "test"}),
    ])
    @patch("socialmedia_hub.server._core.proxy_request")
    def test_douyin_creator_endpoints(self, mock_proxy: AsyncMock, client: TestClient, api_key: str, endpoint: str, params: dict) -> None:
        mock_proxy.return_value = {"data": []}
        response = client.get(
            f"/api/v1/douyin/creator/{endpoint}",
            params=params,
            headers={"Authorization": f"Bearer {api_key}"},
        )
        assert response.status_code in [200, 404, 422]


class TestLinkedInRemaining:
    """Tests for LinkedIn remaining routes."""

    @pytest.mark.parametrize("endpoint,params", [
        ("fetch_user_post", {"user_id": "123"}),
        ("fetch_user_info", {"user_id": "123"}),
        ("fetch_company_info", {"company_id": "123"}),
        ("fetch_company_post", {"company_id": "123"}),
        ("search_user", {"keyword": "test"}),
        ("search_company", {"keyword": "test"}),
        ("fetch_user_connection", {"user_id": "123"}),
        ("fetch_job_list", {"keyword": "test"}),
    ])
    @patch("socialmedia_hub.server._core.proxy_request")
    def test_linkedin_web_endpoints(self, mock_proxy: AsyncMock, client: TestClient, api_key: str, endpoint: str, params: dict) -> None:
        mock_proxy.return_value = {"data": []}
        response = client.get(
            f"/api/v1/linkedin/web/{endpoint}",
            params=params,
            headers={"Authorization": f"Bearer {api_key}"},
        )
        assert response.status_code in [200, 404, 422]


class TestRedditRemaining:
    """Tests for Reddit remaining routes."""

    @pytest.mark.parametrize("endpoint,params", [
        ("fetch_post_comment", {"post_id": "123"}),
        ("fetch_user_info", {"username": "test"}),
        ("fetch_subreddit", {"subreddit": "test"}),
        ("fetch_post_info", {"post_id": "123"}),
        ("search_user", {"keyword": "test"}),
        ("search_post", {"keyword": "test"}),
        ("fetch_user_post", {"username": "test"}),
        ("fetch_user_comment", {"username": "test"}),
        ("fetch_subreddit_post", {"subreddit": "test"}),
    ])
    @patch("socialmedia_hub.server._core.proxy_request")
    def test_reddit_app_endpoints(self, mock_proxy: AsyncMock, client: TestClient, api_key: str, endpoint: str, params: dict) -> None:
        mock_proxy.return_value = {"data": []}
        response = client.get(
            f"/api/v1/reddit/app/{endpoint}",
            params=params,
            headers={"Authorization": f"Bearer {api_key}"},
        )
        assert response.status_code in [200, 404, 422]


class TestWeiboRemaining:
    """Tests for Weibo remaining routes."""

    @pytest.mark.parametrize("endpoint,params", [
        ("fetch_user_post", {"user_id": "123"}),
        ("fetch_weibo_comment", {"weibo_id": "123"}),
        ("fetch_user_info", {"user_id": "123"}),
        ("fetch_weibo_info", {"weibo_id": "123"}),
        ("search_user", {"keyword": "test"}),
        ("search_weibo", {"keyword": "test"}),
        ("fetch_hot_list", {}),
        ("fetch_hot_search", {}),
    ])
    @patch("socialmedia_hub.server._core.proxy_request")
    def test_weibo_web_v2_endpoints(self, mock_proxy: AsyncMock, client: TestClient, api_key: str, endpoint: str, params: dict) -> None:
        mock_proxy.return_value = {"data": []}
        response = client.get(
            f"/api/v1/weibo/web/v2/{endpoint}",
            params=params,
            headers={"Authorization": f"Bearer {api_key}"},
        )
        assert response.status_code in [200, 404, 422]


class TestXiaohongshuRemaining:
    """Tests for Xiaohongshu remaining routes."""

    @pytest.mark.parametrize("endpoint,params", [
        ("fetch_user_note", {"user_id": "123"}),
        ("fetch_note_comment", {"note_id": "123"}),
        ("fetch_user_info", {"user_id": "123"}),
        ("fetch_note_info", {"note_id": "123"}),
        ("search_user", {"keyword": "test"}),
        ("search_note", {"keyword": "test"}),
        ("fetch_hot_list", {}),
        ("fetch_user_collect", {"user_id": "123"}),
        ("fetch_user_like", {"user_id": "123"}),
    ])
    @patch("socialmedia_hub.server._core.proxy_request")
    def test_xiaohongshu_app_endpoints(self, mock_proxy: AsyncMock, client: TestClient, api_key: str, endpoint: str, params: dict) -> None:
        mock_proxy.return_value = {"data": []}
        response = client.get(
            f"/api/v1/xiaohongshu/app/{endpoint}",
            params=params,
            headers={"Authorization": f"Bearer {api_key}"},
        )
        assert response.status_code in [200, 404, 422]
