"""Auto-generated routes for Douyin-Search-API."""

from __future__ import annotations

from typing import Any

from fastapi import APIRouter, Depends, Request

from socialmedia_hub.server._core import proxy_request, verify_api_key

router = APIRouter(prefix="/api/v1/douyin/search", tags=["douyin_search"])

@router.post("/fetch_general_search_v1")
async def fetch_general_search_v1(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取综合搜索 V1/Fetch general search V1"""
    body = await request.json()
    return await proxy_request("douyin", "/api/v1/douyin/search/fetch_general_search_v1", json_body=body)

@router.post("/fetch_general_search_v2")
async def fetch_general_search_v2(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取综合搜索 V2/Fetch general search V2"""
    body = await request.json()
    return await proxy_request("douyin", "/api/v1/douyin/search/fetch_general_search_v2", json_body=body)

@router.post("/fetch_search_suggest")
async def fetch_search_suggest(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取搜索关键词推荐/Fetch search keyword suggestions"""
    body = await request.json()
    return await proxy_request("douyin", "/api/v1/douyin/search/fetch_search_suggest", json_body=body)

@router.post("/fetch_video_search_v1")
async def fetch_video_search_v1(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取视频搜索 V1/Fetch video search V1"""
    body = await request.json()
    return await proxy_request("douyin", "/api/v1/douyin/search/fetch_video_search_v1", json_body=body)

@router.post("/fetch_video_search_v2")
async def fetch_video_search_v2(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取视频搜索 V2/Fetch video search V2"""
    body = await request.json()
    return await proxy_request("douyin", "/api/v1/douyin/search/fetch_video_search_v2", json_body=body)

@router.post("/fetch_multi_search")
async def fetch_multi_search(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取多重搜索/Fetch multi-type search"""
    body = await request.json()
    return await proxy_request("douyin", "/api/v1/douyin/search/fetch_multi_search", json_body=body)

@router.post("/fetch_user_search")
async def fetch_user_search(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户搜索/Fetch user search"""
    body = await request.json()
    return await proxy_request("douyin", "/api/v1/douyin/search/fetch_user_search", json_body=body)

@router.post("/fetch_user_search_v2")
async def fetch_user_search_v2(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户搜索 V2/Fetch user search V2"""
    body = await request.json()
    return await proxy_request("douyin", "/api/v1/douyin/search/fetch_user_search_v2", json_body=body)

@router.post("/fetch_image_search")
async def fetch_image_search(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取图片搜索/Fetch image search"""
    body = await request.json()
    return await proxy_request("douyin", "/api/v1/douyin/search/fetch_image_search", json_body=body)

@router.post("/fetch_image_search_v3")
async def fetch_image_search_v3(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取图文搜索 V3/Fetch image-text search V3"""
    body = await request.json()
    return await proxy_request("douyin", "/api/v1/douyin/search/fetch_image_search_v3", json_body=body)

@router.post("/fetch_live_search_v1")
async def fetch_live_search_v1(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取直播搜索 V1/Fetch live search V1"""
    body = await request.json()
    return await proxy_request("douyin", "/api/v1/douyin/search/fetch_live_search_v1", json_body=body)

@router.post("/fetch_challenge_search_v1")
async def fetch_challenge_search_v1(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取话题搜索 V1/Fetch hashtag search V1"""
    body = await request.json()
    return await proxy_request("douyin", "/api/v1/douyin/search/fetch_challenge_search_v1", json_body=body)

@router.post("/fetch_challenge_search_v2")
async def fetch_challenge_search_v2(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取话题搜索 V2/Fetch hashtag search V2"""
    body = await request.json()
    return await proxy_request("douyin", "/api/v1/douyin/search/fetch_challenge_search_v2", json_body=body)

@router.post("/fetch_challenge_suggest")
async def fetch_challenge_suggest(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取话题推荐搜索/Fetch hashtag suggestions"""
    body = await request.json()
    return await proxy_request("douyin", "/api/v1/douyin/search/fetch_challenge_suggest", json_body=body)

@router.post("/fetch_experience_search")
async def fetch_experience_search(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取经验搜索/Fetch experience search"""
    body = await request.json()
    return await proxy_request("douyin", "/api/v1/douyin/search/fetch_experience_search", json_body=body)

@router.post("/fetch_music_search")
async def fetch_music_search(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取音乐搜索/Fetch music search"""
    body = await request.json()
    return await proxy_request("douyin", "/api/v1/douyin/search/fetch_music_search", json_body=body)

@router.post("/fetch_discuss_search")
async def fetch_discuss_search(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取讨论搜索/Fetch discussion search"""
    body = await request.json()
    return await proxy_request("douyin", "/api/v1/douyin/search/fetch_discuss_search", json_body=body)

@router.post("/fetch_school_search")
async def fetch_school_search(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取学校搜索/Fetch school search"""
    body = await request.json()
    return await proxy_request("douyin", "/api/v1/douyin/search/fetch_school_search", json_body=body)

@router.post("/fetch_vision_search")
async def fetch_vision_search(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取图像识别搜索/Fetch vision search (image-based search)"""
    body = await request.json()
    return await proxy_request("douyin", "/api/v1/douyin/search/fetch_vision_search", json_body=body)
