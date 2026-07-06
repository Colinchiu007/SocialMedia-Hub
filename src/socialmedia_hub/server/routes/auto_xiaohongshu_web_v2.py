"""Auto-generated routes for Xiaohongshu-Web-V2-API."""

from __future__ import annotations

from typing import Any

from fastapi import APIRouter, Depends, Request

from socialmedia_hub.server._core import proxy_request, verify_api_key

router = APIRouter(prefix="/api/v1/xiaohongshu/web/v2", tags=["xiaohongshu_web_v2"])

@router.get("/fetch_feed_notes")
async def fetch_feed_notes(
    note_id: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取单一笔记和推荐笔记 V1 (已弃用)/Fetch one note and feed notes V1 (deprecated)"""
    body = await request.json()
    params: dict[str, Any] = {}
    if note_id is not None:
        params["note_id"] = note_id
    return await proxy_request("xiaohongshu", "/api/v1/xiaohongshu/web_v2/fetch_feed_notes", params=params, json_body=body)

@router.get("/fetch_feed_notes_v2")
async def fetch_feed_notes_v2(
    note_id: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取单一笔记和推荐笔记 V2/Fetch one note and feed notes V2(v2稳定, 推荐使用此接口)"""
    body = await request.json()
    params: dict[str, Any] = {}
    if note_id is not None:
        params["note_id"] = note_id
    return await proxy_request("xiaohongshu", "/api/v1/xiaohongshu/web_v2/fetch_feed_notes_v2", params=params, json_body=body)

@router.get("/fetch_feed_notes_v3")
async def fetch_feed_notes_v3(
    short_url: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取单一笔记和推荐笔记 V3/Fetch one note and feed notes V3(通过短链获取笔记详情)"""
    body = await request.json()
    params: dict[str, Any] = {}
    if short_url is not None:
        params["short_url"] = short_url
    return await proxy_request("xiaohongshu", "/api/v1/xiaohongshu/web_v2/fetch_feed_notes_v3", params=params, json_body=body)

@router.get("/fetch_feed_notes_v4")
async def fetch_feed_notes_v4(
    note_id: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取单一笔记和推荐笔记 V4 (互动量有延迟)/Fetch one note and feed notes V4 (interaction volume has a delay)"""
    body = await request.json()
    params: dict[str, Any] = {}
    if note_id is not None:
        params["note_id"] = note_id
    return await proxy_request("xiaohongshu", "/api/v1/xiaohongshu/web_v2/fetch_feed_notes_v4", params=params, json_body=body)

@router.get("/fetch_feed_notes_v5")
async def fetch_feed_notes_v5(
    note_id: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取单一笔记和推荐笔记 V5 (互动量有缺失)/Fetch one note and feed notes V5 (interaction volume has a missing)"""
    body = await request.json()
    params: dict[str, Any] = {}
    if note_id is not None:
        params["note_id"] = note_id
    return await proxy_request("xiaohongshu", "/api/v1/xiaohongshu/web_v2/fetch_feed_notes_v5", params=params, json_body=body)

@router.get("/fetch_note_image")
async def fetch_note_image(
    note_id: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取小红书笔记图片/Fetch Xiaohongshu note image"""
    body = await request.json()
    params: dict[str, Any] = {}
    if note_id is not None:
        params["note_id"] = note_id
    return await proxy_request("xiaohongshu", "/api/v1/xiaohongshu/web_v2/fetch_note_image", params=params, json_body=body)

@router.get("/fetch_search_notes")
async def fetch_search_notes(
    keywords: str,
    request: Request,
    page: int | None = None,
    sort_type: str | None = None,
    note_type: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取搜索笔记/Fetch search notes"""
    body = await request.json()
    params: dict[str, Any] = {}
    if keywords is not None:
        params["keywords"] = keywords
    if page is not None:
        params["page"] = page
    if sort_type is not None:
        params["sort_type"] = sort_type
    if note_type is not None:
        params["note_type"] = note_type
    return await proxy_request("xiaohongshu", "/api/v1/xiaohongshu/web_v2/fetch_search_notes", params=params, json_body=body)

@router.get("/fetch_search_users")
async def fetch_search_users(
    keywords: str,
    request: Request,
    page: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取搜索用户/Fetch search users"""
    body = await request.json()
    params: dict[str, Any] = {}
    if keywords is not None:
        params["keywords"] = keywords
    if page is not None:
        params["page"] = page
    return await proxy_request("xiaohongshu", "/api/v1/xiaohongshu/web_v2/fetch_search_users", params=params, json_body=body)

@router.get("/fetch_home_notes")
async def fetch_home_notes(
    user_id: str,
    request: Request,
    cursor: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取Web用户主页笔记/Fetch web user profile notes"""
    body = await request.json()
    params: dict[str, Any] = {}
    if user_id is not None:
        params["user_id"] = user_id
    if cursor is not None:
        params["cursor"] = cursor
    return await proxy_request("xiaohongshu", "/api/v1/xiaohongshu/web_v2/fetch_home_notes", params=params, json_body=body)

@router.get("/fetch_home_notes_app")
async def fetch_home_notes_app(
    user_id: str,
    request: Request,
    cursor: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取App用户主页笔记/Fetch App user home notes"""
    body = await request.json()
    params: dict[str, Any] = {}
    if user_id is not None:
        params["user_id"] = user_id
    if cursor is not None:
        params["cursor"] = cursor
    return await proxy_request("xiaohongshu", "/api/v1/xiaohongshu/web_v2/fetch_home_notes_app", params=params, json_body=body)

@router.get("/fetch_note_comments")
async def fetch_note_comments(
    note_id: str,
    request: Request,
    cursor: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取笔记评论/Fetch note comments"""
    body = await request.json()
    params: dict[str, Any] = {}
    if note_id is not None:
        params["note_id"] = note_id
    if cursor is not None:
        params["cursor"] = cursor
    return await proxy_request("xiaohongshu", "/api/v1/xiaohongshu/web_v2/fetch_note_comments", params=params, json_body=body)

@router.get("/fetch_sub_comments")
async def fetch_sub_comments(
    note_id: str,
    comment_id: str,
    request: Request,
    cursor: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取子评论/Fetch sub comments"""
    body = await request.json()
    params: dict[str, Any] = {}
    if note_id is not None:
        params["note_id"] = note_id
    if comment_id is not None:
        params["comment_id"] = comment_id
    if cursor is not None:
        params["cursor"] = cursor
    return await proxy_request("xiaohongshu", "/api/v1/xiaohongshu/web_v2/fetch_sub_comments", params=params, json_body=body)

@router.get("/fetch_user_info")
async def fetch_user_info(
    user_id: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户信息/Fetch user info"""
    body = await request.json()
    params: dict[str, Any] = {}
    if user_id is not None:
        params["user_id"] = user_id
    return await proxy_request("xiaohongshu", "/api/v1/xiaohongshu/web_v2/fetch_user_info", params=params, json_body=body)

@router.get("/fetch_user_info_app")
async def fetch_user_info_app(
    user_id: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取App用户信息/Fetch App user info"""
    body = await request.json()
    params: dict[str, Any] = {}
    if user_id is not None:
        params["user_id"] = user_id
    return await proxy_request("xiaohongshu", "/api/v1/xiaohongshu/web_v2/fetch_user_info_app", params=params, json_body=body)

@router.get("/fetch_follower_list")
async def fetch_follower_list(
    user_id: str,
    request: Request,
    cursor: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户粉丝列表/Fetch follower list"""
    body = await request.json()
    params: dict[str, Any] = {}
    if user_id is not None:
        params["user_id"] = user_id
    if cursor is not None:
        params["cursor"] = cursor
    return await proxy_request("xiaohongshu", "/api/v1/xiaohongshu/web_v2/fetch_follower_list", params=params, json_body=body)

@router.get("/fetch_following_list")
async def fetch_following_list(
    user_id: str,
    request: Request,
    cursor: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户关注列表/Fetch following list"""
    body = await request.json()
    params: dict[str, Any] = {}
    if user_id is not None:
        params["user_id"] = user_id
    if cursor is not None:
        params["cursor"] = cursor
    return await proxy_request("xiaohongshu", "/api/v1/xiaohongshu/web_v2/fetch_following_list", params=params, json_body=body)

@router.get("/fetch_product_list")
async def fetch_product_list(
    user_id: str,
    request: Request,
    page: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取小红书商品列表/Fetch Xiaohongshu product list"""
    body = await request.json()
    params: dict[str, Any] = {}
    if user_id is not None:
        params["user_id"] = user_id
    if page is not None:
        params["page"] = page
    return await proxy_request("xiaohongshu", "/api/v1/xiaohongshu/web_v2/fetch_product_list", params=params, json_body=body)

@router.get("/fetch_hot_list")
async def fetch_hot_list(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取小红书热榜/Fetch Xiaohongshu hot list"""
    body = await request.json()
    return await proxy_request("xiaohongshu", "/api/v1/xiaohongshu/web_v2/fetch_hot_list", json_body=body)
