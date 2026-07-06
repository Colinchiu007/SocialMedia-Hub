"""Auto-generated routes for iOS-Shortcut."""

from __future__ import annotations

from typing import Any

from fastapi import APIRouter, Depends, Request

from socialmedia_hub.server._core import proxy_request, verify_api_key

router = APIRouter(prefix="/api/v1/ios_shortcut", tags=["ios_shortcut"])

@router.get("/shortcut")
async def shortcut(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """用于iOS快捷指令的版本更新信息/Version update information for iOS shortcuts"""
    return await proxy_request("ios_shortcut", "/api/v1/ios_shortcut/shortcut")
