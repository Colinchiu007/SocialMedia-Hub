"""Auto-generated routes for Lemon8-App-API."""

from __future__ import annotations

from typing import Any

from fastapi import APIRouter, Depends, Request

from socialmedia_hub.server._core import proxy_request, verify_api_key

router = APIRouter(prefix="/api/v1/lemon8/app", tags=["lemon8_app"])

@router.get("/fetch_user_profile")
async def fetch_user_profile(
    user_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取指定用户的信息/Get information of specified user"""
        params: dict[str, Any] = {}
        if user_id is not None:
            params["user_id"] = user_id
        body = await request.json()
        return await proxy_request("lemon8", "/api/v1/lemon8/app/fetch_user_profile", json_body=body)

@router.get("/fetch_post_detail")
async def fetch_post_detail(
    item_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取指定作品的信息/Get information of specified post"""
        params: dict[str, Any] = {}
        if item_id is not None:
            params["item_id"] = item_id
        body = await request.json()
        return await proxy_request("lemon8", "/api/v1/lemon8/app/fetch_post_detail", json_body=body)

@router.get("/fetch_user_follower_list")
async def fetch_user_follower_list(
    cursor: str | None = None,
    user_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取指定用户的粉丝列表/Get fans list of specified user"""
        params: dict[str, Any] = {}
        if user_id is not None:
            params["user_id"] = user_id
        if cursor is not None:
            params["cursor"] = cursor
        body = await request.json()
        return await proxy_request("lemon8", "/api/v1/lemon8/app/fetch_user_follower_list", json_body=body)

@router.get("/fetch_user_following_list")
async def fetch_user_following_list(
    cursor: str | None = None,
    user_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取指定用户的关注列表/Get following list of specified user"""
        params: dict[str, Any] = {}
        if user_id is not None:
            params["user_id"] = user_id
        if cursor is not None:
            params["cursor"] = cursor
        body = await request.json()
        return await proxy_request("lemon8", "/api/v1/lemon8/app/fetch_user_following_list", json_body=body)

@router.get("/fetch_post_comment_list")
async def fetch_post_comment_list(
    offset: str | None = None,
    media_id: str,
    item_id: str,
    group_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取指定作品的评论列表/Get comments list of specified post"""
        params: dict[str, Any] = {}
        if group_id is not None:
            params["group_id"] = group_id
        if item_id is not None:
            params["item_id"] = item_id
        if media_id is not None:
            params["media_id"] = media_id
        if offset is not None:
            params["offset"] = offset
        body = await request.json()
        return await proxy_request("lemon8", "/api/v1/lemon8/app/fetch_post_comment_list", json_body=body)

@router.get("/fetch_discover_banners")
async def fetch_discover_banners(
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取发现页Banner/Get banners of discover page"""
        body = await request.json()
        return await proxy_request("lemon8", "/api/v1/lemon8/app/fetch_discover_banners", json_body=body)

@router.get("/fetch_discover_tab")
async def fetch_discover_tab(
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取发现页主体内容/Get main content of discover page"""
        body = await request.json()
        return await proxy_request("lemon8", "/api/v1/lemon8/app/fetch_discover_tab", json_body=body)

@router.get("/fetch_discover_tab_information_tabs")
async def fetch_discover_tab_information_tabs(
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取发现页的 Editor's Picks/Get Editor's Picks of discover page"""
        body = await request.json()
        return await proxy_request("lemon8", "/api/v1/lemon8/app/fetch_discover_tab_information_tabs", json_body=body)

@router.get("/fetch_hot_search_keywords")
async def fetch_hot_search_keywords(
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取热搜关键词/Get hot search keywords"""
        body = await request.json()
        return await proxy_request("lemon8", "/api/v1/lemon8/app/fetch_hot_search_keywords", json_body=body)

@router.get("/fetch_topic_info")
async def fetch_topic_info(
    forum_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取话题信息/Get topic information"""
        params: dict[str, Any] = {}
        if forum_id is not None:
            params["forum_id"] = forum_id
        body = await request.json()
        return await proxy_request("lemon8", "/api/v1/lemon8/app/fetch_topic_info", json_body=body)

@router.get("/fetch_topic_post_list")
async def fetch_topic_post_list(
    sort_type: str | None = None,
    hashtag_name: str,
    category_parameter: str,
    max_behot_time: str | None = None,
    category: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取话题作品列表/Get topic post list"""
        params: dict[str, Any] = {}
        if category is not None:
            params["category"] = category
        if max_behot_time is not None:
            params["max_behot_time"] = max_behot_time
        if category_parameter is not None:
            params["category_parameter"] = category_parameter
        if hashtag_name is not None:
            params["hashtag_name"] = hashtag_name
        if sort_type is not None:
            params["sort_type"] = sort_type
        body = await request.json()
        return await proxy_request("lemon8", "/api/v1/lemon8/app/fetch_topic_post_list", json_body=body)

@router.get("/fetch_search")
async def fetch_search(
    search_tab: str | None = None,
    order_by: str | None = None,
    filter_type: str | None = None,
    max_cursor: str | None = None,
    query: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """搜索接口/Search API"""
        params: dict[str, Any] = {}
        if query is not None:
            params["query"] = query
        if max_cursor is not None:
            params["max_cursor"] = max_cursor
        if filter_type is not None:
            params["filter_type"] = filter_type
        if order_by is not None:
            params["order_by"] = order_by
        if search_tab is not None:
            params["search_tab"] = search_tab
        body = await request.json()
        return await proxy_request("lemon8", "/api/v1/lemon8/app/fetch_search", json_body=body)

@router.get("/get_item_id")
async def get_item_id(
    share_text: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """通过分享链接获取作品ID/Get post ID through sharing link"""
        params: dict[str, Any] = {}
        if share_text is not None:
            params["share_text"] = share_text
        body = await request.json()
        return await proxy_request("lemon8", "/api/v1/lemon8/app/get_item_id", json_body=body)

@router.get("/get_user_id")
async def get_user_id(
    share_text: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """通过分享链接获取用户ID/Get user ID through sharing link"""
        params: dict[str, Any] = {}
        if share_text is not None:
            params["share_text"] = share_text
        body = await request.json()
        return await proxy_request("lemon8", "/api/v1/lemon8/app/get_user_id", json_body=body)

@router.post("/get_item_ids")
async def get_item_ids(
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """通过分享链接批量获取作品ID/Get post IDs in batch through sharing links"""
        body = await request.json()
        return await proxy_request("lemon8", "/api/v1/lemon8/app/get_item_ids", json_body=body)

@router.post("/get_user_ids")
async def get_user_ids(
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """通过分享链接批量获取用户ID/Get user IDs in batch through sharing links"""
        body = await request.json()
        return await proxy_request("lemon8", "/api/v1/lemon8/app/get_user_ids", json_body=body)
