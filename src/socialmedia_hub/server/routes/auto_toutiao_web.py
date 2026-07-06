"""Auto-generated routes for Toutiao-Web-API."""

from __future__ import annotations

from typing import Any

from fastapi import APIRouter, Depends, Request

from socialmedia_hub.server._core import proxy_request, verify_api_key

router = APIRouter(prefix="/api/v1/toutiao/web", tags=["toutiao_web"])

@router.get("/get_article_info")
async def get_article_info(
    aweme_id: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取指定文章的信息/Get information of specified article"""
    body = await request.json()
    params: dict[str, Any] = {}
    if aweme_id is not None:
        params["aweme_id"] = aweme_id
    return await proxy_request("toutiao", "/api/v1/toutiao/web/get_article_info", params=params, json_body=body)

@router.get("/get_video_info")
async def get_video_info(
    aweme_id: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取指定视频的信息/Get information of specified video"""
    body = await request.json()
    params: dict[str, Any] = {}
    if aweme_id is not None:
        params["aweme_id"] = aweme_id
    return await proxy_request("toutiao", "/api/v1/toutiao/web/get_video_info", params=params, json_body=body)
