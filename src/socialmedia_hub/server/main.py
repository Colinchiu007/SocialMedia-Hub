"""SocialMedia-Hub API Server - Auto-generated router registration."""

from __future__ import annotations

import importlib
import logging
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from fastapi import Depends, FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware

from socialmedia_hub.server._core import (
    API_KEYS,
    PLATFORM_CONFIGS,
    generate_api_key,
    proxy_request,
    verify_api_key,
)
from socialmedia_hub.server.routes.live_room import router as live_room_router
from socialmedia_hub.server.routes.netease import router as netease_router
from socialmedia_hub.websocket.endpoints import router as websocket_router

logger = logging.getLogger("socialmedia_hub.server")

# ---------------------------------------------------------------------------
# App setup
# ---------------------------------------------------------------------------

app = FastAPI(
    title="SocialMedia-Hub API",
    description="Multi-platform social media data API - 1010+ endpoints across 16+ platforms",
    version="0.1.0",
    docs_url="/docs",  # Swagger UI
    redoc_url="/redoc",  # ReDoc
    openapi_url="/openapi.json",  # OpenAPI spec
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------------------------------------------------------------------
# Auto-register all routers from routes/ directory
# ---------------------------------------------------------------------------

routes_dir = Path(__file__).parent / "routes"
sys.path.insert(0, str(routes_dir.parent))

for route_file in sorted(routes_dir.glob("auto_*.py")):
    module_name = route_file.stem
    try:
        spec = importlib.util.spec_from_file_location(
            f"socialmedia_hub.server.routes.{module_name}",
            route_file,
        )
        if spec and spec.loader:
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            if hasattr(module, "router"):
                app.include_router(module.router)
                logger.info(f"Registered router from {module_name}")
    except Exception as e:
        logger.warning(f"Failed to load {module_name}: {e}")

# Register hand-written routers
app.include_router(live_room_router)
app.include_router(netease_router)
app.include_router(websocket_router)


# ---------------------------------------------------------------------------
# Routes: Health
# ---------------------------------------------------------------------------


@app.get("/api/v1/health/check")
async def health_check() -> dict[str, Any]:
    """Health check endpoint."""
    return {"status": "ok", "version": "0.1.0", "timestamp": datetime.now(timezone.utc).isoformat()}


@app.get("/api/v1/health/platforms")
async def list_platforms() -> dict[str, Any]:
    """List supported platforms."""
    return {
        "platforms": list(PLATFORM_CONFIGS.keys()),
        "count": len(PLATFORM_CONFIGS),
    }


@app.get("/api/v1/health/stats")
async def health_stats() -> dict[str, Any]:
    """Get API statistics."""
    return {
        "total_endpoints": 1043,
        "platforms": len(PLATFORM_CONFIGS),
        "active_keys": len(API_KEYS),
        "version": "0.1.0",
        "mcp_tools": 36,
    }


# ---------------------------------------------------------------------------
# Routes: API Monitoring
# ---------------------------------------------------------------------------


@app.get("/api/v1/monitor/status")
async def monitor_status() -> dict[str, Any]:
    """Get API server status."""
    return {
        "status": "operational",
        "version": "0.1.0",
        "uptime": "running",
        "platforms_supported": len(PLATFORM_CONFIGS),
        "endpoints_total": 1043,
        "mcp_enabled": True,
        "swagger_enabled": True,
    }


@app.get("/api/v1/monitor/metrics")
async def monitor_metrics() -> dict[str, Any]:
    """Get API metrics."""
    return {
        "requests_total": 0,
        "requests_per_minute": 0,
        "error_rate": 0.0,
        "avg_response_time_ms": 0,
        "active_connections": 0,
        "rate_limit_hits": 0,
    }


@app.get("/api/v1/monitor/platforms")
async def monitor_platforms() -> dict[str, Any]:
    """Get platform status."""
    platforms = {}
    for name, config in PLATFORM_CONFIGS.items():
        platforms[name] = {
            "name": name,
            "base_url": config["base_url"],
            "status": "available",
            "endpoints": "dynamic",
        }
    return {"platforms": platforms, "count": len(platforms)}


# ---------------------------------------------------------------------------
# Routes: API Key Management
# ---------------------------------------------------------------------------


@app.post("/api/v1/auth/create_key")
async def create_api_key(name: str = "default", tier: str = "free") -> dict[str, Any]:
    """Create a new API key."""
    key = generate_api_key(name, tier)
    return {"api_key": key, "name": name, "tier": tier}


@app.get("/api/v1/auth/verify")
async def verify_key(token: str = Depends(verify_api_key)) -> dict[str, Any]:
    """Verify an API key."""
    key_info = API_KEYS[token]
    return {"valid": True, "name": key_info["name"], "tier": key_info["tier"]}


# ---------------------------------------------------------------------------
# Routes: MCP (Model Context Protocol) - MUST be before generic proxy
# ---------------------------------------------------------------------------


@app.get("/api/v1/mcp/tools")
async def mcp_list_tools(token: str = Depends(verify_api_key)) -> dict[str, Any]:
    """List all available MCP tools."""
    from socialmedia_hub.mcp.server import create_mcp_server
    mcp = create_mcp_server(api_key=token, base_url="http://127.0.0.1:8000")
    return {"tools": mcp.list_tools(), "count": len(mcp.tools)}


@app.post("/api/v1/mcp/call")
async def mcp_call_tool(
    request: Request,
    token: str = Depends(verify_api_key),
) -> dict[str, Any]:
    """Call an MCP tool."""
    from socialmedia_hub.mcp.server import create_mcp_server
    try:
        body = await request.json()
    except Exception:
        return {"error": "Invalid JSON body"}

    tool_name = body.get("tool")
    arguments = body.get("arguments", {})

    if not tool_name:
        return {"error": "Missing 'tool' parameter"}

    mcp = create_mcp_server(api_key=token, base_url="http://127.0.0.1:8000")
    return mcp.call_tool(tool_name, arguments)


@app.get("/api/v1/mcp/config")
async def mcp_config(token: str = Depends(verify_api_key)) -> dict[str, Any]:
    """Get MCP server configuration for Claude Desktop."""
    return {
        "mcpServers": {
            "socialmedia-hub": {
                "command": "npx",
                "args": [
                    "mcp-remote",
                    "http://127.0.0.1:8000/api/v1/mcp/sse",
                    "--header",
                    f"Authorization: Bearer {token}"
                ]
            }
        }
    }


# ---------------------------------------------------------------------------
# Routes: Generic Platform Proxy - AFTER MCP routes
# ---------------------------------------------------------------------------


@app.api_route(
    "/api/v1/{platform}/{path:path}",
    methods=["GET", "POST", "PUT", "DELETE", "PATCH"],
)
async def generic_proxy(
    platform: str,
    path: str,
    request: Request,
    token: str = Depends(verify_api_key),
) -> dict[str, Any]:
    """Generic proxy for any supported platform."""
    # Exclude system routes from proxy
    excluded_platforms = {"health", "auth", "monitor", "mcp"}
    if platform in excluded_platforms:
        raise HTTPException(status_code=404, detail=f"Route not found: /api/v1/{platform}/{path}")

    params = dict(request.query_params)

    json_body = None
    if request.method in ("POST", "PUT", "PATCH"):
        try:
            json_body = await request.json()
        except Exception:
            pass

    cookies = {}
    cookie_header = request.headers.get("cookie")
    if cookie_header:
        for item in cookie_header.split(";"):
            if "=" in item:
                k, v = item.split("=", 1)
                cookies[k.strip()] = v.strip()

    return await proxy_request(
        platform=platform,
        path=path,
        method=request.method,
        params=params or None,
        json_body=json_body,
        cookies=cookies or None,
    )


# ---------------------------------------------------------------------------
# Server entry point
# ---------------------------------------------------------------------------


def run_server(host: str = "0.0.0.0", port: int = 8000):
    """Run the API server."""
    import uvicorn
    uvicorn.run(app, host=host, port=port)


if __name__ == "__main__":
    run_server()
