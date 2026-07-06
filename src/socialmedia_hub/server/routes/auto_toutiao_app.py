"""Auto-generated routes for Toutiao-App-API."""

from __future__ import annotations

from typing import Any

from fastapi import APIRouter, Depends, Request

from socialmedia_hub.server._core import proxy_request, verify_api_key

router = APIRouter(prefix="/api/v1/toutiao/app", tags=["toutiao_app"])

@router.get("/get_article_info")
async def get_article_info(
    group_id: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取指定文章的信息/Get information of specified article"""
    body = await request.json()
    params: dict[str, Any] = {}
    if group_id is not None:
        params["group_id"] = group_id
    return await proxy_request("toutiao", "/api/v1/toutiao/app/get_article_info", params=params, json_body=body)

@router.get("/get_video_info")
async def get_video_info(
    group_id: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取指定视频的信息/Get information of specified video"""
    body = await request.json()
    params: dict[str, Any] = {}
    if group_id is not None:
        params["group_id"] = group_id
    return await proxy_request("toutiao", "/api/v1/toutiao/app/get_video_info", params=params, json_body=body)

@router.get("/get_comments")
async def get_comments(
    group_id: str,
    offset: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取指定作品的评论/Get comments of specified post"""
    body = await request.json()
    params: dict[str, Any] = {}
    if group_id is not None:
        params["group_id"] = group_id
    if offset is not None:
        params["offset"] = offset
    return await proxy_request("toutiao", "/api/v1/toutiao/app/get_comments", params=params, json_body=body)

@router.get("/get_user_info")
async def get_user_info(
    user_id: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取指定用户的信息/Get information of specified user"""
    body = await request.json()
    params: dict[str, Any] = {}
    if user_id is not None:
        params["user_id"] = user_id
    return await proxy_request("toutiao", "/api/v1/toutiao/app/get_user_info", params=params, json_body=body)

@router.get("/get_user_id")
async def get_user_id(
    user_profile_url: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """从头条用户主页获取用户user_id/Get user_id from user profile"""
    body = await request.json()
    params: dict[str, Any] = {}
    if user_profile_url is not None:
        params["user_profile_url"] = user_profile_url
    return await proxy_request("toutiao", "/api/v1/toutiao/app/get_user_id", params=params, json_body=body)
