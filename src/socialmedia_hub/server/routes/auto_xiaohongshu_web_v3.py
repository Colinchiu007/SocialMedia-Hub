"""Auto-generated routes for Xiaohongshu-Web-V3-API."""

from __future__ import annotations

from typing import Any

from fastapi import APIRouter, Depends, Request

from socialmedia_hub.server._core import proxy_request, verify_api_key

router = APIRouter(prefix="/api/v1/xiaohongshu/web/v3", tags=["xiaohongshu_web_v3"])

@router.get("/fetch_note_detail")
async def fetch_note_detail(
    note_id: str,
    request: Request,
    xsec_token: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取笔记详情/Fetch note detail"""
    body = await request.json()
    params: dict[str, Any] = {}
    if note_id is not None:
        params["note_id"] = note_id
    if xsec_token is not None:
        params["xsec_token"] = xsec_token
    return await proxy_request("xiaohongshu", "/api/v1/xiaohongshu/web_v3/fetch_note_detail", params=params, json_body=body)

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
    return await proxy_request("xiaohongshu", "/api/v1/xiaohongshu/web_v3/fetch_note_comments", params=params, json_body=body)

@router.get("/fetch_sub_comments")
async def fetch_sub_comments(
    note_id: str,
    root_comment_id: str,
    request: Request,
    num: int | None = None,
    cursor: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取子评论/Fetch sub comments"""
    body = await request.json()
    params: dict[str, Any] = {}
    if note_id is not None:
        params["note_id"] = note_id
    if root_comment_id is not None:
        params["root_comment_id"] = root_comment_id
    if num is not None:
        params["num"] = num
    if cursor is not None:
        params["cursor"] = cursor
    return await proxy_request("xiaohongshu", "/api/v1/xiaohongshu/web_v3/fetch_sub_comments", params=params, json_body=body)

@router.get("/fetch_search_notes")
async def fetch_search_notes(
    keyword: str,
    request: Request,
    page: int | None = None,
    sort: str | None = None,
    note_type: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """搜索笔记/Search notes"""
    body = await request.json()
    params: dict[str, Any] = {}
    if keyword is not None:
        params["keyword"] = keyword
    if page is not None:
        params["page"] = page
    if sort is not None:
        params["sort"] = sort
    if note_type is not None:
        params["note_type"] = note_type
    return await proxy_request("xiaohongshu", "/api/v1/xiaohongshu/web_v3/fetch_search_notes", params=params, json_body=body)

@router.get("/fetch_search_users")
async def fetch_search_users(
    keyword: str,
    request: Request,
    page: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """搜索用户/Search users"""
    body = await request.json()
    params: dict[str, Any] = {}
    if keyword is not None:
        params["keyword"] = keyword
    if page is not None:
        params["page"] = page
    return await proxy_request("xiaohongshu", "/api/v1/xiaohongshu/web_v3/fetch_search_users", params=params, json_body=body)

@router.get("/fetch_trending")
async def fetch_trending(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取热搜词/Fetch trending keywords"""
    body = await request.json()
    return await proxy_request("xiaohongshu", "/api/v1/xiaohongshu/web_v3/fetch_trending", json_body=body)

@router.get("/fetch_search_suggest")
async def fetch_search_suggest(
    request: Request,
    keyword: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取搜索联想词/Fetch search suggestions"""
    body = await request.json()
    params: dict[str, Any] = {}
    if keyword is not None:
        params["keyword"] = keyword
    return await proxy_request("xiaohongshu", "/api/v1/xiaohongshu/web_v3/fetch_search_suggest", params=params, json_body=body)

@router.get("/fetch_homefeed")
async def fetch_homefeed(
    request: Request,
    num: int | None = None,
    cursor_score: str | None = None,
    category: str | None = None,
    need_filter_image: bool | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取首页推荐/Fetch homepage feed"""
    body = await request.json()
    params: dict[str, Any] = {}
    if num is not None:
        params["num"] = num
    if cursor_score is not None:
        params["cursor_score"] = cursor_score
    if category is not None:
        params["category"] = category
    if need_filter_image is not None:
        params["need_filter_image"] = need_filter_image
    return await proxy_request("xiaohongshu", "/api/v1/xiaohongshu/web_v3/fetch_homefeed", params=params, json_body=body)

@router.get("/fetch_homefeed_categories")
async def fetch_homefeed_categories(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取首页分类列表/Fetch homepage categories"""
    body = await request.json()
    return await proxy_request("xiaohongshu", "/api/v1/xiaohongshu/web_v3/fetch_homefeed_categories", json_body=body)

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
    return await proxy_request("xiaohongshu", "/api/v1/xiaohongshu/web_v3/fetch_user_info", params=params, json_body=body)

@router.get("/fetch_user_notes")
async def fetch_user_notes(
    user_id: str,
    request: Request,
    cursor: str | None = None,
    num: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户笔记列表/Fetch user notes"""
    body = await request.json()
    params: dict[str, Any] = {}
    if user_id is not None:
        params["user_id"] = user_id
    if cursor is not None:
        params["cursor"] = cursor
    if num is not None:
        params["num"] = num
    return await proxy_request("xiaohongshu", "/api/v1/xiaohongshu/web_v3/fetch_user_notes", params=params, json_body=body)
