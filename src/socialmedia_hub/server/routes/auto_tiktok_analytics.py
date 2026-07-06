"""Auto-generated routes for TikTok-Analytics-API."""

from __future__ import annotations

from typing import Any

from fastapi import APIRouter, Depends, Request

from socialmedia_hub.server._core import proxy_request, verify_api_key

router = APIRouter(prefix="/api/v1/tiktok/analytics", tags=["tiktok_analytics"])

@router.get("/fetch_video_metrics")
async def fetch_video_metrics(
    item_id: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取作品的统计数据/Get video metrics"""
    body = await request.json()
    params: dict[str, Any] = {}
    if item_id is not None:
        params["item_id"] = item_id
    return await proxy_request("tiktok", "/api/v1/tiktok/analytics/fetch_video_metrics", params=params, json_body=body)

@router.get("/detect_fake_views")
async def detect_fake_views(
    item_id: str,
    request: Request,
    content_category: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """检测视频虚假流量分析/Detect fake views in video"""
    body = await request.json()
    params: dict[str, Any] = {}
    if item_id is not None:
        params["item_id"] = item_id
    if content_category is not None:
        params["content_category"] = content_category
    return await proxy_request("tiktok", "/api/v1/tiktok/analytics/detect_fake_views", params=params, json_body=body)

@router.get("/fetch_comment_keywords")
async def fetch_comment_keywords(
    item_id: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取视频评论关键词分析/Get comment keywords analysis"""
    body = await request.json()
    params: dict[str, Any] = {}
    if item_id is not None:
        params["item_id"] = item_id
    return await proxy_request("tiktok", "/api/v1/tiktok/analytics/fetch_comment_keywords", params=params, json_body=body)

@router.get("/fetch_creator_info_and_milestones")
async def fetch_creator_info_and_milestones(
    user_id: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取创作者信息和里程碑数据/Get creator info and milestones"""
    body = await request.json()
    params: dict[str, Any] = {}
    if user_id is not None:
        params["user_id"] = user_id
    return await proxy_request("tiktok", "/api/v1/tiktok/analytics/fetch_creator_info_and_milestones", params=params, json_body=body)
