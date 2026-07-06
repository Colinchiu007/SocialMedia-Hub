"""Auto-generated routes for Instagram-V1-API."""

from __future__ import annotations

from typing import Any

from fastapi import APIRouter, Depends, Request

from socialmedia_hub.server._core import proxy_request, verify_api_key

router = APIRouter(prefix="/api/v1/instagram/v1", tags=["instagram_v1"])

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
        return await proxy_request("instagram", "/api/v1/instagram/v1/shortcode_to_media_id", json_body=body)

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
        return await proxy_request("instagram", "/api/v1/instagram/v1/media_id_to_shortcode", json_body=body)

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
        return await proxy_request("instagram", "/api/v1/instagram/v1/user_id_to_username", json_body=body)

@router.get("/fetch_user_info_by_username")
async def fetch_user_info_by_username(
    username: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """根据用户名获取用户数据/Get user data by username"""
        params: dict[str, Any] = {}
        if username is not None:
            params["username"] = username
        body = await request.json()
        return await proxy_request("instagram", "/api/v1/instagram/v1/fetch_user_info_by_username", json_body=body)

@router.get("/fetch_user_info_by_username_v2")
async def fetch_user_info_by_username_v2(
    username: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """根据用户名获取用户数据V2/Get user data by username V2"""
        params: dict[str, Any] = {}
        if username is not None:
            params["username"] = username
        body = await request.json()
        return await proxy_request("instagram", "/api/v1/instagram/v1/fetch_user_info_by_username_v2", json_body=body)

@router.get("/fetch_user_info_by_username_v3")
async def fetch_user_info_by_username_v3(
    username: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """根据用户名获取用户数据V3/Get user data by username V3"""
        params: dict[str, Any] = {}
        if username is not None:
            params["username"] = username
        body = await request.json()
        return await proxy_request("instagram", "/api/v1/instagram/v1/fetch_user_info_by_username_v3", json_body=body)

@router.get("/fetch_user_info_by_id")
async def fetch_user_info_by_id(
    user_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """根据用户ID获取用户数据/Get user data by user ID"""
        params: dict[str, Any] = {}
        if user_id is not None:
            params["user_id"] = user_id
        body = await request.json()
        return await proxy_request("instagram", "/api/v1/instagram/v1/fetch_user_info_by_id", json_body=body)

@router.get("/fetch_user_info_by_id_v2")
async def fetch_user_info_by_id_v2(
    user_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """根据用户ID获取用户数据V2/Get user data by user ID V2"""
        params: dict[str, Any] = {}
        if user_id is not None:
            params["user_id"] = user_id
        body = await request.json()
        return await proxy_request("instagram", "/api/v1/instagram/v1/fetch_user_info_by_id_v2", json_body=body)

@router.get("/fetch_user_about_info")
async def fetch_user_about_info(
    user_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户的About信息/Get user about info"""
        params: dict[str, Any] = {}
        if user_id is not None:
            params["user_id"] = user_id
        body = await request.json()
        return await proxy_request("instagram", "/api/v1/instagram/v1/fetch_user_about_info", json_body=body)

@router.get("/fetch_user_posts")
async def fetch_user_posts(
    max_id: str | None = None,
    count: int | None = None,
    user_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户帖子列表/Get user posts list"""
        params: dict[str, Any] = {}
        if user_id is not None:
            params["user_id"] = user_id
        if count is not None:
            params["count"] = count
        if max_id is not None:
            params["max_id"] = max_id
        body = await request.json()
        return await proxy_request("instagram", "/api/v1/instagram/v1/fetch_user_posts", json_body=body)

@router.get("/fetch_user_posts_v2")
async def fetch_user_posts_v2(
    end_cursor: str | None = None,
    count: int | None = None,
    user_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户帖子列表V2/Get user posts list V2"""
        params: dict[str, Any] = {}
        if user_id is not None:
            params["user_id"] = user_id
        if count is not None:
            params["count"] = count
        if end_cursor is not None:
            params["end_cursor"] = end_cursor
        body = await request.json()
        return await proxy_request("instagram", "/api/v1/instagram/v1/fetch_user_posts_v2", json_body=body)

@router.get("/fetch_user_reels")
async def fetch_user_reels(
    max_id: str | None = None,
    count: int | None = None,
    user_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户Reels列表/Get user Reels list"""
        params: dict[str, Any] = {}
        if user_id is not None:
            params["user_id"] = user_id
        if count is not None:
            params["count"] = count
        if max_id is not None:
            params["max_id"] = max_id
        body = await request.json()
        return await proxy_request("instagram", "/api/v1/instagram/v1/fetch_user_reels", json_body=body)

@router.get("/fetch_user_reposts")
async def fetch_user_reposts(
    max_id: str | None = None,
    user_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户转发列表/Get user reposts list"""
        params: dict[str, Any] = {}
        if user_id is not None:
            params["user_id"] = user_id
        if max_id is not None:
            params["max_id"] = max_id
        body = await request.json()
        return await proxy_request("instagram", "/api/v1/instagram/v1/fetch_user_reposts", json_body=body)

@router.get("/fetch_user_tagged_posts")
async def fetch_user_tagged_posts(
    end_cursor: str | None = None,
    count: int | None = None,
    user_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户被标记的帖子/Get user tagged posts"""
        params: dict[str, Any] = {}
        if user_id is not None:
            params["user_id"] = user_id
        if count is not None:
            params["count"] = count
        if end_cursor is not None:
            params["end_cursor"] = end_cursor
        body = await request.json()
        return await proxy_request("instagram", "/api/v1/instagram/v1/fetch_user_tagged_posts", json_body=body)

@router.get("/fetch_related_profiles")
async def fetch_related_profiles(
    user_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取相关用户推荐/Get related profiles"""
        params: dict[str, Any] = {}
        if user_id is not None:
            params["user_id"] = user_id
        body = await request.json()
        return await proxy_request("instagram", "/api/v1/instagram/v1/fetch_related_profiles", json_body=body)

@router.get("/fetch_search")
async def fetch_search(
    select: str | None = None,
    query: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """搜索用户/话题/地点/Search users/hashtags/places"""
        params: dict[str, Any] = {}
        if query is not None:
            params["query"] = query
        if select is not None:
            params["select"] = select
        body = await request.json()
        return await proxy_request("instagram", "/api/v1/instagram/v1/fetch_search", json_body=body)

@router.get("/fetch_post_by_url")
async def fetch_post_by_url(
    post_url: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """通过URL获取帖子详情/Get post by URL"""
        params: dict[str, Any] = {}
        if post_url is not None:
            params["post_url"] = post_url
        body = await request.json()
        return await proxy_request("instagram", "/api/v1/instagram/v1/fetch_post_by_url", json_body=body)

@router.get("/fetch_post_by_url_v2")
async def fetch_post_by_url_v2(
    post_url: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """通过URL获取帖子详情 V2/Get post by URL V2"""
        params: dict[str, Any] = {}
        if post_url is not None:
            params["post_url"] = post_url
        body = await request.json()
        return await proxy_request("instagram", "/api/v1/instagram/v1/fetch_post_by_url_v2", json_body=body)

@router.get("/fetch_post_by_id")
async def fetch_post_by_id(
    post_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """通过ID获取帖子详情/Get post by ID"""
        params: dict[str, Any] = {}
        if post_id is not None:
            params["post_id"] = post_id
        body = await request.json()
        return await proxy_request("instagram", "/api/v1/instagram/v1/fetch_post_by_id", json_body=body)

@router.get("/fetch_post_comments_v2")
async def fetch_post_comments_v2(
    min_id: str | None = None,
    sort_order: str | None = None,
    media_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取帖子评论列表V2/Get post comments V2"""
        params: dict[str, Any] = {}
        if media_id is not None:
            params["media_id"] = media_id
        if sort_order is not None:
            params["sort_order"] = sort_order
        if min_id is not None:
            params["min_id"] = min_id
        body = await request.json()
        return await proxy_request("instagram", "/api/v1/instagram/v1/fetch_post_comments_v2", json_body=body)

@router.get("/fetch_comment_replies")
async def fetch_comment_replies(
    min_id: str | None = None,
    comment_id: str,
    media_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取评论的子评论列表/Get comment replies"""
        params: dict[str, Any] = {}
        if media_id is not None:
            params["media_id"] = media_id
        if comment_id is not None:
            params["comment_id"] = comment_id
        if min_id is not None:
            params["min_id"] = min_id
        body = await request.json()
        return await proxy_request("instagram", "/api/v1/instagram/v1/fetch_comment_replies", json_body=body)

@router.get("/fetch_music_posts")
async def fetch_music_posts(
    max_id: str | None = None,
    music_url: str | None = None,
    music_id: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取使用特定音乐的帖子/Get posts using specific music"""
        params: dict[str, Any] = {}
        if music_id is not None:
            params["music_id"] = music_id
        if music_url is not None:
            params["music_url"] = music_url
        if max_id is not None:
            params["max_id"] = max_id
        body = await request.json()
        return await proxy_request("instagram", "/api/v1/instagram/v1/fetch_music_posts", json_body=body)

@router.get("/fetch_hashtag_posts")
async def fetch_hashtag_posts(
    end_cursor: str | None = None,
    hashtag: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取话题标签下的帖子/Get posts by hashtag"""
        params: dict[str, Any] = {}
        if hashtag is not None:
            params["hashtag"] = hashtag
        if end_cursor is not None:
            params["end_cursor"] = end_cursor
        body = await request.json()
        return await proxy_request("instagram", "/api/v1/instagram/v1/fetch_hashtag_posts", json_body=body)

@router.get("/fetch_location_info")
async def fetch_location_info(
    location_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取地点信息/Get location info"""
        params: dict[str, Any] = {}
        if location_id is not None:
            params["location_id"] = location_id
        body = await request.json()
        return await proxy_request("instagram", "/api/v1/instagram/v1/fetch_location_info", json_body=body)

@router.get("/fetch_location_posts")
async def fetch_location_posts(
    end_cursor: str | None = None,
    tab: str | None = None,
    location_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取地点下的帖子/Get posts by location"""
        params: dict[str, Any] = {}
        if location_id is not None:
            params["location_id"] = location_id
        if tab is not None:
            params["tab"] = tab
        if end_cursor is not None:
            params["end_cursor"] = end_cursor
        body = await request.json()
        return await proxy_request("instagram", "/api/v1/instagram/v1/fetch_location_posts", json_body=body)

@router.get("/fetch_cities")
async def fetch_cities(
    page: int | None = None,
    country_code: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取国家城市列表/Get cities by country"""
        params: dict[str, Any] = {}
        if country_code is not None:
            params["country_code"] = country_code
        if page is not None:
            params["page"] = page
        body = await request.json()
        return await proxy_request("instagram", "/api/v1/instagram/v1/fetch_cities", json_body=body)

@router.get("/fetch_locations")
async def fetch_locations(
    page: int | None = None,
    city_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取城市地点列表/Get locations by city"""
        params: dict[str, Any] = {}
        if city_id is not None:
            params["city_id"] = city_id
        if page is not None:
            params["page"] = page
        body = await request.json()
        return await proxy_request("instagram", "/api/v1/instagram/v1/fetch_locations", json_body=body)

@router.get("/fetch_explore_sections")
async def fetch_explore_sections(
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取探索页面分类/Get explore page sections"""
        body = await request.json()
        return await proxy_request("instagram", "/api/v1/instagram/v1/fetch_explore_sections", json_body=body)

@router.get("/fetch_section_posts")
async def fetch_section_posts(
    max_id: str | None = None,
    count: int | None = None,
    section_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取分类下的帖子/Get posts by section"""
        params: dict[str, Any] = {}
        if section_id is not None:
            params["section_id"] = section_id
        if count is not None:
            params["count"] = count
        if max_id is not None:
            params["max_id"] = max_id
        body = await request.json()
        return await proxy_request("instagram", "/api/v1/instagram/v1/fetch_section_posts", json_body=body)
