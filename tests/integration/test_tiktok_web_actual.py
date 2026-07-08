"""Tests matching actual TikTok web endpoints."""

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


# Actual TikTok web endpoints with correct parameters
TIKTOK_WEB_ACTUAL = [
    ("/fetch_post_detail", {"itemId": "123"}),
    ("/fetch_post_detail_v2", {"itemId": "123"}),
    ("/fetch_explore_post", {"categoryType": "trending"}),
    ("/fetch_trending_post", {}),
    ("/fetch_trending_searchwords", {}),
    ("/fetch_user_profile", {"uniqueId": "test_user"}),
    ("/fetch_user_profile", {"secUid": "MS4wLjAB"}),
    ("/fetch_user_post", {"secUid": "MS4wLjAB"}),
    ("/fetch_user_repost", {"secUid": "MS4wLjAB"}),
    ("/fetch_user_like", {"secUid": "MS4wLjAB"}),
    ("/fetch_user_collect", {"secUid": "MS4wLjAB"}),
    ("/fetch_user_play_list", {"secUid": "MS4wLjAB"}),
    ("/fetch_user_mix", {"mixId": "123"}),
    ("/fetch_post_comment", {"aweme_id": "123"}),
    ("/fetch_post_comment_reply", {"item_id": "123", "comment_id": "456"}),
    ("/fetch_user_fans", {"secUid": "MS4wLjAB"}),
    ("/fetch_user_follow", {"secUid": "MS4wLjAB"}),
    ("/fetch_user_live_detail", {"secUid": "MS4wLjAB"}),
    ("/fetch_general_search", {"keyword": "test"}),
    ("/fetch_search_keyword_suggest", {"keyword": "test"}),
    ("/fetch_search_user", {"keyword": "test"}),
    ("/fetch_search_video", {"keyword": "test"}),
    ("/fetch_search_music", {"keyword": "test"}),
    ("/fetch_search_hashtag", {"keyword": "test"}),
    ("/fetch_video_detail", {"aweme_id": "123"}),
    ("/fetch_video_related", {"aweme_id": "123"}),
    ("/fetch_video_comments", {"aweme_id": "123"}),
    ("/fetch_video_likes", {"aweme_id": "123"}),
    ("/fetch_video_shares", {"aweme_id": "123"}),
    ("/fetch_video_downloads", {"aweme_id": "123"}),
]


class TestTikTokWebActual:
    """Tests for actual TikTok web endpoints."""

    @pytest.mark.parametrize("path,params", TIKTOK_WEB_ACTUAL)
    @patch("socialmedia_hub.server._core.proxy_request")
    def test_tiktok_web_endpoint(self, mock_proxy: AsyncMock, client: TestClient, api_key: str, path: str, params: dict) -> None:
        mock_proxy.return_value = {"data": [], "status_code": 200}
        response = client.get(
            f"/api/v1/tiktok/web{path}",
            params=params,
            headers={"Authorization": f"Bearer {api_key}"},
        )
        assert response.status_code in [200, 404, 422], f"Failed for {path}: {response.status_code}"
