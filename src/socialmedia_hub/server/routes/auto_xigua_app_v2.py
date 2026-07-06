"""Auto-generated routes for Xigua-App-V2-API."""

from __future__ import annotations

from typing import Any

from fastapi import APIRouter, Depends, Request

from socialmedia_hub.server._core import proxy_request, verify_api_key

router = APIRouter(prefix="/api/v1/xigua/app/v2", tags=["xigua_app_v2"])

@router.get("/fetch_one_video")
async def fetch_one_video(
    item_id: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取单个作品数据/Get single video data"""
    body = await request.json()
    params: dict[str, Any] = {}
    if item_id is not None:
        params["item_id"] = item_id
    return await proxy_request("xigua", "/api/v1/xigua/app/v2/fetch_one_video", params=params, json_body=body)

@router.get("/fetch_one_video_v2")
async def fetch_one_video_v2(
    item_id: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取单个作品数据 V2/Get single video data V2"""
    body = await request.json()
    params: dict[str, Any] = {}
    if item_id is not None:
        params["item_id"] = item_id
    return await proxy_request("xigua", "/api/v1/xigua/app/v2/fetch_one_video_v2", params=params, json_body=body)

@router.get("/fetch_one_video_play_url")
async def fetch_one_video_play_url(
    item_id: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取单个作品的播放链接/Get single video play URL"""
    body = await request.json()
    params: dict[str, Any] = {}
    if item_id is not None:
        params["item_id"] = item_id
    return await proxy_request("xigua", "/api/v1/xigua/app/v2/fetch_one_video_play_url", params=params, json_body=body)

@router.get("/fetch_video_comment_list")
async def fetch_video_comment_list(
    item_id: str,
    request: Request,
    offset: int | None = None,
    count: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """视频评论列表/Video comment list"""
    body = await request.json()
    params: dict[str, Any] = {}
    if item_id is not None:
        params["item_id"] = item_id
    if offset is not None:
        params["offset"] = offset
    if count is not None:
        params["count"] = count
    return await proxy_request("xigua", "/api/v1/xigua/app/v2/fetch_video_comment_list", params=params, json_body=body)

@router.get("/search_video")
async def search_video(
    keyword: str,
    request: Request,
    offset: int | None = None,
    order_type: str | None = None,
    min_duration: int | None = None,
    max_duration: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """搜索视频/Search video"""
    body = await request.json()
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
    return await proxy_request("xigua", "/api/v1/xigua/app/v2/search_video", params=params, json_body=body)

@router.get("/fetch_user_info")
async def fetch_user_info(
    user_id: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """个人信息/Personal information"""
    body = await request.json()
    params: dict[str, Any] = {}
    if user_id is not None:
        params["user_id"] = user_id
    return await proxy_request("xigua", "/api/v1/xigua/app/v2/fetch_user_info", params=params, json_body=body)

@router.get("/fetch_user_post_list")
async def fetch_user_post_list(
    user_id: str,
    request: Request,
    max_behot_time: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取个人作品列表/Get user post list"""
    body = await request.json()
    params: dict[str, Any] = {}
    if user_id is not None:
        params["user_id"] = user_id
    if max_behot_time is not None:
        params["max_behot_time"] = max_behot_time
    return await proxy_request("xigua", "/api/v1/xigua/app/v2/fetch_user_post_list", params=params, json_body=body)
