"""Auto-generated routes for PiPiXia-App-API."""

from __future__ import annotations

from typing import Any

from fastapi import APIRouter, Depends, Request

from socialmedia_hub.server._core import proxy_request, verify_api_key

router = APIRouter(prefix="/api/v1/pipixia/app", tags=["pipixia_app"])

@router.get("/fetch_post_detail")
async def fetch_post_detail(
    cell_id: str,
    request: Request,
    cell_type: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取单个作品数据/Get single video data"""
    body = await request.json()
    params: dict[str, Any] = {}
    if cell_id is not None:
        params["cell_id"] = cell_id
    if cell_type is not None:
        params["cell_type"] = cell_type
    return await proxy_request("pipixia", "/api/v1/pipixia/app/fetch_post_detail", params=params, json_body=body)

@router.get("/fetch_increase_post_view_count")
async def fetch_increase_post_view_count(
    cell_id: str,
    request: Request,
    cell_type: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """增加作品浏览数/Increase post view count"""
    body = await request.json()
    params: dict[str, Any] = {}
    if cell_id is not None:
        params["cell_id"] = cell_id
    if cell_type is not None:
        params["cell_type"] = cell_type
    return await proxy_request("pipixia", "/api/v1/pipixia/app/fetch_increase_post_view_count", params=params, json_body=body)

@router.get("/fetch_post_statistics")
async def fetch_post_statistics(
    cell_id: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取作品统计数据/Get post statistics"""
    body = await request.json()
    params: dict[str, Any] = {}
    if cell_id is not None:
        params["cell_id"] = cell_id
    return await proxy_request("pipixia", "/api/v1/pipixia/app/fetch_post_statistics", params=params, json_body=body)

@router.get("/fetch_user_info")
async def fetch_user_info(
    user_id: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户信息/Get user information"""
    body = await request.json()
    params: dict[str, Any] = {}
    if user_id is not None:
        params["user_id"] = user_id
    return await proxy_request("pipixia", "/api/v1/pipixia/app/fetch_user_info", params=params, json_body=body)

@router.get("/fetch_user_post_list")
async def fetch_user_post_list(
    user_id: str,
    request: Request,
    cursor: str | None = None,
    feed_count: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户作品列表/Get user post list"""
    body = await request.json()
    params: dict[str, Any] = {}
    if user_id is not None:
        params["user_id"] = user_id
    if cursor is not None:
        params["cursor"] = cursor
    if feed_count is not None:
        params["feed_count"] = feed_count
    return await proxy_request("pipixia", "/api/v1/pipixia/app/fetch_user_post_list", params=params, json_body=body)

@router.get("/fetch_user_follower_list")
async def fetch_user_follower_list(
    user_id: str,
    request: Request,
    cursor: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户粉丝列表/Get user follower list"""
    body = await request.json()
    params: dict[str, Any] = {}
    if user_id is not None:
        params["user_id"] = user_id
    if cursor is not None:
        params["cursor"] = cursor
    return await proxy_request("pipixia", "/api/v1/pipixia/app/fetch_user_follower_list", params=params, json_body=body)

@router.get("/fetch_user_following_list")
async def fetch_user_following_list(
    user_id: str,
    request: Request,
    cursor: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户关注列表/Get user following list"""
    body = await request.json()
    params: dict[str, Any] = {}
    if user_id is not None:
        params["user_id"] = user_id
    if cursor is not None:
        params["cursor"] = cursor
    return await proxy_request("pipixia", "/api/v1/pipixia/app/fetch_user_following_list", params=params, json_body=body)

@router.get("/fetch_post_comment_list")
async def fetch_post_comment_list(
    cell_id: str,
    request: Request,
    cell_type: int | None = None,
    offset: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取作品评论列表/Get post comment list"""
    body = await request.json()
    params: dict[str, Any] = {}
    if cell_id is not None:
        params["cell_id"] = cell_id
    if cell_type is not None:
        params["cell_type"] = cell_type
    if offset is not None:
        params["offset"] = offset
    return await proxy_request("pipixia", "/api/v1/pipixia/app/fetch_post_comment_list", params=params, json_body=body)

@router.get("/fetch_short_url")
async def fetch_short_url(
    original_url: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """生成短连接/Generate short URL"""
    body = await request.json()
    params: dict[str, Any] = {}
    if original_url is not None:
        params["original_url"] = original_url
    return await proxy_request("pipixia", "/api/v1/pipixia/app/fetch_short_url", params=params, json_body=body)

@router.get("/fetch_home_feed")
async def fetch_home_feed(
    request: Request,
    cursor: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取首页推荐/Get home feed"""
    body = await request.json()
    params: dict[str, Any] = {}
    if cursor is not None:
        params["cursor"] = cursor
    return await proxy_request("pipixia", "/api/v1/pipixia/app/fetch_home_feed", params=params, json_body=body)

@router.get("/fetch_hot_search_words")
async def fetch_hot_search_words(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取热搜词条/Get hot search words"""
    body = await request.json()
    return await proxy_request("pipixia", "/api/v1/pipixia/app/fetch_hot_search_words", json_body=body)

@router.get("/fetch_hot_search_board_list")
async def fetch_hot_search_board_list(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取热搜榜单列表/Get hot search board list"""
    body = await request.json()
    return await proxy_request("pipixia", "/api/v1/pipixia/app/fetch_hot_search_board_list", json_body=body)

@router.get("/fetch_hot_search_board_detail")
async def fetch_hot_search_board_detail(
    block_type: int,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取热搜榜单详情/Get hot search board detail"""
    body = await request.json()
    params: dict[str, Any] = {}
    if block_type is not None:
        params["block_type"] = block_type
    return await proxy_request("pipixia", "/api/v1/pipixia/app/fetch_hot_search_board_detail", params=params, json_body=body)

@router.get("/fetch_search")
async def fetch_search(
    keyword: str,
    request: Request,
    offset: str | None = None,
    search_type: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """搜索接口/Search API"""
    body = await request.json()
    params: dict[str, Any] = {}
    if keyword is not None:
        params["keyword"] = keyword
    if offset is not None:
        params["offset"] = offset
    if search_type is not None:
        params["search_type"] = search_type
    return await proxy_request("pipixia", "/api/v1/pipixia/app/fetch_search", params=params, json_body=body)

@router.get("/fetch_hashtag_detail")
async def fetch_hashtag_detail(
    hashtag_id: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取话题详情/Get hashtag detail"""
    body = await request.json()
    params: dict[str, Any] = {}
    if hashtag_id is not None:
        params["hashtag_id"] = hashtag_id
    return await proxy_request("pipixia", "/api/v1/pipixia/app/fetch_hashtag_detail", params=params, json_body=body)

@router.get("/fetch_hashtag_post_list")
async def fetch_hashtag_post_list(
    hashtag_id: str,
    request: Request,
    cursor: str | None = None,
    feed_count: str | None = None,
    hashtag_request_type: str | None = None,
    hashtag_sort_type: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取话题作品列表/Get hashtag post list"""
    body = await request.json()
    params: dict[str, Any] = {}
    if hashtag_id is not None:
        params["hashtag_id"] = hashtag_id
    if cursor is not None:
        params["cursor"] = cursor
    if feed_count is not None:
        params["feed_count"] = feed_count
    if hashtag_request_type is not None:
        params["hashtag_request_type"] = hashtag_request_type
    if hashtag_sort_type is not None:
        params["hashtag_sort_type"] = hashtag_sort_type
    return await proxy_request("pipixia", "/api/v1/pipixia/app/fetch_hashtag_post_list", params=params, json_body=body)

@router.get("/fetch_home_short_drama_feed")
async def fetch_home_short_drama_feed(
    request: Request,
    page: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取首页短剧推荐/Get home short drama feed"""
    body = await request.json()
    params: dict[str, Any] = {}
    if page is not None:
        params["page"] = page
    return await proxy_request("pipixia", "/api/v1/pipixia/app/fetch_home_short_drama_feed", params=params, json_body=body)
