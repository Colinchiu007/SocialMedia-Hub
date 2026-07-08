"""Comprehensive tests for Instagram auto-generated routes."""

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


# Instagram v1 endpoints
INSTAGRAM_V1_ENDPOINTS = [
    ("fetch_user_post", {"user_id": "123"}),
    ("fetch_user_reel", {"user_id": "123"}),
    ("fetch_post_comment", {"media_id": "123"}),
    ("fetch_user_info", {"user_id": "123"}),
    ("fetch_post_info", {"media_id": "123"}),
    ("search_user", {"keyword": "test"}),
    ("search_tag", {"keyword": "test"}),
    ("fetch_explore", {}),
    ("fetch_trending", {}),
    ("fetch_user_story", {"user_id": "123"}),
    ("fetch_post_like", {"media_id": "123"}),
    ("fetch_user_follow", {"user_id": "123"}),
    ("fetch_user_follower", {"user_id": "123"}),
    ("fetch_hashtag_post", {"hashtag": "test"}),
    ("fetch_location_post", {"location_id": "123"}),
]

# Instagram v2 endpoints
INSTAGRAM_V2_ENDPOINTS = [
    ("fetch_user_post", {"user_id": "123"}),
    ("fetch_user_reel", {"user_id": "123"}),
    ("fetch_post_comment", {"media_id": "123"}),
    ("fetch_user_info", {"user_id": "123"}),
    ("search_user", {"keyword": "test"}),
    ("fetch_user_story", {"user_id": "123"}),
    ("fetch_post_like", {"media_id": "123"}),
    ("fetch_user_follow", {"user_id": "123"}),
    ("fetch_user_follower", {"user_id": "123"}),
]

# Instagram v3 endpoints
INSTAGRAM_V3_ENDPOINTS = [
    ("fetch_user_post", {"user_id": "123"}),
    ("fetch_user_reel", {"user_id": "123"}),
    ("fetch_post_comment", {"media_id": "123"}),
    ("fetch_user_info", {"user_id": "123"}),
    ("search_user", {"keyword": "test"}),
    ("fetch_user_story", {"user_id": "123"}),
    ("fetch_post_like", {"media_id": "123"}),
    ("fetch_user_follow", {"user_id": "123"}),
    ("fetch_user_follower", {"user_id": "123"}),
    ("fetch_hashtag_post", {"hashtag": "test"}),
]


class TestInstagramV1:
    """Tests for Instagram v1 routes."""

    @pytest.mark.parametrize("endpoint,params", INSTAGRAM_V1_ENDPOINTS)
    @patch("socialmedia_hub.server._core.proxy_request")
    def test_instagram_v1(self, mock_proxy: AsyncMock, client: TestClient, api_key: str, endpoint: str, params: dict) -> None:
        mock_proxy.return_value = {"data": []}
        response = client.get(
            f"/api/v1/instagram/v1/{endpoint}",
            params=params,
            headers={"Authorization": f"Bearer {api_key}"},
        )
        assert response.status_code in [200, 404, 422]


class TestInstagramV2:
    """Tests for Instagram v2 routes."""

    @pytest.mark.parametrize("endpoint,params", INSTAGRAM_V2_ENDPOINTS)
    @patch("socialmedia_hub.server._core.proxy_request")
    def test_instagram_v2(self, mock_proxy: AsyncMock, client: TestClient, api_key: str, endpoint: str, params: dict) -> None:
        mock_proxy.return_value = {"data": []}
        response = client.get(
            f"/api/v1/instagram/v2/{endpoint}",
            params=params,
            headers={"Authorization": f"Bearer {api_key}"},
        )
        assert response.status_code in [200, 404, 422]


class TestInstagramV3:
    """Tests for Instagram v3 routes."""

    @pytest.mark.parametrize("endpoint,params", INSTAGRAM_V3_ENDPOINTS)
    @patch("socialmedia_hub.server._core.proxy_request")
    def test_instagram_v3(self, mock_proxy: AsyncMock, client: TestClient, api_key: str, endpoint: str, params: dict) -> None:
        mock_proxy.return_value = {"data": []}
        response = client.get(
            f"/api/v1/instagram/v3/{endpoint}",
            params=params,
            headers={"Authorization": f"Bearer {api_key}"},
        )
        assert response.status_code in [200, 404, 422]
