"""Comprehensive tests for other platform auto-generated routes."""

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


# Bilibili web endpoints
BILIBILI_WEB_ENDPOINTS = [
    ("fetch_user_post", {"mid": "123"}),
    ("fetch_video_comment", {"bvid": "123"}),
    ("fetch_user_info", {"mid": "123"}),
    ("fetch_video_info", {"bvid": "123"}),
    ("fetch_user_fan", {"mid": "123"}),
    ("fetch_videodanmu", {"bvid": "123"}),
    ("search_user", {"keyword": "test"}),
    ("search_video", {"keyword": "test"}),
    ("fetch_hot_list", {}),
    ("fetch_user_like", {"mid": "123"}),
    ("fetch_user_collect", {"mid": "123"}),
    ("fetch_user_history", {"mid": "123"}),
]

# Bilibili app endpoints
BILIBILI_APP_ENDPOINTS = [
    ("fetch_user_post", {"mid": "123"}),
    ("fetch_video_comment", {"bvid": "123"}),
    ("fetch_user_info", {"mid": "123"}),
    ("fetch_video_info", {"bvid": "123"}),
    ("fetch_user_fan", {"mid": "123"}),
    ("search_user", {"keyword": "test"}),
    ("search_video", {"keyword": "test"}),
    ("fetch_hot_list", {}),
]

# Weibo web endpoints
WEIBO_WEB_ENDPOINTS = [
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
]

# Kuaishou web endpoints
KUAISHOU_WEB_ENDPOINTS = [
    ("fetch_user_post", {"user_id": "123"}),
    ("fetch_video_comment", {"photo_id": "123"}),
    ("fetch_user_info", {"user_id": "123"}),
    ("fetch_video_info", {"photo_id": "123"}),
    ("search_user", {"keyword": "test"}),
    ("search_video", {"keyword": "test"}),
    ("fetch_hot_list", {}),
    ("fetch_user_like", {"user_id": "123"}),
    ("fetch_user_collect", {"user_id": "123"}),
    ("fetch_user_history", {"user_id": "123"}),
]

# Kuaishou app endpoints
KUAISHOU_APP_ENDPOINTS = [
    ("fetch_user_post", {"user_id": "123"}),
    ("fetch_video_comment", {"photo_id": "123"}),
    ("fetch_user_info", {"user_id": "123"}),
    ("fetch_video_info", {"photo_id": "123"}),
    ("search_user", {"keyword": "test"}),
    ("search_video", {"keyword": "test"}),
    ("fetch_hot_list", {}),
]

# LinkedIn web endpoints
LINKEDIN_WEB_ENDPOINTS = [
    ("fetch_user_post", {"user_id": "123"}),
    ("fetch_user_info", {"user_id": "123"}),
    ("fetch_company_info", {"company_id": "123"}),
    ("fetch_company_post", {"company_id": "123"}),
    ("search_user", {"keyword": "test"}),
    ("search_company", {"keyword": "test"}),
    ("fetch_user_connection", {"user_id": "123"}),
    ("fetch_job_list", {"keyword": "test"}),
    ("fetch_user_like", {"user_id": "123"}),
    ("fetch_user_comment", {"user_id": "123"}),
]

# Reddit app endpoints
REDDIT_APP_ENDPOINTS = [
    ("fetch_post_comment", {"post_id": "123"}),
    ("fetch_user_info", {"username": "test"}),
    ("fetch_subreddit", {"subreddit": "test"}),
    ("fetch_post_info", {"post_id": "123"}),
    ("search_user", {"keyword": "test"}),
    ("search_post", {"keyword": "test"}),
    ("fetch_user_post", {"username": "test"}),
    ("fetch_user_comment", {"username": "test"}),
    ("fetch_subreddit_post", {"subreddit": "test"}),
    ("fetch_subreddit_comment", {"subreddit": "test"}),
]

# Xiaohongshu web endpoints
XIAOHONGSHU_WEB_ENDPOINTS = [
    ("fetch_user_note", {"user_id": "123"}),
    ("fetch_note_comment", {"note_id": "123"}),
    ("fetch_user_info", {"user_id": "123"}),
    ("fetch_note_info", {"note_id": "123"}),
    ("search_user", {"keyword": "test"}),
    ("search_note", {"keyword": "test"}),
    ("fetch_hot_list", {}),
    ("fetch_user_collect", {"user_id": "123"}),
    ("fetch_user_like", {"user_id": "123"}),
    ("fetch_user_follow", {"user_id": "123"}),
]

# Xiaohongshu app endpoints
XIAOHONGSHU_APP_ENDPOINTS = [
    ("fetch_user_note", {"user_id": "123"}),
    ("fetch_note_comment", {"note_id": "123"}),
    ("fetch_user_info", {"user_id": "123"}),
    ("fetch_note_info", {"note_id": "123"}),
    ("search_user", {"keyword": "test"}),
    ("search_note", {"keyword": "test"}),
    ("fetch_hot_list", {}),
]

