"""Auto-generated routes for Demo-API."""

from __future__ import annotations

from typing import Any

from fastapi import APIRouter, Depends, Request

from socialmedia_hub.server._core import proxy_request, verify_api_key

router = APIRouter(prefix="/api/v1/demo", tags=["demo"])

@router.get("/cache_status")
async def cache_status(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """查看Demo缓存状态/View Demo Cache Status"""
    body = await request.json()
    return await proxy_request("demo", "/api/v1/demo/demo/cache_status", json_body=body)

@router.get("/fetch_one_video")
async def fetch_one_video(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """【Demo】抖音Web获取固定作品数据（1小时缓存）/[Demo] Fetch Douyin Web Fixed Video Data with Cache"""
    body = await request.json()
    return await proxy_request("demo", "/api/v1/demo/douyin/web/fetch_one_video", json_body=body)

@router.get("/fetch_one_video")
async def fetch_one_video(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """【Demo】抖音APP获取固定作品数据（1小时缓存）/[Demo] Fetch Douyin APP Fixed Video Data with Cache"""
    body = await request.json()
    return await proxy_request("demo", "/api/v1/demo/douyin/app/fetch_one_video", json_body=body)

@router.get("/general_search")
async def general_search(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """【Demo】抖音搜索综合搜索（1小时缓存）/[Demo] Douyin General Search with Cache"""
    body = await request.json()
    return await proxy_request("demo", "/api/v1/demo/douyin_search/app/general_search", json_body=body)

@router.get("/fetch_one_video")
async def fetch_one_video(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """【Demo】快手获取固定视频信息（1小时缓存）/[Demo] Kuaishou Fixed Video with Cache"""
    body = await request.json()
    return await proxy_request("demo", "/api/v1/demo/kuaishou/web/fetch_one_video", json_body=body)

@router.get("/fetch_user_profile")
async def fetch_user_profile(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """【Demo】TikTok固定用户信息（1小时缓存）/[Demo] TikTok Fixed User Profile with Cache"""
    body = await request.json()
    return await proxy_request("demo", "/api/v1/demo/tiktok/web/fetch_user_profile", json_body=body)

@router.get("/fetch_one_video")
async def fetch_one_video(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """【Demo】TikTok APP获取固定视频详情（1小时缓存）/[Demo] TikTok APP Fixed Video Detail with Cache"""
    body = await request.json()
    return await proxy_request("demo", "/api/v1/demo/tiktok/app/fetch_one_video", json_body=body)

@router.get("/fetch_user_info")
async def fetch_user_info(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """【Demo】Instagram获取固定用户信息（1小时缓存）/[Demo] Instagram Fixed User Profile with Cache"""
    body = await request.json()
    return await proxy_request("demo", "/api/v1/demo/instagram/web/fetch_user_info", json_body=body)

@router.get("/article_extract")
async def article_extract(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """【Demo】微信公众号文章提取（1小时缓存）/[Demo] WeChat Article Extract with Cache"""
    body = await request.json()
    return await proxy_request("demo", "/api/v1/demo/wechat/article_extract", json_body=body)
