"""Auto-generated routes for Instagram-V3-API."""

from __future__ import annotations

from typing import Any

from fastapi import APIRouter, Depends, Request

from socialmedia_hub.server._core import proxy_request, verify_api_key

router = APIRouter(prefix="/api/v1/instagram/v3", tags=["instagram_v3"])

@router.get("/search_users")
async def search_users(
    rank_token: str | None = None,
    query: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """搜索用户/Search users"""
        params: dict[str, Any] = {}
        if query is not None:
            params["query"] = query
        if rank_token is not None:
            params["rank_token"] = rank_token
        body = await request.json()
        return await proxy_request("instagram", "/api/v1/instagram/v3/search_users", json_body=body)

@router.get("/search_hashtags")
async def search_hashtags(
    rank_token: str | None = None,
    query: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """搜索话题标签/Search hashtags"""
        params: dict[str, Any] = {}
        if query is not None:
            params["query"] = query
        if rank_token is not None:
            params["rank_token"] = rank_token
        body = await request.json()
        return await proxy_request("instagram", "/api/v1/instagram/v3/search_hashtags", json_body=body)

@router.get("/search_places")
async def search_places(
    rank_token: str | None = None,
    query: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """搜索地点/Search places"""
        params: dict[str, Any] = {}
        if query is not None:
            params["query"] = query
        if rank_token is not None:
            params["rank_token"] = rank_token
        body = await request.json()
        return await proxy_request("instagram", "/api/v1/instagram/v3/search_places", json_body=body)

@router.get("/general_search")
async def general_search(
    enable_metadata: bool | None = None,
    rank_token: str | None = None,
    next_max_id: str | None = None,
    query: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """综合搜索（支持分页）/General search (with pagination)"""
        params: dict[str, Any] = {}
        if query is not None:
            params["query"] = query
        if next_max_id is not None:
            params["next_max_id"] = next_max_id
        if rank_token is not None:
            params["rank_token"] = rank_token
        if enable_metadata is not None:
            params["enable_metadata"] = enable_metadata
        body = await request.json()
        return await proxy_request("instagram", "/api/v1/instagram/v3/general_search", json_body=body)

@router.get("/get_user_id_by_username")
async def get_user_id_by_username(
    username: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """通过用户名获取用户ID/Get user ID by username"""
        params: dict[str, Any] = {}
        if username is not None:
            params["username"] = username
        body = await request.json()
        return await proxy_request("instagram", "/api/v1/instagram/v3/get_user_id_by_username", json_body=body)

@router.get("/get_user_profile")
async def get_user_profile(
    username: str | None = None,
    user_id: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户信息/Get user profile"""
        params: dict[str, Any] = {}
        if user_id is not None:
            params["user_id"] = user_id
        if username is not None:
            params["username"] = username
        body = await request.json()
        return await proxy_request("instagram", "/api/v1/instagram/v3/get_user_profile", json_body=body)

@router.get("/get_user_brief")
async def get_user_brief(
    username: str,
    user_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户短详情/Get user brief info"""
        params: dict[str, Any] = {}
        if user_id is not None:
            params["user_id"] = user_id
        if username is not None:
            params["username"] = username
        body = await request.json()
        return await proxy_request("instagram", "/api/v1/instagram/v3/get_user_brief", json_body=body)

@router.get("/get_user_posts")
async def get_user_posts(
    count: int | None = None,
    last: int | None = None,
    before: str | None = None,
    after: str | None = None,
    first: int | None = None,
    username: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户帖子列表/Get user posts"""
        params: dict[str, Any] = {}
        if username is not None:
            params["username"] = username
        if first is not None:
            params["first"] = first
        if after is not None:
            params["after"] = after
        if before is not None:
            params["before"] = before
        if last is not None:
            params["last"] = last
        if count is not None:
            params["count"] = count
        body = await request.json()
        return await proxy_request("instagram", "/api/v1/instagram/v3/get_user_posts", json_body=body)

@router.get("/get_user_tagged_posts")
async def get_user_tagged_posts(
    count: int | None = None,
    last: int | None = None,
    before: str | None = None,
    after: str | None = None,
    first: int | None = None,
    username: str | None = None,
    user_id: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户被标记的帖子/Get user tagged posts"""
        params: dict[str, Any] = {}
        if user_id is not None:
            params["user_id"] = user_id
        if username is not None:
            params["username"] = username
        if first is not None:
            params["first"] = first
        if after is not None:
            params["after"] = after
        if before is not None:
            params["before"] = before
        if last is not None:
            params["last"] = last
        if count is not None:
            params["count"] = count
        body = await request.json()
        return await proxy_request("instagram", "/api/v1/instagram/v3/get_user_tagged_posts", json_body=body)

@router.get("/get_user_reels")
async def get_user_reels(
    page_size: int | None = None,
    last: int | None = None,
    before: str | None = None,
    after: str | None = None,
    first: int | None = None,
    username: str | None = None,
    user_id: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户Reels列表/Get user reels"""
        params: dict[str, Any] = {}
        if user_id is not None:
            params["user_id"] = user_id
        if username is not None:
            params["username"] = username
        if first is not None:
            params["first"] = first
        if after is not None:
            params["after"] = after
        if before is not None:
            params["before"] = before
        if last is not None:
            params["last"] = last
        if page_size is not None:
            params["page_size"] = page_size
        body = await request.json()
        return await proxy_request("instagram", "/api/v1/instagram/v3/get_user_reels", json_body=body)

@router.get("/get_user_highlights")
async def get_user_highlights(
    last: int | None = None,
    before: str | None = None,
    after: str | None = None,
    first: int | None = None,
    username: str | None = None,
    user_id: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户精选Highlights列表/Get user highlights"""
        params: dict[str, Any] = {}
        if user_id is not None:
            params["user_id"] = user_id
        if username is not None:
            params["username"] = username
        if first is not None:
            params["first"] = first
        if after is not None:
            params["after"] = after
        if before is not None:
            params["before"] = before
        if last is not None:
            params["last"] = last
        body = await request.json()
        return await proxy_request("instagram", "/api/v1/instagram/v3/get_user_highlights", json_body=body)

@router.get("/get_highlight_stories")
async def get_highlight_stories(
    last: int | None = None,
    first: int | None = None,
    reel_ids: str | None = None,
    highlight_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取Highlight精选详情/Get highlight stories"""
        params: dict[str, Any] = {}
        if highlight_id is not None:
            params["highlight_id"] = highlight_id
        if reel_ids is not None:
            params["reel_ids"] = reel_ids
        if first is not None:
            params["first"] = first
        if last is not None:
            params["last"] = last
        body = await request.json()
        return await proxy_request("instagram", "/api/v1/instagram/v3/get_highlight_stories", json_body=body)

@router.get("/get_user_about")
async def get_user_about(
    username: str | None = None,
    user_id: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户账户简介/Get user about info"""
        params: dict[str, Any] = {}
        if user_id is not None:
            params["user_id"] = user_id
        if username is not None:
            params["username"] = username
        body = await request.json()
        return await proxy_request("instagram", "/api/v1/instagram/v3/get_user_about", json_body=body)

@router.get("/get_user_former_usernames")
async def get_user_former_usernames(
    username: str | None = None,
    user_id: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户曾用用户名/Get user former usernames"""
        params: dict[str, Any] = {}
        if user_id is not None:
            params["user_id"] = user_id
        if username is not None:
            params["username"] = username
        body = await request.json()
        return await proxy_request("instagram", "/api/v1/instagram/v3/get_user_former_usernames", json_body=body)

@router.get("/get_user_stories")
async def get_user_stories(
    username: str | None = None,
    user_id: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户Stories（快拍）/Get user stories"""
        params: dict[str, Any] = {}
        if user_id is not None:
            params["user_id"] = user_id
        if username is not None:
            params["username"] = username
        body = await request.json()
        return await proxy_request("instagram", "/api/v1/instagram/v3/get_user_stories", json_body=body)

@router.get("/get_recommended_reels")
async def get_recommended_reels(
    after: str | None = None,
    first: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取Reels推荐列表/Get recommended Reels feed"""
        params: dict[str, Any] = {}
        if first is not None:
            params["first"] = first
        if after is not None:
            params["after"] = after
        body = await request.json()
        return await proxy_request("instagram", "/api/v1/instagram/v3/get_recommended_reels", json_body=body)

@router.get("/get_post_info")
async def get_post_info(
    media_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取帖子详情/Get post info (media_id or URL)"""
        params: dict[str, Any] = {}
        if media_id is not None:
            params["media_id"] = media_id
        body = await request.json()
        return await proxy_request("instagram", "/api/v1/instagram/v3/get_post_info", json_body=body)

@router.get("/get_post_info_by_code")
async def get_post_info_by_code(
    code: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取帖子详情(code)/Get post info by shortcode"""
        params: dict[str, Any] = {}
        if code is not None:
            params["code"] = code
        body = await request.json()
        return await proxy_request("instagram", "/api/v1/instagram/v3/get_post_info_by_code", json_body=body)

@router.get("/get_post_comments")
async def get_post_comments(
    sort_order: str | None = None,
    min_id: str | None = None,
    code: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取帖子评论/Get post comments"""
        params: dict[str, Any] = {}
        if code is not None:
            params["code"] = code
        if min_id is not None:
            params["min_id"] = min_id
        if sort_order is not None:
            params["sort_order"] = sort_order
        body = await request.json()
        return await proxy_request("instagram", "/api/v1/instagram/v3/get_post_comments", json_body=body)

@router.get("/get_comment_replies")
async def get_comment_replies(
    min_id: str | None = None,
    comment_id: str,
    media_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取评论的子评论/回复/Get comment replies"""
        params: dict[str, Any] = {}
        if media_id is not None:
            params["media_id"] = media_id
        if comment_id is not None:
            params["comment_id"] = comment_id
        if min_id is not None:
            params["min_id"] = min_id
        body = await request.json()
        return await proxy_request("instagram", "/api/v1/instagram/v3/get_comment_replies", json_body=body)

@router.get("/get_post_oembed")
async def get_post_oembed(
    maxwidth: int | None = None,
    hidecaption: bool | None = None,
    url: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取帖子oEmbed内嵌信息/Get post oEmbed info"""
        params: dict[str, Any] = {}
        if url is not None:
            params["url"] = url
        if hidecaption is not None:
            params["hidecaption"] = hidecaption
        if maxwidth is not None:
            params["maxwidth"] = maxwidth
        body = await request.json()
        return await proxy_request("instagram", "/api/v1/instagram/v3/get_post_oembed", json_body=body)

@router.get("/translate_comment")
async def translate_comment(
    comment_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """翻译评论/帖子文本/Translate comment or caption"""
        params: dict[str, Any] = {}
        if comment_id is not None:
            params["comment_id"] = comment_id
        body = await request.json()
        return await proxy_request("instagram", "/api/v1/instagram/v3/translate_comment", json_body=body)

@router.get("/bulk_translate_comments")
async def bulk_translate_comments(
    comment_ids: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """批量翻译评论/Bulk translate comments"""
        params: dict[str, Any] = {}
        if comment_ids is not None:
            params["comment_ids"] = comment_ids
        body = await request.json()
        return await proxy_request("instagram", "/api/v1/instagram/v3/bulk_translate_comments", json_body=body)

@router.get("/get_explore")
async def get_explore(
    max_id: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取探索页推荐帖子/Get explore feed"""
        params: dict[str, Any] = {}
        if max_id is not None:
            params["max_id"] = max_id
        body = await request.json()
        return await proxy_request("instagram", "/api/v1/instagram/v3/get_explore", json_body=body)

@router.get("/get_user_following")
async def get_user_following(
    max_id: str | None = None,
    count: int | None = None,
    username: str | None = None,
    user_id: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户关注列表/Get user following list"""
        params: dict[str, Any] = {}
        if user_id is not None:
            params["user_id"] = user_id
        if username is not None:
            params["username"] = username
        if count is not None:
            params["count"] = count
        if max_id is not None:
            params["max_id"] = max_id
        body = await request.json()
        return await proxy_request("instagram", "/api/v1/instagram/v3/get_user_following", json_body=body)

@router.get("/get_user_followers")
async def get_user_followers(
    max_id: str | None = None,
    count: int | None = None,
    username: str | None = None,
    user_id: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户粉丝列表/Get user followers list"""
        params: dict[str, Any] = {}
        if user_id is not None:
            params["user_id"] = user_id
        if username is not None:
            params["username"] = username
        if count is not None:
            params["count"] = count
        if max_id is not None:
            params["max_id"] = max_id
        body = await request.json()
        return await proxy_request("instagram", "/api/v1/instagram/v3/get_user_followers", json_body=body)

@router.get("/get_location_info")
async def get_location_info(
    show_nearby: bool | None = None,
    location_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取地点详情/Get location info"""
        params: dict[str, Any] = {}
        if location_id is not None:
            params["location_id"] = location_id
        if show_nearby is not None:
            params["show_nearby"] = show_nearby
        body = await request.json()
        return await proxy_request("instagram", "/api/v1/instagram/v3/get_location_info", json_body=body)

@router.get("/get_location_posts")
async def get_location_posts(
    page_size_override: int | None = None,
    after: str | None = None,
    first: int | None = None,
    tab: str | None = None,
    location_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取地点相关帖子/Get location posts"""
        params: dict[str, Any] = {}
        if location_id is not None:
            params["location_id"] = location_id
        if tab is not None:
            params["tab"] = tab
        if first is not None:
            params["first"] = first
        if after is not None:
            params["after"] = after
        if page_size_override is not None:
            params["page_size_override"] = page_size_override
        body = await request.json()
        return await proxy_request("instagram", "/api/v1/instagram/v3/get_location_posts", json_body=body)

@router.get("/get_location_nearby")
async def get_location_nearby(
    location_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取地点附近内容/Get nearby location content"""
        params: dict[str, Any] = {}
        if location_id is not None:
            params["location_id"] = location_id
        body = await request.json()
        return await proxy_request("instagram", "/api/v1/instagram/v3/get_location_nearby", json_body=body)

@router.get("/shortcode_to_media_id")
async def shortcode_to_media_id(
    shortcode: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """短码转媒体ID/Convert shortcode to media ID"""
        params: dict[str, Any] = {}
        if shortcode is not None:
            params["shortcode"] = shortcode
        body = await request.json()
        return await proxy_request("instagram", "/api/v1/instagram/v3/shortcode_to_media_id", json_body=body)

@router.get("/media_id_to_shortcode")
async def media_id_to_shortcode(
    media_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """媒体ID转短码/Convert media ID to shortcode"""
        params: dict[str, Any] = {}
        if media_id is not None:
            params["media_id"] = media_id
        body = await request.json()
        return await proxy_request("instagram", "/api/v1/instagram/v3/media_id_to_shortcode", json_body=body)

@router.get("/extract_shortcode")
async def extract_shortcode(
    url: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """从URL提取短码/Extract shortcode from URL"""
        params: dict[str, Any] = {}
        if url is not None:
            params["url"] = url
        body = await request.json()
        return await proxy_request("instagram", "/api/v1/instagram/v3/extract_shortcode", json_body=body)
