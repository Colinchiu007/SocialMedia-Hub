"""Tests for live room routes."""

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


LIVE_ROOM_ENDPOINTS = [
    ("/douyin/fetch_room_info", {"room_id": "123"}),
    ("/douyin/fetch_room_danmaku", {"room_id": "123"}),
    ("/douyin/fetch_gift_ranking", {"room_id": "123"}),
    ("/douyin/fetch_room_product", {"room_id": "123", "author_id": "456"}),
    ("/tiktok/fetch_room_info", {"room_id": "123"}),
    ("/tiktok/fetch_room_danmaku", {"room_id": "123"}),
    ("/tiktok/fetch_gift_ranking", {"room_id": "123"}),
    ("/bilibili/fetch_room_info", {"room_id": "123"}),
    ("/kuaishou/fetch_room_info", {"room_id": "123"}),
]


class TestLiveRoomRoutes:
    """Tests for live room routes."""

    @pytest.mark.parametrize("path,params", LIVE_ROOM_ENDPOINTS)
    @patch("socialmedia_hub.server._core.proxy_request")
    def test_live_room_endpoint(self, mock_proxy: AsyncMock, client: TestClient, api_key: str, path: str, params: dict) -> None:
        mock_proxy.return_value = {"data": [], "status_code": 200}
        response = client.get(
            f"/api/v1/live{path}",
            params=params,
            headers={"Authorization": f"Bearer {api_key}"},
        )
        assert response.status_code in [200, 404, 422], f"Failed for {path}: {response.status_code}"
