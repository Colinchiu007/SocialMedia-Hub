"""Extended MCP tool tests."""

from __future__ import annotations

import pytest

from socialmedia_hub.mcp.server import MCPServer, create_mcp_server


@pytest.fixture
def mcp():
    return create_mcp_server(api_key="test")


class TestMCPTikTokTools:
    """Test TikTok MCP tools."""

    def test_tiktok_tools_count(self, mcp):
        tools = [name for name in mcp.tools if "tiktok" in name]
        assert len(tools) >= 25

    def test_tiktok_fetch_video(self, mcp):
        assert "tiktok_fetch_video" in mcp.tools

    def test_tiktok_fetch_user(self, mcp):
        assert "tiktok_fetch_user" in mcp.tools

    def test_tiktok_search(self, mcp):
        assert "tiktok_search" in mcp.tools


class TestMCPDouyinTools:
    """Test Douyin MCP tools."""

    def test_douyin_tools_count(self, mcp):
        tools = [name for name in mcp.tools if "douyin" in name]
        assert len(tools) >= 30

    def test_douyin_fetch_video(self, mcp):
        assert "douyin_fetch_video" in mcp.tools

    def test_douyin_search(self, mcp):
        assert "douyin_search" in mcp.tools


class TestMCPIInstagramTools:
    """Test Instagram MCP tools."""

    def test_instagram_tools_count(self, mcp):
        tools = [name for name in mcp.tools if "instagram" in name]
        assert len(tools) >= 20


class TestMCPYouTubeTools:
    """Test YouTube MCP tools."""

    def test_youtube_tools_count(self, mcp):
        tools = [name for name in mcp.tools if "youtube" in name]
        assert len(tools) >= 15


class TestMCPTwitterTools:
    """Test Twitter MCP tools."""

    def test_twitter_tools_count(self, mcp):
        tools = [name for name in mcp.tools if "twitter" in name]
        assert len(tools) >= 15


class TestMCPXiaohongshuTools:
    """Test Xiaohongshu MCP tools."""

    def test_xiaohongshu_tools_count(self, mcp):
        tools = [name for name in mcp.tools if "xiaohongshu" in name]
        assert len(tools) >= 15


class TestMCPBilibiliTools:
    """Test Bilibili MCP tools."""

    def test_bilibili_tools_count(self, mcp):
        tools = [name for name in mcp.tools if "bilibili" in name]
        assert len(tools) >= 15


class TestMCPWeiboTools:
    """Test Weibo MCP tools."""

    def test_weibo_tools_count(self, mcp):
        tools = [name for name in mcp.tools if "weibo" in name]
        assert len(tools) >= 10


class TestMCPKuaishouTools:
    """Test Kuaishou MCP tools."""

    def test_kuaishou_tools_count(self, mcp):
        tools = [name for name in mcp.tools if "kuaishou" in name]
        assert len(tools) >= 10


class TestMCPLinkedinTools:
    """Test LinkedIn MCP tools."""

    def test_linkedin_tools_count(self, mcp):
        tools = [name for name in mcp.tools if "linkedin" in name]
        assert len(tools) >= 10


class TestMCPRedditTools:
    """Test Reddit MCP tools."""

    def test_reddit_tools_count(self, mcp):
        tools = [name for name in mcp.tools if "reddit" in name]
        assert len(tools) >= 10


class TestMCPZhihuTools:
    """Test Zhihu MCP tools."""

    def test_zhihu_tools_count(self, mcp):
        tools = [name for name in mcp.tools if "zhihu" in name]
        assert len(tools) >= 10


class TestMCPThreadsTools:
    """Test Threads MCP tools."""

    def test_threads_tools_count(self, mcp):
        tools = [name for name in mcp.tools if "threads" in name]
        assert len(tools) >= 5


class TestMCPWeChatTools:
    """Test WeChat MCP tools."""

    def test_wechat_tools_count(self, mcp):
        tools = [name for name in mcp.tools if "wechat" in name]
        assert len(tools) >= 5


class TestMCPLemon8Tools:
    """Test Lemon8 MCP tools."""

    def test_lemon8_tools_count(self, mcp):
        tools = [name for name in mcp.tools if "lemon8" in name]
        assert len(tools) >= 5


class TestMCPUtilityTools:
    """Test utility MCP tools."""

    def test_utility_tools_count(self, mcp):
        tools = [name for name in mcp.tools if "health" in name or "hybrid" in name]
        assert len(tools) >= 5
