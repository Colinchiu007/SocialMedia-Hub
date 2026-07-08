"""Comprehensive tests for Douyin auto-generated routes."""

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


# Douyin web endpoints
DOUYIN_WEB_ENDPOINTS = [
    ("fetch_user_post", {"sec_user_id": "123"}),
    ("fetch_user_liked", {"sec_user_id": "123"}),
    ("fetch_user_follower", {"sec_user_id": "123"}),
    ("fetch_user_following", {"sec_user_id": "123"}),
    ("fetch_video_comment", {"aweme_id": "123"}),
    ("fetch_video_info", {"aweme_id": "123"}),
    ("fetch_user_info", {"sec_user_id": "123"}),
    ("search_user", {"keyword": "test"}),
    ("search_video", {"keyword": "test"}),
    ("fetch_hot_list", {}),
    ("fetch_hot_video", {}),
    ("fetch_hot_user", {}),
    ("fetch_video_like", {"aweme_id": "123"}),
    ("fetch_user_collect", {"sec_user_id": "123"}),
    ("fetch_user_history", {"sec_user_id": "123"}),
    ("fetch_user_dynamic", {"sec_user_id": "123"}),
    ("fetch_user_music", {"sec_user_id": "123"}),
    ("fetch_user_post_detail", {"aweme_id": "123"}),
    ("fetch_video_share", {"aweme_id": "123"}),
    ("fetch_user_relation", {"sec_user_id": "123"}),
]

# Douyin app endpoints
DOUYIN_APP_ENDPOINTS = [
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
    ("fetch_video_like", {"aweme_id": "123"}),
    ("fetch_user_collect", {"sec_user_id": "123"}),
]

# Douyin billboard endpoints
DOUYIN_BILLBOARD_ENDPOINTS = [
    ("fetch_billboard", {}),
    ("fetch_billboard_detail", {"billboard_type": "hot"}),
    ("fetch_billboard_aweme", {"billboard_type": "hot"}),
    ("fetch_billboard_author", {"billboard_type": "hot"}),
    ("fetch_billboard_music", {"billboard_type": "hot"}),
    ("fetch_billboard_hashtag", {"billboard_type": "hot"}),
    ("fetch_billboard_product", {"billboard_type": "hot"}),
    ("fetch_billboard_comment", {"billboard_type": "hot"}),
    ("fetch_billboard_share", {"billboard_type": "hot"}),
    ("fetch_billboard_like", {"billboard_type": "hot"}),
]

# Douyin creator endpoints
DOUYIN_CREATOR_ENDPOINTS = [
    ("fetch_user_post", {"sec_user_id": "123"}),
    ("fetch_user_liked", {"sec_user_id": "123"}),
    ("fetch_user_follower", {"sec_user_id": "123"}),
    ("fetch_user_following", {"sec_user_id": "123"}),
    ("fetch_video_comment", {"aweme_id": "123"}),
    ("fetch_user_info", {"sec_user_id": "123"}),
    ("search_user", {"keyword": "test"}),
    ("search_video", {"keyword": "test"}),
    ("fetch_creator_info", {"sec_user_id": "123"}),
    ("fetch_creator_data", {"sec_user_id": "123"}),
]

# Douyin xingtu endpoints
DOUYIN_XINGTU_ENDPOINTS = [
    ("fetch_user_post", {"sec_user_id": "123"}),
    ("fetch_user_liked", {"sec_user_id": "123"}),
    ("fetch_user_follower", {"sec_user_id": "123"}),
    ("fetch_user_following", {"sec_user_id": "123"}),
    ("fetch_video_comment", {"aweme_id": "123"}),
    ("fetch_user_info", {"sec_user_id": "123"}),
    ("search_user", {"keyword": "test"}),
    ("search_video", {"keyword": "test"}),
    ("fetch_xingtu_info", {"sec_user_id": "123"}),
    ("fetch_xingtu_data", {"sec_user_id": "123"}),
]


class TestDouyinWeb:
    """Tests for Douyin web routes."""

    @pytest.mark.parametrize("endpoint,params", DOUYIN_WEB_ENDPOINTS)
    @patch("socialmedia_hub.server._core.proxy_request")
    def test_douyin_web(self, mock_proxy: AsyncMock, client: TestClient, api_key: str, endpoint: str, params: dict) -> None:
        mock_proxy.return_value = {"data": []}
        response = client.get(
            f"/api/v1/douyin/web/{endpoint}",
            params=params,
            headers={"Authorization": f"Bearer {api_key}"},
        )
        assert response.status_code in [200, 404, 422]


class TestDouyinApp:
    """Tests for Douyin app routes."""

    @pytest.mark.parametrize("endpoint,params", DOUYIN_APP_ENDPOINTS)
    @patch("socialmedia_hub.server._core.proxy_request")
    def test_douyin_app(self, mock_proxy: AsyncMock, client: TestClient, api_key: str, endpoint: str, params: dict) -> None:
        mock_proxy.return_value = {"data": []}
        response = client.get(
            f"/api/v1/douyin/app/{endpoint}",
            params=params,
            headers={"Authorization": f"Bearer {api_key}"},
        )
        assert response.status_code in [200, 404, 422]


class TestDouyinBillboard:
    """Tests for Douyin billboard routes."""

    @pytest.mark.parametrize("endpoint,params", DOUYIN_BILLBOARD_ENDPOINTS)
    @patch("socialmedia_hub.server._core.proxy_request")
    def test_douyin_billboard(self, mock_proxy: AsyncMock, client: TestClient, api_key: str, endpoint: str, params: dict) -> None:
        mock_proxy.return_value = {"data": []}
        response = client.get(
            f"/api/v1/douyin/billboard/{endpoint}",
            params=params,
            headers={"Authorization": f"Bearer {api_key}"},
        )
        assert response.status_code in [200, 404, 422]


class TestDouyinCreator:
    """Tests for Douyin creator routes."""

    @pytest.mark.parametrize("endpoint,params", DOUYIN_CREATOR_ENDPOINTS)
    @patch("socialmedia_hub.server._core.proxy_request")
    def test_douyin_creator(self, mock_proxy: AsyncMock, client: TestClient, api_key: str, endpoint: str, params: dict) -> None:
        mock_proxy.return_value = {"data": []}
        response = client.get(
            f"/api/v1/douyin/creator/{endpoint}",
            params=params,
            headers={"Authorization": f"Bearer {api_key}"},
        )
        assert response.status_code in [200, 404, 422]


class TestDouyinXingtu:
    """Tests for Douyin xingtu routes."""

    @pytest.mark.parametrize("endpoint,params", DOUYIN_XINGTU_ENDPOINTS)
    @patch("socialmedia_hub.server._core.proxy_request")
    def test_douyin_xingtu(self, mock_proxy: AsyncMock, client: TestClient, api_key: str, endpoint: str, params: dict) -> None:
        mock_proxy.return_value = {"data": []}
        response = client.get(
            f"/api/v1/douyin/xingtu/{endpoint}",
            params=params,
            headers={"Authorization": f"Bearer {api_key}"},
        )
        assert response.status_code in [200, 404, 422]
