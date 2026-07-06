"""Auto-generated routes for Xigua-App-V2-API."""

from __future__ import annotations

from typing import Any

from fastapi import APIRouter, Depends, Request

from socialmedia_hub.server._core import proxy_request, verify_api_key

router = APIRouter(prefix="/api/v1/xigua/app/v2", tags=["xigua_app_v2"])

@router.get("/fetch_one_video")
async def fetch_one_video(
    item_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取单个作品数据/Get single video data"""
        params: dict[str, Any] = {}
        if item_id is not None:
            params["item_id"] = item_id
        body = await request.json()
        return await proxy_request("xigua", "/api/v1/xigua/app/v2/fetch_one_video", json_body=body)

@router.get("/fetch_one_video_v2")
async def fetch_one_video_v2(
    item_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取单个作品数据 V2/Get single video data V2"""
        params: dict[str, Any] = {}
        if item_id is not None:
            params["item_id"] = item_id
        body = await request.json()
        return await proxy_request("xigua", "/api/v1/xigua/app/v2/fetch_one_video_v2", json_body=body)

@router.get("/fetch_one_video_play_url")
async def fetch_one_video_play_url(
    item_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取单个作品的播放链接/Get single video play URL"""
        params: dict[str, Any] = {}
        if item_id is not None:
            params["item_id"] = item_id
        body = await request.json()
        return await proxy_request("xigua", "/api/v1/xigua/app/v2/fetch_one_video_play_url", json_body=body)

@router.get("/fetch_video_comment_list")
async def fetch_video_comment_list(
    count: int | None = None,
    offset: int | None = None,
    item_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """视频评论列表/Video comment list"""
        params: dict[str, Any] = {}
        if item_id is not None:
            params["item_id"] = item_id
        if offset is not None:
            params["offset"] = offset
        if count is not None:
            params["count"] = count
        body = await request.json()
        return await proxy_request("xigua", "/api/v1/xigua/app/v2/fetch_video_comment_list", json_body=body)

@router.get("/search_video")
async def search_video(
    max_duration: int | None = None,
    min_duration: int | None = None,
    order_type: str | None = None,
    offset: int | None = None,
    keyword: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """搜索视频/Search video"""
        params: dict[str, Any] = {}
        if keyword is not None:
            params["keyword"] = keyword
        if offset is not None:
            params["offset"] = offset
        if order_type is not None:
            params["order_type"] = order_type
        if min_duration is not None:
            params["min_duration"] = min_duration
        if max_duration is not None:
            params["max_duration"] = max_duration
        body = await request.json()
        return await proxy_request("xigua", "/api/v1/xigua/app/v2/search_video", json_body=body)

@router.get("/fetch_user_info")
async def fetch_user_info(
    user_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """个人信息/Personal information"""
        params: dict[str, Any] = {}
        if user_id is not None:
            params["user_id"] = user_id
        body = await request.json()
        return await proxy_request("xigua", "/api/v1/xigua/app/v2/fetch_user_info", json_body=body)

@router.get("/fetch_user_post_list")
async def fetch_user_post_list(
    max_behot_time: str | None = None,
    user_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取个人作品列表/Get user post list"""
        params: dict[str, Any] = {}
        if user_id is not None:
            params["user_id"] = user_id
        if max_behot_time is not None:
            params["max_behot_time"] = max_behot_time
        body = await request.json()
        return await proxy_request("xigua", "/api/v1/xigua/app/v2/fetch_user_post_list", json_body=body)
