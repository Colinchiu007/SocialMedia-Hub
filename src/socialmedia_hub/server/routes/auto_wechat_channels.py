"""Auto-generated routes for WeChat-Channels-API."""

from __future__ import annotations

from typing import Any

from fastapi import APIRouter, Depends, Request

from socialmedia_hub.server._core import proxy_request, verify_api_key

router = APIRouter(prefix="/api/v1/wechat/channels", tags=["wechat_channels"])

@router.post("/fetch_default_search")
async def fetch_default_search(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """微信视频号默认搜索/WeChat Channels Default Search"""
    body = await request.json()
    return await proxy_request("wechat", "/api/v1/wechat_channels/fetch_default_search", json_body=body)

@router.get("/fetch_search_latest")
async def fetch_search_latest(
    keywords: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """微信视频号搜索最新视频/WeChat Channels Search Latest Videos"""
    params: dict[str, Any] = {}
    if keywords is not None:
        params["keywords"] = keywords
    return await proxy_request("wechat", "/api/v1/wechat_channels/fetch_search_latest", params=params)

@router.get("/fetch_search_ordinary")
async def fetch_search_ordinary(
    keywords: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """微信视频号综合搜索/WeChat Channels Comprehensive Search"""
    params: dict[str, Any] = {}
    if keywords is not None:
        params["keywords"] = keywords
    return await proxy_request("wechat", "/api/v1/wechat_channels/fetch_search_ordinary", params=params)

@router.get("/fetch_user_search")
async def fetch_user_search(
    keywords: str,
    request: Request,
    page: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """微信视频号用户搜索/WeChat Channels User Search"""
    params: dict[str, Any] = {}
    if keywords is not None:
        params["keywords"] = keywords
    if page is not None:
        params["page"] = page
    return await proxy_request("wechat", "/api/v1/wechat_channels/fetch_user_search", params=params)

@router.get("/fetch_user_search_v2")
async def fetch_user_search_v2(
    request: Request,
    keywords: str | None = None,
    page: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """微信视频号用户搜索V2/WeChat Channels User Search V2"""
    params: dict[str, Any] = {}
    if keywords is not None:
        params["keywords"] = keywords
    if page is not None:
        params["page"] = page
    return await proxy_request("wechat", "/api/v1/wechat_channels/fetch_user_search_v2", params=params)

@router.get("/fetch_video_detail")
async def fetch_video_detail(
    request: Request,
    id: str | None = None,
    exportId: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """微信视频号视频详情/WeChat Channels Video Detail"""
    params: dict[str, Any] = {}
    if id is not None:
        params["id"] = id
    if exportId is not None:
        params["exportId"] = exportId
    return await proxy_request("wechat", "/api/v1/wechat_channels/fetch_video_detail", params=params)

@router.post("/fetch_home_page")
async def fetch_home_page(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """微信视频号主页/WeChat Channels Home Page"""
    body = await request.json()
    return await proxy_request("wechat", "/api/v1/wechat_channels/fetch_home_page", json_body=body)

@router.post("/fetch_comments")
async def fetch_comments(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """微信视频号评论/WeChat Channels Comments"""
    body = await request.json()
    return await proxy_request("wechat", "/api/v1/wechat_channels/fetch_comments", json_body=body)

@router.get("/fetch_live_history")
async def fetch_live_history(
    username: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """微信视频号直播回放/WeChat Channels Live History"""
    params: dict[str, Any] = {}
    if username is not None:
        params["username"] = username
    return await proxy_request("wechat", "/api/v1/wechat_channels/fetch_live_history", params=params)

@router.get("/fetch_hot_words")
async def fetch_hot_words(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """微信视频号热门话题/WeChat Channels Hot Topics"""
    return await proxy_request("wechat", "/api/v1/wechat_channels/fetch_hot_words")
