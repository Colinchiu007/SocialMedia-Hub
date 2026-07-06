"""Auto-generated routes for Xiaohongshu-App-API."""

from __future__ import annotations

from typing import Any

from fastapi import APIRouter, Depends, Request

from socialmedia_hub.server._core import proxy_request, verify_api_key

router = APIRouter(prefix="/api/v1/xiaohongshu/app", tags=["xiaohongshu_app"])

@router.get("/get_note_info")
async def get_note_info(
    share_text: str | None = None,
    note_id: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取笔记信息 V1/Get note info V1"""
        params: dict[str, Any] = {}
        if note_id is not None:
            params["note_id"] = note_id
        if share_text is not None:
            params["share_text"] = share_text
        body = await request.json()
        return await proxy_request("xiaohongshu", "/api/v1/xiaohongshu/app/get_note_info", json_body=body)

@router.get("/get_note_info_v2")
async def get_note_info_v2(
    share_text: str | None = None,
    note_id: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取笔记信息 V2 (蒲公英商家后台)/Get note info V2 (Pugongying Business Backend)"""
        params: dict[str, Any] = {}
        if note_id is not None:
            params["note_id"] = note_id
        if share_text is not None:
            params["share_text"] = share_text
        body = await request.json()
        return await proxy_request("xiaohongshu", "/api/v1/xiaohongshu/app/get_note_info_v2", json_body=body)

@router.get("/get_note_comments")
async def get_note_comments(
    sort_strategy: int | None = None,
    start: str | None = None,
    note_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取笔记评论/Get note comments"""
        params: dict[str, Any] = {}
        if note_id is not None:
            params["note_id"] = note_id
        if start is not None:
            params["start"] = start
        if sort_strategy is not None:
            params["sort_strategy"] = sort_strategy
        body = await request.json()
        return await proxy_request("xiaohongshu", "/api/v1/xiaohongshu/app/get_note_comments", json_body=body)

@router.get("/get_sub_comments")
async def get_sub_comments(
    start: str | None = None,
    comment_id: str,
    note_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取子评论/Get sub comments"""
        params: dict[str, Any] = {}
        if note_id is not None:
            params["note_id"] = note_id
        if comment_id is not None:
            params["comment_id"] = comment_id
        if start is not None:
            params["start"] = start
        body = await request.json()
        return await proxy_request("xiaohongshu", "/api/v1/xiaohongshu/app/get_sub_comments", json_body=body)

@router.get("/get_notes_by_topic")
async def get_notes_by_topic(
    cursor_score: str | None = None,
    last_note_id: str | None = None,
    last_note_ct: str | None = None,
    session_id: str | None = None,
    sort: str | None = None,
    first_load_time: str,
    page_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """[已弃用/Deprecated] 根据话题标签获取作品/Get notes by topic"""
        params: dict[str, Any] = {}
        if page_id is not None:
            params["page_id"] = page_id
        if first_load_time is not None:
            params["first_load_time"] = first_load_time
        if sort is not None:
            params["sort"] = sort
        if session_id is not None:
            params["session_id"] = session_id
        if last_note_ct is not None:
            params["last_note_ct"] = last_note_ct
        if last_note_id is not None:
            params["last_note_id"] = last_note_id
        if cursor_score is not None:
            params["cursor_score"] = cursor_score
        body = await request.json()
        return await proxy_request("xiaohongshu", "/api/v1/xiaohongshu/app/get_notes_by_topic", json_body=body)

@router.get("/search_notes")
async def search_notes(
    filter_note_time: str | None = None,
    filter_note_type: str | None = None,
    sort_type: str | None = None,
    session_id: str | None = None,
    search_id: str | None = None,
    page: int,
    keyword: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """搜索笔记/Search notes"""
        params: dict[str, Any] = {}
        if keyword is not None:
            params["keyword"] = keyword
        if page is not None:
            params["page"] = page
        if search_id is not None:
            params["search_id"] = search_id
        if session_id is not None:
            params["session_id"] = session_id
        if sort_type is not None:
            params["sort_type"] = sort_type
        if filter_note_type is not None:
            params["filter_note_type"] = filter_note_type
        if filter_note_time is not None:
            params["filter_note_time"] = filter_note_time
        body = await request.json()
        return await proxy_request("xiaohongshu", "/api/v1/xiaohongshu/app/search_notes", json_body=body)

@router.get("/get_user_info")
async def get_user_info(
    user_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户信息/Get user info"""
        params: dict[str, Any] = {}
        if user_id is not None:
            params["user_id"] = user_id
        body = await request.json()
        return await proxy_request("xiaohongshu", "/api/v1/xiaohongshu/app/get_user_info", json_body=body)

@router.get("/get_user_notes")
async def get_user_notes(
    cursor: str | None = None,
    user_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户作品列表/Get user notes"""
        params: dict[str, Any] = {}
        if user_id is not None:
            params["user_id"] = user_id
        if cursor is not None:
            params["cursor"] = cursor
        body = await request.json()
        return await proxy_request("xiaohongshu", "/api/v1/xiaohongshu/app/get_user_notes", json_body=body)

@router.get("/extract_share_info")
async def extract_share_info(
    share_link: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """提取分享链接信息/Extract share link info"""
        params: dict[str, Any] = {}
        if share_link is not None:
            params["share_link"] = share_link
        body = await request.json()
        return await proxy_request("xiaohongshu", "/api/v1/xiaohongshu/app/extract_share_info", json_body=body)

@router.get("/get_user_id_and_xsec_token")
async def get_user_id_and_xsec_token(
    share_link: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """从分享链接中提取用户ID和xsec_token/Extract user ID and xsec_token from share link"""
        params: dict[str, Any] = {}
        if share_link is not None:
            params["share_link"] = share_link
        body = await request.json()
        return await proxy_request("xiaohongshu", "/api/v1/xiaohongshu/app/get_user_id_and_xsec_token", json_body=body)

@router.get("/get_product_detail")
async def get_product_detail(
    sku_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取商品详情/Get product detail"""
        params: dict[str, Any] = {}
        if sku_id is not None:
            params["sku_id"] = sku_id
        body = await request.json()
        return await proxy_request("xiaohongshu", "/api/v1/xiaohongshu/app/get_product_detail", json_body=body)

@router.get("/search_products")
async def search_products(
    super_promotion: str | None = None,
    max_price: str | None = None,
    min_price: str | None = None,
    service_guarantee: str | None = None,
    scope: str | None = None,
    sort: str | None = None,
    session_id: str | None = None,
    search_id: str | None = None,
    page: int,
    keyword: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """搜索商品/Search products"""
        params: dict[str, Any] = {}
        if keyword is not None:
            params["keyword"] = keyword
        if page is not None:
            params["page"] = page
        if search_id is not None:
            params["search_id"] = search_id
        if session_id is not None:
            params["session_id"] = session_id
        if sort is not None:
            params["sort"] = sort
        if scope is not None:
            params["scope"] = scope
        if service_guarantee is not None:
            params["service_guarantee"] = service_guarantee
        if min_price is not None:
            params["min_price"] = min_price
        if max_price is not None:
            params["max_price"] = max_price
        if super_promotion is not None:
            params["super_promotion"] = super_promotion
        body = await request.json()
        return await proxy_request("xiaohongshu", "/api/v1/xiaohongshu/app/search_products", json_body=body)
