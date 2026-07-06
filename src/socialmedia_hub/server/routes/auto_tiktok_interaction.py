"""Auto-generated routes for TikTok-Interaction-API."""

from __future__ import annotations

from typing import Any

from fastapi import APIRouter, Depends, Request

from socialmedia_hub.server._core import proxy_request, verify_api_key

router = APIRouter(prefix="/api/v1/tiktok/interaction", tags=["tiktok_interaction"])

@router.get("/apply")
async def apply(
    api_key: str,
    invite_code: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """申请使用TikTok交互API权限（Scope）/Apply for TikTok Interaction API permission (Scope)"""
    params: dict[str, Any] = {}
    if api_key is not None:
        params["api_key"] = api_key
    if invite_code is not None:
        params["invite_code"] = invite_code
    return await proxy_request("tiktok", "/api/v1/tiktok/interaction/apply", params=params)

@router.post("/post_comment")
async def post_comment(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """发送评论/Post comment"""
    body = await request.json()
    return await proxy_request("tiktok", "/api/v1/tiktok/interaction/post_comment", json_body=body)

@router.post("/reply_comment")
async def reply_comment(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """回复评论/Reply to comment"""
    body = await request.json()
    return await proxy_request("tiktok", "/api/v1/tiktok/interaction/reply_comment", json_body=body)

@router.post("/like")
async def like(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """点赞/Like"""
    body = await request.json()
    return await proxy_request("tiktok", "/api/v1/tiktok/interaction/like", json_body=body)

@router.post("/follow")
async def follow(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """关注/Follow"""
    body = await request.json()
    return await proxy_request("tiktok", "/api/v1/tiktok/interaction/follow", json_body=body)

@router.post("/collect")
async def collect(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """收藏/Collect"""
    body = await request.json()
    return await proxy_request("tiktok", "/api/v1/tiktok/interaction/collect", json_body=body)

@router.post("/forward")
async def forward(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """转发/Forward"""
    body = await request.json()
    return await proxy_request("tiktok", "/api/v1/tiktok/interaction/forward", json_body=body)