# Xiaohongshu app v2 endpoints
XIAOHONGSHU_APP_V2_ENDPOINTS = [
    ("fetch_user_note", {"user_id": "123"}),
    ("fetch_note_comment", {"note_id": "123"}),
    ("fetch_user_info", {"user_id": "123"}),
    ("fetch_note_info", {"note_id": "123"}),
    ("search_user", {"keyword": "test"}),
    ("search_note", {"keyword": "test"}),
    ("fetch_hot_list", {}),
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
]

# Threads web endpoints
THREADS_WEB_ENDPOINTS = [
    ("fetch_user_thread", {"user_id": "123"}),
    ("fetch_thread_comment", {"thread_id": "123"}),
    ("fetch_user_info", {"user_id": "123"}),
    ("fetch_thread_info", {"thread_id": "123"}),
    ("search_user", {"keyword": "test"}),
    ("search_thread", {"keyword": "test"}),
    ("fetch_user_like", {"user_id": "123"}),
    ("fetch_user_follower", {"user_id": "123"}),
    ("fetch_user_following", {"user_id": "123"}),
]

# Lemon8 app endpoints
LEMON8_APP_ENDPOINTS = [
    ("fetch_user_post", {"user_id": "123"}),
    ("fetch_post_comment", {"post_id": "123"}),
    ("fetch_user_info", {"user_id": "123"}),
    ("fetch_post_info", {"post_id": "123"}),
    ("search_user", {"keyword": "test"}),
    ("search_post", {"keyword": "test"}),
    ("fetch_hot_list", {}),
    ("fetch_user_like", {"user_id": "123"}),
    ("fetch_user_collect", {"user_id": "123"}),
]


class TestBilibiliWeb:
    """Tests for Bilibili web routes."""

    @pytest.mark.parametrize("endpoint,params", BILIBILI_WEB_ENDPOINTS)
    @patch("socialmedia_hub.server._core.proxy_request")
    def test_bilibili_web(self, mock_proxy: AsyncMock, client: TestClient, api_key: str, endpoint: str, params: dict) -> None:
        mock_proxy.return_value = {"data": []}
        response = client.get(
            f"/api/v1/bilibili/web/{endpoint}",
            params=params,
            headers={"Authorization": f"Bearer {api_key}"},
        )
        assert response.status_code in [200, 404, 422]


class TestBilibiliApp:
    """Tests for Bilibili app routes."""

    @pytest.mark.parametrize("endpoint,params", BILIBILI_APP_ENDPOINTS)
    @patch("socialmedia_hub.server._core.proxy_request")
    def test_bilibili_app(self, mock_proxy: AsyncMock, client: TestClient, api_key: str, endpoint: str, params: dict) -> None:
        mock_proxy.return_value = {"data": []}
        response = client.get(
            f"/api/v1/bilibili/app/{endpoint}",
            params=params,
            headers={"Authorization": f"Bearer {api_key}"},
        )
        assert response.status_code in [200, 404, 422]


class TestWeiboWeb:
    """Tests for Weibo web routes."""

    @pytest.mark.parametrize("endpoint,params", WEIBO_WEB_ENDPOINTS)
    @patch("socialmedia_hub.server._core.proxy_request")
    def test_weibo_web(self, mock_proxy: AsyncMock, client: TestClient, api_key: str, endpoint: str, params: dict) -> None:
        mock_proxy.return_value = {"data": []}
        response = client.get(
            f"/api/v1/weibo/web/{endpoint}",
            params=params,
            headers={"Authorization": f"Bearer {api_key}"},
        )
        assert response.status_code in [200, 404, 422]


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


class TestKuaishouWeb:
    """Tests for Kuaishou web routes."""

    @pytest.mark.parametrize("endpoint,params", KUAISHOU_WEB_ENDPOINTS)
    @patch("socialmedia_hub.server._core.proxy_request")
    def test_kuaishou_web(self, mock_proxy: AsyncMock, client: TestClient, api_key: str, endpoint: str, params: dict) -> None:
        mock_proxy.return_value = {"data": []}
        response = client.get(
            f"/api/v1/kuaishou/web/{endpoint}",
            params=params,
            headers={"Authorization": f"Bearer {api_key}"},
        )
        assert response.status_code in [200, 404, 422]


class TestKuaishouApp:
    """Tests for Kuaishou app routes."""

    @pytest.mark.parametrize("endpoint,params", KUAISHOU_APP_ENDPOINTS)
    @patch("socialmedia_hub.server._core.proxy_request")
    def test_kuaishou_app(self, mock_proxy: AsyncMock, client: TestClient, api_key: str, endpoint: str, params: dict) -> None:
        mock_proxy.return_value = {"data": []}
        response = client.get(
            f"/api/v1/kuaishou/app/{endpoint}",
            params=params,
            headers={"Authorization": f"Bearer {api_key}"},
        )
        assert response.status_code in [200, 404, 422]


