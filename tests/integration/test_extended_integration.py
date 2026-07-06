"""Extended integration tests for SocialMedia-Hub."""

from __future__ import annotations

import pytest
from fastapi.testclient import TestClient

from socialmedia_hub.mcp.server import create_mcp_server
from socialmedia_hub.server.main import app


@pytest.fixture
def client():
    """Create test client."""
    return TestClient(app)


@pytest.fixture
def api_key(client):
    """Create test API key."""
    response = client.post("/api/v1/auth/create_key?name=integration-test&tier=free")
    return response.json()["api_key"]


@pytest.fixture
def auth_headers(api_key):
    """Create auth headers."""
    return {"Authorization": f"Bearer {api_key}"}


class TestAPIEndpointCoverage:
    """Test coverage of API endpoints."""

    def test_all_health_endpoints(self, client):
        """Test all health endpoints."""
        endpoints = [
            "/api/v1/health/check",
            "/api/v1/health/platforms",
            "/api/v1/health/stats",
        ]
        for endpoint in endpoints:
            response = client.get(endpoint)
            assert response.status_code == 200, f"Failed: {endpoint}"

    def test_all_monitor_endpoints(self, client):
        """Test all monitor endpoints."""
        endpoints = [
            "/api/v1/monitor/status",
            "/api/v1/monitor/metrics",
            "/api/v1/monitor/platforms",
        ]
        for endpoint in endpoints:
            response = client.get(endpoint)
            assert response.status_code == 200, f"Failed: {endpoint}"

    def test_auth_flow(self, client):
        """Test complete auth flow."""
        # Create key
        response = client.post("/api/v1/auth/create_key?name=test&tier=pro")
        assert response.status_code == 200
        api_key = response.json()["api_key"]

        # Verify key
        response = client.get(
            "/api/v1/auth/verify",
            headers={"Authorization": f"Bearer {api_key}"}
        )
        assert response.status_code == 200
        assert response.json()["valid"] is True

    def test_mcp_endpoints(self, client, auth_headers):
        """Test all MCP endpoints."""
        endpoints = [
            ("GET", "/api/v1/mcp/tools"),
            ("GET", "/api/v1/mcp/config"),
        ]
        for method, endpoint in endpoints:
            if method == "GET":
                response = client.get(endpoint, headers=auth_headers)
            else:
                response = client.post(endpoint, headers=auth_headers)
            assert response.status_code == 200, f"Failed: {method} {endpoint}"


class TestMCPToolIntegration:
    """Test MCP tool integration."""

    def test_mcp_server_initialization(self):
        """Test MCP server initialization."""
        mcp = create_mcp_server(api_key="test")
        assert len(mcp.tools) > 0
        assert mcp.api_key == "test"

    def test_mcp_tool_listing(self):
        """Test MCP tool listing."""
        mcp = create_mcp_server(api_key="test")
        tools = mcp.list_tools()
        assert len(tools) > 0
        assert all("name" in tool for tool in tools)
        assert all("description" in tool for tool in tools)
        assert all("inputSchema" in tool for tool in tools)

    def test_mcp_tool_categories(self):
        """Test MCP tools are organized by platform."""
        mcp = create_mcp_server(api_key="test")
        tools = mcp.list_tools()
        tool_names = [t["name"] for t in tools]

        # Check for tools from different platforms
        platforms = ["tiktok", "douyin", "instagram", "youtube", "twitter"]
        for platform in platforms:
            assert any(platform in name for name in tool_names), f"No tools for {platform}"

    def test_mcp_tool_call_nonexistent(self):
        """Test calling non-existent MCP tool."""
        mcp = create_mcp_server(api_key="test")
        result = mcp.call_tool("nonexistent_tool", {})
        assert "error" in result

    def test_mcp_tool_count(self):
        """Test MCP tool count exceeds 300."""
        mcp = create_mcp_server(api_key="test")
        assert len(mcp.tools) >= 300, f"Expected >= 300 tools, got {len(mcp.tools)}"

    def test_mcp_tool_export(self):
        """Test MCP server export."""
        mcp = create_mcp_server(api_key="test")
        config = mcp.to_dict()
        assert "name" in config
        assert "version" in config
        assert "tools" in config
        assert config["name"] == "socialmedia-hub"


class TestWebSocketIntegration:
    """Test WebSocket integration."""

    def test_websocket_manager_exists(self):
        """Test WebSocket manager exists."""
        from socialmedia_hub.websocket import manager
        assert manager is not None

    def test_websocket_manager_subscribe(self):
        """Test WebSocket manager subscription."""
        import asyncio

        from socialmedia_hub.websocket.manager import ConnectionManager

        mgr = ConnectionManager()

        async def test():
            await mgr.subscribe("client1", "channel1")
            assert "channel1" in mgr.subscriptions
            assert "client1" in mgr.subscriptions["channel1"]

        asyncio.run(test())

    def test_websocket_manager_unsubscribe(self):
        """Test WebSocket manager unsubscription."""
        import asyncio

        from socialmedia_hub.websocket.manager import ConnectionManager

        mgr = ConnectionManager()

        async def test():
            await mgr.subscribe("client1", "channel1")
            await mgr.unsubscribe("client1", "channel1")
            assert "client1" not in mgr.subscriptions.get("channel1", set())

        asyncio.run(test())

    def test_websocket_manager_broadcast(self):
        """Test WebSocket manager broadcast."""
        import asyncio

        from socialmedia_hub.websocket.manager import ConnectionManager

        mgr = ConnectionManager()

        async def test():
            # Broadcast to empty channel should not raise
            await mgr.broadcast_to_channel("empty", {"type": "test"})

        asyncio.run(test())


class TestErrorHandlingIntegration:
    """Test error handling integration."""

    def test_invalid_json_handling(self, client, auth_headers):
        """Test invalid JSON handling."""
        response = client.post(
            "/api/v1/mcp/call",
            content="not json",
            headers={**auth_headers, "Content-Type": "application/json"}
        )
        assert response.status_code in [200, 400, 422]

    def test_missing_auth_handling(self, client):
        """Test missing auth handling."""
        response = client.get("/api/v1/auth/verify")
        assert response.status_code == 401

    def test_invalid_auth_handling(self, client):
        """Test invalid auth handling."""
        response = client.get(
            "/api/v1/auth/verify",
            headers={"Authorization": "Bearer invalid"}
        )
        assert response.status_code == 401

    def test_rate_limit_handling(self, client):
        """Test rate limit handling."""
        # Create key
        response = client.post("/api/v1/auth/create_key?name=test&tier=free")
        api_key = response.json()["api_key"]

        # Make multiple requests
        for _ in range(5):
            response = client.get(
                "/api/v1/health/check",
                headers={"Authorization": f"Bearer {api_key}"}
            )
            assert response.status_code == 200


class TestPerformanceIntegration:
    """Test performance integration."""

    def test_response_time_under_threshold(self, client):
        """Test response time is under threshold."""
        import time

        endpoints = [
            "/api/v1/health/check",
            "/api/v1/health/platforms",
            "/api/v1/monitor/status",
        ]

        for endpoint in endpoints:
            start = time.perf_counter()
            client.get(endpoint)
            elapsed = (time.perf_counter() - start) * 1000
            assert elapsed < 100, f"{endpoint} took {elapsed:.2f}ms"

    def test_concurrent_requests_stability(self, client):
        """Test concurrent request stability."""
        import concurrent.futures

        def make_request():
            return client.get("/api/v1/health/check")

        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            futures = [executor.submit(make_request) for _ in range(20)]
            results = [f.result() for f in futures]

        assert all(r.status_code == 200 for r in results)
