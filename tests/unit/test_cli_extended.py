"""Extended tests for CLI module."""

from __future__ import annotations

from unittest.mock import MagicMock, patch

from typer.testing import CliRunner

from socialmedia_hub.cli.main import _detect_platform, app

runner = CliRunner()


class TestDetectPlatform:
    """Tests for _detect_platform function."""

    def test_douyin(self):
        assert _detect_platform("https://www.douyin.com/video/123") == "douyin"

    def test_douyin_short(self):
        assert _detect_platform("https://v.douyin.com/abc") == "douyin"

    def test_tiktok(self):
        assert _detect_platform("https://www.tiktok.com/@user/video/123") == "tiktok"

    def test_instagram(self):
        assert _detect_platform("https://www.instagram.com/p/abc") == "instagram"

    def test_youtube(self):
        assert _detect_platform("https://www.youtube.com/watch?v=123") == "youtube"

    def test_youtube_short(self):
        assert _detect_platform("https://youtu.be/123") == "youtube"

    def test_twitter(self):
        assert _detect_platform("https://twitter.com/user/status/123") == "twitter"

    def test_twitter_x(self):
        assert _detect_platform("https://x.com/user/status/123") == "twitter"

    def test_xiaohongshu(self):
        assert _detect_platform("https://www.xiaohongshu.com/explore/123") == "xiaohongshu"

    def test_xhslink(self):
        assert _detect_platform("https://xhslink.com/abc") == "xiaohongshu"

    def test_bilibili(self):
        assert _detect_platform("https://www.bilibili.com/video/BV123") == "bilibili"

    def test_weibo(self):
        assert _detect_platform("https://weibo.com/user/123") == "weibo"

    def test_weibo_mobile(self):
        assert _detect_platform("https://m.weibo.cn/status/123") == "weibo"

    def test_kuaishou(self):
        assert _detect_platform("https://www.kuaishou.com/short-video/123") == "kuaishou"

    def test_reddit(self):
        assert _detect_platform("https://www.reddit.com/r/test/123") == "reddit"

    def test_threads(self):
        assert _detect_platform("https://www.threads.net/@user/post/123") == "threads"

    def test_linkedin(self):
        assert _detect_platform("https://www.linkedin.com/posts/user-123") == "linkedin"

    def test_zhihu(self):
        assert _detect_platform("https://www.zhihu.com/question/123") == "zhihu"

    def test_unknown(self):
        assert _detect_platform("https://example.com") is None

    def test_case_insensitive(self):
        assert _detect_platform("https://WWW.TIKTOK.COM/video/123") == "tiktok"


class TestCLICommands:
    """Tests for CLI commands."""

    def test_version(self):
        result = runner.invoke(app, ["version"])
        assert result.exit_code == 0
        assert "socialmedia-hub" in result.output

    def test_help(self):
        result = runner.invoke(app, ["--help"])
        assert result.exit_code == 0
        assert "SocialMedia-Hub CLI" in result.output

    def test_health_success(self):
        mock_response = MagicMock()
        mock_response.json.return_value = {"status": "ok"}
        mock_client = MagicMock()
        mock_client.__enter__ = MagicMock(return_value=mock_client)
        mock_client.__exit__ = MagicMock(return_value=False)
        mock_client.get.return_value = mock_response

        with patch("socialmedia_hub.cli.main.httpx.Client", return_value=mock_client):
            result = runner.invoke(app, ["health"])
            assert result.exit_code == 0

    def test_health_error(self):
        mock_client = MagicMock()
        mock_client.__enter__ = MagicMock(return_value=mock_client)
        mock_client.__exit__ = MagicMock(return_value=False)
        mock_client.get.side_effect = Exception("Connection refused")

        with patch("socialmedia_hub.cli.main.httpx.Client", return_value=mock_client):
            result = runner.invoke(app, ["health"])
            assert result.exit_code == 1

    def test_platforms_requires_api_key(self):
        result = runner.invoke(app, ["platforms"], catch_exceptions=False)
        assert result.exit_code != 0

    def test_server_help(self):
        result = runner.invoke(app, ["server", "--help"])
        assert result.exit_code == 0
        assert "Server management" in result.output

    def test_create_key(self):
        mock_response = MagicMock()
        mock_response.json.return_value = {"api_key": "smh_test"}
        mock_client = MagicMock()
        mock_client.__enter__ = MagicMock(return_value=mock_client)
        mock_client.__exit__ = MagicMock(return_value=False)
        mock_client.post.return_value = mock_response

        with patch("socialmedia_hub.cli.main.httpx.Client", return_value=mock_client):
            result = runner.invoke(app, ["create-key", "--name", "test"])
            assert result.exit_code == 0

    def test_fetch_unknown_platform(self):
        result = runner.invoke(app, ["fetch", "https://example.com/video", "--api-key", "test"])
        assert result.exit_code == 1
        assert "Could not detect platform" in result.output

    def test_server_status_offline(self):
        mock_client = MagicMock()
        mock_client.__enter__ = MagicMock(return_value=mock_client)
        mock_client.__exit__ = MagicMock(return_value=False)
        mock_client.get.side_effect = Exception("Connection refused")

        with patch("socialmedia_hub.cli.main.httpx.Client", return_value=mock_client):
            result = runner.invoke(app, ["server", "status"])
            assert result.exit_code == 1
            assert "Offline" in result.output

    def test_server_status_online(self):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"version": "1.0.0"}
        mock_client = MagicMock()
        mock_client.__enter__ = MagicMock(return_value=mock_client)
        mock_client.__exit__ = MagicMock(return_value=False)
        mock_client.get.return_value = mock_response

        with patch("socialmedia_hub.cli.main.httpx.Client", return_value=mock_client):
            result = runner.invoke(app, ["server", "status"])
            assert result.exit_code == 0
            assert "OK" in result.output
