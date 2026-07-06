"""Auto-generated routes for Weibo-Web-API."""

from __future__ import annotations

from typing import Any

from fastapi import APIRouter, Depends, Request

from socialmedia_hub.server._core import proxy_request, verify_api_key

router = APIRouter(prefix="/api/v1/weibo/web", tags=["weibo_web"])

@router.get("/fetch_config_list")
async def fetch_config_list(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取频道配置列表/Get channel config list"""
    return await proxy_request("weibo", "/api/v1/weibo/web/fetch_config_list")

@router.get("/fetch_trend_top")
async def fetch_trend_top(
    containerid: str,
    request: Request,
    page: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取频道热门趋势/Get channel trend top"""
    params: dict[str, Any] = {}
    if containerid is not None:
        params["containerid"] = containerid
    if page is not None:
        params["page"] = page
    return await proxy_request("weibo", "/api/v1/weibo/web/fetch_trend_top", params=params)

@router.get("/fetch_channel_feed")
async def fetch_channel_feed(
    request: Request,
    channel_name: str | None = None,
    page: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """根据频道名称获取热门内容/Get channel feed by name"""
    params: dict[str, Any] = {}
    if channel_name is not None:
        params["channel_name"] = channel_name
    if page is not None:
        params["page"] = page
    return await proxy_request("weibo", "/api/v1/weibo/web/fetch_channel_feed", params=params)

@router.get("/fetch_user_info")
async def fetch_user_info(
    uid: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户信息/Get user information"""
    params: dict[str, Any] = {}
    if uid is not None:
        params["uid"] = uid
    return await proxy_request("weibo", "/api/v1/weibo/web/fetch_user_info", params=params)

@router.get("/fetch_user_posts")
async def fetch_user_posts(
    uid: str,
    request: Request,
    page: int | None = None,
    since_id: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户微博列表/Get user posts"""
    params: dict[str, Any] = {}
    if uid is not None:
        params["uid"] = uid
    if page is not None:
        params["page"] = page
    if since_id is not None:
        params["since_id"] = since_id
    return await proxy_request("weibo", "/api/v1/weibo/web/fetch_user_posts", params=params)

@router.get("/fetch_post_detail")
async def fetch_post_detail(
    post_id: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取微博详情/Get post detail"""
    params: dict[str, Any] = {}
    if post_id is not None:
        params["post_id"] = post_id
    return await proxy_request("weibo", "/api/v1/weibo/web/fetch_post_detail", params=params)

@router.get("/fetch_post_comments")
async def fetch_post_comments(
    post_id: str,
    mid: str,
    request: Request,
    max_id: str | None = None,
    max_id_type: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取微博评论/Get post comments"""
    params: dict[str, Any] = {}
    if post_id is not None:
        params["post_id"] = post_id
    if mid is not None:
        params["mid"] = mid
    if max_id is not None:
        params["max_id"] = max_id
    if max_id_type is not None:
        params["max_id_type"] = max_id_type
    return await proxy_request("weibo", "/api/v1/weibo/web/fetch_post_comments", params=params)

@router.get("/fetch_comment_replies")
async def fetch_comment_replies(
    cid: str,
    request: Request,
    max_id: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取评论子评论/Get comment replies"""
    params: dict[str, Any] = {}
    if cid is not None:
        params["cid"] = cid
    if max_id is not None:
        params["max_id"] = max_id
    return await proxy_request("weibo", "/api/v1/weibo/web/fetch_comment_replies", params=params)

@router.get("/fetch_search")
async def fetch_search(
    keyword: str,
    request: Request,
    page: int | None = None,
    search_type: str | None = None,
    time_scope: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """搜索微博/Search Weibo"""
    params: dict[str, Any] = {}
    if keyword is not None:
        params["keyword"] = keyword
    if page is not None:
        params["page"] = page
    if search_type is not None:
        params["search_type"] = search_type
    if time_scope is not None:
        params["time_scope"] = time_scope
    return await proxy_request("weibo", "/api/v1/weibo/web/fetch_search", params=params)

@router.get("/fetch_hot_search")
async def fetch_hot_search(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取热搜榜/Get hot search ranking"""
    return await proxy_request("weibo", "/api/v1/weibo/web/fetch_hot_search")

@router.get("/fetch_search_topics")
async def fetch_search_topics(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取搜索页热搜词/Get search page hot topics"""
    return await proxy_request("weibo", "/api/v1/weibo/web/fetch_search_topics")
