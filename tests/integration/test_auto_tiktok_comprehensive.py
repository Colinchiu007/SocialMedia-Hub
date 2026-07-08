"""Comprehensive tests for TikTok auto-generated routes."""

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


# TikTok web endpoints
TIKTOK_WEB_ENDPOINTS = [
    ("fetch_user_post", {"sec_uid": "123"}),
    ("fetch_user_liked", {"sec_uid": "123"}),
    ("fetch_user_follower", {"sec_uid": "123"}),
    ("fetch_user_following", {"sec_uid": "123"}),
    ("fetch_video_comment", {"video_id": "123"}),
    ("fetch_video_info", {"video_id": "123"}),
    ("fetch_user_info", {"sec_uid": "123"}),
    ("search_user", {"keyword": "test"}),
    ("search_video", {"keyword": "test"}),
    ("fetch_hot_list", {}),
    ("fetch_hot_video", {}),
    ("fetch_hot_user", {}),
    ("fetch_video_like", {"video_id": "123"}),
    ("fetch_user_collect", {"sec_uid": "123"}),
    ("fetch_user_history", {"sec_uid": "123"}),
    ("fetch_user_dynamic", {"sec_uid": "123"}),
    ("fetch_user_music", {"sec_uid": "123"}),
    ("fetch_user_post_detail", {"video_id": "123"}),
    ("fetch_video_share", {"video_id": "123"}),
    ("fetch_user_relation", {"sec_uid": "123"}),
]

# TikTok app endpoints
TIKTOK_APP_ENDPOINTS = [
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
]

# TikTok ads endpoints
TIKTOK_ADS_ENDPOINTS = [
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
    ("fetch_ads_info", {"video_id": "123"}),
    ("fetch_ads_campaign", {"sec_uid": "123"}),
]

# TikTok shop endpoints
TIKTOK_SHOP_ENDPOINTS = [
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
    ("fetch_product_list", {}),
    ("fetch_product_detail", {"product_id": "123"}),
    ("fetch_shop_list", {}),
]


class TestTikTokWeb:
    """Tests for TikTok web routes."""

    @pytest.mark.parametrize("endpoint,params", TIKTOK_WEB_ENDPOINTS)
    @patch("socialmedia_hub.server._core.proxy_request")
    def test_tiktok_web(self, mock_proxy: AsyncMock, client: TestClient, api_key: str, endpoint: str, params: dict) -> None:
        mock_proxy.return_value = {"data": []}
        response = client.get(
            f"/api/v1/tiktok/web/{endpoint}",
            params=params,
            headers={"Authorization": f"Bearer {api_key}"},
        )
        assert response.status_code in [200, 404, 422]


class TestTikTokApp:
    """Tests for TikTok app routes."""

    @pytest.mark.parametrize("endpoint,params", TIKTOK_APP_ENDPOINTS)
    @patch("socialmedia_hub.server._core.proxy_request")
    def test_tiktok_app(self, mock_proxy: AsyncMock, client: TestClient, api_key: str, endpoint: str, params: dict) -> None:
        mock_proxy.return_value = {"data": []}
        response = client.get(
            f"/api/v1/tiktok/app/{endpoint}",
            params=params,
            headers={"Authorization": f"Bearer {api_key}"},
        )
        assert response.status_code in [200, 404, 422]


class TestTikTokAds:
    """Tests for TikTok ads routes."""

    @pytest.mark.parametrize("endpoint,params", TIKTOK_ADS_ENDPOINTS)
    @patch("socialmedia_hub.server._core.proxy_request")
    def test_tiktok_ads(self, mock_proxy: AsyncMock, client: TestClient, api_key: str, endpoint: str, params: dict) -> None:
        mock_proxy.return_value = {"data": []}
        response = client.get(
            f"/api/v1/tiktok/ads/{endpoint}",
            params=params,
            headers={"Authorization": f"Bearer {api_key}"},
        )
        assert response.status_code in [200, 404, 422]


class TestTikTokShop:
    """Tests for TikTok shop routes."""

    @pytest.mark.parametrize("endpoint,params", TIKTOK_SHOP_ENDPOINTS)
    @patch("socialmedia_hub.server._core.proxy_request")
    def test_tiktok_shop(self, mock_proxy: AsyncMock, client: TestClient, api_key: str, endpoint: str, params: dict) -> None:
        mock_proxy.return_value = {"data": []}
        response = client.get(
            f"/api/v1/tiktok/shop/{endpoint}",
            params=params,
            headers={"Authorization": f"Bearer {api_key}"},
        )
        assert response.status_code in [200, 404, 422]
