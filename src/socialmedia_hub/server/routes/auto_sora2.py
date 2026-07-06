"""Auto-generated routes for Sora2-API."""

from __future__ import annotations

from typing import Any

from fastapi import APIRouter, Depends, Request

from socialmedia_hub.server._core import proxy_request, verify_api_key

router = APIRouter(prefix="/api/v1/sora2", tags=["sora2"])

@router.get("/get_post_detail")
async def get_post_detail(
    request: Request,
    post_id: str | None = None,
    post_url: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取单一作品详情/Fetch single post detail"""
    params: dict[str, Any] = {}
    if post_id is not None:
        params["post_id"] = post_id
    if post_url is not None:
        params["post_url"] = post_url
    return await proxy_request("sora2", "/api/v1/sora2/get_post_detail", params=params)

@router.get("/get_post_remix_list")
async def get_post_remix_list(
    request: Request,
    post_id: str | None = None,
    post_url: str | None = None,
    cursor: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取作品的 Remix 列表/Fetch post remix list"""
    params: dict[str, Any] = {}
    if post_id is not None:
        params["post_id"] = post_id
    if post_url is not None:
        params["post_url"] = post_url
    if cursor is not None:
        params["cursor"] = cursor
    return await proxy_request("sora2", "/api/v1/sora2/get_post_remix_list", params=params)

@router.get("/get_video_download_info")
async def get_video_download_info(
    request: Request,
    post_id: str | None = None,
    post_url: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取无水印视频下载信息/Fetch none watermark video download info"""
    params: dict[str, Any] = {}
    if post_id is not None:
        params["post_id"] = post_id
    if post_url is not None:
        params["post_url"] = post_url
    return await proxy_request("sora2", "/api/v1/sora2/get_video_download_info", params=params)

@router.get("/get_post_comments")
async def get_post_comments(
    post_id: str,
    request: Request,
    cursor: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取作品一级评论/Fetch post comments"""
    params: dict[str, Any] = {}
    if post_id is not None:
        params["post_id"] = post_id
    if cursor is not None:
        params["cursor"] = cursor
    return await proxy_request("sora2", "/api/v1/sora2/get_post_comments", params=params)

@router.get("/get_comment_replies")
async def get_comment_replies(
    comment_id: str,
    request: Request,
    cursor: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取评论的回复/Fetch comment replies"""
    params: dict[str, Any] = {}
    if comment_id is not None:
        params["comment_id"] = comment_id
    if cursor is not None:
        params["cursor"] = cursor
    return await proxy_request("sora2", "/api/v1/sora2/get_comment_replies", params=params)

@router.get("/get_user_profile")
async def get_user_profile(
    user_id: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户信息档案/Fetch user profile"""
    params: dict[str, Any] = {}
    if user_id is not None:
        params["user_id"] = user_id
    return await proxy_request("sora2", "/api/v1/sora2/get_user_profile", params=params)

@router.get("/get_user_posts")
async def get_user_posts(
    user_id: str,
    request: Request,
    cursor: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户发布的帖子列表/Fetch user posts"""
    params: dict[str, Any] = {}
    if user_id is not None:
        params["user_id"] = user_id
    if cursor is not None:
        params["cursor"] = cursor
    return await proxy_request("sora2", "/api/v1/sora2/get_user_posts", params=params)

@router.get("/get_cameo_leaderboard")
async def get_cameo_leaderboard(
    request: Request,
    cursor: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取 Cameo 出镜秀达人排行榜/Fetch Cameo leaderboard"""
    params: dict[str, Any] = {}
    if cursor is not None:
        params["cursor"] = cursor
    return await proxy_request("sora2", "/api/v1/sora2/get_cameo_leaderboard", params=params)

@router.get("/get_user_cameo_appearances")
async def get_user_cameo_appearances(
    user_id: str,
    request: Request,
    cursor: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户Cameo出镜秀列表/Fetch user cameo appearances"""
    params: dict[str, Any] = {}
    if user_id is not None:
        params["user_id"] = user_id
    if cursor is not None:
        params["cursor"] = cursor
    return await proxy_request("sora2", "/api/v1/sora2/get_user_cameo_appearances", params=params)

@router.get("/get_user_followers")
async def get_user_followers(
    user_id: str,
    request: Request,
    cursor: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户粉丝列表/Fetch user followers"""
    params: dict[str, Any] = {}
    if user_id is not None:
        params["user_id"] = user_id
    if cursor is not None:
        params["cursor"] = cursor
    return await proxy_request("sora2", "/api/v1/sora2/get_user_followers", params=params)

@router.get("/get_user_following")
async def get_user_following(
    user_id: str,
    request: Request,
    cursor: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户关注列表/Fetch user following"""
    params: dict[str, Any] = {}
    if user_id is not None:
        params["user_id"] = user_id
    if cursor is not None:
        params["cursor"] = cursor
    return await proxy_request("sora2", "/api/v1/sora2/get_user_following", params=params)

@router.get("/get_feed")
async def get_feed(
    request: Request,
    cursor: str | None = None,
    eager_views: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取Feed流（热门/推荐视频）/Fetch feed"""
    params: dict[str, Any] = {}
    if cursor is not None:
        params["cursor"] = cursor
    if eager_views is not None:
        params["eager_views"] = eager_views
    return await proxy_request("sora2", "/api/v1/sora2/get_feed", params=params)

@router.get("/search_users")
async def search_users(
    username: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """搜索用户/Search users"""
    params: dict[str, Any] = {}
    if username is not None:
        params["username"] = username
    return await proxy_request("sora2", "/api/v1/sora2/search_users", params=params)

@router.post("/upload_image")
async def upload_image(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """上传图片获取media_id/Upload image to get media_id"""
    body = await request.json()
    return await proxy_request("sora2", "/api/v1/sora2/upload_image", json_body=body)

@router.post("/create_video")
async def create_video(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """[已弃用/Deprecated] 文本/图片生成视频/Create video from text or image"""
    body = await request.json()
    return await proxy_request("sora2", "/api/v1/sora2/create_video", json_body=body)

@router.get("/get_task_status")
async def get_task_status(
    task_id: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """[已弃用/Deprecated] 查询任务状态/Get task status"""
    params: dict[str, Any] = {}
    if task_id is not None:
        params["task_id"] = task_id
    return await proxy_request("sora2", "/api/v1/sora2/get_task_status", params=params)

@router.get("/get_task_detail")
async def get_task_detail(
    request: Request,
    task_id: str | None = None,
    generation_id: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """[已弃用/Deprecated] 获取任务生成的作品详情（无水印版本）/Get task-generated post detail (watermark-free)"""
    params: dict[str, Any] = {}
    if task_id is not None:
        params["task_id"] = task_id
    if generation_id is not None:
        params["generation_id"] = generation_id
    return await proxy_request("sora2", "/api/v1/sora2/get_task_detail", params=params)
