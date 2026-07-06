"""Tests for API endpoints."""

from __future__ import annotations

import pytest
from fastapi.testclient import TestClient

from socialmedia_hub.server.main import app


@pytest.fixture
def client():
    """Create test client."""
    return TestClient(app)


@pytest.fixture
def api_key(client):
    """Create test API key."""
    response = client.post("/api/v1/auth/create_key?name=test&tier=free")
    return response.json()["api_key"]


@pytest.fixture
def auth_headers(api_key):
    """Create auth headers."""
    return {"Authorization": f"Bearer {api_key}"}


class TestHealthEndpoints:
    """Test health check endpoints."""

    def test_health_check(self, client):
        response = client.get("/api/v1/health/check")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "ok"
        assert "version" in data
        assert "timestamp" in data

    def test_list_platforms(self, client):
        response = client.get("/api/v1/health/platforms")
        assert response.status_code == 200
        data = response.json()
        assert "platforms" in data
        assert "count" in data
        assert data["count"] > 0

    def test_health_stats(self, client):
        response = client.get("/api/v1/health/stats")
        assert response.status_code == 200
        data = response.json()
        assert "total_endpoints" in data
        assert "platforms" in data


class TestAuthEndpoints:
    """Test authentication endpoints."""

    def test_create_api_key(self, client):
        response = client.post("/api/v1/auth/create_key?name=test&tier=free")
        assert response.status_code == 200
        data = response.json()
        assert "api_key" in data
        assert data["name"] == "test"
        assert data["tier"] == "free"

    def test_verify_api_key(self, client, auth_headers):
        response = client.get("/api/v1/auth/verify", headers=auth_headers)
        assert response.status_code == 200
        data = response.json()
        assert data["valid"] is True

    def test_invalid_api_key(self, client):
        response = client.get(
            "/api/v1/auth/verify",
            headers={"Authorization": "Bearer invalid_key"}
        )
        assert response.status_code == 401

    def test_missing_api_key(self, client):
        response = client.get("/api/v1/auth/verify")
        assert response.status_code == 401


class TestMonitorEndpoints:
    """Test monitoring endpoints."""

    def test_monitor_status(self, client):
        response = client.get("/api/v1/monitor/status")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "operational"
        assert "version" in data

    def test_monitor_metrics(self, client):
        response = client.get("/api/v1/monitor/metrics")
        assert response.status_code == 200
        data = response.json()
        assert "requests_total" in data
        assert "error_rate" in data

    def test_monitor_platforms(self, client):
        response = client.get("/api/v1/monitor/platforms")
        assert response.status_code == 200
        data = response.json()
        assert "platforms" in data
        assert "count" in data


class TestMCPEndpoints:
    """Test MCP endpoints."""

    def test_mcp_list_tools(self, client, auth_headers):
        response = client.get("/api/v1/mcp/tools", headers=auth_headers)
        assert response.status_code == 200
        data = response.json()
        assert "tools" in data
        assert "count" in data
        assert data["count"] > 0

    def test_mcp_config(self, client, auth_headers):
        response = client.get("/api/v1/mcp/config", headers=auth_headers)
        assert response.status_code == 200
        data = response.json()
        assert "mcpServers" in data
        assert "socialmedia-hub" in data["mcpServers"]

    def test_mcp_call_tool(self, client, auth_headers):
        response = client.post(
            "/api/v1/mcp/call",
            json={"tool": "health_check", "arguments": {}},
            headers=auth_headers,
        )
        assert response.status_code == 200
        data = response.json()
        # Tool call may fail if server is not running, but the endpoint should work
        assert "result" in data or "error" in data

    def test_mcp_call_nonexistent_tool(self, client, auth_headers):
        response = client.post(
            "/api/v1/mcp/call",
            json={"tool": "nonexistent", "arguments": {}},
            headers=auth_headers,
        )
        assert response.status_code == 200
        data = response.json()
        assert "error" in data


class TestGenericProxy:
    """Test generic proxy endpoint."""

    def test_generic_proxy_requires_auth(self, client):
        response = client.get("/api/v1/douyin/web/fetch_video?video_id=123")
        assert response.status_code == 401

    def test_generic_proxy_with_auth(self, client, auth_headers):
        response = client.get(
            "/api/v1/douyin/web/fetch_video?video_id=123",
            headers=auth_headers,
        )
        # Will fail with upstream error, but auth should pass
        assert response.status_code in [200, 502, 504]
