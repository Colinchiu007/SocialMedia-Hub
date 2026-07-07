"""Auto-discovery and test all endpoints to maximize coverage."""

from __future__ import annotations

import warnings
from unittest.mock import AsyncMock, patch

import pytest
from fastapi.testclient import TestClient
from fastapi.routing import APIRoute

from socialmedia_hub.server._core import generate_api_key
from socialmedia_hub.server.main import app


@pytest.fixture
def api_key() -> str:
    return generate_api_key("test", "pro")


@pytest.fixture
def client() -> TestClient:
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        return TestClient(app, raise_server_exceptions=False)


def get_all_routes() -> list[dict]:
    """Extract all API routes with their parameters."""
    routes = []
    for route in app.routes:
        if isinstance(route, APIRoute) and hasattr(route, "methods"):
            # Skip health/monitor endpoints (no auth needed)
            if "/health/" in route.path or "/monitor/" in route.path:
                continue
            # Skip websocket endpoints
            if "/ws/" in route.path:
                continue
            # Skip OpenAPI/docs endpoints
            if route.path in ["/docs", "/redoc", "/openapi.json"]:
                continue
            # Skip POST/PUT/PATCH endpoints (only test GET for coverage)
            if "GET" not in route.methods:
                continue

            # Extract path parameters from route path
            import re
            path_params = re.findall(r"\{(\w+)\}", route.path)

            # Simple parameter defaults
            params = {}
            for param_name in path_params:
                params[param_name] = "123"

            # Add common query parameters
            if "/api/v1/" in route.path:
                # Most endpoints need some identifier
                if "sec_uid" in str(route.dependant.query_params):
                    params["sec_uid"] = "123"
                if "sec_user_id" in str(route.dependant.query_params):
                    params["sec_user_id"] = "123"
                if "user_id" in str(route.dependant.query_params):
                    params["user_id"] = "123"
                if "video_id" in str(route.dependant.query_params):
                    params["video_id"] = "123"
                if "aweme_id" in str(route.dependant.query_params):
                    params["aweme_id"] = "123"
                if "media_id" in str(route.dependant.query_params):
                    params["media_id"] = "123"
                if "channel_id" in str(route.dependant.query_params):
                    params["channel_id"] = "123"
                if "mid" in str(route.dependant.query_params):
                    params["mid"] = "123"
                if "bvid" in str(route.dependant.query_params):
                    params["bvid"] = "123"
                if "weibo_id" in str(route.dependant.query_params):
                    params["weibo_id"] = "123"
                if "photo_id" in str(route.dependant.query_params):
                    params["photo_id"] = "123"
                if "company_id" in str(route.dependant.query_params):
                    params["company_id"] = "123"
                if "post_id" in str(route.dependant.query_params):
                    params["post_id"] = "123"
                if "username" in str(route.dependant.query_params):
                    params["username"] = "test"
                if "subreddit" in str(route.dependant.query_params):
                    params["subreddit"] = "test"
                if "question_id" in str(route.dependant.query_params):
                    params["question_id"] = "123"
                if "answer_id" in str(route.dependant.query_params):
                    params["answer_id"] = "123"
                if "note_id" in str(route.dependant.query_params):
                    params["note_id"] = "123"
                if "thread_id" in str(route.dependant.query_params):
                    params["thread_id"] = "123"
                if "tweet_id" in str(route.dependant.query_params):
                    params["tweet_id"] = "123"
                if "artist_id" in str(route.dependant.query_params):
                    params["artist_id"] = "123"
                if "playlist_id" in str(route.dependant.query_params):
                    params["playlist_id"] = "123"
                if "song_id" in str(route.dependant.query_params):
                    params["song_id"] = "123"
                if "keyword" in str(route.dependant.query_params):
                    params["keyword"] = "test"
                if "billboard_type" in str(route.dependant.query_params):
                    params["billboard_type"] = "hot"
                if "product_id" in str(route.dependant.query_params):
                    params["product_id"] = "123"

            routes.append({
                "path": route.path,
                "methods": list(route.methods),
                "params": params,
                "name": route.name,
            })
    return routes


# Get all routes once
ALL_ROUTES = get_all_routes()


class TestAllEndpoints:
    """Test all discovered endpoints to maximize coverage."""

    @pytest.mark.parametrize("route_info", ALL_ROUTES, ids=[r["path"] for r in ALL_ROUTES])
    @patch("socialmedia_hub.server._core.proxy_request")
    def test_endpoint(self, mock_proxy: AsyncMock, client: TestClient, api_key: str, route_info: dict) -> None:
        """Test a single endpoint with minimal valid request."""
        mock_proxy.return_value = {"data": [], "status": "ok"}

        path = route_info["path"]
        params = route_info["params"].copy()

        # Make request
        response = client.get(
            path,
            params=params,
            headers={"Authorization": f"Bearer {api_key}"},
        )

        # We just need the endpoint to not crash with 500
        # 200, 400, 404, 422 are all acceptable
        assert response.status_code in [200, 400, 404, 422], f"Unexpected status {response.status_code} for {path}"
