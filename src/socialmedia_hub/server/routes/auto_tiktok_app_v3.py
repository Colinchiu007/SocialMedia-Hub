"""Auto-generated routes for TikTok-App-V3-API."""

from __future__ import annotations

from typing import Any

from fastapi import APIRouter, Depends, Request

from socialmedia_hub.server._core import proxy_request, verify_api_key

router = APIRouter(prefix="/api/v1/tiktok/app/v3", tags=["tiktok_app_v3"])

@router.get("/fetch_one_video")
async def fetch_one_video(
    aweme_id: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取单个作品数据/Get single video data"""
    body = await request.json()
    params: dict[str, Any] = {}
    if aweme_id is not None:
        params["aweme_id"] = aweme_id
    return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_one_video", params=params, json_body=body)

@router.get("/fetch_one_video_v2")
async def fetch_one_video_v2(
    aweme_id: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取单个作品数据 V2/Get single video data V2"""
    body = await request.json()
    params: dict[str, Any] = {}
    if aweme_id is not None:
        params["aweme_id"] = aweme_id
    return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_one_video_v2", params=params, json_body=body)

@router.get("/fetch_one_video_v3")
async def fetch_one_video_v3(
    aweme_id: str,
    request: Request,
    region: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取单个作品数据 V3(支持国家参数)/Get single video data V3 (support country parameter)"""
    body = await request.json()
    params: dict[str, Any] = {}
    if aweme_id is not None:
        params["aweme_id"] = aweme_id
    if region is not None:
        params["region"] = region
    return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_one_video_v3", params=params, json_body=body)

@router.post("/fetch_multi_video")
async def fetch_multi_video(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """批量获取视频信息/Batch Get Video Information"""
    body = await request.json()
    return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_multi_video", json_body=body)

@router.post("/fetch_multi_video_v2")
async def fetch_multi_video_v2(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """批量获取视频信息 V2/Batch Get Video Information V2"""
    body = await request.json()
    return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_multi_video_v2", json_body=body)

@router.get("/fetch_one_video_by_share_url_v2")
async def fetch_one_video_by_share_url_v2(
    share_url: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """根据分享链接获取单个作品数据/Get single video data by sharing link"""
    body = await request.json()
    params: dict[str, Any] = {}
    if share_url is not None:
        params["share_url"] = share_url
    return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_one_video_by_share_url_v2", params=params, json_body=body)

@router.get("/fetch_one_video_by_share_url")
async def fetch_one_video_by_share_url(
    share_url: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """根据分享链接获取单个作品数据/Get single video data by sharing link"""
    body = await request.json()
    params: dict[str, Any] = {}
    if share_url is not None:
        params["share_url"] = share_url
    return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_one_video_by_share_url", params=params, json_body=body)

@router.get("/get_user_id_and_sec_user_id_by_username")
async def get_user_id_and_sec_user_id_by_username(
    username: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """使用用户名获取用户 user_id 和 sec_user_id/Get user_id and sec_user_id by Username"""
    body = await request.json()
    params: dict[str, Any] = {}
    if username is not None:
        params["username"] = username
    return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/get_user_id_and_sec_user_id_by_username", params=params, json_body=body)

@router.get("/handler_user_profile")
async def handler_user_profile(
    request: Request,
    user_id: str | None = None,
    sec_user_id: str | None = None,
    unique_id: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取指定用户的信息/Get information of specified user"""
    body = await request.json()
    params: dict[str, Any] = {}
    if user_id is not None:
        params["user_id"] = user_id
    if sec_user_id is not None:
        params["sec_user_id"] = sec_user_id
    if unique_id is not None:
        params["unique_id"] = unique_id
    return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/handler_user_profile", params=params, json_body=body)

@router.get("/fetch_webcast_user_info")
async def fetch_webcast_user_info(
    request: Request,
    user_id: str | None = None,
    sec_user_id: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取指定 Webcast 用户的信息/Get information of specified Webcast user"""
    body = await request.json()
    params: dict[str, Any] = {}
    if user_id is not None:
        params["user_id"] = user_id
    if sec_user_id is not None:
        params["sec_user_id"] = sec_user_id
    return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_webcast_user_info", params=params, json_body=body)

@router.get("/fetch_user_country_by_username")
async def fetch_user_country_by_username(
    username: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """通过用户名获取用户账号国家地区/Get user account country by username"""
    body = await request.json()
    params: dict[str, Any] = {}
    if username is not None:
        params["username"] = username
    return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_user_country_by_username", params=params, json_body=body)

@router.get("/fetch_similar_user_recommendations")
async def fetch_similar_user_recommendations(
    sec_uid: str,
    request: Request,
    page_token: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取类似用户推荐/Similar User Recommendations"""
    body = await request.json()
    params: dict[str, Any] = {}
    if sec_uid is not None:
        params["sec_uid"] = sec_uid
    if page_token is not None:
        params["page_token"] = page_token
    return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_similar_user_recommendations", params=params, json_body=body)

@router.get("/fetch_user_repost_videos")
async def fetch_user_repost_videos(
    user_id: int,
    request: Request,
    offset: int | None = None,
    count: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户转发的作品数据/Get user repost video data"""
    body = await request.json()
    params: dict[str, Any] = {}
    if user_id is not None:
        params["user_id"] = user_id
    if offset is not None:
        params["offset"] = offset
    if count is not None:
        params["count"] = count
    return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_user_repost_videos", params=params, json_body=body)

@router.get("/fetch_user_post_videos")
async def fetch_user_post_videos(
    request: Request,
    sec_user_id: str | None = None,
    unique_id: str | None = None,
    max_cursor: int | None = None,
    count: int | None = None,
    sort_type: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户主页作品数据 V1/Get user homepage video data V1"""
    body = await request.json()
    params: dict[str, Any] = {}
    if sec_user_id is not None:
        params["sec_user_id"] = sec_user_id
    if unique_id is not None:
        params["unique_id"] = unique_id
    if max_cursor is not None:
        params["max_cursor"] = max_cursor
    if count is not None:
        params["count"] = count
    if sort_type is not None:
        params["sort_type"] = sort_type
    return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_user_post_videos", params=params, json_body=body)

@router.get("/fetch_user_post_videos_v2")
async def fetch_user_post_videos_v2(
    request: Request,
    sec_user_id: str | None = None,
    unique_id: str | None = None,
    max_cursor: int | None = None,
    count: int | None = None,
    sort_type: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户主页作品数据 V2/Get user homepage video data V2"""
    body = await request.json()
    params: dict[str, Any] = {}
    if sec_user_id is not None:
        params["sec_user_id"] = sec_user_id
    if unique_id is not None:
        params["unique_id"] = unique_id
    if max_cursor is not None:
        params["max_cursor"] = max_cursor
    if count is not None:
        params["count"] = count
    if sort_type is not None:
        params["sort_type"] = sort_type
    return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_user_post_videos_v2", params=params, json_body=body)

@router.get("/fetch_user_post_videos_v3")
async def fetch_user_post_videos_v3(
    request: Request,
    sec_user_id: str | None = None,
    unique_id: str | None = None,
    max_cursor: int | None = None,
    count: int | None = None,
    sort_type: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户主页作品数据 V3（精简数据-更快速）/Get user homepage video data V3 (simplified data - faster)"""
    body = await request.json()
    params: dict[str, Any] = {}
    if sec_user_id is not None:
        params["sec_user_id"] = sec_user_id
    if unique_id is not None:
        params["unique_id"] = unique_id
    if max_cursor is not None:
        params["max_cursor"] = max_cursor
    if count is not None:
        params["count"] = count
    if sort_type is not None:
        params["sort_type"] = sort_type
    return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_user_post_videos_v3", params=params, json_body=body)

@router.get("/fetch_user_like_videos")
async def fetch_user_like_videos(
    sec_user_id: str,
    request: Request,
    max_cursor: int | None = None,
    counts: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户喜欢作品数据/Get user like video data"""
    body = await request.json()
    params: dict[str, Any] = {}
    if sec_user_id is not None:
        params["sec_user_id"] = sec_user_id
    if max_cursor is not None:
        params["max_cursor"] = max_cursor
    if counts is not None:
        params["counts"] = counts
    return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_user_like_videos", params=params, json_body=body)

@router.get("/fetch_video_comments")
async def fetch_video_comments(
    aweme_id: str,
    request: Request,
    cursor: int | None = None,
    count: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取单个视频评论数据/Get single video comments data"""
    body = await request.json()
    params: dict[str, Any] = {}
    if aweme_id is not None:
        params["aweme_id"] = aweme_id
    if cursor is not None:
        params["cursor"] = cursor
    if count is not None:
        params["count"] = count
    return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_video_comments", params=params, json_body=body)

@router.get("/fetch_video_comment_replies")
async def fetch_video_comment_replies(
    item_id: str,
    comment_id: str,
    request: Request,
    cursor: int | None = None,
    count: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取指定视频的评论回复数据/Get comment replies data of specified video"""
    body = await request.json()
    params: dict[str, Any] = {}
    if item_id is not None:
        params["item_id"] = item_id
    if comment_id is not None:
        params["comment_id"] = comment_id
    if cursor is not None:
        params["cursor"] = cursor
    if count is not None:
        params["count"] = count
    return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_video_comment_replies", params=params, json_body=body)

@router.get("/fetch_general_search_result")
async def fetch_general_search_result(
    keyword: str,
    request: Request,
    offset: int | None = None,
    count: int | None = None,
    sort_type: int | None = None,
    publish_time: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取指定关键词的综合搜索结果/Get comprehensive search results of specified keywords"""
    body = await request.json()
    params: dict[str, Any] = {}
    if keyword is not None:
        params["keyword"] = keyword
    if offset is not None:
        params["offset"] = offset
    if count is not None:
        params["count"] = count
    if sort_type is not None:
        params["sort_type"] = sort_type
    if publish_time is not None:
        params["publish_time"] = publish_time
    return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_general_search_result", params=params, json_body=body)

@router.get("/fetch_video_search_result")
async def fetch_video_search_result(
    keyword: str,
    request: Request,
    offset: int | None = None,
    count: int | None = None,
    sort_type: int | None = None,
    publish_time: int | None = None,
    region: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取指定关键词的视频搜索结果/Get video search results of specified keywords"""
    body = await request.json()
    params: dict[str, Any] = {}
    if keyword is not None:
        params["keyword"] = keyword
    if offset is not None:
        params["offset"] = offset
    if count is not None:
        params["count"] = count
    if sort_type is not None:
        params["sort_type"] = sort_type
    if publish_time is not None:
        params["publish_time"] = publish_time
    if region is not None:
        params["region"] = region
    return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_video_search_result", params=params, json_body=body)

@router.get("/fetch_user_search_result")
async def fetch_user_search_result(
    keyword: str,
    request: Request,
    offset: int | None = None,
    count: int | None = None,
    user_search_follower_count: str | None = None,
    user_search_profile_type: str | None = None,
    user_search_other_pref: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取指定关键词的用户搜索结果/Get user search results of specified keywords"""
    body = await request.json()
    params: dict[str, Any] = {}
    if keyword is not None:
        params["keyword"] = keyword
    if offset is not None:
        params["offset"] = offset
    if count is not None:
        params["count"] = count
    if user_search_follower_count is not None:
        params["user_search_follower_count"] = user_search_follower_count
    if user_search_profile_type is not None:
        params["user_search_profile_type"] = user_search_profile_type
    if user_search_other_pref is not None:
        params["user_search_other_pref"] = user_search_other_pref
    return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_user_search_result", params=params, json_body=body)

@router.get("/fetch_music_search_result")
async def fetch_music_search_result(
    keyword: str,
    request: Request,
    offset: int | None = None,
    count: int | None = None,
    filter_by: int | None = None,
    sort_type: int | None = None,
    region: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取指定关键词的音乐搜索结果/Get music search results of specified keywords"""
    body = await request.json()
    params: dict[str, Any] = {}
    if keyword is not None:
        params["keyword"] = keyword
    if offset is not None:
        params["offset"] = offset
    if count is not None:
        params["count"] = count
    if filter_by is not None:
        params["filter_by"] = filter_by
    if sort_type is not None:
        params["sort_type"] = sort_type
    if region is not None:
        params["region"] = region
    return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_music_search_result", params=params, json_body=body)

@router.get("/fetch_hashtag_search_result")
async def fetch_hashtag_search_result(
    keyword: str,
    request: Request,
    offset: int | None = None,
    count: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取指定关键词的话题搜索结果/Get hashtag search results of specified keywords"""
    body = await request.json()
    params: dict[str, Any] = {}
    if keyword is not None:
        params["keyword"] = keyword
    if offset is not None:
        params["offset"] = offset
    if count is not None:
        params["count"] = count
    return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_hashtag_search_result", params=params, json_body=body)

@router.get("/fetch_live_search_result")
async def fetch_live_search_result(
    keyword: str,
    request: Request,
    offset: int | None = None,
    count: int | None = None,
    region: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取指定关键词的直播搜索结果/Get live search results of specified keywords"""
    body = await request.json()
    params: dict[str, Any] = {}
    if keyword is not None:
        params["keyword"] = keyword
    if offset is not None:
        params["offset"] = offset
    if count is not None:
        params["count"] = count
    if region is not None:
        params["region"] = region
    return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_live_search_result", params=params, json_body=body)

@router.get("/fetch_location_search")
async def fetch_location_search(
    keyword: str,
    request: Request,
    offset: int | None = None,
    count: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取地点搜索结果/Get location search results"""
    body = await request.json()
    params: dict[str, Any] = {}
    if keyword is not None:
        params["keyword"] = keyword
    if offset is not None:
        params["offset"] = offset
    if count is not None:
        params["count"] = count
    return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_location_search", params=params, json_body=body)

@router.get("/fetch_music_detail")
async def fetch_music_detail(
    music_id: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取指定音乐的详情数据/Get details of specified music"""
    body = await request.json()
    params: dict[str, Any] = {}
    if music_id is not None:
        params["music_id"] = music_id
    return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_music_detail", params=params, json_body=body)

@router.get("/fetch_music_video_list")
async def fetch_music_video_list(
    music_id: str,
    request: Request,
    cursor: int | None = None,
    count: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取指定音乐的视频列表数据/Get video list of specified music"""
    body = await request.json()
    params: dict[str, Any] = {}
    if music_id is not None:
        params["music_id"] = music_id
    if cursor is not None:
        params["cursor"] = cursor
    if count is not None:
        params["count"] = count
    return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_music_video_list", params=params, json_body=body)

@router.get("/fetch_hashtag_detail")
async def fetch_hashtag_detail(
    ch_id: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取指定话题的详情数据/Get details of specified hashtag"""
    body = await request.json()
    params: dict[str, Any] = {}
    if ch_id is not None:
        params["ch_id"] = ch_id
    return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_hashtag_detail", params=params, json_body=body)

@router.get("/fetch_hashtag_video_list")
async def fetch_hashtag_video_list(
    ch_id: str,
    request: Request,
    cursor: int | None = None,
    count: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取指定话题的作品数据/Get video list of specified hashtag"""
    body = await request.json()
    params: dict[str, Any] = {}
    if ch_id is not None:
        params["ch_id"] = ch_id
    if cursor is not None:
        params["cursor"] = cursor
    if count is not None:
        params["count"] = count
    return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_hashtag_video_list", params=params, json_body=body)

@router.get("/fetch_user_follower_list")
async def fetch_user_follower_list(
    request: Request,
    user_id: str | None = None,
    sec_user_id: str | None = None,
    count: int | None = None,
    min_time: int | None = None,
    page_token: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取指定用户的粉丝列表数据/Get follower list of specified user"""
    body = await request.json()
    params: dict[str, Any] = {}
    if user_id is not None:
        params["user_id"] = user_id
    if sec_user_id is not None:
        params["sec_user_id"] = sec_user_id
    if count is not None:
        params["count"] = count
    if min_time is not None:
        params["min_time"] = min_time
    if page_token is not None:
        params["page_token"] = page_token
    return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_user_follower_list", params=params, json_body=body)

@router.get("/fetch_user_following_list")
async def fetch_user_following_list(
    request: Request,
    user_id: str | None = None,
    sec_user_id: str | None = None,
    count: int | None = None,
    min_time: int | None = None,
    page_token: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取指定用户的关注列表数据/Get following list of specified user"""
    body = await request.json()
    params: dict[str, Any] = {}
    if user_id is not None:
        params["user_id"] = user_id
    if sec_user_id is not None:
        params["sec_user_id"] = sec_user_id
    if count is not None:
        params["count"] = count
    if min_time is not None:
        params["min_time"] = min_time
    if page_token is not None:
        params["page_token"] = page_token
    return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_user_following_list", params=params, json_body=body)

@router.get("/fetch_creator_search_insights")
async def fetch_creator_search_insights(
    request: Request,
    offset: int | None = None,
    limit: int | None = None,
    tab: str | None = None,
    language_filters: str | None = None,
    category_filters: str | None = None,
    creator_source: str | None = None,
    force_refresh: bool | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """创作者搜索洞察/Creator Search Insights"""
    body = await request.json()
    params: dict[str, Any] = {}
    if offset is not None:
        params["offset"] = offset
    if limit is not None:
        params["limit"] = limit
    if tab is not None:
        params["tab"] = tab
    if language_filters is not None:
        params["language_filters"] = language_filters
    if category_filters is not None:
        params["category_filters"] = category_filters
    if creator_source is not None:
        params["creator_source"] = creator_source
    if force_refresh is not None:
        params["force_refresh"] = force_refresh
    return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_creator_search_insights", params=params, json_body=body)

@router.get("/fetch_creator_search_insights_detail")
async def fetch_creator_search_insights_detail(
    query_id_str: str,
    request: Request,
    time_range: str | None = None,
    start_date: int | None = None,
    end_date: int | None = None,
    dimension_list: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """创作者搜索洞察详情/Creator Search Insights Detail"""
    body = await request.json()
    params: dict[str, Any] = {}
    if query_id_str is not None:
        params["query_id_str"] = query_id_str
    if time_range is not None:
        params["time_range"] = time_range
    if start_date is not None:
        params["start_date"] = start_date
    if end_date is not None:
        params["end_date"] = end_date
    if dimension_list is not None:
        params["dimension_list"] = dimension_list
    return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_creator_search_insights_detail", params=params, json_body=body)

@router.get("/fetch_creator_search_insights_trend")
async def fetch_creator_search_insights_trend(
    query_id_str: str,
    request: Request,
    from_tab_path: str | None = None,
    query_analysis_required: bool | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """创作者搜索洞察趋势/Creator Search Insights Trend"""
    body = await request.json()
    params: dict[str, Any] = {}
    if query_id_str is not None:
        params["query_id_str"] = query_id_str
    if from_tab_path is not None:
        params["from_tab_path"] = from_tab_path
    if query_analysis_required is not None:
        params["query_analysis_required"] = query_analysis_required
    return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_creator_search_insights_trend", params=params, json_body=body)

@router.get("/fetch_creator_search_insights_videos")
async def fetch_creator_search_insights_videos(
    keyword: str,
    request: Request,
    offset: int | None = None,
    count: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """创作者搜索洞察相关视频/Creator Search Insights Videos"""
    body = await request.json()
    params: dict[str, Any] = {}
    if keyword is not None:
        params["keyword"] = keyword
    if offset is not None:
        params["offset"] = offset
    if count is not None:
        params["count"] = count
    return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_creator_search_insights_videos", params=params, json_body=body)

@router.get("/fetch_music_chart_list")
async def fetch_music_chart_list(
    request: Request,
    scene: int | None = None,
    cursor: int | None = None,
    count: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """音乐排行榜/Music Chart List"""
    body = await request.json()
    params: dict[str, Any] = {}
    if scene is not None:
        params["scene"] = scene
    if cursor is not None:
        params["cursor"] = cursor
    if count is not None:
        params["count"] = count
    return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_music_chart_list", params=params, json_body=body)

@router.get("/search_follower_list")
async def search_follower_list(
    user_id: str,
    keyword: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """搜索粉丝列表/Search follower list"""
    body = await request.json()
    params: dict[str, Any] = {}
    if user_id is not None:
        params["user_id"] = user_id
    if keyword is not None:
        params["keyword"] = keyword
    return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/search_follower_list", params=params, json_body=body)

@router.get("/search_following_list")
async def search_following_list(
    user_id: str,
    keyword: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """搜索关注列表/Search following list"""
    body = await request.json()
    params: dict[str, Any] = {}
    if user_id is not None:
        params["user_id"] = user_id
    if keyword is not None:
        params["keyword"] = keyword
    return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/search_following_list", params=params, json_body=body)

@router.get("/fetch_live_room_info")
async def fetch_live_room_info(
    room_id: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取指定直播间的数据/Get data of specified live room"""
    body = await request.json()
    params: dict[str, Any] = {}
    if room_id is not None:
        params["room_id"] = room_id
    return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_live_room_info", params=params, json_body=body)

@router.get("/fetch_live_ranking_list")
async def fetch_live_ranking_list(
    room_id: str,
    anchor_id: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取直播间排行榜数据/Get live room ranking list"""
    body = await request.json()
    params: dict[str, Any] = {}
    if room_id is not None:
        params["room_id"] = room_id
    if anchor_id is not None:
        params["anchor_id"] = anchor_id
    return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_live_ranking_list", params=params, json_body=body)

@router.get("/check_live_room_online")
async def check_live_room_online(
    room_id: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """检测直播间是否在线/Check if live room is online"""
    body = await request.json()
    params: dict[str, Any] = {}
    if room_id is not None:
        params["room_id"] = room_id
    return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/check_live_room_online", params=params, json_body=body)

@router.post("/check_live_room_online_batch")
async def check_live_room_online_batch(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """批量检测直播间是否在线/Batch check if live rooms are online"""
    body = await request.json()
    return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/check_live_room_online_batch", json_body=body)

@router.get("/fetch_share_short_link")
async def fetch_share_short_link(
    url: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取分享短链接/Get share short link"""
    body = await request.json()
    params: dict[str, Any] = {}
    if url is not None:
        params["url"] = url
    return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_share_short_link", params=params, json_body=body)

@router.get("/fetch_share_qr_code")
async def fetch_share_qr_code(
    object_id: str,
    request: Request,
    schema_type: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取分享二维码/Get share QR code"""
    body = await request.json()
    params: dict[str, Any] = {}
    if object_id is not None:
        params["object_id"] = object_id
    if schema_type is not None:
        params["schema_type"] = schema_type
    return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_share_qr_code", params=params, json_body=body)

@router.get("/fetch_product_search")
async def fetch_product_search(
    keyword: str,
    request: Request,
    cursor: int | None = None,
    count: int | None = None,
    sort_type: int | None = None,
    customer_review_four_star: bool | None = None,
    have_discount: bool | None = None,
    min_price: str | None = None,
    max_price: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取商品搜索结果/Get product search results"""
    body = await request.json()
    params: dict[str, Any] = {}
    if keyword is not None:
        params["keyword"] = keyword
    if cursor is not None:
        params["cursor"] = cursor
    if count is not None:
        params["count"] = count
    if sort_type is not None:
        params["sort_type"] = sort_type
    if customer_review_four_star is not None:
        params["customer_review_four_star"] = customer_review_four_star
    if have_discount is not None:
        params["have_discount"] = have_discount
    if min_price is not None:
        params["min_price"] = min_price
    if max_price is not None:
        params["max_price"] = max_price
    return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_product_search", params=params, json_body=body)

@router.get("/fetch_creator_info")
async def fetch_creator_info(
    creator_uid: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取带货创作者信息/Get shopping creator information"""
    body = await request.json()
    params: dict[str, Any] = {}
    if creator_uid is not None:
        params["creator_uid"] = creator_uid
    return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_creator_info", params=params, json_body=body)

@router.get("/fetch_creator_showcase_product_list")
async def fetch_creator_showcase_product_list(
    kol_id: str,
    request: Request,
    count: int | None = None,
    next_scroll_param: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取创作者橱窗商品列表/Get creator showcase product list"""
    body = await request.json()
    params: dict[str, Any] = {}
    if kol_id is not None:
        params["kol_id"] = kol_id
    if count is not None:
        params["count"] = count
    if next_scroll_param is not None:
        params["next_scroll_param"] = next_scroll_param
    return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_creator_showcase_product_list", params=params, json_body=body)

@router.get("/fetch_shop_id_by_share_link")
async def fetch_shop_id_by_share_link(
    share_link: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """通过分享链接获取店铺ID/Get Shop ID by Share Link"""
    body = await request.json()
    params: dict[str, Any] = {}
    if share_link is not None:
        params["share_link"] = share_link
    return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_shop_id_by_share_link", params=params, json_body=body)

@router.get("/fetch_product_id_by_share_link")
async def fetch_product_id_by_share_link(
    share_link: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """通过分享链接获取商品ID/Get Product ID by Share Link"""
    body = await request.json()
    params: dict[str, Any] = {}
    if share_link is not None:
        params["share_link"] = share_link
    return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_product_id_by_share_link", params=params, json_body=body)

@router.get("/fetch_product_detail")
async def fetch_product_detail(
    product_id: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取商品详情数据（即将弃用，使用 fetch_product_detail_v2 代替）/Get product detail data (will be deprecated, use fetch_product_detail_v2 instead)"""
    body = await request.json()
    params: dict[str, Any] = {}
    if product_id is not None:
        params["product_id"] = product_id
    return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_product_detail", params=params, json_body=body)

@router.get("/fetch_product_detail_v2")
async def fetch_product_detail_v2(
    product_id: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取商品详情数据V2/Get product detail data V2"""
    body = await request.json()
    params: dict[str, Any] = {}
    if product_id is not None:
        params["product_id"] = product_id
    return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_product_detail_v2", params=params, json_body=body)

@router.get("/fetch_product_detail_v3")
async def fetch_product_detail_v3(
    product_id: str,
    request: Request,
    region: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取商品详情数据V3 / Get product detail data V3"""
    body = await request.json()
    params: dict[str, Any] = {}
    if product_id is not None:
        params["product_id"] = product_id
    if region is not None:
        params["region"] = region
    return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_product_detail_v3", params=params, json_body=body)

@router.get("/fetch_product_detail_v4")
async def fetch_product_detail_v4(
    product_id: str,
    request: Request,
    region: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取商品详情数据V4 / Get product detail data V4"""
    body = await request.json()
    params: dict[str, Any] = {}
    if product_id is not None:
        params["product_id"] = product_id
    if region is not None:
        params["region"] = region
    return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_product_detail_v4", params=params, json_body=body)

@router.get("/fetch_product_review")
async def fetch_product_review(
    product_id: str,
    request: Request,
    cursor: int | None = None,
    size: int | None = None,
    filter_id: int | None = None,
    sort_type: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取商品评价数据/Get product review data"""
    body = await request.json()
    params: dict[str, Any] = {}
    if product_id is not None:
        params["product_id"] = product_id
    if cursor is not None:
        params["cursor"] = cursor
    if size is not None:
        params["size"] = size
    if filter_id is not None:
        params["filter_id"] = filter_id
    if sort_type is not None:
        params["sort_type"] = sort_type
    return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_product_review", params=params, json_body=body)

@router.get("/fetch_shop_home_page_list")
async def fetch_shop_home_page_list(
    seller_id: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取商家主页Page列表数据/Get shop home page list data"""
    body = await request.json()
    params: dict[str, Any] = {}
    if seller_id is not None:
        params["seller_id"] = seller_id
    return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_shop_home_page_list", params=params, json_body=body)

@router.get("/fetch_shop_home")
async def fetch_shop_home(
    page_id: str,
    seller_id: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取商家主页数据/Get shop home page data"""
    body = await request.json()
    params: dict[str, Any] = {}
    if page_id is not None:
        params["page_id"] = page_id
    if seller_id is not None:
        params["seller_id"] = seller_id
    return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_shop_home", params=params, json_body=body)

@router.get("/fetch_shop_product_recommend")
async def fetch_shop_product_recommend(
    seller_id: str,
    request: Request,
    scroll_param: str | None = None,
    page_size: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取商家商品推荐数据/Get shop product recommend data"""
    body = await request.json()
    params: dict[str, Any] = {}
    if seller_id is not None:
        params["seller_id"] = seller_id
    if scroll_param is not None:
        params["scroll_param"] = scroll_param
    if page_size is not None:
        params["page_size"] = page_size
    return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_shop_product_recommend", params=params, json_body=body)

@router.get("/fetch_shop_product_list")
async def fetch_shop_product_list(
    seller_id: str,
    request: Request,
    scroll_params: str | None = None,
    page_size: int | None = None,
    sort_field: int | None = None,
    sort_order: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取商家商品列表数据/Get shop product list data"""
    body = await request.json()
    params: dict[str, Any] = {}
    if seller_id is not None:
        params["seller_id"] = seller_id
    if scroll_params is not None:
        params["scroll_params"] = scroll_params
    if page_size is not None:
        params["page_size"] = page_size
    if sort_field is not None:
        params["sort_field"] = sort_field
    if sort_order is not None:
        params["sort_order"] = sort_order
    return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_shop_product_list", params=params, json_body=body)

@router.get("/fetch_shop_product_list_v2")
async def fetch_shop_product_list_v2(
    seller_id: str,
    request: Request,
    scroll_params: str | None = None,
    page_size: int | None = None,
    sort_field: int | None = None,
    sort_order: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取商家商品列表数据 V2/Get shop product list data V2"""
    body = await request.json()
    params: dict[str, Any] = {}
    if seller_id is not None:
        params["seller_id"] = seller_id
    if scroll_params is not None:
        params["scroll_params"] = scroll_params
    if page_size is not None:
        params["page_size"] = page_size
    if sort_field is not None:
        params["sort_field"] = sort_field
    if sort_order is not None:
        params["sort_order"] = sort_order
    return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_shop_product_list_v2", params=params, json_body=body)

@router.get("/fetch_shop_info")
async def fetch_shop_info(
    shop_id: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取商家信息数据/Get shop information data"""
    body = await request.json()
    params: dict[str, Any] = {}
    if shop_id is not None:
        params["shop_id"] = shop_id
    return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_shop_info", params=params, json_body=body)

@router.get("/fetch_shop_product_category")
async def fetch_shop_product_category(
    seller_id: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取商家产品分类数据/Get shop product category data"""
    body = await request.json()
    params: dict[str, Any] = {}
    if seller_id is not None:
        params["seller_id"] = seller_id
    return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_shop_product_category", params=params, json_body=body)

@router.get("/fetch_live_daily_rank")
async def fetch_live_daily_rank(
    request: Request,
    anchor_id: str | None = None,
    room_id: str | None = None,
    rank_type: int | None = None,
    region_type: int | None = None,
    gap_interval: int | None = None,
    cookie: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取直播每日榜单数据/Get live daily rank data"""
    body = await request.json()
    params: dict[str, Any] = {}
    if anchor_id is not None:
        params["anchor_id"] = anchor_id
    if room_id is not None:
        params["room_id"] = room_id
    if rank_type is not None:
        params["rank_type"] = rank_type
    if region_type is not None:
        params["region_type"] = region_type
    if gap_interval is not None:
        params["gap_interval"] = gap_interval
    if cookie is not None:
        params["cookie"] = cookie
    return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_live_daily_rank", params=params, json_body=body)

@router.get("/fetch_user_music_list")
async def fetch_user_music_list(
    sec_uid: str,
    request: Request,
    cursor: int | None = None,
    count: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户音乐列表数据/Get user music list data"""
    body = await request.json()
    params: dict[str, Any] = {}
    if sec_uid is not None:
        params["sec_uid"] = sec_uid
    if cursor is not None:
        params["cursor"] = cursor
    if count is not None:
        params["count"] = count
    return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_user_music_list", params=params, json_body=body)

@router.post("/fetch_content_translate")
async def fetch_content_translate(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取内容翻译数据/Get content translation data"""
    body = await request.json()
    return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_content_translate", json_body=body)

@router.post("/fetch_home_feed")
async def fetch_home_feed(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取主页视频推荐数据/Get home feed(recommend) video data"""
    body = await request.json()
    return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_home_feed", json_body=body)

@router.post("/TTencrypt_algorithm")
async def TTencrypt_algorithm(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """TikTok APP加密算法/TikTok APP encryption algorithm"""
    body = await request.json()
    return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/TTencrypt_algorithm", json_body=body)

@router.get("/fetch_live_room_product_list")
async def fetch_live_room_product_list(
    room_id: str,
    author_id: str,
    request: Request,
    page_size: int | None = None,
    offset: int | None = None,
    region: str | None = None,
    cookie: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取直播间商品列表数据/Get live room product list data"""
    body = await request.json()
    params: dict[str, Any] = {}
    if room_id is not None:
        params["room_id"] = room_id
    if author_id is not None:
        params["author_id"] = author_id
    if page_size is not None:
        params["page_size"] = page_size
    if offset is not None:
        params["offset"] = offset
    if region is not None:
        params["region"] = region
    if cookie is not None:
        params["cookie"] = cookie
    return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_live_room_product_list", params=params, json_body=body)

@router.get("/fetch_live_room_product_list_v2")
async def fetch_live_room_product_list_v2(
    room_id: str,
    author_id: str,
    request: Request,
    page_size: int | None = None,
    offset: int | None = None,
    region: str | None = None,
    cookie: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取直播间商品列表数据 V2 /Get live room product list data V2"""
    body = await request.json()
    params: dict[str, Any] = {}
    if room_id is not None:
        params["room_id"] = room_id
    if author_id is not None:
        params["author_id"] = author_id
    if page_size is not None:
        params["page_size"] = page_size
    if offset is not None:
        params["offset"] = offset
    if region is not None:
        params["region"] = region
    if cookie is not None:
        params["cookie"] = cookie
    return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_live_room_product_list_v2", params=params, json_body=body)

@router.get("/add_video_play_count")
async def add_video_play_count(
    aweme_type: int,
    item_id: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """根据视频ID来增加作品的播放数/Increase the number of plays of the work according to the video ID"""
    body = await request.json()
    params: dict[str, Any] = {}
    if aweme_type is not None:
        params["aweme_type"] = aweme_type
    if item_id is not None:
        params["item_id"] = item_id
    return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/add_video_play_count", params=params, json_body=body)

@router.post("/encrypt_decrypt_login_request")
async def encrypt_decrypt_login_request(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """加密或解密 TikTok APP 登录请求体/Encrypt or Decrypt TikTok APP login request body"""
    body = await request.json()
    return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/encrypt_decrypt_login_request", json_body=body)

@router.get("/open_tiktok_app_to_video_detail")
async def open_tiktok_app_to_video_detail(
    aweme_id: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """生成TikTok分享链接，唤起TikTok APP，跳转指定作品详情页/Generate TikTok share link, call TikTok APP, and jump to the specified video details page"""
    body = await request.json()
    params: dict[str, Any] = {}
    if aweme_id is not None:
        params["aweme_id"] = aweme_id
    return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/open_tiktok_app_to_video_detail", params=params, json_body=body)

@router.get("/open_tiktok_app_to_user_profile")
async def open_tiktok_app_to_user_profile(
    uid: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """生成TikTok分享链接，唤起TikTok APP，跳转指定用户主页/Generate TikTok share link, call TikTok APP, and jump to the specified user profile"""
    body = await request.json()
    params: dict[str, Any] = {}
    if uid is not None:
        params["uid"] = uid
    return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/open_tiktok_app_to_user_profile", params=params, json_body=body)

@router.get("/open_tiktok_app_to_keyword_search")
async def open_tiktok_app_to_keyword_search(
    keyword: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """生成TikTok分享链接，唤起TikTok APP，跳转指定关键词搜索结果/Generate TikTok share link, call TikTok APP, and jump to the specified keyword search result"""
    body = await request.json()
    params: dict[str, Any] = {}
    if keyword is not None:
        params["keyword"] = keyword
    return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/open_tiktok_app_to_keyword_search", params=params, json_body=body)

@router.get("/open_tiktok_app_to_send_private_message")
async def open_tiktok_app_to_send_private_message(
    uid: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """生成TikTok分享链接，唤起TikTok APP，给指定用户发送私信/Generate TikTok share link, call TikTok APP, and send private messages to specified users"""
    body = await request.json()
    params: dict[str, Any] = {}
    if uid is not None:
        params["uid"] = uid
    return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/open_tiktok_app_to_send_private_message", params=params, json_body=body)