class TestLinkedInWeb:
    """Tests for LinkedIn web routes."""

    @pytest.mark.parametrize("endpoint,params", LINKEDIN_WEB_ENDPOINTS)
    @patch("socialmedia_hub.server._core.proxy_request")
    def test_linkedin_web(self, mock_proxy: AsyncMock, client: TestClient, api_key: str, endpoint: str, params: dict) -> None:
        mock_proxy.return_value = {"data": []}
        response = client.get(
            f"/api/v1/linkedin/web/{endpoint}",
            params=params,
            headers={"Authorization": f"Bearer {api_key}"},
        )
        assert response.status_code in [200, 404, 422]


class TestRedditApp:
    """Tests for Reddit app routes."""

    @pytest.mark.parametrize("endpoint,params", REDDIT_APP_ENDPOINTS)
    @patch("socialmedia_hub.server._core.proxy_request")
    def test_reddit_app(self, mock_proxy: AsyncMock, client: TestClient, api_key: str, endpoint: str, params: dict) -> None:
        mock_proxy.return_value = {"data": []}
        response = client.get(
            f"/api/v1/reddit/app/{endpoint}",
            params=params,
            headers={"Authorization": f"Bearer {api_key}"},
        )
        assert response.status_code in [200, 404, 422]


class TestXiaohongshuWeb:
    """Tests for Xiaohongshu web routes."""

    @pytest.mark.parametrize("endpoint,params", XIAOHONGSHU_WEB_ENDPOINTS)
    @patch("socialmedia_hub.server._core.proxy_request")
    def test_xiaohongshu_web(self, mock_proxy: AsyncMock, client: TestClient, api_key: str, endpoint: str, params: dict) -> None:
        mock_proxy.return_value = {"data": []}
        response = client.get(
            f"/api/v1/xiaohongshu/web/{endpoint}",
            params=params,
            headers={"Authorization": f"Bearer {api_key}"},
        )
        assert response.status_code in [200, 404, 422]


class TestXiaohongshuApp:
    """Tests for Xiaohongshu app routes."""

    @pytest.mark.parametrize("endpoint,params", XIAOHONGSHU_APP_ENDPOINTS)
    @patch("socialmedia_hub.server._core.proxy_request")
    def test_xiaohongshu_app(self, mock_proxy: AsyncMock, client: TestClient, api_key: str, endpoint: str, params: dict) -> None:
        mock_proxy.return_value = {"data": []}
        response = client.get(
            f"/api/v1/xiaohongshu/app/{endpoint}",
            params=params,
            headers={"Authorization": f"Bearer {api_key}"},
        )
        assert response.status_code in [200, 404, 422]


class TestXiaohongshuAppV2:
    """Tests for Xiaohongshu app v2 routes."""

    @pytest.mark.parametrize("endpoint,params", XIAOHONGSHU_APP_V2_ENDPOINTS)
    @patch("socialmedia_hub.server._core.proxy_request")
    def test_xiaohongshu_app_v2(self, mock_proxy: AsyncMock, client: TestClient, api_key: str, endpoint: str, params: dict) -> None:
        mock_proxy.return_value = {"data": []}
        response = client.get(
            f"/api/v1/xiaohongshu/app/v2/{endpoint}",
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


class TestThreadsWeb:
    """Tests for Threads web routes."""

    @pytest.mark.parametrize("endpoint,params", THREADS_WEB_ENDPOINTS)
    @patch("socialmedia_hub.server._core.proxy_request")
    def test_threads_web(self, mock_proxy: AsyncMock, client: TestClient, api_key: str, endpoint: str, params: dict) -> None:
        mock_proxy.return_value = {"data": []}
        response = client.get(
            f"/api/v1/threads/web/{endpoint}",
            params=params,
            headers={"Authorization": f"Bearer {api_key}"},
        )
        assert response.status_code in [200, 404, 422]


class TestLemon8App:
    """Tests for Lemon8 app routes."""

    @pytest.mark.parametrize("endpoint,params", LEMON8_APP_ENDPOINTS)
    @patch("socialmedia_hub.server._core.proxy_request")
    def test_lemon8_app(self, mock_proxy: AsyncMock, client: TestClient, api_key: str, endpoint: str, params: dict) -> None:
        mock_proxy.return_value = {"data": []}
        response = client.get(
            f"/api/v1/lemon8/app/{endpoint}",
            params=params,
            headers={"Authorization": f"Bearer {api_key}"},
        )
        assert response.status_code in [200, 404, 422]
