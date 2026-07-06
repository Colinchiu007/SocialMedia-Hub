"""Auto-generated routes for TikTok-App-V3-API."""

from __future__ import annotations

from typing import Any

from fastapi import APIRouter, Depends, Request

from socialmedia_hub.server._core import proxy_request, verify_api_key

router = APIRouter(prefix="/api/v1/tiktok/app/v3", tags=["tiktok_app_v3"])

@router.get("/fetch_one_video")
async def fetch_one_video(
    aweme_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取单个作品数据/Get single video data"""
        params: dict[str, Any] = {}
        if aweme_id is not None:
            params["aweme_id"] = aweme_id
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_one_video", json_body=body)

@router.get("/fetch_one_video_v2")
async def fetch_one_video_v2(
    aweme_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取单个作品数据 V2/Get single video data V2"""
        params: dict[str, Any] = {}
        if aweme_id is not None:
            params["aweme_id"] = aweme_id
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_one_video_v2", json_body=body)

@router.get("/fetch_one_video_v3")
async def fetch_one_video_v3(
    region: str | None = None,
    aweme_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取单个作品数据 V3(支持国家参数)/Get single video data V3 (support country parameter)"""
        params: dict[str, Any] = {}
        if aweme_id is not None:
            params["aweme_id"] = aweme_id
        if region is not None:
            params["region"] = region
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_one_video_v3", json_body=body)

@router.post("/fetch_multi_video")
async def fetch_multi_video(
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """批量获取视频信息/Batch Get Video Information"""
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_multi_video", json_body=body)

@router.post("/fetch_multi_video_v2")
async def fetch_multi_video_v2(
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """批量获取视频信息 V2/Batch Get Video Information V2"""
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_multi_video_v2", json_body=body)

@router.get("/fetch_one_video_by_share_url_v2")
async def fetch_one_video_by_share_url_v2(
    share_url: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """根据分享链接获取单个作品数据/Get single video data by sharing link"""
        params: dict[str, Any] = {}
        if share_url is not None:
            params["share_url"] = share_url
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_one_video_by_share_url_v2", json_body=body)

@router.get("/fetch_one_video_by_share_url")
async def fetch_one_video_by_share_url(
    share_url: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """根据分享链接获取单个作品数据/Get single video data by sharing link"""
        params: dict[str, Any] = {}
        if share_url is not None:
            params["share_url"] = share_url
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_one_video_by_share_url", json_body=body)

@router.get("/get_user_id_and_sec_user_id_by_username")
async def get_user_id_and_sec_user_id_by_username(
    username: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """使用用户名获取用户 user_id 和 sec_user_id/Get user_id and sec_user_id by Username"""
        params: dict[str, Any] = {}
        if username is not None:
            params["username"] = username
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/get_user_id_and_sec_user_id_by_username", json_body=body)

@router.get("/handler_user_profile")
async def handler_user_profile(
    unique_id: str | None = None,
    sec_user_id: str | None = None,
    user_id: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取指定用户的信息/Get information of specified user"""
        params: dict[str, Any] = {}
        if user_id is not None:
            params["user_id"] = user_id
        if sec_user_id is not None:
            params["sec_user_id"] = sec_user_id
        if unique_id is not None:
            params["unique_id"] = unique_id
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/handler_user_profile", json_body=body)

@router.get("/fetch_webcast_user_info")
async def fetch_webcast_user_info(
    sec_user_id: str | None = None,
    user_id: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取指定 Webcast 用户的信息/Get information of specified Webcast user"""
        params: dict[str, Any] = {}
        if user_id is not None:
            params["user_id"] = user_id
        if sec_user_id is not None:
            params["sec_user_id"] = sec_user_id
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_webcast_user_info", json_body=body)

@router.get("/fetch_user_country_by_username")
async def fetch_user_country_by_username(
    username: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """通过用户名获取用户账号国家地区/Get user account country by username"""
        params: dict[str, Any] = {}
        if username is not None:
            params["username"] = username
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_user_country_by_username", json_body=body)

@router.get("/fetch_similar_user_recommendations")
async def fetch_similar_user_recommendations(
    page_token: str | None = None,
    sec_uid: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取类似用户推荐/Similar User Recommendations"""
        params: dict[str, Any] = {}
        if sec_uid is not None:
            params["sec_uid"] = sec_uid
        if page_token is not None:
            params["page_token"] = page_token
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_similar_user_recommendations", json_body=body)

@router.get("/fetch_user_repost_videos")
async def fetch_user_repost_videos(
    count: int | None = None,
    offset: int | None = None,
    user_id: int,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户转发的作品数据/Get user repost video data"""
        params: dict[str, Any] = {}
        if user_id is not None:
            params["user_id"] = user_id
        if offset is not None:
            params["offset"] = offset
        if count is not None:
            params["count"] = count
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_user_repost_videos", json_body=body)

@router.get("/fetch_user_post_videos")
async def fetch_user_post_videos(
    sort_type: int | None = None,
    count: int | None = None,
    max_cursor: int | None = None,
    unique_id: str | None = None,
    sec_user_id: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户主页作品数据 V1/Get user homepage video data V1"""
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
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_user_post_videos", json_body=body)

@router.get("/fetch_user_post_videos_v2")
async def fetch_user_post_videos_v2(
    sort_type: int | None = None,
    count: int | None = None,
    max_cursor: int | None = None,
    unique_id: str | None = None,
    sec_user_id: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户主页作品数据 V2/Get user homepage video data V2"""
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
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_user_post_videos_v2", json_body=body)

@router.get("/fetch_user_post_videos_v3")
async def fetch_user_post_videos_v3(
    sort_type: int | None = None,
    count: int | None = None,
    max_cursor: int | None = None,
    unique_id: str | None = None,
    sec_user_id: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户主页作品数据 V3（精简数据-更快速）/Get user homepage video data V3 (simplified data - faster)"""
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
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_user_post_videos_v3", json_body=body)

@router.get("/fetch_user_like_videos")
async def fetch_user_like_videos(
    counts: int | None = None,
    max_cursor: int | None = None,
    sec_user_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户喜欢作品数据/Get user like video data"""
        params: dict[str, Any] = {}
        if sec_user_id is not None:
            params["sec_user_id"] = sec_user_id
        if max_cursor is not None:
            params["max_cursor"] = max_cursor
        if counts is not None:
            params["counts"] = counts
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_user_like_videos", json_body=body)

@router.get("/fetch_video_comments")
async def fetch_video_comments(
    count: int | None = None,
    cursor: int | None = None,
    aweme_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取单个视频评论数据/Get single video comments data"""
        params: dict[str, Any] = {}
        if aweme_id is not None:
            params["aweme_id"] = aweme_id
        if cursor is not None:
            params["cursor"] = cursor
        if count is not None:
            params["count"] = count
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_video_comments", json_body=body)

@router.get("/fetch_video_comment_replies")
async def fetch_video_comment_replies(
    count: int | None = None,
    cursor: int | None = None,
    comment_id: str,
    item_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取指定视频的评论回复数据/Get comment replies data of specified video"""
        params: dict[str, Any] = {}
        if item_id is not None:
            params["item_id"] = item_id
        if comment_id is not None:
            params["comment_id"] = comment_id
        if cursor is not None:
            params["cursor"] = cursor
        if count is not None:
            params["count"] = count
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_video_comment_replies", json_body=body)

@router.get("/fetch_general_search_result")
async def fetch_general_search_result(
    publish_time: int | None = None,
    sort_type: int | None = None,
    count: int | None = None,
    offset: int | None = None,
    keyword: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取指定关键词的综合搜索结果/Get comprehensive search results of specified keywords"""
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
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_general_search_result", json_body=body)

@router.get("/fetch_video_search_result")
async def fetch_video_search_result(
    region: str | None = None,
    publish_time: int | None = None,
    sort_type: int | None = None,
    count: int | None = None,
    offset: int | None = None,
    keyword: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取指定关键词的视频搜索结果/Get video search results of specified keywords"""
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
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_video_search_result", json_body=body)

@router.get("/fetch_user_search_result")
async def fetch_user_search_result(
    user_search_other_pref: str | None = None,
    user_search_profile_type: str | None = None,
    user_search_follower_count: str | None = None,
    count: int | None = None,
    offset: int | None = None,
    keyword: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取指定关键词的用户搜索结果/Get user search results of specified keywords"""
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
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_user_search_result", json_body=body)

@router.get("/fetch_music_search_result")
async def fetch_music_search_result(
    region: str | None = None,
    sort_type: int | None = None,
    filter_by: int | None = None,
    count: int | None = None,
    offset: int | None = None,
    keyword: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取指定关键词的音乐搜索结果/Get music search results of specified keywords"""
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
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_music_search_result", json_body=body)

@router.get("/fetch_hashtag_search_result")
async def fetch_hashtag_search_result(
    count: int | None = None,
    offset: int | None = None,
    keyword: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取指定关键词的话题搜索结果/Get hashtag search results of specified keywords"""
        params: dict[str, Any] = {}
        if keyword is not None:
            params["keyword"] = keyword
        if offset is not None:
            params["offset"] = offset
        if count is not None:
            params["count"] = count
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_hashtag_search_result", json_body=body)

@router.get("/fetch_live_search_result")
async def fetch_live_search_result(
    region: str | None = None,
    count: int | None = None,
    offset: int | None = None,
    keyword: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取指定关键词的直播搜索结果/Get live search results of specified keywords"""
        params: dict[str, Any] = {}
        if keyword is not None:
            params["keyword"] = keyword
        if offset is not None:
            params["offset"] = offset
        if count is not None:
            params["count"] = count
        if region is not None:
            params["region"] = region
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_live_search_result", json_body=body)

@router.get("/fetch_location_search")
async def fetch_location_search(
    count: int | None = None,
    offset: int | None = None,
    keyword: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取地点搜索结果/Get location search results"""
        params: dict[str, Any] = {}
        if keyword is not None:
            params["keyword"] = keyword
        if offset is not None:
            params["offset"] = offset
        if count is not None:
            params["count"] = count
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_location_search", json_body=body)

@router.get("/fetch_music_detail")
async def fetch_music_detail(
    music_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取指定音乐的详情数据/Get details of specified music"""
        params: dict[str, Any] = {}
        if music_id is not None:
            params["music_id"] = music_id
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_music_detail", json_body=body)

@router.get("/fetch_music_video_list")
async def fetch_music_video_list(
    count: int | None = None,
    cursor: int | None = None,
    music_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取指定音乐的视频列表数据/Get video list of specified music"""
        params: dict[str, Any] = {}
        if music_id is not None:
            params["music_id"] = music_id
        if cursor is not None:
            params["cursor"] = cursor
        if count is not None:
            params["count"] = count
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_music_video_list", json_body=body)

@router.get("/fetch_hashtag_detail")
async def fetch_hashtag_detail(
    ch_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取指定话题的详情数据/Get details of specified hashtag"""
        params: dict[str, Any] = {}
        if ch_id is not None:
            params["ch_id"] = ch_id
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_hashtag_detail", json_body=body)

@router.get("/fetch_hashtag_video_list")
async def fetch_hashtag_video_list(
    count: int | None = None,
    cursor: int | None = None,
    ch_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取指定话题的作品数据/Get video list of specified hashtag"""
        params: dict[str, Any] = {}
        if ch_id is not None:
            params["ch_id"] = ch_id
        if cursor is not None:
            params["cursor"] = cursor
        if count is not None:
            params["count"] = count
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_hashtag_video_list", json_body=body)

@router.get("/fetch_user_follower_list")
async def fetch_user_follower_list(
    page_token: str | None = None,
    min_time: int | None = None,
    count: int | None = None,
    sec_user_id: str | None = None,
    user_id: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取指定用户的粉丝列表数据/Get follower list of specified user"""
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
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_user_follower_list", json_body=body)

@router.get("/fetch_user_following_list")
async def fetch_user_following_list(
    page_token: str | None = None,
    min_time: int | None = None,
    count: int | None = None,
    sec_user_id: str | None = None,
    user_id: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取指定用户的关注列表数据/Get following list of specified user"""
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
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_user_following_list", json_body=body)

@router.get("/fetch_creator_search_insights")
async def fetch_creator_search_insights(
    force_refresh: bool | None = None,
    creator_source: str | None = None,
    category_filters: str | None = None,
    language_filters: str | None = None,
    tab: str | None = None,
    limit: int | None = None,
    offset: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """创作者搜索洞察/Creator Search Insights"""
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
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_creator_search_insights", json_body=body)

@router.get("/fetch_creator_search_insights_detail")
async def fetch_creator_search_insights_detail(
    dimension_list: str | None = None,
    end_date: int | None = None,
    start_date: int | None = None,
    time_range: str | None = None,
    query_id_str: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """创作者搜索洞察详情/Creator Search Insights Detail"""
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
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_creator_search_insights_detail", json_body=body)

@router.get("/fetch_creator_search_insights_trend")
async def fetch_creator_search_insights_trend(
    query_analysis_required: bool | None = None,
    from_tab_path: str | None = None,
    query_id_str: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """创作者搜索洞察趋势/Creator Search Insights Trend"""
        params: dict[str, Any] = {}
        if query_id_str is not None:
            params["query_id_str"] = query_id_str
        if from_tab_path is not None:
            params["from_tab_path"] = from_tab_path
        if query_analysis_required is not None:
            params["query_analysis_required"] = query_analysis_required
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_creator_search_insights_trend", json_body=body)

@router.get("/fetch_creator_search_insights_videos")
async def fetch_creator_search_insights_videos(
    count: int | None = None,
    offset: int | None = None,
    keyword: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """创作者搜索洞察相关视频/Creator Search Insights Videos"""
        params: dict[str, Any] = {}
        if keyword is not None:
            params["keyword"] = keyword
        if offset is not None:
            params["offset"] = offset
        if count is not None:
            params["count"] = count
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_creator_search_insights_videos", json_body=body)

@router.get("/fetch_music_chart_list")
async def fetch_music_chart_list(
    count: int | None = None,
    cursor: int | None = None,
    scene: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """音乐排行榜/Music Chart List"""
        params: dict[str, Any] = {}
        if scene is not None:
            params["scene"] = scene
        if cursor is not None:
            params["cursor"] = cursor
        if count is not None:
            params["count"] = count
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_music_chart_list", json_body=body)

@router.get("/search_follower_list")
async def search_follower_list(
    keyword: str,
    user_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """搜索粉丝列表/Search follower list"""
        params: dict[str, Any] = {}
        if user_id is not None:
            params["user_id"] = user_id
        if keyword is not None:
            params["keyword"] = keyword
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/search_follower_list", json_body=body)

@router.get("/search_following_list")
async def search_following_list(
    keyword: str,
    user_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """搜索关注列表/Search following list"""
        params: dict[str, Any] = {}
        if user_id is not None:
            params["user_id"] = user_id
        if keyword is not None:
            params["keyword"] = keyword
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/search_following_list", json_body=body)

@router.get("/fetch_live_room_info")
async def fetch_live_room_info(
    room_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取指定直播间的数据/Get data of specified live room"""
        params: dict[str, Any] = {}
        if room_id is not None:
            params["room_id"] = room_id
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_live_room_info", json_body=body)

@router.get("/fetch_live_ranking_list")
async def fetch_live_ranking_list(
    anchor_id: str,
    room_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取直播间排行榜数据/Get live room ranking list"""
        params: dict[str, Any] = {}
        if room_id is not None:
            params["room_id"] = room_id
        if anchor_id is not None:
            params["anchor_id"] = anchor_id
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_live_ranking_list", json_body=body)

@router.get("/check_live_room_online")
async def check_live_room_online(
    room_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """检测直播间是否在线/Check if live room is online"""
        params: dict[str, Any] = {}
        if room_id is not None:
            params["room_id"] = room_id
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/check_live_room_online", json_body=body)

@router.post("/check_live_room_online_batch")
async def check_live_room_online_batch(
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """批量检测直播间是否在线/Batch check if live rooms are online"""
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/check_live_room_online_batch", json_body=body)

@router.get("/fetch_share_short_link")
async def fetch_share_short_link(
    url: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取分享短链接/Get share short link"""
        params: dict[str, Any] = {}
        if url is not None:
            params["url"] = url
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_share_short_link", json_body=body)

@router.get("/fetch_share_qr_code")
async def fetch_share_qr_code(
    schema_type: int | None = None,
    object_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取分享二维码/Get share QR code"""
        params: dict[str, Any] = {}
        if object_id is not None:
            params["object_id"] = object_id
        if schema_type is not None:
            params["schema_type"] = schema_type
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_share_qr_code", json_body=body)

@router.get("/fetch_product_search")
async def fetch_product_search(
    max_price: str | None = None,
    min_price: str | None = None,
    have_discount: bool | None = None,
    customer_review_four_star: bool | None = None,
    sort_type: int | None = None,
    count: int | None = None,
    cursor: int | None = None,
    keyword: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取商品搜索结果/Get product search results"""
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
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_product_search", json_body=body)

@router.get("/fetch_creator_info")
async def fetch_creator_info(
    creator_uid: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取带货创作者信息/Get shopping creator information"""
        params: dict[str, Any] = {}
        if creator_uid is not None:
            params["creator_uid"] = creator_uid
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_creator_info", json_body=body)

@router.get("/fetch_creator_showcase_product_list")
async def fetch_creator_showcase_product_list(
    next_scroll_param: str | None = None,
    count: int | None = None,
    kol_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取创作者橱窗商品列表/Get creator showcase product list"""
        params: dict[str, Any] = {}
        if kol_id is not None:
            params["kol_id"] = kol_id
        if count is not None:
            params["count"] = count
        if next_scroll_param is not None:
            params["next_scroll_param"] = next_scroll_param
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_creator_showcase_product_list", json_body=body)

@router.get("/fetch_shop_id_by_share_link")
async def fetch_shop_id_by_share_link(
    share_link: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """通过分享链接获取店铺ID/Get Shop ID by Share Link"""
        params: dict[str, Any] = {}
        if share_link is not None:
            params["share_link"] = share_link
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_shop_id_by_share_link", json_body=body)

@router.get("/fetch_product_id_by_share_link")
async def fetch_product_id_by_share_link(
    share_link: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """通过分享链接获取商品ID/Get Product ID by Share Link"""
        params: dict[str, Any] = {}
        if share_link is not None:
            params["share_link"] = share_link
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_product_id_by_share_link", json_body=body)

@router.get("/fetch_product_detail")
async def fetch_product_detail(
    product_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取商品详情数据（即将弃用，使用 fetch_product_detail_v2 代替）/Get product detail data (will be deprecated, use fetch_product_detail_v2 instead)"""
        params: dict[str, Any] = {}
        if product_id is not None:
            params["product_id"] = product_id
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_product_detail", json_body=body)

@router.get("/fetch_product_detail_v2")
async def fetch_product_detail_v2(
    product_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取商品详情数据V2/Get product detail data V2"""
        params: dict[str, Any] = {}
        if product_id is not None:
            params["product_id"] = product_id
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_product_detail_v2", json_body=body)

@router.get("/fetch_product_detail_v3")
async def fetch_product_detail_v3(
    region: str | None = None,
    product_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取商品详情数据V3 / Get product detail data V3"""
        params: dict[str, Any] = {}
        if product_id is not None:
            params["product_id"] = product_id
        if region is not None:
            params["region"] = region
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_product_detail_v3", json_body=body)

@router.get("/fetch_product_detail_v4")
async def fetch_product_detail_v4(
    region: str | None = None,
    product_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取商品详情数据V4 / Get product detail data V4"""
        params: dict[str, Any] = {}
        if product_id is not None:
            params["product_id"] = product_id
        if region is not None:
            params["region"] = region
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_product_detail_v4", json_body=body)

@router.get("/fetch_product_review")
async def fetch_product_review(
    sort_type: int | None = None,
    filter_id: int | None = None,
    size: int | None = None,
    cursor: int | None = None,
    product_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取商品评价数据/Get product review data"""
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
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_product_review", json_body=body)

@router.get("/fetch_shop_home_page_list")
async def fetch_shop_home_page_list(
    seller_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取商家主页Page列表数据/Get shop home page list data"""
        params: dict[str, Any] = {}
        if seller_id is not None:
            params["seller_id"] = seller_id
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_shop_home_page_list", json_body=body)

@router.get("/fetch_shop_home")
async def fetch_shop_home(
    seller_id: str,
    page_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取商家主页数据/Get shop home page data"""
        params: dict[str, Any] = {}
        if page_id is not None:
            params["page_id"] = page_id
        if seller_id is not None:
            params["seller_id"] = seller_id
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_shop_home", json_body=body)

@router.get("/fetch_shop_product_recommend")
async def fetch_shop_product_recommend(
    page_size: int | None = None,
    scroll_param: str | None = None,
    seller_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取商家商品推荐数据/Get shop product recommend data"""
        params: dict[str, Any] = {}
        if seller_id is not None:
            params["seller_id"] = seller_id
        if scroll_param is not None:
            params["scroll_param"] = scroll_param
        if page_size is not None:
            params["page_size"] = page_size
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_shop_product_recommend", json_body=body)

@router.get("/fetch_shop_product_list")
async def fetch_shop_product_list(
    sort_order: int | None = None,
    sort_field: int | None = None,
    page_size: int | None = None,
    scroll_params: str | None = None,
    seller_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取商家商品列表数据/Get shop product list data"""
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
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_shop_product_list", json_body=body)

@router.get("/fetch_shop_product_list_v2")
async def fetch_shop_product_list_v2(
    sort_order: int | None = None,
    sort_field: int | None = None,
    page_size: int | None = None,
    scroll_params: str | None = None,
    seller_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取商家商品列表数据 V2/Get shop product list data V2"""
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
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_shop_product_list_v2", json_body=body)

@router.get("/fetch_shop_info")
async def fetch_shop_info(
    shop_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取商家信息数据/Get shop information data"""
        params: dict[str, Any] = {}
        if shop_id is not None:
            params["shop_id"] = shop_id
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_shop_info", json_body=body)

@router.get("/fetch_shop_product_category")
async def fetch_shop_product_category(
    seller_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取商家产品分类数据/Get shop product category data"""
        params: dict[str, Any] = {}
        if seller_id is not None:
            params["seller_id"] = seller_id
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_shop_product_category", json_body=body)

@router.get("/fetch_live_daily_rank")
async def fetch_live_daily_rank(
    cookie: str | None = None,
    gap_interval: int | None = None,
    region_type: int | None = None,
    rank_type: int | None = None,
    room_id: str | None = None,
    anchor_id: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取直播每日榜单数据/Get live daily rank data"""
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
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_live_daily_rank", json_body=body)

@router.get("/fetch_user_music_list")
async def fetch_user_music_list(
    count: int | None = None,
    cursor: int | None = None,
    sec_uid: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户音乐列表数据/Get user music list data"""
        params: dict[str, Any] = {}
        if sec_uid is not None:
            params["sec_uid"] = sec_uid
        if cursor is not None:
            params["cursor"] = cursor
        if count is not None:
            params["count"] = count
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_user_music_list", json_body=body)

@router.post("/fetch_content_translate")
async def fetch_content_translate(
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取内容翻译数据/Get content translation data"""
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_content_translate", json_body=body)

@router.post("/fetch_home_feed")
async def fetch_home_feed(
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取主页视频推荐数据/Get home feed(recommend) video data"""
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_home_feed", json_body=body)

@router.post("/TTencrypt_algorithm")
async def TTencrypt_algorithm(
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """TikTok APP加密算法/TikTok APP encryption algorithm"""
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/TTencrypt_algorithm", json_body=body)

@router.get("/fetch_live_room_product_list")
async def fetch_live_room_product_list(
    cookie: str | None = None,
    region: str | None = None,
    offset: int | None = None,
    page_size: int | None = None,
    author_id: str,
    room_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取直播间商品列表数据/Get live room product list data"""
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
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_live_room_product_list", json_body=body)

@router.get("/fetch_live_room_product_list_v2")
async def fetch_live_room_product_list_v2(
    cookie: str | None = None,
    region: str | None = None,
    offset: int | None = None,
    page_size: int | None = None,
    author_id: str,
    room_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取直播间商品列表数据 V2 /Get live room product list data V2"""
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
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/fetch_live_room_product_list_v2", json_body=body)

@router.get("/add_video_play_count")
async def add_video_play_count(
    item_id: str,
    aweme_type: int,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """根据视频ID来增加作品的播放数/Increase the number of plays of the work according to the video ID"""
        params: dict[str, Any] = {}
        if aweme_type is not None:
            params["aweme_type"] = aweme_type
        if item_id is not None:
            params["item_id"] = item_id
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/add_video_play_count", json_body=body)

@router.post("/encrypt_decrypt_login_request")
async def encrypt_decrypt_login_request(
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """加密或解密 TikTok APP 登录请求体/Encrypt or Decrypt TikTok APP login request body"""
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/encrypt_decrypt_login_request", json_body=body)

@router.get("/open_tiktok_app_to_video_detail")
async def open_tiktok_app_to_video_detail(
    aweme_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """生成TikTok分享链接，唤起TikTok APP，跳转指定作品详情页/Generate TikTok share link, call TikTok APP, and jump to the specified video details page"""
        params: dict[str, Any] = {}
        if aweme_id is not None:
            params["aweme_id"] = aweme_id
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/open_tiktok_app_to_video_detail", json_body=body)

@router.get("/open_tiktok_app_to_user_profile")
async def open_tiktok_app_to_user_profile(
    uid: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """生成TikTok分享链接，唤起TikTok APP，跳转指定用户主页/Generate TikTok share link, call TikTok APP, and jump to the specified user profile"""
        params: dict[str, Any] = {}
        if uid is not None:
            params["uid"] = uid
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/open_tiktok_app_to_user_profile", json_body=body)

@router.get("/open_tiktok_app_to_keyword_search")
async def open_tiktok_app_to_keyword_search(
    keyword: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """生成TikTok分享链接，唤起TikTok APP，跳转指定关键词搜索结果/Generate TikTok share link, call TikTok APP, and jump to the specified keyword search result"""
        params: dict[str, Any] = {}
        if keyword is not None:
            params["keyword"] = keyword
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/open_tiktok_app_to_keyword_search", json_body=body)

@router.get("/open_tiktok_app_to_send_private_message")
async def open_tiktok_app_to_send_private_message(
    uid: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """生成TikTok分享链接，唤起TikTok APP，给指定用户发送私信/Generate TikTok share link, call TikTok APP, and send private messages to specified users"""
        params: dict[str, Any] = {}
        if uid is not None:
            params["uid"] = uid
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/app/v3/open_tiktok_app_to_send_private_message", json_body=body)
