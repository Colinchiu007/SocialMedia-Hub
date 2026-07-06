"""Tests for MCP Server."""

from __future__ import annotations

from socialmedia_hub.mcp.server import create_mcp_server


class TestMCPServer:
    """Test MCP Server functionality."""

    def test_create_mcp_server(self) -> None:
        """Test creating MCP server."""
        mcp = create_mcp_server(api_key="test-key", base_url="http://test:8000")
        assert mcp.api_key == "test-key"
        assert mcp.base_url == "http://test:8000"

    def test_list_tools(self) -> None:
        """Test listing MCP tools."""
        mcp = create_mcp_server(api_key="test-key")
        tools = mcp.list_tools()
        assert isinstance(tools, list)
        assert len(tools) > 0

    def test_tool_structure(self) -> None:
        """Test tool structure."""
        mcp = create_mcp_server(api_key="test-key")
        tools = mcp.list_tools()
        for tool in tools:
            assert "name" in tool
            assert "description" in tool
            assert "inputSchema" in tool

    def test_tool_categories(self) -> None:
        """Test that tools are organized by platform."""
        mcp = create_mcp_server(api_key="test-key")
        tools = mcp.list_tools()
        tool_names = [t["name"] for t in tools]

        # Check for tools from different platforms
        assert any("tiktok" in name for name in tool_names)
        assert any("douyin" in name for name in tool_names)
        assert any("instagram" in name for name in tool_names)
        assert any("youtube" in name for name in tool_names)
        assert any("twitter" in name for name in tool_names)

    def test_call_nonexistent_tool(self) -> None:
        """Test calling a non-existent tool."""
        mcp = create_mcp_server(api_key="test-key")
        result = mcp.call_tool("nonexistent_tool", {})
        assert "error" in result

    def test_to_dict(self) -> None:
        """Test exporting MCP server as dict."""
        mcp = create_mcp_server(api_key="test-key")
        config = mcp.to_dict()
        assert "name" in config
        assert "version" in config
        assert "tools" in config
        assert config["name"] == "socialmedia-hub"

    def test_tool_count(self) -> None:
        """Test that we have a reasonable number of tools."""
        mcp = create_mcp_server(api_key="test-key")
        tools = mcp.list_tools()
        # Should have at least 100 tools
        assert len(tools) >= 100


class TestMCPServerIntegration:
    """Integration tests for MCP Server."""

    def test_tiktok_tools_registered(self) -> None:
        """Test that TikTok tools are registered."""
        mcp = create_mcp_server(api_key="test-key")
        tools = mcp.list_tools()
        tool_names = [t["name"] for t in tools]

        tiktok_tools = [name for name in tool_names if name.startswith("tiktok_")]
        assert len(tiktok_tools) >= 10

    def test_douyin_tools_registered(self) -> None:
        """Test that Douyin tools are registered."""
        mcp = create_mcp_server(api_key="test-key")
        tools = mcp.list_tools()
        tool_names = [t["name"] for t in tools]

        douyin_tools = [name for name in tool_names if name.startswith("douyin_")]
        assert len(douyin_tools) >= 10

    def test_instagram_tools_registered(self) -> None:
        """Test that Instagram tools are registered."""
        mcp = create_mcp_server(api_key="test-key")
        tools = mcp.list_tools()
        tool_names = [t["name"] for t in tools]

        instagram_tools = [name for name in tool_names if name.startswith("instagram_")]
        assert len(instagram_tools) >= 5

    def test_youtube_tools_registered(self) -> None:
        """Test that YouTube tools are registered."""
        mcp = create_mcp_server(api_key="test-key")
        tools = mcp.list_tools()
        tool_names = [t["name"] for t in tools]

        youtube_tools = [name for name in tool_names if name.startswith("youtube_")]
        assert len(youtube_tools) >= 5

    def test_twitter_tools_registered(self) -> None:
        """Test that Twitter tools are registered."""
        mcp = create_mcp_server(api_key="test-key")
        tools = mcp.list_tools()
        tool_names = [t["name"] for t in tools]

        twitter_tools = [name for name in tool_names if name.startswith("twitter_")]
        assert len(twitter_tools) >= 5

    def test_utility_tools_registered(self) -> None:
        """Test that utility tools are registered."""
        mcp = create_mcp_server(api_key="test-key")
        tools = mcp.list_tools()
        tool_names = [t["name"] for t in tools]

        utility_tools = [name for name in tool_names if name.startswith("health_") or name.startswith("hybrid_")]
        assert len(utility_tools) >= 3
