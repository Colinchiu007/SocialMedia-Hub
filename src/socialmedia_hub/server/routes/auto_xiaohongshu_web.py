"""Auto-generated routes for Xiaohongshu-Web-API."""

from __future__ import annotations

from typing import Any

from fastapi import APIRouter, Depends, Request

from socialmedia_hub.server._core import proxy_request, verify_api_key

router = APIRouter(prefix="/api/v1/xiaohongshu/web", tags=["xiaohongshu_web"])

@router.post("/get_home_recommend")
async def get_home_recommend(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取首页推荐/Get home recommend"""
    body = await request.json()
    return await proxy_request("xiaohongshu", "/api/v1/xiaohongshu/web/get_home_recommend", json_body=body)

@router.get("/get_note_info_v2")
async def get_note_info_v2(
    request: Request,
    note_id: str | None = None,
    share_text: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取笔记信息 V2/Get note info V2"""
    params: dict[str, Any] = {}
    if note_id is not None:
        params["note_id"] = note_id
    if share_text is not None:
        params["share_text"] = share_text
    return await proxy_request("xiaohongshu", "/api/v1/xiaohongshu/web/get_note_info_v2", params=params)

@router.get("/get_note_info_v4")
async def get_note_info_v4(
    request: Request,
    note_id: str | None = None,
    share_text: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取笔记信息 V4/Get note info V4"""
    params: dict[str, Any] = {}
    if note_id is not None:
        params["note_id"] = note_id
    if share_text is not None:
        params["share_text"] = share_text
    return await proxy_request("xiaohongshu", "/api/v1/xiaohongshu/web/get_note_info_v4", params=params)

@router.post("/get_note_info_v5")
async def get_note_info_v5(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取笔记信息 V5 (自带Cookie)/Get note info V5 (Self-provided Cookie)"""
    body = await request.json()
    return await proxy_request("xiaohongshu", "/api/v1/xiaohongshu/web/get_note_info_v5", json_body=body)

@router.get("/get_note_info_v7")
async def get_note_info_v7(
    request: Request,
    note_id: str | None = None,
    share_text: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取笔记信息 V7/Get note info V7"""
    params: dict[str, Any] = {}
    if note_id is not None:
        params["note_id"] = note_id
    if share_text is not None:
        params["share_text"] = share_text
    return await proxy_request("xiaohongshu", "/api/v1/xiaohongshu/web/get_note_info_v7", params=params)

@router.get("/get_note_comments")
async def get_note_comments(
    note_id: str,
    request: Request,
    lastCursor: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取笔记评论 V1/Get note comments V1"""
    params: dict[str, Any] = {}
    if note_id is not None:
        params["note_id"] = note_id
    if lastCursor is not None:
        params["lastCursor"] = lastCursor
    return await proxy_request("xiaohongshu", "/api/v1/xiaohongshu/web/get_note_comments", params=params)

@router.get("/get_note_comment_replies")
async def get_note_comment_replies(
    note_id: str,
    comment_id: str,
    request: Request,
    lastCursor: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取笔记评论回复 V1/Get note comment replies V1"""
    params: dict[str, Any] = {}
    if note_id is not None:
        params["note_id"] = note_id
    if comment_id is not None:
        params["comment_id"] = comment_id
    if lastCursor is not None:
        params["lastCursor"] = lastCursor
    return await proxy_request("xiaohongshu", "/api/v1/xiaohongshu/web/get_note_comment_replies", params=params)

@router.get("/get_user_info")
async def get_user_info(
    user_id: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户信息 V1/Get user info V1"""
    params: dict[str, Any] = {}
    if user_id is not None:
        params["user_id"] = user_id
    return await proxy_request("xiaohongshu", "/api/v1/xiaohongshu/web/get_user_info", params=params)

@router.get("/get_user_info_v2")
async def get_user_info_v2(
    request: Request,
    user_id: str | None = None,
    share_text: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户信息 V2/Get user info V2"""
    params: dict[str, Any] = {}
    if user_id is not None:
        params["user_id"] = user_id
    if share_text is not None:
        params["share_text"] = share_text
    return await proxy_request("xiaohongshu", "/api/v1/xiaohongshu/web/get_user_info_v2", params=params)

@router.get("/search_notes")
async def search_notes(
    keyword: str,
    request: Request,
    page: int | None = None,
    sort: str | None = None,
    noteType: str | None = None,
    noteTime: str | None = None,
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
    if noteType is not None:
        params["noteType"] = noteType
    if noteTime is not None:
        params["noteTime"] = noteTime
    return await proxy_request("xiaohongshu", "/api/v1/xiaohongshu/web/search_notes", params=params)

@router.get("/search_notes_v3")
async def search_notes_v3(
    keyword: str,
    request: Request,
    page: int | None = None,
    sort: str | None = None,
    noteType: str | None = None,
    noteTime: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """搜索笔记 V3/Search notes V3"""
    params: dict[str, Any] = {}
    if keyword is not None:
        params["keyword"] = keyword
    if page is not None:
        params["page"] = page
    if sort is not None:
        params["sort"] = sort
    if noteType is not None:
        params["noteType"] = noteType
    if noteTime is not None:
        params["noteTime"] = noteTime
    return await proxy_request("xiaohongshu", "/api/v1/xiaohongshu/web/search_notes_v3", params=params)

@router.get("/search_users")
async def search_users(
    keyword: str,
    request: Request,
    page: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """搜索用户/Search users"""
    params: dict[str, Any] = {}
    if keyword is not None:
        params["keyword"] = keyword
    if page is not None:
        params["page"] = page
    return await proxy_request("xiaohongshu", "/api/v1/xiaohongshu/web/search_users", params=params)

@router.get("/get_user_notes_v2")
async def get_user_notes_v2(
    user_id: str,
    request: Request,
    lastCursor: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户的笔记 V2/Get user notes V2"""
    params: dict[str, Any] = {}
    if user_id is not None:
        params["user_id"] = user_id
    if lastCursor is not None:
        params["lastCursor"] = lastCursor
    return await proxy_request("xiaohongshu", "/api/v1/xiaohongshu/web/get_user_notes_v2", params=params)

@router.get("/get_visitor_cookie")
async def get_visitor_cookie(
    request: Request,
    proxy: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取游客Cookie/Get visitor cookie"""
    params: dict[str, Any] = {}
    if proxy is not None:
        params["proxy"] = proxy
    return await proxy_request("xiaohongshu", "/api/v1/xiaohongshu/web/get_visitor_cookie", params=params)

@router.post("/sign")
async def sign(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """小红书Web签名/Xiaohongshu Web sign"""
    body = await request.json()
    return await proxy_request("xiaohongshu", "/api/v1/xiaohongshu/web/sign", json_body=body)

@router.get("/get_note_id_and_xsec_token")
async def get_note_id_and_xsec_token(
    share_text: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """通过分享链接获取小红书的Note ID 和 xsec_token/Get Xiaohongshu Note ID and xsec_token by share link"""
    params: dict[str, Any] = {}
    if share_text is not None:
        params["share_text"] = share_text
    return await proxy_request("xiaohongshu", "/api/v1/xiaohongshu/web/get_note_id_and_xsec_token", params=params)

@router.get("/get_product_info")
async def get_product_info(
    request: Request,
    share_text: str | None = None,
    item_id: str | None = None,
    xsec_token: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取小红书商品信息/Get Xiaohongshu product info"""
    params: dict[str, Any] = {}
    if share_text is not None:
        params["share_text"] = share_text
    if item_id is not None:
        params["item_id"] = item_id
    if xsec_token is not None:
        params["xsec_token"] = xsec_token
    return await proxy_request("xiaohongshu", "/api/v1/xiaohongshu/web/get_product_info", params=params)
