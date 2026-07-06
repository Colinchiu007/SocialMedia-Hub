"""Auto-generated routes for Bilibili-App-API."""

from __future__ import annotations

from typing import Any

from fastapi import APIRouter, Depends, Request

from socialmedia_hub.server._core import proxy_request, verify_api_key

router = APIRouter(prefix="/api/v1/bilibili/app", tags=["bilibili_app"])

@router.get("/fetch_one_video")
async def fetch_one_video(
    request: Request,
    av_id: str | None = None,
    bv_id: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取单个视频详情信息/Get single video data"""
    body = await request.json()
    params: dict[str, Any] = {}
    if av_id is not None:
        params["av_id"] = av_id
    if bv_id is not None:
        params["bv_id"] = bv_id
    return await proxy_request("bilibili", "/api/v1/bilibili/app/fetch_one_video", params=params, json_body=body)

@router.get("/fetch_video_comments")
async def fetch_video_comments(
    request: Request,
    av_id: str | None = None,
    bv_id: str | None = None,
    mode: int | None = None,
    next_offset: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取视频评论列表/Get video comments"""
    body = await request.json()
    params: dict[str, Any] = {}
    if av_id is not None:
        params["av_id"] = av_id
    if bv_id is not None:
        params["bv_id"] = bv_id
    if mode is not None:
        params["mode"] = mode
    if next_offset is not None:
        params["next_offset"] = next_offset
    return await proxy_request("bilibili", "/api/v1/bilibili/app/fetch_video_comments", params=params, json_body=body)

@router.get("/fetch_reply_detail")
async def fetch_reply_detail(
    root: str,
    request: Request,
    av_id: str | None = None,
    bv_id: str | None = None,
    next_offset: int | None = None,
    ps: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取二级评论回复/Get reply detail"""
    body = await request.json()
    params: dict[str, Any] = {}
    if root is not None:
        params["root"] = root
    if av_id is not None:
        params["av_id"] = av_id
    if bv_id is not None:
        params["bv_id"] = bv_id
    if next_offset is not None:
        params["next_offset"] = next_offset
    if ps is not None:
        params["ps"] = ps
    return await proxy_request("bilibili", "/api/v1/bilibili/app/fetch_reply_detail", params=params, json_body=body)

@router.get("/fetch_user_videos")
async def fetch_user_videos(
    user_id: str,
    request: Request,
    post_filter: str | None = None,
    page: int | None = None,
    ps: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户投稿视频/Get user videos"""
    body = await request.json()
    params: dict[str, Any] = {}
    if user_id is not None:
        params["user_id"] = user_id
    if post_filter is not None:
        params["post_filter"] = post_filter
    if page is not None:
        params["page"] = page
    if ps is not None:
        params["ps"] = ps
    return await proxy_request("bilibili", "/api/v1/bilibili/app/fetch_user_videos", params=params, json_body=body)

@router.get("/fetch_user_info")
async def fetch_user_info(
    user_id: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户信息/Get user info"""
    body = await request.json()
    params: dict[str, Any] = {}
    if user_id is not None:
        params["user_id"] = user_id
    return await proxy_request("bilibili", "/api/v1/bilibili/app/fetch_user_info", params=params, json_body=body)

@router.get("/fetch_home_feed")
async def fetch_home_feed(
    request: Request,
    idx: int | None = None,
    flush: int | None = None,
    pull: bool | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取主页推荐视频流/Get home feed"""
    body = await request.json()
    params: dict[str, Any] = {}
    if idx is not None:
        params["idx"] = idx
    if flush is not None:
        params["flush"] = flush
    if pull is not None:
        params["pull"] = pull
    return await proxy_request("bilibili", "/api/v1/bilibili/app/fetch_home_feed", params=params, json_body=body)

@router.get("/fetch_popular_feed")
async def fetch_popular_feed(
    request: Request,
    idx: int | None = None,
    last_param: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取热门推荐/Get popular feed"""
    body = await request.json()
    params: dict[str, Any] = {}
    if idx is not None:
        params["idx"] = idx
    if last_param is not None:
        params["last_param"] = last_param
    return await proxy_request("bilibili", "/api/v1/bilibili/app/fetch_popular_feed", params=params, json_body=body)

@router.get("/fetch_search_all")
async def fetch_search_all(
    keyword: str,
    request: Request,
    page: int | None = None,
    page_size: int | None = None,
    order: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """综合搜索/search all"""
    body = await request.json()
    params: dict[str, Any] = {}
    if keyword is not None:
        params["keyword"] = keyword
    if page is not None:
        params["page"] = page
    if page_size is not None:
        params["page_size"] = page_size
    if order is not None:
        params["order"] = order
    return await proxy_request("bilibili", "/api/v1/bilibili/app/fetch_search_all", params=params, json_body=body)

@router.get("/fetch_search_by_type")
async def fetch_search_by_type(
    keyword: str,
    request: Request,
    search_type: str | None = None,
    page: int | None = None,
    page_size: int | None = None,
    order: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """分类搜索/ search by type"""
    body = await request.json()
    params: dict[str, Any] = {}
    if keyword is not None:
        params["keyword"] = keyword
    if search_type is not None:
        params["search_type"] = search_type
    if page is not None:
        params["page"] = page
    if page_size is not None:
        params["page_size"] = page_size
    if order is not None:
        params["order"] = order
    return await proxy_request("bilibili", "/api/v1/bilibili/app/fetch_search_by_type", params=params, json_body=body)

@router.get("/fetch_cinema_tab")
async def fetch_cinema_tab(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取影视推荐/Get cinema tab"""
    body = await request.json()
    return await proxy_request("bilibili", "/api/v1/bilibili/app/fetch_cinema_tab", json_body=body)

@router.get("/fetch_bangumi_tab")
async def fetch_bangumi_tab(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取番剧推荐/Get bangumi tab"""
    body = await request.json()
    return await proxy_request("bilibili", "/api/v1/bilibili/app/fetch_bangumi_tab", json_body=body)
