"""Auto-generated routes for Weibo-Web-API."""

from __future__ import annotations

from typing import Any

from fastapi import APIRouter, Depends, Request

from socialmedia_hub.server._core import proxy_request, verify_api_key

router = APIRouter(prefix="/api/v1/weibo/web", tags=["weibo_web"])

@router.get("/fetch_config_list")
async def fetch_config_list(
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取频道配置列表/Get channel config list"""
        body = await request.json()
        return await proxy_request("weibo", "/api/v1/weibo/web/fetch_config_list", json_body=body)

@router.get("/fetch_trend_top")
async def fetch_trend_top(
    page: int | None = None,
    containerid: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取频道热门趋势/Get channel trend top"""
        params: dict[str, Any] = {}
        if containerid is not None:
            params["containerid"] = containerid
        if page is not None:
            params["page"] = page
        body = await request.json()
        return await proxy_request("weibo", "/api/v1/weibo/web/fetch_trend_top", json_body=body)

@router.get("/fetch_channel_feed")
async def fetch_channel_feed(
    page: int | None = None,
    channel_name: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """根据频道名称获取热门内容/Get channel feed by name"""
        params: dict[str, Any] = {}
        if channel_name is not None:
            params["channel_name"] = channel_name
        if page is not None:
            params["page"] = page
        body = await request.json()
        return await proxy_request("weibo", "/api/v1/weibo/web/fetch_channel_feed", json_body=body)

@router.get("/fetch_user_info")
async def fetch_user_info(
    uid: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户信息/Get user information"""
        params: dict[str, Any] = {}
        if uid is not None:
            params["uid"] = uid
        body = await request.json()
        return await proxy_request("weibo", "/api/v1/weibo/web/fetch_user_info", json_body=body)

@router.get("/fetch_user_posts")
async def fetch_user_posts(
    since_id: str | None = None,
    page: int | None = None,
    uid: str,
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
        body = await request.json()
        return await proxy_request("weibo", "/api/v1/weibo/web/fetch_user_posts", json_body=body)

@router.get("/fetch_post_detail")
async def fetch_post_detail(
    post_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取微博详情/Get post detail"""
        params: dict[str, Any] = {}
        if post_id is not None:
            params["post_id"] = post_id
        body = await request.json()
        return await proxy_request("weibo", "/api/v1/weibo/web/fetch_post_detail", json_body=body)

@router.get("/fetch_post_comments")
async def fetch_post_comments(
    max_id_type: int | None = None,
    max_id: str | None = None,
    mid: str,
    post_id: str,
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
        body = await request.json()
        return await proxy_request("weibo", "/api/v1/weibo/web/fetch_post_comments", json_body=body)

@router.get("/fetch_comment_replies")
async def fetch_comment_replies(
    max_id: str | None = None,
    cid: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取评论子评论/Get comment replies"""
        params: dict[str, Any] = {}
        if cid is not None:
            params["cid"] = cid
        if max_id is not None:
            params["max_id"] = max_id
        body = await request.json()
        return await proxy_request("weibo", "/api/v1/weibo/web/fetch_comment_replies", json_body=body)

@router.get("/fetch_search")
async def fetch_search(
    time_scope: str | None = None,
    search_type: str | None = None,
    page: int | None = None,
    keyword: str,
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
        body = await request.json()
        return await proxy_request("weibo", "/api/v1/weibo/web/fetch_search", json_body=body)

@router.get("/fetch_hot_search")
async def fetch_hot_search(
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取热搜榜/Get hot search ranking"""
        body = await request.json()
        return await proxy_request("weibo", "/api/v1/weibo/web/fetch_hot_search", json_body=body)

@router.get("/fetch_search_topics")
async def fetch_search_topics(
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取搜索页热搜词/Get search page hot topics"""
        body = await request.json()
        return await proxy_request("weibo", "/api/v1/weibo/web/fetch_search_topics", json_body=body)
