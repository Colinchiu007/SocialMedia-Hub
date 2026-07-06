"""Auto-generated routes for TikHub-Downloader-API."""

from __future__ import annotations

from typing import Any

from fastapi import APIRouter, Depends, Request

from socialmedia_hub.server._core import proxy_request, verify_api_key

router = APIRouter(prefix="/api/v1/tikhub/downloader", tags=["tikhub_downloader"])

@router.get("/version")
async def version(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """检查TikHub下载器的版本更新 / Check for TikHub Downloader version updates"""
    body = await request.json()
    return await proxy_request("tikhub", "/api/v1/tikhub/downloader/version", json_body=body)

@router.get("/redirect_download")
async def redirect_download(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """重定向到最新版本的下载链接 / Redirect to the latest version download link"""
    body = await request.json()
    return await proxy_request("tikhub", "/api/v1/tikhub/downloader/redirect_download", json_body=body)
