"""Auto-generated routes for Reddit-APP-API."""

from __future__ import annotations

from typing import Any

from fastapi import APIRouter, Depends, Request

from socialmedia_hub.server._core import proxy_request, verify_api_key

router = APIRouter(prefix="/api/v1/reddit/app", tags=["reddit_app"])

@router.get("/fetch_home_feed")
async def fetch_home_feed(
    request: Request,
    sort: str | None = None,
    filter_posts: str | None = None,
    after: str | None = None,
    need_format: bool | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取Reddit APP首页推荐内容/Fetch Reddit APP Home Feed"""
    body = await request.json()
    params: dict[str, Any] = {}
    if sort is not None:
        params["sort"] = sort
    if filter_posts is not None:
        params["filter_posts"] = filter_posts
    if after is not None:
        params["after"] = after
    if need_format is not None:
        params["need_format"] = need_format
    return await proxy_request("reddit", "/api/v1/reddit/app/fetch_home_feed", params=params, json_body=body)

@router.get("/fetch_popular_feed")
async def fetch_popular_feed(
    request: Request,
    sort: str | None = None,
    time: str | None = None,
    filter_posts: str | None = None,
    after: str | None = None,
    need_format: bool | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取Reddit APP流行推荐内容/Fetch Reddit APP Popular Feed"""
    body = await request.json()
    params: dict[str, Any] = {}
    if sort is not None:
        params["sort"] = sort
    if time is not None:
        params["time"] = time
    if filter_posts is not None:
        params["filter_posts"] = filter_posts
    if after is not None:
        params["after"] = after
    if need_format is not None:
        params["need_format"] = need_format
    return await proxy_request("reddit", "/api/v1/reddit/app/fetch_popular_feed", params=params, json_body=body)

@router.get("/fetch_games_feed")
async def fetch_games_feed(
    request: Request,
    sort: str | None = None,
    time: str | None = None,
    after: str | None = None,
    need_format: bool | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取Reddit APP游戏推荐内容/Fetch Reddit APP Games Feed"""
    body = await request.json()
    params: dict[str, Any] = {}
    if sort is not None:
        params["sort"] = sort
    if time is not None:
        params["time"] = time
    if after is not None:
        params["after"] = after
    if need_format is not None:
        params["need_format"] = need_format
    return await proxy_request("reddit", "/api/v1/reddit/app/fetch_games_feed", params=params, json_body=body)

@router.get("/fetch_news_feed")
async def fetch_news_feed(
    request: Request,
    subtopic_ids: str | None = None,
    after: str | None = None,
    need_format: bool | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取Reddit APP资讯推荐内容/Fetch Reddit APP News Feed"""
    body = await request.json()
    params: dict[str, Any] = {}
    if subtopic_ids is not None:
        params["subtopic_ids"] = subtopic_ids
    if after is not None:
        params["after"] = after
    if need_format is not None:
        params["need_format"] = need_format
    return await proxy_request("reddit", "/api/v1/reddit/app/fetch_news_feed", params=params, json_body=body)

@router.get("/fetch_post_details")
async def fetch_post_details(
    post_id: str,
    request: Request,
    include_comment_id: bool | None = None,
    comment_id: str | None = None,
    need_format: bool | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取单个Reddit帖子详情/Fetch Single Reddit Post Details"""
    body = await request.json()
    params: dict[str, Any] = {}
    if post_id is not None:
        params["post_id"] = post_id
    if include_comment_id is not None:
        params["include_comment_id"] = include_comment_id
    if comment_id is not None:
        params["comment_id"] = comment_id
    if need_format is not None:
        params["need_format"] = need_format
    return await proxy_request("reddit", "/api/v1/reddit/app/fetch_post_details", params=params, json_body=body)

@router.get("/fetch_post_details_batch")
async def fetch_post_details_batch(
    post_ids: str,
    request: Request,
    include_comment_id: bool | None = None,
    comment_id: str | None = None,
    need_format: bool | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """批量获取Reddit帖子详情(最多5条)/Fetch Reddit Post Details in Batch (Max 5)"""
    body = await request.json()
    params: dict[str, Any] = {}
    if post_ids is not None:
        params["post_ids"] = post_ids
    if include_comment_id is not None:
        params["include_comment_id"] = include_comment_id
    if comment_id is not None:
        params["comment_id"] = comment_id
    if need_format is not None:
        params["need_format"] = need_format
    return await proxy_request("reddit", "/api/v1/reddit/app/fetch_post_details_batch", params=params, json_body=body)

@router.get("/fetch_post_details_batch_large")
async def fetch_post_details_batch_large(
    post_ids: str,
    request: Request,
    include_comment_id: bool | None = None,
    comment_id: str | None = None,
    need_format: bool | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """大批量获取Reddit帖子详情(最多30条)/Fetch Reddit Post Details in Large Batch (Max 30)"""
    body = await request.json()
    params: dict[str, Any] = {}
    if post_ids is not None:
        params["post_ids"] = post_ids
    if include_comment_id is not None:
        params["include_comment_id"] = include_comment_id
    if comment_id is not None:
        params["comment_id"] = comment_id
    if need_format is not None:
        params["need_format"] = need_format
    return await proxy_request("reddit", "/api/v1/reddit/app/fetch_post_details_batch_large", params=params, json_body=body)

@router.get("/fetch_post_comments")
async def fetch_post_comments(
    post_id: str,
    request: Request,
    sort_type: str | None = None,
    after: str | None = None,
    need_format: bool | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取Reddit APP帖子评论/Fetch Reddit APP Post Comments"""
    body = await request.json()
    params: dict[str, Any] = {}
    if post_id is not None:
        params["post_id"] = post_id
    if sort_type is not None:
        params["sort_type"] = sort_type
    if after is not None:
        params["after"] = after
    if need_format is not None:
        params["need_format"] = need_format
    return await proxy_request("reddit", "/api/v1/reddit/app/fetch_post_comments", params=params, json_body=body)

@router.get("/fetch_comment_replies")
async def fetch_comment_replies(
    post_id: str,
    cursor: str,
    request: Request,
    sort_type: str | None = None,
    need_format: bool | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取Reddit APP评论回复（二级评论）/Fetch Reddit APP Comment Replies (Sub-comments)"""
    body = await request.json()
    params: dict[str, Any] = {}
    if post_id is not None:
        params["post_id"] = post_id
    if cursor is not None:
        params["cursor"] = cursor
    if sort_type is not None:
        params["sort_type"] = sort_type
    if need_format is not None:
        params["need_format"] = need_format
    return await proxy_request("reddit", "/api/v1/reddit/app/fetch_comment_replies", params=params, json_body=body)

@router.get("/fetch_subreddit_style")
async def fetch_subreddit_style(
    request: Request,
    subreddit_name: str | None = None,
    need_format: bool | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取Reddit APP版块规则样式信息/Fetch Reddit APP Subreddit Rules and Style Info"""
    body = await request.json()
    params: dict[str, Any] = {}
    if subreddit_name is not None:
        params["subreddit_name"] = subreddit_name
    if need_format is not None:
        params["need_format"] = need_format
    return await proxy_request("reddit", "/api/v1/reddit/app/fetch_subreddit_style", params=params, json_body=body)

@router.get("/fetch_subreddit_post_channels")
async def fetch_subreddit_post_channels(
    request: Request,
    subreddit_name: str | None = None,
    sort: str | None = None,
    range: str | None = None,
    need_format: bool | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取Reddit APP版块帖子频道信息/Fetch Reddit APP Subreddit Post Channels"""
    body = await request.json()
    params: dict[str, Any] = {}
    if subreddit_name is not None:
        params["subreddit_name"] = subreddit_name
    if sort is not None:
        params["sort"] = sort
    if range is not None:
        params["range"] = range
    if need_format is not None:
        params["need_format"] = need_format
    return await proxy_request("reddit", "/api/v1/reddit/app/fetch_subreddit_post_channels", params=params, json_body=body)

@router.get("/fetch_subreddit_info")
async def fetch_subreddit_info(
    request: Request,
    subreddit_name: str | None = None,
    need_format: bool | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取Reddit APP版块信息/Fetch Reddit APP Subreddit Info"""
    body = await request.json()
    params: dict[str, Any] = {}
    if subreddit_name is not None:
        params["subreddit_name"] = subreddit_name
    if need_format is not None:
        params["need_format"] = need_format
    return await proxy_request("reddit", "/api/v1/reddit/app/fetch_subreddit_info", params=params, json_body=body)

@router.get("/fetch_subreddit_settings")
async def fetch_subreddit_settings(
    subreddit_id: str,
    request: Request,
    need_format: bool | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取Reddit APP版块设置/Fetch Reddit APP Subreddit Settings"""
    body = await request.json()
    params: dict[str, Any] = {}
    if subreddit_id is not None:
        params["subreddit_id"] = subreddit_id
    if need_format is not None:
        params["need_format"] = need_format
    return await proxy_request("reddit", "/api/v1/reddit/app/fetch_subreddit_settings", params=params, json_body=body)

@router.get("/fetch_search_typeahead")
async def fetch_search_typeahead(
    query: str,
    request: Request,
    safe_search: str | None = None,
    allow_nsfw: str | None = None,
    need_format: bool | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取Reddit APP搜索自动补全建议/Fetch Reddit APP Search Typeahead Suggestions"""
    body = await request.json()
    params: dict[str, Any] = {}
    if query is not None:
        params["query"] = query
    if safe_search is not None:
        params["safe_search"] = safe_search
    if allow_nsfw is not None:
        params["allow_nsfw"] = allow_nsfw
    if need_format is not None:
        params["need_format"] = need_format
    return await proxy_request("reddit", "/api/v1/reddit/app/fetch_search_typeahead", params=params, json_body=body)

@router.get("/fetch_dynamic_search")
async def fetch_dynamic_search(
    query: str,
    request: Request,
    search_type: str | None = None,
    sort: str | None = None,
    time_range: str | None = None,
    safe_search: str | None = None,
    allow_nsfw: str | None = None,
    after: str | None = None,
    need_format: bool | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取Reddit APP动态搜索结果/Fetch Reddit APP Dynamic Search Results"""
    body = await request.json()
    params: dict[str, Any] = {}
    if query is not None:
        params["query"] = query
    if search_type is not None:
        params["search_type"] = search_type
    if sort is not None:
        params["sort"] = sort
    if time_range is not None:
        params["time_range"] = time_range
    if safe_search is not None:
        params["safe_search"] = safe_search
    if allow_nsfw is not None:
        params["allow_nsfw"] = allow_nsfw
    if after is not None:
        params["after"] = after
    if need_format is not None:
        params["need_format"] = need_format
    return await proxy_request("reddit", "/api/v1/reddit/app/fetch_dynamic_search", params=params, json_body=body)

@router.get("/fetch_community_highlights")
async def fetch_community_highlights(
    subreddit_id: str,
    request: Request,
    need_format: bool | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取Reddit APP社区亮点/Fetch Reddit APP Community Highlights"""
    body = await request.json()
    params: dict[str, Any] = {}
    if subreddit_id is not None:
        params["subreddit_id"] = subreddit_id
    if need_format is not None:
        params["need_format"] = need_format
    return await proxy_request("reddit", "/api/v1/reddit/app/fetch_community_highlights", params=params, json_body=body)

@router.get("/fetch_trending_searches")
async def fetch_trending_searches(
    request: Request,
    need_format: bool | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取Reddit APP今日热门搜索/Fetch Reddit APP Trending Searches"""
    body = await request.json()
    params: dict[str, Any] = {}
    if need_format is not None:
        params["need_format"] = need_format
    return await proxy_request("reddit", "/api/v1/reddit/app/fetch_trending_searches", params=params, json_body=body)

@router.get("/fetch_user_profile")
async def fetch_user_profile(
    username: str,
    request: Request,
    need_format: bool | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取Reddit APP用户资料信息/Fetch Reddit APP User Profile"""
    body = await request.json()
    params: dict[str, Any] = {}
    if username is not None:
        params["username"] = username
    if need_format is not None:
        params["need_format"] = need_format
    return await proxy_request("reddit", "/api/v1/reddit/app/fetch_user_profile", params=params, json_body=body)

@router.get("/fetch_user_active_subreddits")
async def fetch_user_active_subreddits(
    username: str,
    request: Request,
    need_format: bool | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户活跃的社区列表/Fetch User's Active Subreddits"""
    body = await request.json()
    params: dict[str, Any] = {}
    if username is not None:
        params["username"] = username
    if need_format is not None:
        params["need_format"] = need_format
    return await proxy_request("reddit", "/api/v1/reddit/app/fetch_user_active_subreddits", params=params, json_body=body)

@router.get("/fetch_user_comments")
async def fetch_user_comments(
    username: str,
    request: Request,
    sort: str | None = None,
    page_size: int | None = None,
    after: str | None = None,
    need_format: bool | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户评论列表/Fetch User Comments"""
    body = await request.json()
    params: dict[str, Any] = {}
    if username is not None:
        params["username"] = username
    if sort is not None:
        params["sort"] = sort
    if page_size is not None:
        params["page_size"] = page_size
    if after is not None:
        params["after"] = after
    if need_format is not None:
        params["need_format"] = need_format
    return await proxy_request("reddit", "/api/v1/reddit/app/fetch_user_comments", params=params, json_body=body)

@router.get("/fetch_user_posts")
async def fetch_user_posts(
    username: str,
    request: Request,
    sort: str | None = None,
    after: str | None = None,
    need_format: bool | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户发布的帖子列表/Fetch User Posts"""
    body = await request.json()
    params: dict[str, Any] = {}
    if username is not None:
        params["username"] = username
    if sort is not None:
        params["sort"] = sort
    if after is not None:
        params["after"] = after
    if need_format is not None:
        params["need_format"] = need_format
    return await proxy_request("reddit", "/api/v1/reddit/app/fetch_user_posts", params=params, json_body=body)

@router.get("/fetch_subreddit_feed")
async def fetch_subreddit_feed(
    subreddit_name: str,
    request: Request,
    sort: str | None = None,
    filter_posts: str | None = None,
    after: str | None = None,
    need_format: bool | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取Reddit APP版块Feed内容/Fetch Reddit APP Subreddit Feed"""
    body = await request.json()
    params: dict[str, Any] = {}
    if subreddit_name is not None:
        params["subreddit_name"] = subreddit_name
    if sort is not None:
        params["sort"] = sort
    if filter_posts is not None:
        params["filter_posts"] = filter_posts
    if after is not None:
        params["after"] = after
    if need_format is not None:
        params["need_format"] = need_format
    return await proxy_request("reddit", "/api/v1/reddit/app/fetch_subreddit_feed", params=params, json_body=body)

@router.get("/check_subreddit_muted")
async def check_subreddit_muted(
    subreddit_id: str,
    request: Request,
    need_format: bool | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """检查版块是否静音/Check if Subreddit is Muted"""
    body = await request.json()
    params: dict[str, Any] = {}
    if subreddit_id is not None:
        params["subreddit_id"] = subreddit_id
    if need_format is not None:
        params["need_format"] = need_format
    return await proxy_request("reddit", "/api/v1/reddit/app/check_subreddit_muted", params=params, json_body=body)

@router.get("/fetch_user_trophies")
async def fetch_user_trophies(
    username: str,
    request: Request,
    need_format: bool | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户公开奖杯/Fetch User Public Trophies"""
    body = await request.json()
    params: dict[str, Any] = {}
    if username is not None:
        params["username"] = username
    if need_format is not None:
        params["need_format"] = need_format
    return await proxy_request("reddit", "/api/v1/reddit/app/fetch_user_trophies", params=params, json_body=body)
