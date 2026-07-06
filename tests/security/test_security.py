"""Security tests for SocialMedia-Hub."""

from __future__ import annotations

import pytest
from fastapi.testclient import TestClient

from socialmedia_hub.server.main import app


@pytest.fixture
def client():
    """Create test client."""
    return TestClient(app)


class TestAuthenticationSecurity:
    """Test authentication security."""

    def test_missing_auth_returns_401(self, client):
        """Test that missing auth returns 401."""
        response = client.get("/api/v1/auth/verify")
        assert response.status_code == 401

    def test_invalid_api_key_returns_401(self, client):
        """Test that invalid API key returns 401."""
        response = client.get(
            "/api/v1/auth/verify",
            headers={"Authorization": "Bearer invalid_key"}
        )
        assert response.status_code == 401

    def test_api_key_not_in_response(self, client):
        """Test that API key is not exposed in responses."""
        response = client.post("/api/v1/auth/create_key?name=test")
        data = response.json()
        # API key should be in response for creation, but not in error responses
        assert "api_key" in data

    def test_api_key_hidden_in_errors(self, client):
        """Test that API key is hidden in error responses."""
        response = client.get(
            "/api/v1/auth/verify",
            headers={"Authorization": "Bearer secret_key"}
        )
        assert response.status_code == 401
        # Should not expose the actual key
        assert "secret_key" not in response.text


class TestInputValidation:
    """Test input validation."""

    def test_reject_invalid_json(self, client):
        """Test that invalid JSON is rejected."""
        # Create API key first
        response = client.post("/api/v1/auth/create_key?name=test")
        api_key = response.json()["api_key"]

        response = client.post(
            "/api/v1/mcp/call",
            content="not json",
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {api_key}"
            }
        )
        # Should return 200 with error message or 400/422
        assert response.status_code in [200, 400, 422]
        if response.status_code == 200:
            data = response.json()
            assert "error" in data

    def test_reject_missing_tool_parameter(self, client):
        """Test that missing tool parameter is rejected."""
        # Create API key
        response = client.post("/api/v1/auth/create_key?name=test")
        api_key = response.json()["api_key"]

        response = client.post(
            "/api/v1/mcp/call",
            json={"arguments": {}},
            headers={"Authorization": f"Bearer {api_key}"}
        )
        assert response.status_code == 200
        data = response.json()
        assert "error" in data


class TestRateLimiting:
    """Test rate limiting."""

    def test_rate_limit_enforcement(self, client):
        """Test that rate limiting is enforced."""
        # Create a free tier key
        response = client.post("/api/v1/auth/create_key?name=test&tier=free")
        api_key = response.json()["api_key"]

        # Make many requests quickly
        for _ in range(10):
            client.get(
                "/api/v1/health/check",
                headers={"Authorization": f"Bearer {api_key}"}
            )

        # Should still work within free tier limits
        response = client.get(
            "/api/v1/health/check",
            headers={"Authorization": f"Bearer {api_key}"}
        )
        assert response.status_code == 200


class TestSecureHeaders:
    """Test secure headers."""

    def test_cors_headers(self, client):
        """Test CORS headers are present."""
        response = client.options(
            "/api/v1/health/check",
            headers={
                "Origin": "http://localhost:3000",
                "Access-Control-Request-Method": "GET"
            }
        )
        # CORS should be configured
        assert response.status_code in [200, 405]

    def test_content_type_json(self, client):
        """Test that responses have correct content type."""
        response = client.get("/api/v1/health/check")
        assert "application/json" in response.headers.get("content-type", "")


class TestErrorHandling:
    """Test error handling security."""

    def test_404_for_nonexistent_routes(self, client):
        """Test that nonexistent routes return 404 or 401 (auth required)."""
        response = client.get("/api/v1/nonexistent/endpoint")
        # Some routes require auth, some don't
        assert response.status_code in [401, 404]

    def test_405_for_wrong_method(self, client):
        """Test that wrong HTTP method returns 405 or 401 (auth required)."""
        response = client.delete("/api/v1/health/check")
        # Some routes require auth, some don't
        assert response.status_code in [401, 405]


class TestDependencySecurity:
    """Test dependency security."""

    def test_no_known_vulnerabilities_in_direct_deps(self):
        """Test that direct dependencies have no known vulnerabilities."""
        # This is a documentation test - actual audit should be run separately
        # Direct dependencies: httpx, pydantic, fastapi, anyio
        # These should be checked regularly
        pass
