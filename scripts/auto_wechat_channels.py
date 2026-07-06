"""Auto-generated routes for WeChat-Channels-API."""

from __future__ import annotations

from typing import Any

from fastapi import APIRouter, Depends, Request

from socialmedia_hub.server._core import proxy_request, verify_api_key

router = APIRouter(prefix="/api/v1/wechat/channels", tags=["wechat_channels"])

@router.post("/fetch_default_search")
async def fetch_default_search(
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """微信视频号默认搜索/WeChat Channels Default Search"""
        body = await request.json()
        return await proxy_request("wechat", "/api/v1/wechat_channels/fetch_default_search", json_body=body)

@router.get("/fetch_search_latest")
async def fetch_search_latest(
    keywords: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """微信视频号搜索最新视频/WeChat Channels Search Latest Videos"""
        params: dict[str, Any] = {}
        if keywords is not None:
            params["keywords"] = keywords
        body = await request.json()
        return await proxy_request("wechat", "/api/v1/wechat_channels/fetch_search_latest", json_body=body)

@router.get("/fetch_search_ordinary")
async def fetch_search_ordinary(
    keywords: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """微信视频号综合搜索/WeChat Channels Comprehensive Search"""
        params: dict[str, Any] = {}
        if keywords is not None:
            params["keywords"] = keywords
        body = await request.json()
        return await proxy_request("wechat", "/api/v1/wechat_channels/fetch_search_ordinary", json_body=body)

@router.get("/fetch_user_search")
async def fetch_user_search(
    page: int | None = None,
    keywords: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """微信视频号用户搜索/WeChat Channels User Search"""
        params: dict[str, Any] = {}
        if keywords is not None:
            params["keywords"] = keywords
        if page is not None:
            params["page"] = page
        body = await request.json()
        return await proxy_request("wechat", "/api/v1/wechat_channels/fetch_user_search", json_body=body)

@router.get("/fetch_user_search_v2")
async def fetch_user_search_v2(
    page: int | None = None,
    keywords: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """微信视频号用户搜索V2/WeChat Channels User Search V2"""
        params: dict[str, Any] = {}
        if keywords is not None:
            params["keywords"] = keywords
        if page is not None:
            params["page"] = page
        body = await request.json()
        return await proxy_request("wechat", "/api/v1/wechat_channels/fetch_user_search_v2", json_body=body)

@router.get("/fetch_video_detail")
async def fetch_video_detail(
    exportId: str | None = None,
    id: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """微信视频号视频详情/WeChat Channels Video Detail"""
        params: dict[str, Any] = {}
        if id is not None:
            params["id"] = id
        if exportId is not None:
            params["exportId"] = exportId
        body = await request.json()
        return await proxy_request("wechat", "/api/v1/wechat_channels/fetch_video_detail", json_body=body)

@router.post("/fetch_home_page")
async def fetch_home_page(
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """微信视频号主页/WeChat Channels Home Page"""
        body = await request.json()
        return await proxy_request("wechat", "/api/v1/wechat_channels/fetch_home_page", json_body=body)

@router.post("/fetch_comments")
async def fetch_comments(
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """微信视频号评论/WeChat Channels Comments"""
        body = await request.json()
        return await proxy_request("wechat", "/api/v1/wechat_channels/fetch_comments", json_body=body)

@router.get("/fetch_live_history")
async def fetch_live_history(
    username: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """微信视频号直播回放/WeChat Channels Live History"""
        params: dict[str, Any] = {}
        if username is not None:
            params["username"] = username
        body = await request.json()
        return await proxy_request("wechat", "/api/v1/wechat_channels/fetch_live_history", json_body=body)

@router.get("/fetch_hot_words")
async def fetch_hot_words(
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """微信视频号热门话题/WeChat Channels Hot Topics"""
        body = await request.json()
        return await proxy_request("wechat", "/api/v1/wechat_channels/fetch_hot_words", json_body=body)
