"""Auto-generated routes for Weibo-App-API."""

from __future__ import annotations

from typing import Any

from fastapi import APIRouter, Depends, Request

from socialmedia_hub.server._core import proxy_request, verify_api_key

router = APIRouter(prefix="/api/v1/weibo/app", tags=["weibo_app"])

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
        return await proxy_request("weibo", "/api/v1/weibo/app/fetch_user_info", json_body=body)

@router.get("/fetch_user_info_detail")
async def fetch_user_info_detail(
    uid: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户详细信息/Get user detail information"""
        params: dict[str, Any] = {}
        if uid is not None:
            params["uid"] = uid
        body = await request.json()
        return await proxy_request("weibo", "/api/v1/weibo/app/fetch_user_info_detail", json_body=body)

@router.get("/fetch_user_timeline")
async def fetch_user_timeline(
    month: str | None = None,
    filter_type: str | None = None,
    page: int | None = None,
    uid: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户发布的微博/Get user timeline"""
        params: dict[str, Any] = {}
        if uid is not None:
            params["uid"] = uid
        if page is not None:
            params["page"] = page
        if filter_type is not None:
            params["filter_type"] = filter_type
        if month is not None:
            params["month"] = month
        body = await request.json()
        return await proxy_request("weibo", "/api/v1/weibo/app/fetch_user_timeline", json_body=body)

@router.get("/fetch_user_videos")
async def fetch_user_videos(
    since_id: str | None = None,
    uid: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户视频列表/Get user videos"""
        params: dict[str, Any] = {}
        if uid is not None:
            params["uid"] = uid
        if since_id is not None:
            params["since_id"] = since_id
        body = await request.json()
        return await proxy_request("weibo", "/api/v1/weibo/app/fetch_user_videos", json_body=body)

@router.get("/fetch_user_super_topics")
async def fetch_user_super_topics(
    page: int | None = None,
    uid: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户参与的超话列表/Get user super topics"""
        params: dict[str, Any] = {}
        if uid is not None:
            params["uid"] = uid
        if page is not None:
            params["page"] = page
        body = await request.json()
        return await proxy_request("weibo", "/api/v1/weibo/app/fetch_user_super_topics", json_body=body)

@router.get("/fetch_user_album")
async def fetch_user_album(
    since_id: str | None = None,
    uid: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户相册/Get user album"""
        params: dict[str, Any] = {}
        if uid is not None:
            params["uid"] = uid
        if since_id is not None:
            params["since_id"] = since_id
        body = await request.json()
        return await proxy_request("weibo", "/api/v1/weibo/app/fetch_user_album", json_body=body)

@router.get("/fetch_user_articles")
async def fetch_user_articles(
    since_id: str | None = None,
    uid: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户文章列表/Get user articles"""
        params: dict[str, Any] = {}
        if uid is not None:
            params["uid"] = uid
        if since_id is not None:
            params["since_id"] = since_id
        body = await request.json()
        return await proxy_request("weibo", "/api/v1/weibo/app/fetch_user_articles", json_body=body)

@router.get("/fetch_user_audios")
async def fetch_user_audios(
    since_id: str | None = None,
    uid: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户音频列表/Get user audios"""
        params: dict[str, Any] = {}
        if uid is not None:
            params["uid"] = uid
        if since_id is not None:
            params["since_id"] = since_id
        body = await request.json()
        return await proxy_request("weibo", "/api/v1/weibo/app/fetch_user_audios", json_body=body)

@router.get("/fetch_user_profile_feed")
async def fetch_user_profile_feed(
    since_id: str | None = None,
    uid: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户主页动态/Get user profile feed"""
        params: dict[str, Any] = {}
        if uid is not None:
            params["uid"] = uid
        if since_id is not None:
            params["since_id"] = since_id
        body = await request.json()
        return await proxy_request("weibo", "/api/v1/weibo/app/fetch_user_profile_feed", json_body=body)

@router.get("/fetch_status_detail")
async def fetch_status_detail(
    status_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取微博详情/Get post detail"""
        params: dict[str, Any] = {}
        if status_id is not None:
            params["status_id"] = status_id
        body = await request.json()
        return await proxy_request("weibo", "/api/v1/weibo/app/fetch_status_detail", json_body=body)

@router.get("/fetch_status_comments")
async def fetch_status_comments(
    sort_type: str | None = None,
    max_id: str | None = None,
    status_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取微博评论/Get post comments"""
        params: dict[str, Any] = {}
        if status_id is not None:
            params["status_id"] = status_id
        if max_id is not None:
            params["max_id"] = max_id
        if sort_type is not None:
            params["sort_type"] = sort_type
        body = await request.json()
        return await proxy_request("weibo", "/api/v1/weibo/app/fetch_status_comments", json_body=body)

@router.get("/fetch_status_reposts")
async def fetch_status_reposts(
    max_id: str | None = None,
    status_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取微博转发列表/Get post reposts"""
        params: dict[str, Any] = {}
        if status_id is not None:
            params["status_id"] = status_id
        if max_id is not None:
            params["max_id"] = max_id
        body = await request.json()
        return await proxy_request("weibo", "/api/v1/weibo/app/fetch_status_reposts", json_body=body)

@router.get("/fetch_status_likes")
async def fetch_status_likes(
    attitude_type: str | None = None,
    status_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取微博点赞列表/Get post likes"""
        params: dict[str, Any] = {}
        if status_id is not None:
            params["status_id"] = status_id
        if attitude_type is not None:
            params["attitude_type"] = attitude_type
        body = await request.json()
        return await proxy_request("weibo", "/api/v1/weibo/app/fetch_status_likes", json_body=body)

@router.get("/fetch_video_detail")
async def fetch_video_detail(
    mid: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取视频详情/Get video detail"""
        params: dict[str, Any] = {}
        if mid is not None:
            params["mid"] = mid
        body = await request.json()
        return await proxy_request("weibo", "/api/v1/weibo/app/fetch_video_detail", json_body=body)

@router.get("/fetch_video_featured_feed")
async def fetch_video_featured_feed(
    page: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取短视频精选Feed流/Get video featured feed"""
        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        body = await request.json()
        return await proxy_request("weibo", "/api/v1/weibo/app/fetch_video_featured_feed", json_body=body)

@router.get("/fetch_search_all")
async def fetch_search_all(
    search_type: int | None = None,
    page: int | None = None,
    query: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """综合搜索/Comprehensive search"""
        params: dict[str, Any] = {}
        if query is not None:
            params["query"] = query
        if page is not None:
            params["page"] = page
        if search_type is not None:
            params["search_type"] = search_type
        body = await request.json()
        return await proxy_request("weibo", "/api/v1/weibo/app/fetch_search_all", json_body=body)

@router.get("/fetch_ai_smart_search")
async def fetch_ai_smart_search(
    page: int | None = None,
    query: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """AI智搜/AI Smart Search"""
        params: dict[str, Any] = {}
        if query is not None:
            params["query"] = query
        if page is not None:
            params["page"] = page
        body = await request.json()
        return await proxy_request("weibo", "/api/v1/weibo/app/fetch_ai_smart_search", json_body=body)

@router.get("/fetch_home_recommend_feed")
async def fetch_home_recommend_feed(
    count: int | None = None,
    page: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取首页推荐Feed流/Get home recommend feed"""
        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if count is not None:
            params["count"] = count
        body = await request.json()
        return await proxy_request("weibo", "/api/v1/weibo/app/fetch_home_recommend_feed", json_body=body)

@router.get("/fetch_hot_search")
async def fetch_hot_search(
    region_name: str | None = None,
    count: int | None = None,
    page: int | None = None,
    category: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取热搜榜/Get hot search"""
        params: dict[str, Any] = {}
        if category is not None:
            params["category"] = category
        if page is not None:
            params["page"] = page
        if count is not None:
            params["count"] = count
        if region_name is not None:
            params["region_name"] = region_name
        body = await request.json()
        return await proxy_request("weibo", "/api/v1/weibo/app/fetch_hot_search", json_body=body)

@router.get("/fetch_hot_search_categories")
async def fetch_hot_search_categories(
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取热搜分类列表/Get hot search categories"""
        body = await request.json()
        return await proxy_request("weibo", "/api/v1/weibo/app/fetch_hot_search_categories", json_body=body)
