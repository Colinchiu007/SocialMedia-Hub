"""Auto-generated routes for Hybrid-Parsing."""

from __future__ import annotations

from typing import Any

from fastapi import APIRouter, Depends, Request

from socialmedia_hub.server._core import proxy_request, verify_api_key

router = APIRouter(prefix="/api/v1/hybrid", tags=["hybrid_parsing"])

@router.get("/video_data")
async def video_data(
    url: str,
    request: Request,
    minimal: bool | None = None,
    base64_url: bool | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """混合解析单一视频接口/Hybrid parsing single video endpoint"""
    body = await request.json()
    params: dict[str, Any] = {}
    if url is not None:
        params["url"] = url
    if minimal is not None:
        params["minimal"] = minimal
    if base64_url is not None:
        params["base64_url"] = base64_url
    return await proxy_request("hybrid", "/api/v1/hybrid/video_data", params=params, json_body=body)

@router.get("/video_data")
async def video_data(
    url: str,
    request: Request,
    minimal: bool | None = None,
    base64_url: bool | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """混合解析单一视频接口/Hybrid parsing single video endpoint"""
    body = await request.json()
    params: dict[str, Any] = {}
    if url is not None:
        params["url"] = url
    if minimal is not None:
        params["minimal"] = minimal
    if base64_url is not None:
        params["base64_url"] = base64_url
    return await proxy_request("hybrid", "/api/v1/hybrid/video_data", params=params, json_body=body)
