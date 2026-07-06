"""Auto-generated routes for TikTok-Analytics-API."""

from __future__ import annotations

from typing import Any

from fastapi import APIRouter, Depends, Request

from socialmedia_hub.server._core import proxy_request, verify_api_key

router = APIRouter(prefix="/api/v1/tiktok/analytics", tags=["tiktok_analytics"])

@router.get("/fetch_video_metrics")
async def fetch_video_metrics(
    item_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取作品的统计数据/Get video metrics"""
        params: dict[str, Any] = {}
        if item_id is not None:
            params["item_id"] = item_id
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/analytics/fetch_video_metrics", json_body=body)

@router.get("/detect_fake_views")
async def detect_fake_views(
    content_category: str | None = None,
    item_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """检测视频虚假流量分析/Detect fake views in video"""
        params: dict[str, Any] = {}
        if item_id is not None:
            params["item_id"] = item_id
        if content_category is not None:
            params["content_category"] = content_category
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/analytics/detect_fake_views", json_body=body)

@router.get("/fetch_comment_keywords")
async def fetch_comment_keywords(
    item_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取视频评论关键词分析/Get comment keywords analysis"""
        params: dict[str, Any] = {}
        if item_id is not None:
            params["item_id"] = item_id
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/analytics/fetch_comment_keywords", json_body=body)

@router.get("/fetch_creator_info_and_milestones")
async def fetch_creator_info_and_milestones(
    user_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取创作者信息和里程碑数据/Get creator info and milestones"""
        params: dict[str, Any] = {}
        if user_id is not None:
            params["user_id"] = user_id
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/analytics/fetch_creator_info_and_milestones", json_body=body)
