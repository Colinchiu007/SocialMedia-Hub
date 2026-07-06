"""Auto-generated routes for Sora2-API."""

from __future__ import annotations

from typing import Any

from fastapi import APIRouter, Depends, Request

from socialmedia_hub.server._core import proxy_request, verify_api_key

router = APIRouter(prefix="/api/v1/sora2", tags=["sora2"])

@router.get("/get_post_detail")
async def get_post_detail(
    post_url: str | None = None,
    post_id: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取单一作品详情/Fetch single post detail"""
        params: dict[str, Any] = {}
        if post_id is not None:
            params["post_id"] = post_id
        if post_url is not None:
            params["post_url"] = post_url
        body = await request.json()
        return await proxy_request("sora2", "/api/v1/sora2/get_post_detail", json_body=body)

@router.get("/get_post_remix_list")
async def get_post_remix_list(
    cursor: str | None = None,
    post_url: str | None = None,
    post_id: str | None = None,
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
        body = await request.json()
        return await proxy_request("sora2", "/api/v1/sora2/get_post_remix_list", json_body=body)

@router.get("/get_video_download_info")
async def get_video_download_info(
    post_url: str | None = None,
    post_id: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取无水印视频下载信息/Fetch none watermark video download info"""
        params: dict[str, Any] = {}
        if post_id is not None:
            params["post_id"] = post_id
        if post_url is not None:
            params["post_url"] = post_url
        body = await request.json()
        return await proxy_request("sora2", "/api/v1/sora2/get_video_download_info", json_body=body)

@router.get("/get_post_comments")
async def get_post_comments(
    cursor: str | None = None,
    post_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取作品一级评论/Fetch post comments"""
        params: dict[str, Any] = {}
        if post_id is not None:
            params["post_id"] = post_id
        if cursor is not None:
            params["cursor"] = cursor
        body = await request.json()
        return await proxy_request("sora2", "/api/v1/sora2/get_post_comments", json_body=body)

@router.get("/get_comment_replies")
async def get_comment_replies(
    cursor: str | None = None,
    comment_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取评论的回复/Fetch comment replies"""
        params: dict[str, Any] = {}
        if comment_id is not None:
            params["comment_id"] = comment_id
        if cursor is not None:
            params["cursor"] = cursor
        body = await request.json()
        return await proxy_request("sora2", "/api/v1/sora2/get_comment_replies", json_body=body)

@router.get("/get_user_profile")
async def get_user_profile(
    user_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户信息档案/Fetch user profile"""
        params: dict[str, Any] = {}
        if user_id is not None:
            params["user_id"] = user_id
        body = await request.json()
        return await proxy_request("sora2", "/api/v1/sora2/get_user_profile", json_body=body)

@router.get("/get_user_posts")
async def get_user_posts(
    cursor: str | None = None,
    user_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户发布的帖子列表/Fetch user posts"""
        params: dict[str, Any] = {}
        if user_id is not None:
            params["user_id"] = user_id
        if cursor is not None:
            params["cursor"] = cursor
        body = await request.json()
        return await proxy_request("sora2", "/api/v1/sora2/get_user_posts", json_body=body)

@router.get("/get_cameo_leaderboard")
async def get_cameo_leaderboard(
    cursor: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取 Cameo 出镜秀达人排行榜/Fetch Cameo leaderboard"""
        params: dict[str, Any] = {}
        if cursor is not None:
            params["cursor"] = cursor
        body = await request.json()
        return await proxy_request("sora2", "/api/v1/sora2/get_cameo_leaderboard", json_body=body)

@router.get("/get_user_cameo_appearances")
async def get_user_cameo_appearances(
    cursor: str | None = None,
    user_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户Cameo出镜秀列表/Fetch user cameo appearances"""
        params: dict[str, Any] = {}
        if user_id is not None:
            params["user_id"] = user_id
        if cursor is not None:
            params["cursor"] = cursor
        body = await request.json()
        return await proxy_request("sora2", "/api/v1/sora2/get_user_cameo_appearances", json_body=body)

@router.get("/get_user_followers")
async def get_user_followers(
    cursor: str | None = None,
    user_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户粉丝列表/Fetch user followers"""
        params: dict[str, Any] = {}
        if user_id is not None:
            params["user_id"] = user_id
        if cursor is not None:
            params["cursor"] = cursor
        body = await request.json()
        return await proxy_request("sora2", "/api/v1/sora2/get_user_followers", json_body=body)

@router.get("/get_user_following")
async def get_user_following(
    cursor: str | None = None,
    user_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户关注列表/Fetch user following"""
        params: dict[str, Any] = {}
        if user_id is not None:
            params["user_id"] = user_id
        if cursor is not None:
            params["cursor"] = cursor
        body = await request.json()
        return await proxy_request("sora2", "/api/v1/sora2/get_user_following", json_body=body)

@router.get("/get_feed")
async def get_feed(
    eager_views: str | None = None,
    cursor: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取Feed流（热门/推荐视频）/Fetch feed"""
        params: dict[str, Any] = {}
        if cursor is not None:
            params["cursor"] = cursor
        if eager_views is not None:
            params["eager_views"] = eager_views
        body = await request.json()
        return await proxy_request("sora2", "/api/v1/sora2/get_feed", json_body=body)

@router.get("/search_users")
async def search_users(
    username: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """搜索用户/Search users"""
        params: dict[str, Any] = {}
        if username is not None:
            params["username"] = username
        body = await request.json()
        return await proxy_request("sora2", "/api/v1/sora2/search_users", json_body=body)

@router.post("/upload_image")
async def upload_image(
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """上传图片获取media_id/Upload image to get media_id"""
        body = await request.json()
        return await proxy_request("sora2", "/api/v1/sora2/upload_image", json_body=body)

@router.post("/create_video")
async def create_video(
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """[已弃用/Deprecated] 文本/图片生成视频/Create video from text or image"""
        body = await request.json()
        return await proxy_request("sora2", "/api/v1/sora2/create_video", json_body=body)

@router.get("/get_task_status")
async def get_task_status(
    task_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """[已弃用/Deprecated] 查询任务状态/Get task status"""
        params: dict[str, Any] = {}
        if task_id is not None:
            params["task_id"] = task_id
        body = await request.json()
        return await proxy_request("sora2", "/api/v1/sora2/get_task_status", json_body=body)

@router.get("/get_task_detail")
async def get_task_detail(
    generation_id: str | None = None,
    task_id: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """[已弃用/Deprecated] 获取任务生成的作品详情（无水印版本）/Get task-generated post detail (watermark-free)"""
        params: dict[str, Any] = {}
        if task_id is not None:
            params["task_id"] = task_id
        if generation_id is not None:
            params["generation_id"] = generation_id
        body = await request.json()
        return await proxy_request("sora2", "/api/v1/sora2/get_task_detail", json_body=body)
