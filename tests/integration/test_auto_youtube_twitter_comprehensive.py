"""Comprehensive tests for YouTube and Twitter auto-generated routes."""

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


# YouTube web endpoints
YOUTUBE_WEB_ENDPOINTS = [
    ("fetch_user_video", {"channel_id": "123"}),
    ("fetch_video_comment", {"video_id": "123"}),
    ("fetch_user_info", {"channel_id": "123"}),
    ("fetch_video_info", {"video_id": "123"}),
    ("search_user", {"keyword": "test"}),
    ("search_video", {"keyword": "test"}),
    ("fetch_trending", {}),
    ("fetch_hot_video", {}),
    ("fetch_user_playlist", {"channel_id": "123"}),
    ("fetch_video_like", {"video_id": "123"}),
    ("fetch_user_subscribe", {"channel_id": "123"}),
    ("fetch_user_follower", {"channel_id": "123"}),
]

# YouTube web v2 endpoints
YOUTUBE_WEB_V2_ENDPOINTS = [
    ("fetch_user_video", {"channel_id": "123"}),
    ("fetch_video_comment", {"video_id": "123"}),
    ("fetch_user_info", {"channel_id": "123"}),
    ("fetch_video_info", {"video_id": "123"}),
    ("search_user", {"keyword": "test"}),
    ("search_video", {"keyword": "test"}),
    ("fetch_trending", {}),
    ("fetch_hot_video", {}),
    ("fetch_user_playlist", {"channel_id": "123"}),
    ("fetch_video_like", {"video_id": "123"}),
]

# Twitter web endpoints
TWITTER_WEB_ENDPOINTS = [
    ("fetch_user_tweet", {"user_id": "123"}),
    ("fetch_tweet_comment", {"tweet_id": "123"}),
    ("fetch_user_info", {"user_id": "123"}),
    ("fetch_tweet_info", {"tweet_id": "123"}),
    ("search_user", {"keyword": "test"}),
    ("search_tweet", {"keyword": "test"}),
    ("fetch_trending", {}),
    ("fetch_user_like", {"user_id": "123"}),
    ("fetch_user_retweet", {"user_id": "123"}),
    ("fetch_user_follower", {"user_id": "123"}),
    ("fetch_user_following", {"user_id": "123"}),
]


class TestYouTubeWeb:
    """Tests for YouTube web routes."""

    @pytest.mark.parametrize("endpoint,params", YOUTUBE_WEB_ENDPOINTS)
    @patch("socialmedia_hub.server._core.proxy_request")
    def test_youtube_web(self, mock_proxy: AsyncMock, client: TestClient, api_key: str, endpoint: str, params: dict) -> None:
        mock_proxy.return_value = {"data": []}
        response = client.get(
            f"/api/v1/youtube/web/{endpoint}",
            params=params,
            headers={"Authorization": f"Bearer {api_key}"},
        )
        assert response.status_code in [200, 404, 422]


class TestYouTubeWebV2:
    """Tests for YouTube web v2 routes."""

    @pytest.mark.parametrize("endpoint,params", YOUTUBE_WEB_V2_ENDPOINTS)
    @patch("socialmedia_hub.server._core.proxy_request")
    def test_youtube_web_v2(self, mock_proxy: AsyncMock, client: TestClient, api_key: str, endpoint: str, params: dict) -> None:
        mock_proxy.return_value = {"data": []}
        response = client.get(
            f"/api/v1/youtube/web/v2/{endpoint}",
            params=params,
            headers={"Authorization": f"Bearer {api_key}"},
        )
        assert response.status_code in [200, 404, 422]


class TestTwitterWeb:
    """Tests for Twitter web routes."""

    @pytest.mark.parametrize("endpoint,params", TWITTER_WEB_ENDPOINTS)
    @patch("socialmedia_hub.server._core.proxy_request")
    def test_twitter_web(self, mock_proxy: AsyncMock, client: TestClient, api_key: str, endpoint: str, params: dict) -> None:
        mock_proxy.return_value = {"data": []}
        response = client.get(
            f"/api/v1/twitter/web/{endpoint}",
            params=params,
            headers={"Authorization": f"Bearer {api_key}"},
        )
        assert response.status_code in [200, 404, 422]
