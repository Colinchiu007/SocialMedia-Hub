"""Auto-generated routes for Kuaishou-Web-API."""

from __future__ import annotations

from typing import Any

from fastapi import APIRouter, Depends, Request

from socialmedia_hub.server._core import proxy_request, verify_api_key

router = APIRouter(prefix="/api/v1/kuaishou/web", tags=["kuaishou_web"])

@router.get("/fetch_one_video")
async def fetch_one_video(
    share_text: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取单个作品数据 V1/Get single video data V1"""
    body = await request.json()
    params: dict[str, Any] = {}
    if share_text is not None:
        params["share_text"] = share_text
    return await proxy_request("kuaishou", "/api/v1/kuaishou/web/fetch_one_video", params=params, json_body=body)

@router.get("/fetch_one_video_v2")
async def fetch_one_video_v2(
    photo_id: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取单个作品数据 V2/Get single video data V2"""
    body = await request.json()
    params: dict[str, Any] = {}
    if photo_id is not None:
        params["photo_id"] = photo_id
    return await proxy_request("kuaishou", "/api/v1/kuaishou/web/fetch_one_video_v2", params=params, json_body=body)

@router.get("/fetch_one_video_by_url")
async def fetch_one_video_by_url(
    url: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """链接获取作品数据/Fetch single video by URL"""
    body = await request.json()
    params: dict[str, Any] = {}
    if url is not None:
        params["url"] = url
    return await proxy_request("kuaishou", "/api/v1/kuaishou/web/fetch_one_video_by_url", params=params, json_body=body)

@router.get("/fetch_one_video_comment")
async def fetch_one_video_comment(
    photo_id: str,
    request: Request,
    pcursor: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取作品一级评论/Fetch video comments"""
    body = await request.json()
    params: dict[str, Any] = {}
    if photo_id is not None:
        params["photo_id"] = photo_id
    if pcursor is not None:
        params["pcursor"] = pcursor
    return await proxy_request("kuaishou", "/api/v1/kuaishou/web/fetch_one_video_comment", params=params, json_body=body)

@router.get("/fetch_one_video_sub_comment")
async def fetch_one_video_sub_comment(
    photo_id: str,
    root_comment_id: str,
    request: Request,
    pcursor: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取作品二级评论/Fetch video sub comments"""
    body = await request.json()
    params: dict[str, Any] = {}
    if photo_id is not None:
        params["photo_id"] = photo_id
    if pcursor is not None:
        params["pcursor"] = pcursor
    if root_comment_id is not None:
        params["root_comment_id"] = root_comment_id
    return await proxy_request("kuaishou", "/api/v1/kuaishou/web/fetch_one_video_sub_comment", params=params, json_body=body)

@router.get("/generate_share_short_url")
async def generate_share_short_url(
    photo_id: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """生成分享短连接/Generate share short URL"""
    body = await request.json()
    params: dict[str, Any] = {}
    if photo_id is not None:
        params["photo_id"] = photo_id
    return await proxy_request("kuaishou", "/api/v1/kuaishou/web/generate_share_short_url", params=params, json_body=body)

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
    return await proxy_request("kuaishou", "/api/v1/kuaishou/web/fetch_user_info", params=params, json_body=body)

@router.get("/fetch_user_post")
async def fetch_user_post(
    user_id: str,
    request: Request,
    pcursor: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户发布作品/Fetch user posts"""
    body = await request.json()
    params: dict[str, Any] = {}
    if user_id is not None:
        params["user_id"] = user_id
    if pcursor is not None:
        params["pcursor"] = pcursor
    return await proxy_request("kuaishou", "/api/v1/kuaishou/web/fetch_user_post", params=params, json_body=body)

@router.get("/fetch_user_live_replay")
async def fetch_user_live_replay(
    user_id: str,
    request: Request,
    pcursor: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户直播回放/Fetch user live replay"""
    body = await request.json()
    params: dict[str, Any] = {}
    if user_id is not None:
        params["user_id"] = user_id
    if pcursor is not None:
        params["pcursor"] = pcursor
    return await proxy_request("kuaishou", "/api/v1/kuaishou/web/fetch_user_live_replay", params=params, json_body=body)

@router.get("/fetch_user_collect")
async def fetch_user_collect(
    user_id: str,
    request: Request,
    pcursor: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户收藏作品/Fetch user collect"""
    body = await request.json()
    params: dict[str, Any] = {}
    if user_id is not None:
        params["user_id"] = user_id
    if pcursor is not None:
        params["pcursor"] = pcursor
    return await proxy_request("kuaishou", "/api/v1/kuaishou/web/fetch_user_collect", params=params, json_body=body)

@router.get("/fetch_kuaishou_hot_list_v1")
async def fetch_kuaishou_hot_list_v1(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取快手热榜 V1/Fetch Kuaishou Hot List V1"""
    body = await request.json()
    return await proxy_request("kuaishou", "/api/v1/kuaishou/web/fetch_kuaishou_hot_list_v1", json_body=body)

@router.get("/fetch_kuaishou_hot_list_v2")
async def fetch_kuaishou_hot_list_v2(
    request: Request,
    board_type: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取快手热榜 V2/Fetch Kuaishou Hot List V2"""
    body = await request.json()
    params: dict[str, Any] = {}
    if board_type is not None:
        params["board_type"] = board_type
    return await proxy_request("kuaishou", "/api/v1/kuaishou/web/fetch_kuaishou_hot_list_v2", params=params, json_body=body)

@router.get("/fetch_get_user_id")
async def fetch_get_user_id(
    share_link: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户ID/Fetch user ID"""
    body = await request.json()
    params: dict[str, Any] = {}
    if share_link is not None:
        params["share_link"] = share_link
    return await proxy_request("kuaishou", "/api/v1/kuaishou/web/fetch_get_user_id", params=params, json_body=body)
