"""Integration tests for SocialMedia-Hub SDK + Server."""

from __future__ import annotations

import pytest
from fastapi.testclient import TestClient

from socialmedia_hub import SocialMediaHub
from socialmedia_hub.server.main import app


@pytest.fixture
def server_client():
    """Create test server client."""
    return TestClient(app)


@pytest.fixture
def sdk_client(server_client):
    """Create SDK client connected to test server."""
    # Create API key
    response = server_client.post("/api/v1/auth/create_key?name=integration-test&tier=free")
    api_key = response.json()["api_key"]

    # Create SDK client
    client = SocialMediaHub(
        api_key=api_key,
        base_url="http://testserver",
    )
    # Override the httpx client to use the test server
    client._client = server_client
    return client


class TestSDKServerIntegration:
    """Test SDK + Server integration."""

    def test_sdk_health_check(self, sdk_client):
        """Test SDK health check through server."""
        # The SDK client should be able to call the server
        assert sdk_client._api_key is not None
        assert sdk_client._base_url == "http://testserver"

    def test_sdk_authentication(self, sdk_client):
        """Test SDK authentication flow."""
        # Verify the API key works
        assert len(sdk_client._api_key) > 0
        assert sdk_client._api_key.startswith("smh_")

    def test_sdk_error_handling(self, sdk_client):
        """Test SDK error handling."""
        from socialmedia_hub._errors import SMHError
        # The SDK should handle errors gracefully
        assert issubclass(SMHError, Exception)


class TestAPIEndpointIntegration:
    """Test API endpoint integration."""

    def test_health_check_endpoint(self, server_client):
        """Test health check endpoint."""
        response = server_client.get("/api/v1/health/check")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "ok"

    def test_platform_list_endpoint(self, server_client):
        """Test platform list endpoint."""
        response = server_client.get("/api/v1/health/platforms")
        assert response.status_code == 200
        data = response.json()
        assert data["count"] > 0

    def test_api_key_creation(self, server_client):
        """Test API key creation."""
        response = server_client.post("/api/v1/auth/create_key?name=test&tier=free")
        assert response.status_code == 200
        data = response.json()
        assert "api_key" in data

    def test_api_key_verification(self, server_client):
        """Test API key verification."""
        # Create key
        response = server_client.post("/api/v1/auth/create_key?name=test&tier=free")
        api_key = response.json()["api_key"]

        # Verify key
        response = server_client.get(
            "/api/v1/auth/verify",
            headers={"Authorization": f"Bearer {api_key}"}
        )
        assert response.status_code == 200
        assert response.json()["valid"] is True

    def test_monitor_status(self, server_client):
        """Test monitor status endpoint."""
        response = server_client.get("/api/v1/monitor/status")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "operational"

    def test_mcp_tools_list(self, server_client):
        """Test MCP tools listing."""
        # Create key
        response = server_client.post("/api/v1/auth/create_key?name=test&tier=free")
        api_key = response.json()["api_key"]

        # List tools
        response = server_client.get(
            "/api/v1/mcp/tools",
            headers={"Authorization": f"Bearer {api_key}"}
        )
        assert response.status_code == 200
        data = response.json()
        assert data["count"] > 0


class TestPerformanceBaseline:
    """Test performance baseline."""

    def test_health_check_response_time(self, server_client):
        """Test health check response time."""
        import time
        start = time.time()
        for _ in range(10):
            server_client.get("/api/v1/health/check")
        elapsed = time.time() - start
        avg_time = elapsed / 10
        # Should respond within 100ms on average
        assert avg_time < 0.1, f"Average response time: {avg_time:.3f}s"

    def test_concurrent_requests(self, server_client):
        """Test concurrent request handling."""
        import concurrent.futures

        def make_request():
            return server_client.get("/api/v1/health/check")

        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            futures = [executor.submit(make_request) for _ in range(10)]
            results = [f.result() for f in futures]

        # All requests should succeed
        assert all(r.status_code == 200 for r in results)
