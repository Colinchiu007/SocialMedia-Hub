"""Auto-generated routes for Threads-Web-API."""

from __future__ import annotations

from typing import Any

from fastapi import APIRouter, Depends, Request

from socialmedia_hub.server._core import proxy_request, verify_api_key

router = APIRouter(prefix="/api/v1/threads/web", tags=["threads_web"])

@router.get("/fetch_user_info")
async def fetch_user_info(
    username: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户信息/Get user info"""
    params: dict[str, Any] = {}
    if username is not None:
        params["username"] = username
    return await proxy_request("threads", "/api/v1/threads/web/fetch_user_info", params=params)

@router.get("/fetch_user_info_by_id")
async def fetch_user_info_by_id(
    user_id: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """根据用户ID获取用户信息/Get user info by ID"""
    params: dict[str, Any] = {}
    if user_id is not None:
        params["user_id"] = user_id
    return await proxy_request("threads", "/api/v1/threads/web/fetch_user_info_by_id", params=params)

@router.get("/fetch_user_posts")
async def fetch_user_posts(
    user_id: str,
    request: Request,
    end_cursor: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户帖子列表/Get user posts"""
    params: dict[str, Any] = {}
    if user_id is not None:
        params["user_id"] = user_id
    if end_cursor is not None:
        params["end_cursor"] = end_cursor
    return await proxy_request("threads", "/api/v1/threads/web/fetch_user_posts", params=params)

@router.get("/fetch_user_reposts")
async def fetch_user_reposts(
    user_id: str,
    request: Request,
    end_cursor: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户转发列表/Get user reposts"""
    params: dict[str, Any] = {}
    if user_id is not None:
        params["user_id"] = user_id
    if end_cursor is not None:
        params["end_cursor"] = end_cursor
    return await proxy_request("threads", "/api/v1/threads/web/fetch_user_reposts", params=params)

@router.get("/fetch_user_replies")
async def fetch_user_replies(
    user_id: str,
    request: Request,
    end_cursor: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户回复列表/Get user replies"""
    params: dict[str, Any] = {}
    if user_id is not None:
        params["user_id"] = user_id
    if end_cursor is not None:
        params["end_cursor"] = end_cursor
    return await proxy_request("threads", "/api/v1/threads/web/fetch_user_replies", params=params)

@router.get("/fetch_post_detail")
async def fetch_post_detail(
    post_id: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取帖子详情/Get post detail"""
    params: dict[str, Any] = {}
    if post_id is not None:
        params["post_id"] = post_id
    return await proxy_request("threads", "/api/v1/threads/web/fetch_post_detail", params=params)

@router.get("/fetch_post_detail_v2")
async def fetch_post_detail_v2(
    request: Request,
    post_id: str | None = None,
    url: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取帖子详情 V2(支持链接)/Get post detail V2(supports URL)"""
    params: dict[str, Any] = {}
    if post_id is not None:
        params["post_id"] = post_id
    if url is not None:
        params["url"] = url
    return await proxy_request("threads", "/api/v1/threads/web/fetch_post_detail_v2", params=params)

@router.get("/fetch_post_comments")
async def fetch_post_comments(
    post_id: str,
    request: Request,
    end_cursor: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取帖子评论/Get post comments"""
    params: dict[str, Any] = {}
    if post_id is not None:
        params["post_id"] = post_id
    if end_cursor is not None:
        params["end_cursor"] = end_cursor
    return await proxy_request("threads", "/api/v1/threads/web/fetch_post_comments", params=params)

@router.get("/search_top")
async def search_top(
    query: str,
    request: Request,
    end_cursor: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """搜索热门内容/Search top content"""
    params: dict[str, Any] = {}
    if query is not None:
        params["query"] = query
    if end_cursor is not None:
        params["end_cursor"] = end_cursor
    return await proxy_request("threads", "/api/v1/threads/web/search_top", params=params)

@router.get("/search_recent")
async def search_recent(
    query: str,
    request: Request,
    end_cursor: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """搜索最新内容/Search recent content"""
    params: dict[str, Any] = {}
    if query is not None:
        params["query"] = query
    if end_cursor is not None:
        params["end_cursor"] = end_cursor
    return await proxy_request("threads", "/api/v1/threads/web/search_recent", params=params)

@router.get("/search_profiles")
async def search_profiles(
    query: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """搜索用户档案/Search profiles"""
    params: dict[str, Any] = {}
    if query is not None:
        params["query"] = query
    return await proxy_request("threads", "/api/v1/threads/web/search_profiles", params=params)
