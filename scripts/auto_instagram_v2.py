"""Auto-generated routes for Instagram-V2-API."""

from __future__ import annotations

from typing import Any

from fastapi import APIRouter, Depends, Request

from socialmedia_hub.server._core import proxy_request, verify_api_key

router = APIRouter(prefix="/api/v1/instagram/v2", tags=["instagram_v2"])

@router.get("/shortcode_to_media_id")
async def shortcode_to_media_id(
    shortcode: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """Shortcode转Media ID/Convert shortcode to media ID"""
        params: dict[str, Any] = {}
        if shortcode is not None:
            params["shortcode"] = shortcode
        body = await request.json()
        return await proxy_request("instagram", "/api/v1/instagram/v2/shortcode_to_media_id", json_body=body)

@router.get("/media_id_to_shortcode")
async def media_id_to_shortcode(
    media_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """Media ID转Shortcode/Convert media ID to shortcode"""
        params: dict[str, Any] = {}
        if media_id is not None:
            params["media_id"] = media_id
        body = await request.json()
        return await proxy_request("instagram", "/api/v1/instagram/v2/media_id_to_shortcode", json_body=body)

@router.get("/user_id_to_username")
async def user_id_to_username(
    user_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """用户ID转用户信息/Get user info by user ID"""
        params: dict[str, Any] = {}
        if user_id is not None:
            params["user_id"] = user_id
        body = await request.json()
        return await proxy_request("instagram", "/api/v1/instagram/v2/user_id_to_username", json_body=body)

@router.get("/fetch_user_info")
async def fetch_user_info(
    user_id: str | None = None,
    username: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户信息/Get user info"""
        params: dict[str, Any] = {}
        if username is not None:
            params["username"] = username
        if user_id is not None:
            params["user_id"] = user_id
        body = await request.json()
        return await proxy_request("instagram", "/api/v1/instagram/v2/fetch_user_info", json_body=body)

@router.get("/fetch_user_posts")
async def fetch_user_posts(
    pagination_token: str | None = None,
    user_id: str | None = None,
    username: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户帖子/Get user posts"""
        params: dict[str, Any] = {}
        if username is not None:
            params["username"] = username
        if user_id is not None:
            params["user_id"] = user_id
        if pagination_token is not None:
            params["pagination_token"] = pagination_token
        body = await request.json()
        return await proxy_request("instagram", "/api/v1/instagram/v2/fetch_user_posts", json_body=body)

@router.get("/fetch_user_reels")
async def fetch_user_reels(
    pagination_token: str | None = None,
    user_id: str | None = None,
    username: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户Reels/Get user reels"""
        params: dict[str, Any] = {}
        if username is not None:
            params["username"] = username
        if user_id is not None:
            params["user_id"] = user_id
        if pagination_token is not None:
            params["pagination_token"] = pagination_token
        body = await request.json()
        return await proxy_request("instagram", "/api/v1/instagram/v2/fetch_user_reels", json_body=body)

@router.get("/fetch_user_followers")
async def fetch_user_followers(
    pagination_token: str | None = None,
    user_id: str | None = None,
    username: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户粉丝/Get user followers"""
        params: dict[str, Any] = {}
        if username is not None:
            params["username"] = username
        if user_id is not None:
            params["user_id"] = user_id
        if pagination_token is not None:
            params["pagination_token"] = pagination_token
        body = await request.json()
        return await proxy_request("instagram", "/api/v1/instagram/v2/fetch_user_followers", json_body=body)

@router.get("/fetch_user_following")
async def fetch_user_following(
    pagination_token: str | None = None,
    user_id: str | None = None,
    username: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户关注/Get user following"""
        params: dict[str, Any] = {}
        if username is not None:
            params["username"] = username
        if user_id is not None:
            params["user_id"] = user_id
        if pagination_token is not None:
            params["pagination_token"] = pagination_token
        body = await request.json()
        return await proxy_request("instagram", "/api/v1/instagram/v2/fetch_user_following", json_body=body)

@router.get("/fetch_user_stories")
async def fetch_user_stories(
    user_id: str | None = None,
    username: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户故事/Get user stories"""
        params: dict[str, Any] = {}
        if username is not None:
            params["username"] = username
        if user_id is not None:
            params["user_id"] = user_id
        body = await request.json()
        return await proxy_request("instagram", "/api/v1/instagram/v2/fetch_user_stories", json_body=body)

@router.get("/fetch_user_highlights")
async def fetch_user_highlights(
    user_id: str | None = None,
    username: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户精选/Get user highlights"""
        params: dict[str, Any] = {}
        if username is not None:
            params["username"] = username
        if user_id is not None:
            params["user_id"] = user_id
        body = await request.json()
        return await proxy_request("instagram", "/api/v1/instagram/v2/fetch_user_highlights", json_body=body)

@router.get("/fetch_highlight_stories")
async def fetch_highlight_stories(
    highlight_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取精选故事详情/Get highlight stories"""
        params: dict[str, Any] = {}
        if highlight_id is not None:
            params["highlight_id"] = highlight_id
        body = await request.json()
        return await proxy_request("instagram", "/api/v1/instagram/v2/fetch_highlight_stories", json_body=body)

@router.get("/fetch_user_tagged_posts")
async def fetch_user_tagged_posts(
    pagination_token: str | None = None,
    user_id: str | None = None,
    username: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户被标记的帖子/Get user tagged posts"""
        params: dict[str, Any] = {}
        if username is not None:
            params["username"] = username
        if user_id is not None:
            params["user_id"] = user_id
        if pagination_token is not None:
            params["pagination_token"] = pagination_token
        body = await request.json()
        return await proxy_request("instagram", "/api/v1/instagram/v2/fetch_user_tagged_posts", json_body=body)

@router.get("/fetch_similar_users")
async def fetch_similar_users(
    user_id: str | None = None,
    username: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取相似用户/Get similar users"""
        params: dict[str, Any] = {}
        if username is not None:
            params["username"] = username
        if user_id is not None:
            params["user_id"] = user_id
        body = await request.json()
        return await proxy_request("instagram", "/api/v1/instagram/v2/fetch_similar_users", json_body=body)

@router.get("/search_users")
async def search_users(
    keyword: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """搜索用户/Search users"""
        params: dict[str, Any] = {}
        if keyword is not None:
            params["keyword"] = keyword
        body = await request.json()
        return await proxy_request("instagram", "/api/v1/instagram/v2/search_users", json_body=body)

@router.get("/general_search")
async def general_search(
    pagination_token: str | None = None,
    keyword: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """综合搜索/General search"""
        params: dict[str, Any] = {}
        if keyword is not None:
            params["keyword"] = keyword
        if pagination_token is not None:
            params["pagination_token"] = pagination_token
        body = await request.json()
        return await proxy_request("instagram", "/api/v1/instagram/v2/general_search", json_body=body)

@router.get("/search_reels")
async def search_reels(
    pagination_token: str | None = None,
    keyword: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """搜索Reels/Search reels"""
        params: dict[str, Any] = {}
        if keyword is not None:
            params["keyword"] = keyword
        if pagination_token is not None:
            params["pagination_token"] = pagination_token
        body = await request.json()
        return await proxy_request("instagram", "/api/v1/instagram/v2/search_reels", json_body=body)

@router.get("/search_music")
async def search_music(
    keyword: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """搜索音乐/Search music"""
        params: dict[str, Any] = {}
        if keyword is not None:
            params["keyword"] = keyword
        body = await request.json()
        return await proxy_request("instagram", "/api/v1/instagram/v2/search_music", json_body=body)

@router.get("/search_hashtags")
async def search_hashtags(
    keyword: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """搜索话题标签/Search hashtags"""
        params: dict[str, Any] = {}
        if keyword is not None:
            params["keyword"] = keyword
        body = await request.json()
        return await proxy_request("instagram", "/api/v1/instagram/v2/search_hashtags", json_body=body)

@router.get("/search_locations")
async def search_locations(
    keyword: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """搜索地点/Search locations"""
        params: dict[str, Any] = {}
        if keyword is not None:
            params["keyword"] = keyword
        body = await request.json()
        return await proxy_request("instagram", "/api/v1/instagram/v2/search_locations", json_body=body)

@router.get("/search_by_coordinates")
async def search_by_coordinates(
    longitude: float,
    latitude: float,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """根据坐标搜索地点/Search locations by coordinates"""
        params: dict[str, Any] = {}
        if latitude is not None:
            params["latitude"] = latitude
        if longitude is not None:
            params["longitude"] = longitude
        body = await request.json()
        return await proxy_request("instagram", "/api/v1/instagram/v2/search_by_coordinates", json_body=body)

@router.get("/fetch_post_info")
async def fetch_post_info(
    code_or_url: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取帖子详情/Get post info"""
        params: dict[str, Any] = {}
        if code_or_url is not None:
            params["code_or_url"] = code_or_url
        body = await request.json()
        return await proxy_request("instagram", "/api/v1/instagram/v2/fetch_post_info", json_body=body)

@router.get("/fetch_post_likes")
async def fetch_post_likes(
    end_cursor: str | None = None,
    code_or_url: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取帖子点赞列表/Get post likes"""
        params: dict[str, Any] = {}
        if code_or_url is not None:
            params["code_or_url"] = code_or_url
        if end_cursor is not None:
            params["end_cursor"] = end_cursor
        body = await request.json()
        return await proxy_request("instagram", "/api/v1/instagram/v2/fetch_post_likes", json_body=body)

@router.get("/fetch_post_comments")
async def fetch_post_comments(
    pagination_token: str | None = None,
    sort_by: str | None = None,
    code_or_url: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取帖子评论/Get post comments"""
        params: dict[str, Any] = {}
        if code_or_url is not None:
            params["code_or_url"] = code_or_url
        if sort_by is not None:
            params["sort_by"] = sort_by
        if pagination_token is not None:
            params["pagination_token"] = pagination_token
        body = await request.json()
        return await proxy_request("instagram", "/api/v1/instagram/v2/fetch_post_comments", json_body=body)

@router.get("/fetch_comment_replies")
async def fetch_comment_replies(
    pagination_token: str | None = None,
    comment_id: str,
    code_or_url: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取评论回复/Get comment replies"""
        params: dict[str, Any] = {}
        if code_or_url is not None:
            params["code_or_url"] = code_or_url
        if comment_id is not None:
            params["comment_id"] = comment_id
        if pagination_token is not None:
            params["pagination_token"] = pagination_token
        body = await request.json()
        return await proxy_request("instagram", "/api/v1/instagram/v2/fetch_comment_replies", json_body=body)

@router.get("/fetch_music_posts")
async def fetch_music_posts(
    pagination_token: str | None = None,
    audio_canonical_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取音乐帖子/Get music posts"""
        params: dict[str, Any] = {}
        if audio_canonical_id is not None:
            params["audio_canonical_id"] = audio_canonical_id
        if pagination_token is not None:
            params["pagination_token"] = pagination_token
        body = await request.json()
        return await proxy_request("instagram", "/api/v1/instagram/v2/fetch_music_posts", json_body=body)

@router.get("/fetch_location_posts")
async def fetch_location_posts(
    pagination_token: str | None = None,
    location_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取地点帖子/Get location posts"""
        params: dict[str, Any] = {}
        if location_id is not None:
            params["location_id"] = location_id
        if pagination_token is not None:
            params["pagination_token"] = pagination_token
        body = await request.json()
        return await proxy_request("instagram", "/api/v1/instagram/v2/fetch_location_posts", json_body=body)

@router.get("/fetch_hashtag_posts")
async def fetch_hashtag_posts(
    pagination_token: str | None = None,
    feed_type: str | None = None,
    keyword: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取话题帖子/Get hashtag posts"""
        params: dict[str, Any] = {}
        if keyword is not None:
            params["keyword"] = keyword
        if feed_type is not None:
            params["feed_type"] = feed_type
        if pagination_token is not None:
            params["pagination_token"] = pagination_token
        body = await request.json()
        return await proxy_request("instagram", "/api/v1/instagram/v2/fetch_hashtag_posts", json_body=body)
