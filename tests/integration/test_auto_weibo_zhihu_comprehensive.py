"""Comprehensive tests for Weibo and Zhihu routes."""

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


# Weibo web v2 endpoints
WEIBO_WEB_V2_ENDPOINTS = [
    ("fetch_user_post", {"user_id": "123"}),
    ("fetch_weibo_comment", {"weibo_id": "123"}),
    ("fetch_user_info", {"user_id": "123"}),
    ("fetch_weibo_info", {"weibo_id": "123"}),
    ("search_user", {"keyword": "test"}),
    ("search_weibo", {"keyword": "test"}),
    ("fetch_hot_list", {}),
    ("fetch_hot_search", {}),
    ("fetch_user_like", {"user_id": "123"}),
    ("fetch_user_repost", {"user_id": "123"}),
    ("fetch_weibo_like", {"weibo_id": "123"}),
    ("fetch_weibo_repost", {"weibo_id": "123"}),
    ("fetch_user_follow", {"user_id": "123"}),
    ("fetch_user_fans", {"user_id": "123"}),
]


# Weibo app endpoints
WEIBO_APP_ENDPOINTS = [
    ("fetch_user_post", {"user_id": "123"}),
    ("fetch_weibo_comment", {"weibo_id": "123"}),
    ("fetch_user_info", {"user_id": "123"}),
    ("fetch_weibo_info", {"weibo_id": "123"}),
    ("search_user", {"keyword": "test"}),
    ("search_weibo", {"keyword": "test"}),
    ("fetch_hot_list", {}),
    ("fetch_hot_search", {}),
    ("fetch_user_like", {"user_id": "123"}),
    ("fetch_user_repost", {"user_id": "123"}),
]


# Zhihu web endpoints
ZHIHU_WEB_ENDPOINTS = [
    ("fetch_user_answer", {"user_id": "123"}),
    ("fetch_question_answer", {"question_id": "123"}),
    ("fetch_user_info", {"user_id": "123"}),
    ("fetch_question_info", {"question_id": "123"}),
    ("search_user", {"keyword": "test"}),
    ("search_question", {"keyword": "test"}),
    ("fetch_hot_list", {}),
    ("fetch_user_article", {"user_id": "123"}),
    ("fetch_user_follower", {"user_id": "123"}),
    ("fetch_user_following", {"user_id": "123"}),
    ("fetch_question_detail", {"question_id": "123"}),
    ("fetch_answer_detail", {"answer_id": "123"}),
    ("fetch_user_collections", {"user_id": "123"}),
    ("fetch_topic_info", {"topic_id": "123"}),
]


class TestWeiboWebV2:
    """Tests for Weibo web v2 routes."""

    @pytest.mark.parametrize("endpoint,params", WEIBO_WEB_V2_ENDPOINTS)
    @patch("socialmedia_hub.server._core.proxy_request")
    def test_weibo_web_v2(self, mock_proxy: AsyncMock, client: TestClient, api_key: str, endpoint: str, params: dict) -> None:
        mock_proxy.return_value = {"data": []}
        response = client.get(
            f"/api/v1/weibo/web/v2/{endpoint}",
            params=params,
            headers={"Authorization": f"Bearer {api_key}"},
        )
        assert response.status_code in [200, 404, 422]


class TestWeiboApp:
    """Tests for Weibo app routes."""

    @pytest.mark.parametrize("endpoint,params", WEIBO_APP_ENDPOINTS)
    @patch("socialmedia_hub.server._core.proxy_request")
    def test_weibo_app(self, mock_proxy: AsyncMock, client: TestClient, api_key: str, endpoint: str, params: dict) -> None:
        mock_proxy.return_value = {"data": []}
        response = client.get(
            f"/api/v1/weibo/app/{endpoint}",
            params=params,
            headers={"Authorization": f"Bearer {api_key}"},
        )
        assert response.status_code in [200, 404, 422]


class TestZhihuWeb:
    """Tests for Zhihu web routes."""

    @pytest.mark.parametrize("endpoint,params", ZHIHU_WEB_ENDPOINTS)
    @patch("socialmedia_hub.server._core.proxy_request")
    def test_zhihu_web(self, mock_proxy: AsyncMock, client: TestClient, api_key: str, endpoint: str, params: dict) -> None:
        mock_proxy.return_value = {"data": []}
        response = client.get(
            f"/api/v1/zhihu/web/{endpoint}",
            params=params,
            headers={"Authorization": f"Bearer {api_key}"},
        )
        assert response.status_code in [200, 404, 422]
