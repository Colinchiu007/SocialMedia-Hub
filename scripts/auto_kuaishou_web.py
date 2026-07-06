"""Auto-generated routes for Kuaishou-Web-API."""

from __future__ import annotations

from typing import Any

from fastapi import APIRouter, Depends, Request

from socialmedia_hub.server._core import proxy_request, verify_api_key

router = APIRouter(prefix="/api/v1/kuaishou/web", tags=["kuaishou_web"])

@router.get("/fetch_one_video")
async def fetch_one_video(
    share_text: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取单个作品数据 V1/Get single video data V1"""
        params: dict[str, Any] = {}
        if share_text is not None:
            params["share_text"] = share_text
        body = await request.json()
        return await proxy_request("kuaishou", "/api/v1/kuaishou/web/fetch_one_video", json_body=body)

@router.get("/fetch_one_video_v2")
async def fetch_one_video_v2(
    photo_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取单个作品数据 V2/Get single video data V2"""
        params: dict[str, Any] = {}
        if photo_id is not None:
            params["photo_id"] = photo_id
        body = await request.json()
        return await proxy_request("kuaishou", "/api/v1/kuaishou/web/fetch_one_video_v2", json_body=body)

@router.get("/fetch_one_video_by_url")
async def fetch_one_video_by_url(
    url: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """链接获取作品数据/Fetch single video by URL"""
        params: dict[str, Any] = {}
        if url is not None:
            params["url"] = url
        body = await request.json()
        return await proxy_request("kuaishou", "/api/v1/kuaishou/web/fetch_one_video_by_url", json_body=body)

@router.get("/fetch_one_video_comment")
async def fetch_one_video_comment(
    pcursor: str | None = None,
    photo_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取作品一级评论/Fetch video comments"""
        params: dict[str, Any] = {}
        if photo_id is not None:
            params["photo_id"] = photo_id
        if pcursor is not None:
            params["pcursor"] = pcursor
        body = await request.json()
        return await proxy_request("kuaishou", "/api/v1/kuaishou/web/fetch_one_video_comment", json_body=body)

@router.get("/fetch_one_video_sub_comment")
async def fetch_one_video_sub_comment(
    root_comment_id: str,
    pcursor: str | None = None,
    photo_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取作品二级评论/Fetch video sub comments"""
        params: dict[str, Any] = {}
        if photo_id is not None:
            params["photo_id"] = photo_id
        if pcursor is not None:
            params["pcursor"] = pcursor
        if root_comment_id is not None:
            params["root_comment_id"] = root_comment_id
        body = await request.json()
        return await proxy_request("kuaishou", "/api/v1/kuaishou/web/fetch_one_video_sub_comment", json_body=body)

@router.get("/generate_share_short_url")
async def generate_share_short_url(
    photo_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """生成分享短连接/Generate share short URL"""
        params: dict[str, Any] = {}
        if photo_id is not None:
            params["photo_id"] = photo_id
        body = await request.json()
        return await proxy_request("kuaishou", "/api/v1/kuaishou/web/generate_share_short_url", json_body=body)

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
        return await proxy_request("kuaishou", "/api/v1/kuaishou/web/fetch_user_info", json_body=body)

@router.get("/fetch_user_post")
async def fetch_user_post(
    pcursor: str | None = None,
    user_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户发布作品/Fetch user posts"""
        params: dict[str, Any] = {}
        if user_id is not None:
            params["user_id"] = user_id
        if pcursor is not None:
            params["pcursor"] = pcursor
        body = await request.json()
        return await proxy_request("kuaishou", "/api/v1/kuaishou/web/fetch_user_post", json_body=body)

@router.get("/fetch_user_live_replay")
async def fetch_user_live_replay(
    pcursor: str | None = None,
    user_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户直播回放/Fetch user live replay"""
        params: dict[str, Any] = {}
        if user_id is not None:
            params["user_id"] = user_id
        if pcursor is not None:
            params["pcursor"] = pcursor
        body = await request.json()
        return await proxy_request("kuaishou", "/api/v1/kuaishou/web/fetch_user_live_replay", json_body=body)

@router.get("/fetch_user_collect")
async def fetch_user_collect(
    pcursor: str | None = None,
    user_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户收藏作品/Fetch user collect"""
        params: dict[str, Any] = {}
        if user_id is not None:
            params["user_id"] = user_id
        if pcursor is not None:
            params["pcursor"] = pcursor
        body = await request.json()
        return await proxy_request("kuaishou", "/api/v1/kuaishou/web/fetch_user_collect", json_body=body)

@router.get("/fetch_kuaishou_hot_list_v1")
async def fetch_kuaishou_hot_list_v1(
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取快手热榜 V1/Fetch Kuaishou Hot List V1"""
        body = await request.json()
        return await proxy_request("kuaishou", "/api/v1/kuaishou/web/fetch_kuaishou_hot_list_v1", json_body=body)

@router.get("/fetch_kuaishou_hot_list_v2")
async def fetch_kuaishou_hot_list_v2(
    board_type: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取快手热榜 V2/Fetch Kuaishou Hot List V2"""
        params: dict[str, Any] = {}
        if board_type is not None:
            params["board_type"] = board_type
        body = await request.json()
        return await proxy_request("kuaishou", "/api/v1/kuaishou/web/fetch_kuaishou_hot_list_v2", json_body=body)

@router.get("/fetch_get_user_id")
async def fetch_get_user_id(
    share_link: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户ID/Fetch user ID"""
        params: dict[str, Any] = {}
        if share_link is not None:
            params["share_link"] = share_link
        body = await request.json()
        return await proxy_request("kuaishou", "/api/v1/kuaishou/web/fetch_get_user_id", json_body=body)
