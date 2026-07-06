"""Auto-generated routes for Weibo-App-API."""

from __future__ import annotations

from typing import Any

from fastapi import APIRouter, Depends, Request

from socialmedia_hub.server._core import proxy_request, verify_api_key

router = APIRouter(prefix="/api/v1/weibo/app", tags=["weibo_app"])

@router.get("/fetch_user_info")
async def fetch_user_info(
    uid: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户信息/Get user information"""
    body = await request.json()
    params: dict[str, Any] = {}
    if uid is not None:
        params["uid"] = uid
    return await proxy_request("weibo", "/api/v1/weibo/app/fetch_user_info", params=params, json_body=body)

@router.get("/fetch_user_info_detail")
async def fetch_user_info_detail(
    uid: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户详细信息/Get user detail information"""
    body = await request.json()
    params: dict[str, Any] = {}
    if uid is not None:
        params["uid"] = uid
    return await proxy_request("weibo", "/api/v1/weibo/app/fetch_user_info_detail", params=params, json_body=body)

@router.get("/fetch_user_timeline")
async def fetch_user_timeline(
    uid: str,
    request: Request,
    page: int | None = None,
    filter_type: str | None = None,
    month: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户发布的微博/Get user timeline"""
    body = await request.json()
    params: dict[str, Any] = {}
    if uid is not None:
        params["uid"] = uid
    if page is not None:
        params["page"] = page
    if filter_type is not None:
        params["filter_type"] = filter_type
    if month is not None:
        params["month"] = month
    return await proxy_request("weibo", "/api/v1/weibo/app/fetch_user_timeline", params=params, json_body=body)

@router.get("/fetch_user_videos")
async def fetch_user_videos(
    uid: str,
    request: Request,
    since_id: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户视频列表/Get user videos"""
    body = await request.json()
    params: dict[str, Any] = {}
    if uid is not None:
        params["uid"] = uid
    if since_id is not None:
        params["since_id"] = since_id
    return await proxy_request("weibo", "/api/v1/weibo/app/fetch_user_videos", params=params, json_body=body)

@router.get("/fetch_user_super_topics")
async def fetch_user_super_topics(
    uid: str,
    request: Request,
    page: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户参与的超话列表/Get user super topics"""
    body = await request.json()
    params: dict[str, Any] = {}
    if uid is not None:
        params["uid"] = uid
    if page is not None:
        params["page"] = page
    return await proxy_request("weibo", "/api/v1/weibo/app/fetch_user_super_topics", params=params, json_body=body)

@router.get("/fetch_user_album")
async def fetch_user_album(
    uid: str,
    request: Request,
    since_id: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户相册/Get user album"""
    body = await request.json()
    params: dict[str, Any] = {}
    if uid is not None:
        params["uid"] = uid
    if since_id is not None:
        params["since_id"] = since_id
    return await proxy_request("weibo", "/api/v1/weibo/app/fetch_user_album", params=params, json_body=body)

@router.get("/fetch_user_articles")
async def fetch_user_articles(
    uid: str,
    request: Request,
    since_id: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户文章列表/Get user articles"""
    body = await request.json()
    params: dict[str, Any] = {}
    if uid is not None:
        params["uid"] = uid
    if since_id is not None:
        params["since_id"] = since_id
    return await proxy_request("weibo", "/api/v1/weibo/app/fetch_user_articles", params=params, json_body=body)

@router.get("/fetch_user_audios")
async def fetch_user_audios(
    uid: str,
    request: Request,
    since_id: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户音频列表/Get user audios"""
    body = await request.json()
    params: dict[str, Any] = {}
    if uid is not None:
        params["uid"] = uid
    if since_id is not None:
        params["since_id"] = since_id
    return await proxy_request("weibo", "/api/v1/weibo/app/fetch_user_audios", params=params, json_body=body)

@router.get("/fetch_user_profile_feed")
async def fetch_user_profile_feed(
    uid: str,
    request: Request,
    since_id: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户主页动态/Get user profile feed"""
    body = await request.json()
    params: dict[str, Any] = {}
    if uid is not None:
        params["uid"] = uid
    if since_id is not None:
        params["since_id"] = since_id
    return await proxy_request("weibo", "/api/v1/weibo/app/fetch_user_profile_feed", params=params, json_body=body)

@router.get("/fetch_status_detail")
async def fetch_status_detail(
    status_id: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取微博详情/Get post detail"""
    body = await request.json()
    params: dict[str, Any] = {}
    if status_id is not None:
        params["status_id"] = status_id
    return await proxy_request("weibo", "/api/v1/weibo/app/fetch_status_detail", params=params, json_body=body)

@router.get("/fetch_status_comments")
async def fetch_status_comments(
    status_id: str,
    request: Request,
    max_id: str | None = None,
    sort_type: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取微博评论/Get post comments"""
    body = await request.json()
    params: dict[str, Any] = {}
    if status_id is not None:
        params["status_id"] = status_id
    if max_id is not None:
        params["max_id"] = max_id
    if sort_type is not None:
        params["sort_type"] = sort_type
    return await proxy_request("weibo", "/api/v1/weibo/app/fetch_status_comments", params=params, json_body=body)

@router.get("/fetch_status_reposts")
async def fetch_status_reposts(
    status_id: str,
    request: Request,
    max_id: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取微博转发列表/Get post reposts"""
    body = await request.json()
    params: dict[str, Any] = {}
    if status_id is not None:
        params["status_id"] = status_id
    if max_id is not None:
        params["max_id"] = max_id
    return await proxy_request("weibo", "/api/v1/weibo/app/fetch_status_reposts", params=params, json_body=body)

@router.get("/fetch_status_likes")
async def fetch_status_likes(
    status_id: str,
    request: Request,
    attitude_type: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取微博点赞列表/Get post likes"""
    body = await request.json()
    params: dict[str, Any] = {}
    if status_id is not None:
        params["status_id"] = status_id
    if attitude_type is not None:
        params["attitude_type"] = attitude_type
    return await proxy_request("weibo", "/api/v1/weibo/app/fetch_status_likes", params=params, json_body=body)

@router.get("/fetch_video_detail")
async def fetch_video_detail(
    mid: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取视频详情/Get video detail"""
    body = await request.json()
    params: dict[str, Any] = {}
    if mid is not None:
        params["mid"] = mid
    return await proxy_request("weibo", "/api/v1/weibo/app/fetch_video_detail", params=params, json_body=body)

@router.get("/fetch_video_featured_feed")
async def fetch_video_featured_feed(
    request: Request,
    page: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取短视频精选Feed流/Get video featured feed"""
    body = await request.json()
    params: dict[str, Any] = {}
    if page is not None:
        params["page"] = page
    return await proxy_request("weibo", "/api/v1/weibo/app/fetch_video_featured_feed", params=params, json_body=body)

@router.get("/fetch_search_all")
async def fetch_search_all(
    query: str,
    request: Request,
    page: int | None = None,
    search_type: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """综合搜索/Comprehensive search"""
    body = await request.json()
    params: dict[str, Any] = {}
    if query is not None:
        params["query"] = query
    if page is not None:
        params["page"] = page
    if search_type is not None:
        params["search_type"] = search_type
    return await proxy_request("weibo", "/api/v1/weibo/app/fetch_search_all", params=params, json_body=body)

@router.get("/fetch_ai_smart_search")
async def fetch_ai_smart_search(
    query: str,
    request: Request,
    page: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """AI智搜/AI Smart Search"""
    body = await request.json()
    params: dict[str, Any] = {}
    if query is not None:
        params["query"] = query
    if page is not None:
        params["page"] = page
    return await proxy_request("weibo", "/api/v1/weibo/app/fetch_ai_smart_search", params=params, json_body=body)

@router.get("/fetch_home_recommend_feed")
async def fetch_home_recommend_feed(
    request: Request,
    page: str | None = None,
    count: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取首页推荐Feed流/Get home recommend feed"""
    body = await request.json()
    params: dict[str, Any] = {}
    if page is not None:
        params["page"] = page
    if count is not None:
        params["count"] = count
    return await proxy_request("weibo", "/api/v1/weibo/app/fetch_home_recommend_feed", params=params, json_body=body)

@router.get("/fetch_hot_search")
async def fetch_hot_search(
    request: Request,
    category: str | None = None,
    page: int | None = None,
    count: int | None = None,
    region_name: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取热搜榜/Get hot search"""
    body = await request.json()
    params: dict[str, Any] = {}
    if category is not None:
        params["category"] = category
    if page is not None:
        params["page"] = page
    if count is not None:
        params["count"] = count
    if region_name is not None:
        params["region_name"] = region_name
    return await proxy_request("weibo", "/api/v1/weibo/app/fetch_hot_search", params=params, json_body=body)

@router.get("/fetch_hot_search_categories")
async def fetch_hot_search_categories(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取热搜分类列表/Get hot search categories"""
    body = await request.json()
    return await proxy_request("weibo", "/api/v1/weibo/app/fetch_hot_search_categories", json_body=body)
