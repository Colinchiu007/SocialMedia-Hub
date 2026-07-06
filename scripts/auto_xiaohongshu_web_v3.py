"""Auto-generated routes for Xiaohongshu-Web-V3-API."""

from __future__ import annotations

from typing import Any

from fastapi import APIRouter, Depends, Request

from socialmedia_hub.server._core import proxy_request, verify_api_key

router = APIRouter(prefix="/api/v1/xiaohongshu/web/v3", tags=["xiaohongshu_web_v3"])

@router.get("/fetch_note_detail")
async def fetch_note_detail(
    xsec_token: str | None = None,
    note_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取笔记详情/Fetch note detail"""
        params: dict[str, Any] = {}
        if note_id is not None:
            params["note_id"] = note_id
        if xsec_token is not None:
            params["xsec_token"] = xsec_token
        body = await request.json()
        return await proxy_request("xiaohongshu", "/api/v1/xiaohongshu/web_v3/fetch_note_detail", json_body=body)

@router.get("/fetch_note_comments")
async def fetch_note_comments(
    cursor: str | None = None,
    note_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取笔记评论/Fetch note comments"""
        params: dict[str, Any] = {}
        if note_id is not None:
            params["note_id"] = note_id
        if cursor is not None:
            params["cursor"] = cursor
        body = await request.json()
        return await proxy_request("xiaohongshu", "/api/v1/xiaohongshu/web_v3/fetch_note_comments", json_body=body)

@router.get("/fetch_sub_comments")
async def fetch_sub_comments(
    cursor: str | None = None,
    num: int | None = None,
    root_comment_id: str,
    note_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取子评论/Fetch sub comments"""
        params: dict[str, Any] = {}
        if note_id is not None:
            params["note_id"] = note_id
        if root_comment_id is not None:
            params["root_comment_id"] = root_comment_id
        if num is not None:
            params["num"] = num
        if cursor is not None:
            params["cursor"] = cursor
        body = await request.json()
        return await proxy_request("xiaohongshu", "/api/v1/xiaohongshu/web_v3/fetch_sub_comments", json_body=body)

@router.get("/fetch_search_notes")
async def fetch_search_notes(
    note_type: int | None = None,
    sort: str | None = None,
    page: int | None = None,
    keyword: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """搜索笔记/Search notes"""
        params: dict[str, Any] = {}
        if keyword is not None:
            params["keyword"] = keyword
        if page is not None:
            params["page"] = page
        if sort is not None:
            params["sort"] = sort
        if note_type is not None:
            params["note_type"] = note_type
        body = await request.json()
        return await proxy_request("xiaohongshu", "/api/v1/xiaohongshu/web_v3/fetch_search_notes", json_body=body)

@router.get("/fetch_search_users")
async def fetch_search_users(
    page: int | None = None,
    keyword: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """搜索用户/Search users"""
        params: dict[str, Any] = {}
        if keyword is not None:
            params["keyword"] = keyword
        if page is not None:
            params["page"] = page
        body = await request.json()
        return await proxy_request("xiaohongshu", "/api/v1/xiaohongshu/web_v3/fetch_search_users", json_body=body)

@router.get("/fetch_trending")
async def fetch_trending(
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取热搜词/Fetch trending keywords"""
        body = await request.json()
        return await proxy_request("xiaohongshu", "/api/v1/xiaohongshu/web_v3/fetch_trending", json_body=body)

@router.get("/fetch_search_suggest")
async def fetch_search_suggest(
    keyword: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取搜索联想词/Fetch search suggestions"""
        params: dict[str, Any] = {}
        if keyword is not None:
            params["keyword"] = keyword
        body = await request.json()
        return await proxy_request("xiaohongshu", "/api/v1/xiaohongshu/web_v3/fetch_search_suggest", json_body=body)

@router.get("/fetch_homefeed")
async def fetch_homefeed(
    need_filter_image: bool | None = None,
    category: str | None = None,
    cursor_score: str | None = None,
    num: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取首页推荐/Fetch homepage feed"""
        params: dict[str, Any] = {}
        if num is not None:
            params["num"] = num
        if cursor_score is not None:
            params["cursor_score"] = cursor_score
        if category is not None:
            params["category"] = category
        if need_filter_image is not None:
            params["need_filter_image"] = need_filter_image
        body = await request.json()
        return await proxy_request("xiaohongshu", "/api/v1/xiaohongshu/web_v3/fetch_homefeed", json_body=body)

@router.get("/fetch_homefeed_categories")
async def fetch_homefeed_categories(
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取首页分类列表/Fetch homepage categories"""
        body = await request.json()
        return await proxy_request("xiaohongshu", "/api/v1/xiaohongshu/web_v3/fetch_homefeed_categories", json_body=body)

@router.get("/fetch_user_info")
async def fetch_user_info(
    user_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户信息/Fetch user info"""
        params: dict[str, Any] = {}
        if user_id is not None:
            params["user_id"] = user_id
        body = await request.json()
        return await proxy_request("xiaohongshu", "/api/v1/xiaohongshu/web_v3/fetch_user_info", json_body=body)

@router.get("/fetch_user_notes")
async def fetch_user_notes(
    num: int | None = None,
    cursor: str | None = None,
    user_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户笔记列表/Fetch user notes"""
        params: dict[str, Any] = {}
        if user_id is not None:
            params["user_id"] = user_id
        if cursor is not None:
            params["cursor"] = cursor
        if num is not None:
            params["num"] = num
        body = await request.json()
        return await proxy_request("xiaohongshu", "/api/v1/xiaohongshu/web_v3/fetch_user_notes", json_body=body)
