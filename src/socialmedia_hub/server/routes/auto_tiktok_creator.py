"""Auto-generated routes for TikTok-Creator-API."""

from __future__ import annotations

from typing import Any

from fastapi import APIRouter, Depends, Request

from socialmedia_hub.server._core import proxy_request, verify_api_key

router = APIRouter(prefix="/api/v1/tiktok/creator", tags=["tiktok_creator"])

@router.post("/get_account_health_status")
async def get_account_health_status(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取创作者账号健康状态/Get Creator Account Health Status"""
    body = await request.json()
    return await proxy_request("tiktok", "/api/v1/tiktok/creator/get_account_health_status", json_body=body)

@router.post("/get_account_violation_list")
async def get_account_violation_list(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取创作者账号违规记录列表/Get Creator Account Violation Record List"""
    body = await request.json()
    return await proxy_request("tiktok", "/api/v1/tiktok/creator/get_account_violation_list", json_body=body)

@router.post("/get_account_insights_overview")
async def get_account_insights_overview(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取创作者账号概览/Get Creator Account Overview"""
    body = await request.json()
    return await proxy_request("tiktok", "/api/v1/tiktok/creator/get_account_insights_overview", json_body=body)

@router.post("/get_live_analytics_summary")
async def get_live_analytics_summary(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取创作者直播概览/Get Creator Live Overview"""
    body = await request.json()
    return await proxy_request("tiktok", "/api/v1/tiktok/creator/get_live_analytics_summary", json_body=body)

@router.post("/get_video_analytics_summary")
async def get_video_analytics_summary(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取创作者视频概览/Get Creator Video Overview"""
    body = await request.json()
    return await proxy_request("tiktok", "/api/v1/tiktok/creator/get_video_analytics_summary", json_body=body)

@router.post("/get_video_list_analytics")
async def get_video_list_analytics(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取创作者视频列表分析/Get Creator Video List Analytics"""
    body = await request.json()
    return await proxy_request("tiktok", "/api/v1/tiktok/creator/get_video_list_analytics", json_body=body)

@router.post("/get_product_analytics_list")
async def get_product_analytics_list(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取创作者商品列表分析/Get Creator Product List Analytics"""
    body = await request.json()
    return await proxy_request("tiktok", "/api/v1/tiktok/creator/get_product_analytics_list", json_body=body)

@router.post("/get_creator_account_info")
async def get_creator_account_info(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取创作者账号信息/Get Creator Account Info"""
    body = await request.json()
    return await proxy_request("tiktok", "/api/v1/tiktok/creator/get_creator_account_info", json_body=body)

@router.post("/get_showcase_product_list")
async def get_showcase_product_list(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取橱窗商品列表/Get Showcase Product List"""
    body = await request.json()
    return await proxy_request("tiktok", "/api/v1/tiktok/creator/get_showcase_product_list", json_body=body)

@router.post("/get_video_associated_product_list")
async def get_video_associated_product_list(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取视频关联商品列表/Get Video Associated Product List"""
    body = await request.json()
    return await proxy_request("tiktok", "/api/v1/tiktok/creator/get_video_associated_product_list", json_body=body)

@router.post("/get_video_detailed_stats")
async def get_video_detailed_stats(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取视频详细分段统计数据/Get Video Detailed Statistics"""
    body = await request.json()
    return await proxy_request("tiktok", "/api/v1/tiktok/creator/get_video_detailed_stats", json_body=body)

@router.post("/get_video_to_product_stats")
async def get_video_to_product_stats(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取视频与商品关联统计数据/Get Video-Product Association Statistics"""
    body = await request.json()
    return await proxy_request("tiktok", "/api/v1/tiktok/creator/get_video_to_product_stats", json_body=body)

@router.post("/get_product_related_videos")
async def get_product_related_videos(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取同款商品关联视频/Get Product Related Videos"""
    body = await request.json()
    return await proxy_request("tiktok", "/api/v1/tiktok/creator/get_product_related_videos", json_body=body)

@router.post("/get_video_audience_stats")
async def get_video_audience_stats(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取视频受众分析数据/Get Video Audience Analysis Data"""
    body = await request.json()
    return await proxy_request("tiktok", "/api/v1/tiktok/creator/get_video_audience_stats", json_body=body)
