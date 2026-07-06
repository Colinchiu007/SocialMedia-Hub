"""Auto-generated routes for Douyin-App-V3-API."""

from __future__ import annotations

from typing import Any

from fastapi import APIRouter, Depends, Request

from socialmedia_hub.server._core import proxy_request, verify_api_key

router = APIRouter(prefix="/api/v1/douyin/app/v3", tags=["douyin_app_v3"])

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
    return await proxy_request("douyin", "/api/v1/douyin/app/v3/fetch_one_video", params=params, json_body=body)

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
    return await proxy_request("douyin", "/api/v1/douyin/app/v3/fetch_one_video_v2", params=params, json_body=body)

@router.get("/fetch_one_video_v3")
async def fetch_one_video_v3(
    aweme_id: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取单个作品数据 V3 (无版权限制)/Get single video data V3 (No copyright restrictions)"""
    body = await request.json()
    params: dict[str, Any] = {}
    if aweme_id is not None:
        params["aweme_id"] = aweme_id
    return await proxy_request("douyin", "/api/v1/douyin/app/v3/fetch_one_video_v3", params=params, json_body=body)

@router.get("/fetch_share_info_by_share_code")
async def fetch_share_info_by_share_code(
    share_code: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """根据分享口令获取分享信息/Get share info by share code"""
    body = await request.json()
    params: dict[str, Any] = {}
    if share_code is not None:
        params["share_code"] = share_code
    return await proxy_request("douyin", "/api/v1/douyin/app/v3/fetch_share_info_by_share_code", params=params, json_body=body)

@router.post("/fetch_multi_video")
async def fetch_multi_video(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """批量获取视频信息 V1/Batch Get Video Information V1"""
    body = await request.json()
    return await proxy_request("douyin", "/api/v1/douyin/app/v3/fetch_multi_video", json_body=body)

@router.post("/fetch_multi_video_v2")
async def fetch_multi_video_v2(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """批量获取视频信息 V2/Batch Get Video Information V2"""
    body = await request.json()
    return await proxy_request("douyin", "/api/v1/douyin/app/v3/fetch_multi_video_v2", json_body=body)

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
    return await proxy_request("douyin", "/api/v1/douyin/app/v3/fetch_one_video_by_share_url", params=params, json_body=body)

@router.get("/fetch_video_high_quality_play_url")
async def fetch_video_high_quality_play_url(
    request: Request,
    aweme_id: str | None = None,
    share_url: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取视频的最高画质播放链接/Get the highest quality play URL of the video"""
    body = await request.json()
    params: dict[str, Any] = {}
    if aweme_id is not None:
        params["aweme_id"] = aweme_id
    if share_url is not None:
        params["share_url"] = share_url
    return await proxy_request("douyin", "/api/v1/douyin/app/v3/fetch_video_high_quality_play_url", params=params, json_body=body)

@router.post("/fetch_multi_video_high_quality_play_url")
async def fetch_multi_video_high_quality_play_url(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """批量获取视频的最高画质播放链接/Batch get the highest quality play URL of videos"""
    body = await request.json()
    return await proxy_request("douyin", "/api/v1/douyin/app/v3/fetch_multi_video_high_quality_play_url", json_body=body)

@router.get("/fetch_video_statistics")
async def fetch_video_statistics(
    aweme_ids: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """根据视频ID获取作品的统计数据（点赞数、下载数、播放数、分享数）/Get the statistical data of the Post according to the video ID (like count, download count, play count, share count)"""
    body = await request.json()
    params: dict[str, Any] = {}
    if aweme_ids is not None:
        params["aweme_ids"] = aweme_ids
    return await proxy_request("douyin", "/api/v1/douyin/app/v3/fetch_video_statistics", params=params, json_body=body)

@router.get("/fetch_multi_video_statistics")
async def fetch_multi_video_statistics(
    aweme_ids: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """根据视频ID批量获取作品的统计数据（点赞数、下载数、播放数、分享数）/Get the statistical data of the Post according to the video ID (like count, download count, play count, share count)"""
    body = await request.json()
    params: dict[str, Any] = {}
    if aweme_ids is not None:
        params["aweme_ids"] = aweme_ids
    return await proxy_request("douyin", "/api/v1/douyin/app/v3/fetch_multi_video_statistics", params=params, json_body=body)

@router.get("/add_video_play_count")
async def add_video_play_count(
    aweme_type: int,
    item_id: str,
    request: Request,
    cookie: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """根据视频ID来增加作品的播放数/Increase the number of plays of the work according to the video ID"""
    body = await request.json()
    params: dict[str, Any] = {}
    if aweme_type is not None:
        params["aweme_type"] = aweme_type
    if item_id is not None:
        params["item_id"] = item_id
    if cookie is not None:
        params["cookie"] = cookie
    return await proxy_request("douyin", "/api/v1/douyin/app/v3/add_video_play_count", params=params, json_body=body)

@router.get("/handler_user_profile")
async def handler_user_profile(
    sec_user_id: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取指定用户的信息/Get information of specified user"""
    body = await request.json()
    params: dict[str, Any] = {}
    if sec_user_id is not None:
        params["sec_user_id"] = sec_user_id
    return await proxy_request("douyin", "/api/v1/douyin/app/v3/handler_user_profile", params=params, json_body=body)

@router.get("/fetch_user_fans_list")
async def fetch_user_fans_list(
    request: Request,
    sec_user_id: str | None = None,
    max_time: str | None = None,
    count: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户粉丝列表/Get user fans list"""
    body = await request.json()
    params: dict[str, Any] = {}
    if sec_user_id is not None:
        params["sec_user_id"] = sec_user_id
    if max_time is not None:
        params["max_time"] = max_time
    if count is not None:
        params["count"] = count
    return await proxy_request("douyin", "/api/v1/douyin/app/v3/fetch_user_fans_list", params=params, json_body=body)

@router.get("/fetch_user_following_list")
async def fetch_user_following_list(
    request: Request,
    sec_user_id: str | None = None,
    max_time: str | None = None,
    count: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户关注列表 (弃用，使用 /api/v1/douyin/web/fetch_user_following_list 替代)/Get user following list (Deprecated, use /api/v1/douyin/web/fetch_user_following_list instead)"""
    body = await request.json()
    params: dict[str, Any] = {}
    if sec_user_id is not None:
        params["sec_user_id"] = sec_user_id
    if max_time is not None:
        params["max_time"] = max_time
    if count is not None:
        params["count"] = count
    return await proxy_request("douyin", "/api/v1/douyin/app/v3/fetch_user_following_list", params=params, json_body=body)

@router.get("/fetch_user_post_videos")
async def fetch_user_post_videos(
    sec_user_id: str,
    request: Request,
    max_cursor: int | None = None,
    count: int | None = None,
    sort_type: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户主页作品数据/Get user homepage video data"""
    body = await request.json()
    params: dict[str, Any] = {}
    if sec_user_id is not None:
        params["sec_user_id"] = sec_user_id
    if max_cursor is not None:
        params["max_cursor"] = max_cursor
    if count is not None:
        params["count"] = count
    if sort_type is not None:
        params["sort_type"] = sort_type
    return await proxy_request("douyin", "/api/v1/douyin/app/v3/fetch_user_post_videos", params=params, json_body=body)

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
    return await proxy_request("douyin", "/api/v1/douyin/app/v3/fetch_user_like_videos", params=params, json_body=body)

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
    return await proxy_request("douyin", "/api/v1/douyin/app/v3/fetch_video_comments", params=params, json_body=body)

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
    return await proxy_request("douyin", "/api/v1/douyin/app/v3/fetch_video_comment_replies", params=params, json_body=body)

@router.get("/fetch_video_mix_detail")
async def fetch_video_mix_detail(
    mix_id: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取抖音视频合集详情数据/Get Douyin video mix detail data"""
    body = await request.json()
    params: dict[str, Any] = {}
    if mix_id is not None:
        params["mix_id"] = mix_id
    return await proxy_request("douyin", "/api/v1/douyin/app/v3/fetch_video_mix_detail", params=params, json_body=body)

@router.get("/fetch_video_mix_post_list")
async def fetch_video_mix_post_list(
    mix_id: str,
    request: Request,
    cursor: int | None = None,
    count: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取抖音视频合集作品列表数据/Get Douyin video mix post list data"""
    body = await request.json()
    params: dict[str, Any] = {}
    if mix_id is not None:
        params["mix_id"] = mix_id
    if cursor is not None:
        params["cursor"] = cursor
    if count is not None:
        params["count"] = count
    return await proxy_request("douyin", "/api/v1/douyin/app/v3/fetch_video_mix_post_list", params=params, json_body=body)

@router.get("/fetch_user_series_list")
async def fetch_user_series_list(
    request: Request,
    user_id: str | None = None,
    sec_user_id: str | None = None,
    cursor: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户短剧合集列表/Get user series list"""
    body = await request.json()
    params: dict[str, Any] = {}
    if user_id is not None:
        params["user_id"] = user_id
    if sec_user_id is not None:
        params["sec_user_id"] = sec_user_id
    if cursor is not None:
        params["cursor"] = cursor
    return await proxy_request("douyin", "/api/v1/douyin/app/v3/fetch_user_series_list", params=params, json_body=body)

@router.get("/fetch_series_video_list")
async def fetch_series_video_list(
    series_id: str,
    request: Request,
    cursor: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取短剧视频列表/Get series video list"""
    body = await request.json()
    params: dict[str, Any] = {}
    if series_id is not None:
        params["series_id"] = series_id
    if cursor is not None:
        params["cursor"] = cursor
    return await proxy_request("douyin", "/api/v1/douyin/app/v3/fetch_series_video_list", params=params, json_body=body)

@router.get("/fetch_series_detail")
async def fetch_series_detail(
    series_id: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取短剧详情信息/Get series detail"""
    body = await request.json()
    params: dict[str, Any] = {}
    if series_id is not None:
        params["series_id"] = series_id
    return await proxy_request("douyin", "/api/v1/douyin/app/v3/fetch_series_detail", params=params, json_body=body)

@router.get("/fetch_general_search_result")
async def fetch_general_search_result(
    keyword: str,
    request: Request,
    offset: int | None = None,
    count: int | None = None,
    sort_type: str | None = None,
    publish_time: str | None = None,
    filter_duration: str | None = None,
    content_type: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取指定关键词的综合搜索结果（弃用，替代接口见下方文档说明）/Get comprehensive search results of specified keywords (deprecated, see the documentation below for alternative interfaces)"""
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
    if filter_duration is not None:
        params["filter_duration"] = filter_duration
    if content_type is not None:
        params["content_type"] = content_type
    return await proxy_request("douyin", "/api/v1/douyin/app/v3/fetch_general_search_result", params=params, json_body=body)

@router.get("/fetch_video_search_result")
async def fetch_video_search_result(
    keyword: str,
    request: Request,
    offset: int | None = None,
    count: int | None = None,
    sort_type: str | None = None,
    publish_time: str | None = None,
    filter_duration: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取指定关键词的视频搜索结果（弃用，替代接口见下方文档说明）/Get video search results of specified keywords (deprecated, see the documentation below for alternative interfaces)"""
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
    if filter_duration is not None:
        params["filter_duration"] = filter_duration
    return await proxy_request("douyin", "/api/v1/douyin/app/v3/fetch_video_search_result", params=params, json_body=body)

@router.get("/fetch_video_search_result_v2")
async def fetch_video_search_result_v2(
    keyword: str,
    request: Request,
    sort_type: str | None = None,
    publish_time: str | None = None,
    filter_duration: str | None = None,
    page: int | None = None,
    search_id: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取指定关键词的视频搜索结果 V2 （弃用，替代接口见下方文档说明）/Get video search results of specified keywords V2 (deprecated, see the documentation below for alternative interfaces)"""
    body = await request.json()
    params: dict[str, Any] = {}
    if keyword is not None:
        params["keyword"] = keyword
    if sort_type is not None:
        params["sort_type"] = sort_type
    if publish_time is not None:
        params["publish_time"] = publish_time
    if filter_duration is not None:
        params["filter_duration"] = filter_duration
    if page is not None:
        params["page"] = page
    if search_id is not None:
        params["search_id"] = search_id
    return await proxy_request("douyin", "/api/v1/douyin/app/v3/fetch_video_search_result_v2", params=params, json_body=body)

@router.get("/fetch_user_search_result")
async def fetch_user_search_result(
    keyword: str,
    request: Request,
    offset: int | None = None,
    count: int | None = None,
    douyin_user_fans: str | None = None,
    douyin_user_type: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取指定关键词的用户搜索结果（弃用，替代接口见下方文档说明）/Get user search results of specified keywords (deprecated, see the documentation below for alternative interfaces)"""
    body = await request.json()
    params: dict[str, Any] = {}
    if keyword is not None:
        params["keyword"] = keyword
    if offset is not None:
        params["offset"] = offset
    if count is not None:
        params["count"] = count
    if douyin_user_fans is not None:
        params["douyin_user_fans"] = douyin_user_fans
    if douyin_user_type is not None:
        params["douyin_user_type"] = douyin_user_type
    return await proxy_request("douyin", "/api/v1/douyin/app/v3/fetch_user_search_result", params=params, json_body=body)

@router.get("/fetch_live_search_result")
async def fetch_live_search_result(
    keyword: str,
    request: Request,
    cursor: int | None = None,
    count: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取指定关键词的直播搜索结果（弃用，替代接口见下方文档说明）/Get live search results of specified keywords (deprecated, see the documentation below for alternative interfaces)"""
    body = await request.json()
    params: dict[str, Any] = {}
    if keyword is not None:
        params["keyword"] = keyword
    if cursor is not None:
        params["cursor"] = cursor
    if count is not None:
        params["count"] = count
    return await proxy_request("douyin", "/api/v1/douyin/app/v3/fetch_live_search_result", params=params, json_body=body)

@router.get("/fetch_music_search_result")
async def fetch_music_search_result(
    keyword: str,
    request: Request,
    offset: int | None = None,
    count: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取指定关键词的音乐搜索结果（弃用，替代接口见下方文档说明）/Get music search results of specified keywords (deprecated, see the documentation below for alternative interfaces)"""
    body = await request.json()
    params: dict[str, Any] = {}
    if keyword is not None:
        params["keyword"] = keyword
    if offset is not None:
        params["offset"] = offset
    if count is not None:
        params["count"] = count
    return await proxy_request("douyin", "/api/v1/douyin/app/v3/fetch_music_search_result", params=params, json_body=body)

@router.get("/fetch_hashtag_search_result")
async def fetch_hashtag_search_result(
    keyword: str,
    request: Request,
    offset: int | None = None,
    count: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取指定关键词的话题搜索结果（弃用，替代接口见下方文档说明）/Get hashtag search results of specified keywords (deprecated, see the documentation below for alternative interfaces)"""
    body = await request.json()
    params: dict[str, Any] = {}
    if keyword is not None:
        params["keyword"] = keyword
    if offset is not None:
        params["offset"] = offset
    if count is not None:
        params["count"] = count
    return await proxy_request("douyin", "/api/v1/douyin/app/v3/fetch_hashtag_search_result", params=params, json_body=body)

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
    return await proxy_request("douyin", "/api/v1/douyin/app/v3/fetch_music_detail", params=params, json_body=body)

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
    return await proxy_request("douyin", "/api/v1/douyin/app/v3/fetch_music_video_list", params=params, json_body=body)

@router.get("/fetch_hashtag_detail")
async def fetch_hashtag_detail(
    ch_id: int,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取指定话题的详情数据/Get details of specified hashtag"""
    body = await request.json()
    params: dict[str, Any] = {}
    if ch_id is not None:
        params["ch_id"] = ch_id
    return await proxy_request("douyin", "/api/v1/douyin/app/v3/fetch_hashtag_detail", params=params, json_body=body)

@router.get("/fetch_hashtag_video_list")
async def fetch_hashtag_video_list(
    ch_id: str,
    request: Request,
    cursor: int | None = None,
    sort_type: int | None = None,
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
    if sort_type is not None:
        params["sort_type"] = sort_type
    if count is not None:
        params["count"] = count
    return await proxy_request("douyin", "/api/v1/douyin/app/v3/fetch_hashtag_video_list", params=params, json_body=body)

@router.get("/fetch_hot_search_list")
async def fetch_hot_search_list(
    request: Request,
    board_type: str | None = None,
    board_sub_type: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取抖音热搜榜数据/Get Douyin hot search list data"""
    body = await request.json()
    params: dict[str, Any] = {}
    if board_type is not None:
        params["board_type"] = board_type
    if board_sub_type is not None:
        params["board_sub_type"] = board_sub_type
    return await proxy_request("douyin", "/api/v1/douyin/app/v3/fetch_hot_search_list", params=params, json_body=body)

@router.get("/fetch_live_hot_search_list")
async def fetch_live_hot_search_list(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取抖音直播热搜榜数据/Get Douyin live hot search list data"""
    body = await request.json()
    return await proxy_request("douyin", "/api/v1/douyin/app/v3/fetch_live_hot_search_list", json_body=body)

@router.get("/fetch_music_hot_search_list")
async def fetch_music_hot_search_list(
    request: Request,
    chart_type: str | None = None,
    cursor: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取抖音音乐榜数据/Get Douyin music hot search list data"""
    body = await request.json()
    params: dict[str, Any] = {}
    if chart_type is not None:
        params["chart_type"] = chart_type
    if cursor is not None:
        params["cursor"] = cursor
    return await proxy_request("douyin", "/api/v1/douyin/app/v3/fetch_music_hot_search_list", params=params, json_body=body)

@router.get("/fetch_brand_hot_search_list")
async def fetch_brand_hot_search_list(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取抖音品牌热榜分类数据/Get Douyin brand hot search list data"""
    body = await request.json()
    return await proxy_request("douyin", "/api/v1/douyin/app/v3/fetch_brand_hot_search_list", json_body=body)

@router.get("/fetch_brand_hot_search_list_detail")
async def fetch_brand_hot_search_list_detail(
    category_id: int,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取抖音品牌热榜具体分类数据/Get Douyin brand hot search list detail data"""
    body = await request.json()
    params: dict[str, Any] = {}
    if category_id is not None:
        params["category_id"] = category_id
    return await proxy_request("douyin", "/api/v1/douyin/app/v3/fetch_brand_hot_search_list_detail", params=params, json_body=body)

@router.get("/generate_douyin_short_url")
async def generate_douyin_short_url(
    url: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """生成抖音短链接/Generate Douyin short link"""
    body = await request.json()
    params: dict[str, Any] = {}
    if url is not None:
        params["url"] = url
    return await proxy_request("douyin", "/api/v1/douyin/app/v3/generate_douyin_short_url", params=params, json_body=body)

@router.get("/generate_douyin_video_share_qrcode")
async def generate_douyin_video_share_qrcode(
    object_id: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """生成抖音视频分享二维码/Generate Douyin video share QR code"""
    body = await request.json()
    params: dict[str, Any] = {}
    if object_id is not None:
        params["object_id"] = object_id
    return await proxy_request("douyin", "/api/v1/douyin/app/v3/generate_douyin_video_share_qrcode", params=params, json_body=body)

@router.get("/register_device")
async def register_device(
    request: Request,
    proxy: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """抖音APP注册设备/Douyin APP register device"""
    body = await request.json()
    params: dict[str, Any] = {}
    if proxy is not None:
        params["proxy"] = proxy
    return await proxy_request("douyin", "/api/v1/douyin/app/v3/register_device", params=params, json_body=body)

@router.get("/open_douyin_app_to_video_detail")
async def open_douyin_app_to_video_detail(
    aweme_id: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """生成抖音分享链接，唤起抖音APP，跳转指定作品详情页/Generate Douyin share link, call Douyin APP, and jump to the specified video details page"""
    body = await request.json()
    params: dict[str, Any] = {}
    if aweme_id is not None:
        params["aweme_id"] = aweme_id
    return await proxy_request("douyin", "/api/v1/douyin/app/v3/open_douyin_app_to_video_detail", params=params, json_body=body)

@router.get("/open_douyin_app_to_user_profile")
async def open_douyin_app_to_user_profile(
    uid: str,
    sec_uid: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """生成抖音分享链接，唤起抖音APP，跳转指定用户主页/Generate Douyin share link, call Douyin APP, and jump to the specified user profile"""
    body = await request.json()
    params: dict[str, Any] = {}
    if uid is not None:
        params["uid"] = uid
    if sec_uid is not None:
        params["sec_uid"] = sec_uid
    return await proxy_request("douyin", "/api/v1/douyin/app/v3/open_douyin_app_to_user_profile", params=params, json_body=body)

@router.get("/open_douyin_app_to_keyword_search")
async def open_douyin_app_to_keyword_search(
    keyword: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """生成抖音分享链接，唤起抖音APP，跳转指定关键词搜索结果/Generate Douyin share link, call Douyin APP, and jump to the specified keyword search result"""
    body = await request.json()
    params: dict[str, Any] = {}
    if keyword is not None:
        params["keyword"] = keyword
    return await proxy_request("douyin", "/api/v1/douyin/app/v3/open_douyin_app_to_keyword_search", params=params, json_body=body)

@router.get("/open_douyin_app_to_send_private_message")
async def open_douyin_app_to_send_private_message(
    uid: str,
    sec_uid: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """生成抖音分享链接，唤起抖音APP，给指定用户发送私信/Generate Douyin share link, call Douyin APP, and send private messages to specified users"""
    body = await request.json()
    params: dict[str, Any] = {}
    if uid is not None:
        params["uid"] = uid
    if sec_uid is not None:
        params["sec_uid"] = sec_uid
    return await proxy_request("douyin", "/api/v1/douyin/app/v3/open_douyin_app_to_send_private_message", params=params, json_body=body)
