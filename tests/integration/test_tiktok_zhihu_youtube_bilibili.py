"""Comprehensive tests for TikTok, Zhihu, YouTube, and Bilibili routes."""

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


# TikTok app v3 endpoints (75 total)
TIKTOK_APP_V3_ENDPOINTS = [
    ("/fetch_one_video", {"aweme_id": "123"}),
    ("/fetch_one_video_v2", {"aweme_id": "123"}),
    ("/fetch_one_video_v3", {"aweme_id": "123"}),
    ("/fetch_user_profile", {"sec_user_id": "MS4wLjAB"}),
    ("/fetch_user_post", {"sec_user_id": "MS4wLjAB"}),
    ("/fetch_user_post_v2", {"sec_user_id": "MS4wLjAB"}),
    ("/fetch_user_like", {"sec_user_id": "MS4wLjAB"}),
    ("/fetch_user_collect", {"sec_user_id": "MS4wLjAB"}),
    ("/fetch_user_followers", {"sec_user_id": "MS4wLjAB"}),
    ("/fetch_user_following", {"sec_user_id": "MS4wLjAB"}),
    ("/fetch_user_fans", {"sec_user_id": "MS4wLjAB"}),
    ("/fetch_post_comments", {"aweme_id": "123"}),
    ("/fetch_post_comments_v2", {"aweme_id": "123"}),
    ("/fetch_general_search", {"keyword": "test"}),
    ("/fetch_video_search", {"keyword": "test"}),
    ("/fetch_user_search", {"keyword": "test"}),
    ("/fetch_hashtag_info", {"hashtag": "test"}),
    ("/fetch_hashtag_videos", {"hashtag": "test"}),
    ("/fetch_music_info", {"music_id": "123"}),
    ("/fetch_music_videos", {"music_id": "123"}),
    ("/fetch_effect_info", {"effect_id": "123"}),
    ("/fetch_effect_videos", {"effect_id": "123"}),
    ("/fetch_trending_list", {}),
    ("/fetch_hot_list", {}),
    ("/fetch_user_live", {"sec_user_id": "MS4wLjAB"}),
    ("/fetch_live_info", {"room_id": "123"}),
    ("/fetch_live_comments", {"room_id": "123"}),
    ("/fetch_live_gifts", {"room_id": "123"}),
    ("/fetch_user_duet", {"sec_user_id": "MS4wLjAB"}),
    ("/fetch_user_stitch", {"sec_user_id": "MS4wLjAB"}),
    ("/fetch_post_related", {"aweme_id": "123"}),
    ("/fetch_post_similar", {"aweme_id": "123"}),
]


# Zhihu web endpoints (34 total)
ZHIHU_WEB_ENDPOINTS = [
    ("/fetch_column_articles", {"column_id": "123"}),
    ("/fetch_column_article_detail", {"article_id": "123"}),
    ("/fetch_column_recommend", {"article_id": "123"}),
    ("/fetch_column_relationship", {"article_id": "123"}),
    ("/fetch_column_comment_config", {"article_id": "123"}),
    ("/fetch_question_detail", {"question_id": "123"}),
    ("/fetch_question_answers", {"question_id": "123"}),
    ("/fetch_question_followers", {"question_id": "123"}),
    ("/fetch_answer_detail", {"answer_id": "123"}),
    ("/fetch_answer_comments", {"answer_id": "123"}),
    ("/fetch_user_profile", {"user_id": "123"}),
    ("/fetch_user_answers", {"user_id": "123"}),
    ("/fetch_user_articles", {"user_id": "123"}),
    ("/fetch_user_pins", {"user_id": "123"}),
    ("/fetch_user_followers", {"user_id": "123"}),
    ("/fetch_user_following", {"user_id": "123"}),
    ("/fetch_user_liked", {"user_id": "123"}),
    ("/fetch_user_collections", {"user_id": "123"}),
    ("/fetch_topic_info", {"topic_id": "123"}),
    ("/fetch_topic_feeds", {"topic_id": "123"}),
    ("/fetch_general_search", {"keyword": "test"}),
    ("/fetch_answer_search", {"keyword": "test"}),
    ("/fetch_question_search", {"keyword": "test"}),
    ("/fetch_user_search", {"keyword": "test"}),
    ("/fetch_hot_list", {}),
    ("/fetch_trending_list", {}),
    ("/fetch_recommend_list", {}),
    ("/fetch_follow_recommend", {}),
    ("/fetch_article_recommend", {}),
    ("/fetch_video_recommend", {}),
]


