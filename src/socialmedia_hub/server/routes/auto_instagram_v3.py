"""Auto-generated routes for Instagram-V3-API."""

from __future__ import annotations

from typing import Any

from fastapi import APIRouter, Depends, Request

from socialmedia_hub.server._core import proxy_request, verify_api_key

router = APIRouter(prefix="/api/v1/instagram/v3", tags=["instagram_v3"])

@router.get("/search_users")
async def search_users(
    query: str,
    request: Request,
    rank_token: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """搜索用户/Search users"""
    body = await request.json()
    params: dict[str, Any] = {}
    if query is not None:
        params["query"] = query
    if rank_token is not None:
        params["rank_token"] = rank_token
    return await proxy_request("instagram", "/api/v1/instagram/v3/search_users", params=params, json_body=body)

@router.get("/search_hashtags")
async def search_hashtags(
    query: str,
    request: Request,
    rank_token: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """搜索话题标签/Search hashtags"""
    body = await request.json()
    params: dict[str, Any] = {}
    if query is not None:
        params["query"] = query
    if rank_token is not None:
        params["rank_token"] = rank_token
    return await proxy_request("instagram", "/api/v1/instagram/v3/search_hashtags", params=params, json_body=body)

@router.get("/search_places")
async def search_places(
    query: str,
    request: Request,
    rank_token: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """搜索地点/Search places"""
    body = await request.json()
    params: dict[str, Any] = {}
    if query is not None:
        params["query"] = query
    if rank_token is not None:
        params["rank_token"] = rank_token
    return await proxy_request("instagram", "/api/v1/instagram/v3/search_places", params=params, json_body=body)

@router.get("/general_search")
async def general_search(
    query: str,
    request: Request,
    next_max_id: str | None = None,
    rank_token: str | None = None,
    enable_metadata: bool | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """综合搜索（支持分页）/General search (with pagination)"""
    body = await request.json()
    params: dict[str, Any] = {}
    if query is not None:
        params["query"] = query
    if next_max_id is not None:
        params["next_max_id"] = next_max_id
    if rank_token is not None:
        params["rank_token"] = rank_token
    if enable_metadata is not None:
        params["enable_metadata"] = enable_metadata
    return await proxy_request("instagram", "/api/v1/instagram/v3/general_search", params=params, json_body=body)

@router.get("/get_user_id_by_username")
async def get_user_id_by_username(
    username: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """通过用户名获取用户ID/Get user ID by username"""
    body = await request.json()
    params: dict[str, Any] = {}
    if username is not None:
        params["username"] = username
    return await proxy_request("instagram", "/api/v1/instagram/v3/get_user_id_by_username", params=params, json_body=body)

@router.get("/get_user_profile")
async def get_user_profile(
    request: Request,
    user_id: str | None = None,
    username: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户信息/Get user profile"""
    body = await request.json()
    params: dict[str, Any] = {}
    if user_id is not None:
        params["user_id"] = user_id
    if username is not None:
        params["username"] = username
    return await proxy_request("instagram", "/api/v1/instagram/v3/get_user_profile", params=params, json_body=body)

@router.get("/get_user_brief")
async def get_user_brief(
    user_id: str,
    username: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户短详情/Get user brief info"""
    body = await request.json()
    params: dict[str, Any] = {}
    if user_id is not None:
        params["user_id"] = user_id
    if username is not None:
        params["username"] = username
    return await proxy_request("instagram", "/api/v1/instagram/v3/get_user_brief", params=params, json_body=body)

@router.get("/get_user_posts")
async def get_user_posts(
    username: str,
    request: Request,
    first: int | None = None,
    after: str | None = None,
    before: str | None = None,
    last: int | None = None,
    count: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户帖子列表/Get user posts"""
    body = await request.json()
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
    return await proxy_request("instagram", "/api/v1/instagram/v3/get_user_posts", params=params, json_body=body)

@router.get("/get_user_tagged_posts")
async def get_user_tagged_posts(
    request: Request,
    user_id: str | None = None,
    username: str | None = None,
    first: int | None = None,
    after: str | None = None,
    before: str | None = None,
    last: int | None = None,
    count: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户被标记的帖子/Get user tagged posts"""
    body = await request.json()
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
    return await proxy_request("instagram", "/api/v1/instagram/v3/get_user_tagged_posts", params=params, json_body=body)

@router.get("/get_user_reels")
async def get_user_reels(
    request: Request,
    user_id: str | None = None,
    username: str | None = None,
    first: int | None = None,
    after: str | None = None,
    before: str | None = None,
    last: int | None = None,
    page_size: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户Reels列表/Get user reels"""
    body = await request.json()
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
    return await proxy_request("instagram", "/api/v1/instagram/v3/get_user_reels", params=params, json_body=body)

@router.get("/get_user_highlights")
async def get_user_highlights(
    request: Request,
    user_id: str | None = None,
    username: str | None = None,
    first: int | None = None,
    after: str | None = None,
    before: str | None = None,
    last: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户精选Highlights列表/Get user highlights"""
    body = await request.json()
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
    return await proxy_request("instagram", "/api/v1/instagram/v3/get_user_highlights", params=params, json_body=body)

@router.get("/get_highlight_stories")
async def get_highlight_stories(
    highlight_id: str,
    request: Request,
    reel_ids: str | None = None,
    first: int | None = None,
    last: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取Highlight精选详情/Get highlight stories"""
    body = await request.json()
    params: dict[str, Any] = {}
    if highlight_id is not None:
        params["highlight_id"] = highlight_id
    if reel_ids is not None:
        params["reel_ids"] = reel_ids
    if first is not None:
        params["first"] = first
    if last is not None:
        params["last"] = last
    return await proxy_request("instagram", "/api/v1/instagram/v3/get_highlight_stories", params=params, json_body=body)

@router.get("/get_user_about")
async def get_user_about(
    request: Request,
    user_id: str | None = None,
    username: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户账户简介/Get user about info"""
    body = await request.json()
    params: dict[str, Any] = {}
    if user_id is not None:
        params["user_id"] = user_id
    if username is not None:
        params["username"] = username
    return await proxy_request("instagram", "/api/v1/instagram/v3/get_user_about", params=params, json_body=body)

@router.get("/get_user_former_usernames")
async def get_user_former_usernames(
    request: Request,
    user_id: str | None = None,
    username: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户曾用用户名/Get user former usernames"""
    body = await request.json()
    params: dict[str, Any] = {}
    if user_id is not None:
        params["user_id"] = user_id
    if username is not None:
        params["username"] = username
    return await proxy_request("instagram", "/api/v1/instagram/v3/get_user_former_usernames", params=params, json_body=body)

@router.get("/get_user_stories")
async def get_user_stories(
    request: Request,
    user_id: str | None = None,
    username: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户Stories（快拍）/Get user stories"""
    body = await request.json()
    params: dict[str, Any] = {}
    if user_id is not None:
        params["user_id"] = user_id
    if username is not None:
        params["username"] = username
    return await proxy_request("instagram", "/api/v1/instagram/v3/get_user_stories", params=params, json_body=body)

@router.get("/get_recommended_reels")
async def get_recommended_reels(
    request: Request,
    first: int | None = None,
    after: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取Reels推荐列表/Get recommended Reels feed"""
    body = await request.json()
    params: dict[str, Any] = {}
    if first is not None:
        params["first"] = first
    if after is not None:
        params["after"] = after
    return await proxy_request("instagram", "/api/v1/instagram/v3/get_recommended_reels", params=params, json_body=body)

@router.get("/get_post_info")
async def get_post_info(
    media_id: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取帖子详情/Get post info (media_id or URL)"""
    body = await request.json()
    params: dict[str, Any] = {}
    if media_id is not None:
        params["media_id"] = media_id
    return await proxy_request("instagram", "/api/v1/instagram/v3/get_post_info", params=params, json_body=body)

@router.get("/get_post_info_by_code")
async def get_post_info_by_code(
    code: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取帖子详情(code)/Get post info by shortcode"""
    body = await request.json()
    params: dict[str, Any] = {}
    if code is not None:
        params["code"] = code
    return await proxy_request("instagram", "/api/v1/instagram/v3/get_post_info_by_code", params=params, json_body=body)

@router.get("/get_post_comments")
async def get_post_comments(
    code: str,
    request: Request,
    min_id: str | None = None,
    sort_order: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取帖子评论/Get post comments"""
    body = await request.json()
    params: dict[str, Any] = {}
    if code is not None:
        params["code"] = code
    if min_id is not None:
        params["min_id"] = min_id
    if sort_order is not None:
        params["sort_order"] = sort_order
    return await proxy_request("instagram", "/api/v1/instagram/v3/get_post_comments", params=params, json_body=body)

@router.get("/get_comment_replies")
async def get_comment_replies(
    media_id: str,
    comment_id: str,
    request: Request,
    min_id: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取评论的子评论/回复/Get comment replies"""
    body = await request.json()
    params: dict[str, Any] = {}
    if media_id is not None:
        params["media_id"] = media_id
    if comment_id is not None:
        params["comment_id"] = comment_id
    if min_id is not None:
        params["min_id"] = min_id
    return await proxy_request("instagram", "/api/v1/instagram/v3/get_comment_replies", params=params, json_body=body)

@router.get("/get_post_oembed")
async def get_post_oembed(
    url: str,
    request: Request,
    hidecaption: bool | None = None,
    maxwidth: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取帖子oEmbed内嵌信息/Get post oEmbed info"""
    body = await request.json()
    params: dict[str, Any] = {}
    if url is not None:
        params["url"] = url
    if hidecaption is not None:
        params["hidecaption"] = hidecaption
    if maxwidth is not None:
        params["maxwidth"] = maxwidth
    return await proxy_request("instagram", "/api/v1/instagram/v3/get_post_oembed", params=params, json_body=body)

@router.get("/translate_comment")
async def translate_comment(
    comment_id: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """翻译评论/帖子文本/Translate comment or caption"""
    body = await request.json()
    params: dict[str, Any] = {}
    if comment_id is not None:
        params["comment_id"] = comment_id
    return await proxy_request("instagram", "/api/v1/instagram/v3/translate_comment", params=params, json_body=body)

@router.get("/bulk_translate_comments")
async def bulk_translate_comments(
    comment_ids: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """批量翻译评论/Bulk translate comments"""
    body = await request.json()
    params: dict[str, Any] = {}
    if comment_ids is not None:
        params["comment_ids"] = comment_ids
    return await proxy_request("instagram", "/api/v1/instagram/v3/bulk_translate_comments", params=params, json_body=body)

@router.get("/get_explore")
async def get_explore(
    request: Request,
    max_id: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取探索页推荐帖子/Get explore feed"""
    body = await request.json()
    params: dict[str, Any] = {}
    if max_id is not None:
        params["max_id"] = max_id
    return await proxy_request("instagram", "/api/v1/instagram/v3/get_explore", params=params, json_body=body)

@router.get("/get_user_following")
async def get_user_following(
    request: Request,
    user_id: str | None = None,
    username: str | None = None,
    count: int | None = None,
    max_id: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户关注列表/Get user following list"""
    body = await request.json()
    params: dict[str, Any] = {}
    if user_id is not None:
        params["user_id"] = user_id
    if username is not None:
        params["username"] = username
    if count is not None:
        params["count"] = count
    if max_id is not None:
        params["max_id"] = max_id
    return await proxy_request("instagram", "/api/v1/instagram/v3/get_user_following", params=params, json_body=body)

@router.get("/get_user_followers")
async def get_user_followers(
    request: Request,
    user_id: str | None = None,
    username: str | None = None,
    count: int | None = None,
    max_id: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户粉丝列表/Get user followers list"""
    body = await request.json()
    params: dict[str, Any] = {}
    if user_id is not None:
        params["user_id"] = user_id
    if username is not None:
        params["username"] = username
    if count is not None:
        params["count"] = count
    if max_id is not None:
        params["max_id"] = max_id
    return await proxy_request("instagram", "/api/v1/instagram/v3/get_user_followers", params=params, json_body=body)

@router.get("/get_location_info")
async def get_location_info(
    location_id: str,
    request: Request,
    show_nearby: bool | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取地点详情/Get location info"""
    body = await request.json()
    params: dict[str, Any] = {}
    if location_id is not None:
        params["location_id"] = location_id
    if show_nearby is not None:
        params["show_nearby"] = show_nearby
    return await proxy_request("instagram", "/api/v1/instagram/v3/get_location_info", params=params, json_body=body)

@router.get("/get_location_posts")
async def get_location_posts(
    location_id: str,
    request: Request,
    tab: str | None = None,
    first: int | None = None,
    after: str | None = None,
    page_size_override: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取地点相关帖子/Get location posts"""
    body = await request.json()
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
    return await proxy_request("instagram", "/api/v1/instagram/v3/get_location_posts", params=params, json_body=body)

@router.get("/get_location_nearby")
async def get_location_nearby(
    location_id: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取地点附近内容/Get nearby location content"""
    body = await request.json()
    params: dict[str, Any] = {}
    if location_id is not None:
        params["location_id"] = location_id
    return await proxy_request("instagram", "/api/v1/instagram/v3/get_location_nearby", params=params, json_body=body)

@router.get("/shortcode_to_media_id")
async def shortcode_to_media_id(
    shortcode: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """短码转媒体ID/Convert shortcode to media ID"""
    body = await request.json()
    params: dict[str, Any] = {}
    if shortcode is not None:
        params["shortcode"] = shortcode
    return await proxy_request("instagram", "/api/v1/instagram/v3/shortcode_to_media_id", params=params, json_body=body)

@router.get("/media_id_to_shortcode")
async def media_id_to_shortcode(
    media_id: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """媒体ID转短码/Convert media ID to shortcode"""
    body = await request.json()
    params: dict[str, Any] = {}
    if media_id is not None:
        params["media_id"] = media_id
    return await proxy_request("instagram", "/api/v1/instagram/v3/media_id_to_shortcode", params=params, json_body=body)

@router.get("/extract_shortcode")
async def extract_shortcode(
    url: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """从URL提取短码/Extract shortcode from URL"""
    body = await request.json()
    params: dict[str, Any] = {}
    if url is not None:
        params["url"] = url
    return await proxy_request("instagram", "/api/v1/instagram/v3/extract_shortcode", params=params, json_body=body)
