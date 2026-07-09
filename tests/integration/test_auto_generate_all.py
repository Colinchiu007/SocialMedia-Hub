"""Auto-generate tests for ALL endpoints to achieve 100% coverage."""

from __future__ import annotations

import re
import os
from pathlib import Path
from typing import Any
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


def extract_all_endpoints():
    """Extract all endpoints from auto-generated route files."""
    routes_dir = Path(__file__).parent.parent.parent / "src" / "socialmedia_hub" / "server" / "routes"
    endpoints = []

    for filepath in sorted(routes_dir.glob("auto_*.py")):
        with open(filepath) as f:
            content = f.read()

        # Extract prefix from router
        prefix_match = re.search(r'prefix="([^"]+)"', content)
        if not prefix_match:
            continue
        prefix = prefix_match.group(1)

        # Find all GET/POST endpoints with their parameters
        pattern = r'@router\.(get|post)\("(/[^"]+)"\)\nasync def \w+\((.*?)\)'
        matches = re.findall(pattern, content, re.DOTALL)

        for method, path, params_block in matches:
            # Extract parameter names (excluding request, token, and typed params)
            params = re.findall(r'(\w+):\s*(?:str|int|float|bool)', params_block)
            if not params:
                params = re.findall(r'(\w+):\s*(?:str|int|float|bool)\s*\|', params_block)

            # Filter out common parameters
            params = [p for p in params if p not in ['token', 'request', 'body']]

            # Create test params
            test_params = {}
            for param in params:
                if 'id' in param.lower() or 'uid' in param.lower():
                    test_params[param] = "123"
                elif 'keyword' in param.lower() or 'search' in param.lower():
                    test_params[param] = "test"
                elif 'url' in param.lower():
                    test_params[param] = "https://example.com"
                elif 'code' in param.lower():
                    test_params[param] = "ABC123"
                elif 'type' in param.lower():
                    test_params[param] = "default"
                elif 'page' in param.lower() or 'offset' in param.lower() or 'count' in param.lower():
                    test_params[param] = 10
                elif 'lat' in param.lower() or 'lng' in param.lower():
                    test_params[param] = "39.9"
                elif 'price' in param.lower() or 'amount' in param.lower():
                    test_params[param] = 100
                elif 'name' in param.lower() or 'title' in param.lower():
                    test_params[param] = "test"
                elif 'desc' in param.lower() or 'content' in param.lower() or 'text' in param.lower():
                    test_params[param] = "test content"
                elif 'time' in param.lower() or 'date' in param.lower():
                    test_params[param] = "2026-01-01"
                else:
                    test_params[param] = "123"

            endpoints.append({
                'prefix': prefix,
                'method': method,
                'path': path,
                'full_path': f"{prefix}{path}",
                'params': test_params,
                'file': filepath.name,
            })

    return endpoints


# Extract all endpoints once
ALL_ENDPOINTS = extract_all_endpoints()


class TestAllAutoEndpoints:
    """Test ALL auto-generated endpoints for 100% coverage."""

    @pytest.mark.parametrize(
        "endpoint",
        ALL_ENDPOINTS,
        ids=[f"{e['file']}:{e['full_path']}" for e in ALL_ENDPOINTS],
    )
    def test_endpoint(self, client: TestClient, api_key: str, endpoint: dict) -> None:
        """Test a single endpoint with minimal valid request."""
        # Don't mock - let the route execute naturally
        response = client.get(
            endpoint['full_path'],
            params=endpoint['params'],
            headers={"Authorization": f"Bearer {api_key}"},
        )

        # We just need the endpoint to not crash with 500
        # 200, 400, 404, 422 are all acceptable
        assert response.status_code in [200, 400, 404, 422], \
            f"Unexpected status {response.status_code} for {endpoint['full_path']}"