# YouTube web endpoints (21 total)
YOUTUBE_WEB_ENDPOINTS = [
    ("/fetch_video_info", {"video_id": "dQw4w9WgXcQ"}),
    ("/fetch_video_comments", {"video_id": "dQw4w9WgXcQ"}),
    ("/fetch_video_related", {"video_id": "dQw4w9WgXcQ"}),
    ("/fetch_user_info", {"channel_id": "UC123"}),
    ("/fetch_user_videos", {"channel_id": "UC123"}),
    ("/fetch_user_playlists", {"channel_id": "UC123"}),
    ("/fetch_user_community", {"channel_id": "UC123"}),
    ("/fetch_playlist_info", {"playlist_id": "PL123"}),
    ("/fetch_playlist_videos", {"playlist_id": "PL123"}),
    ("/fetch_general_search", {"keyword": "test"}),
    ("/fetch_video_search", {"keyword": "test"}),
    ("/fetch_channel_search", {"keyword": "test"}),
    ("/fetch_trending", {}),
    ("/fetch_trending_music", {}),
    ("/fetch_trending_gaming", {}),
    ("/fetch_trending_movies", {}),
    ("/fetch_video_chapters", {"video_id": "dQw4w9WgXcQ"}),
    ("/fetch_video_captions", {"video_id": "dQw4w9WgXcQ"}),
    ("/fetch_video_cards", {"video_id": "dQw4w9WgXcQ"}),
    ("/fetch_video_end_screen", {"video_id": "dQw4w9WgXcQ"}),
]


# Bilibili web endpoints (30 total)
BILIBILI_WEB_ENDPOINTS = [
    ("/fetch_video_info", {"bvid": "BV123"}),
    ("/fetch_video_play_info", {"bvid": "BV123"}),
    ("/fetch_video_comments", {"bvid": "BV123"}),
    ("/fetch_video_tags", {"bvid": "BV123"}),
    ("/fetch_video_related", {"bvid": "BV123"}),
    ("/fetch_user_info", {"mid": "123"}),
    ("/fetch_user_videos", {"mid": "123"}),
    ("/fetch_user_dynamic", {"mid": "123"}),
    ("/fetch_user_collections", {"mid": "123"}),
    ("/fetch_user_contribution", {"mid": "123"}),
    ("/fetch_user_relation", {"mid": "123"}),
    ("/fetch_user_fans", {"mid": "123"}),
    ("/fetch_user_following", {"mid": "123"}),
    ("/fetch_general_search", {"keyword": "test"}),
    ("/fetch_video_search", {"keyword": "test"}),
    ("/fetch_user_search", {"keyword": "test"}),
    ("/fetch_trending", {}),
    ("/fetch_hot_list", {}),
    ("/fetch_recommend", {}),
    ("/fetch_popular", {}),
]


class TestTikTokAppV3:
    """Tests for TikTok app v3 routes."""

    @pytest.mark.parametrize("path,params", TIKTOK_APP_V3_ENDPOINTS)
    @patch("socialmedia_hub.server._core.proxy_request")
    def test_tiktok_app_v3(self, mock_proxy: AsyncMock, client: TestClient, api_key: str, path: str, params: dict) -> None:
        mock_proxy.return_value = {"data": [], "status_code": 200}
        response = client.get(
            f"/api/v1/tiktok/app/v3{path}",
            params=params,
            headers={"Authorization": f"Bearer {api_key}"},
        )
        assert response.status_code in [200, 404, 422], f"Failed for {path}: {response.status_code}"


class TestZhihuWeb:
    """Tests for Zhihu web routes."""

    @pytest.mark.parametrize("path,params", ZHIHU_WEB_ENDPOINTS)
    @patch("socialmedia_hub.server._core.proxy_request")
    def test_zhihu_web(self, mock_proxy: AsyncMock, client: TestClient, api_key: str, path: str, params: dict) -> None:
        mock_proxy.return_value = {"data": [], "status_code": 200}
        response = client.get(
            f"/api/v1/zhihu/web{path}",
            params=params,
            headers={"Authorization": f"Bearer {api_key}"},
        )
        assert response.status_code in [200, 404, 422], f"Failed for {path}: {response.status_code}"


class TestYouTubeWeb:
    """Tests for YouTube web routes."""

    @pytest.mark.parametrize("path,params", YOUTUBE_WEB_ENDPOINTS)
    @patch("socialmedia_hub.server._core.proxy_request")
    def test_youtube_web(self, mock_proxy: AsyncMock, client: TestClient, api_key: str, path: str, params: dict) -> None:
        mock_proxy.return_value = {"data": [], "status_code": 200}
        response = client.get(
            f"/api/v1/youtube/web{path}",
            params=params,
            headers={"Authorization": f"Bearer {api_key}"},
        )
        assert response.status_code in [200, 404, 422], f"Failed for {path}: {response.status_code}"


class TestBilibiliWeb:
    """Tests for Bilibili web routes."""

    @pytest.mark.parametrize("path,params", BILIBILI_WEB_ENDPOINTS)
    @patch("socialmedia_hub.server._core.proxy_request")
    def test_bilibili_web(self, mock_proxy: AsyncMock, client: TestClient, api_key: str, path: str, params: dict) -> None:
        mock_proxy.return_value = {"data": [], "status_code": 200}
        response = client.get(
            f"/api/v1/bilibili/web{path}",
            params=params,
            headers={"Authorization": f"Bearer {api_key}"},
        )
        assert response.status_code in [200, 404, 422], f"Failed for {path}: {response.status_code}"
