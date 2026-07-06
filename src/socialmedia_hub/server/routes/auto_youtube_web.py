"""Auto-generated routes for YouTube-Web-API."""

from __future__ import annotations

from typing import Any

from fastapi import APIRouter, Depends, Request

from socialmedia_hub.server._core import proxy_request, verify_api_key

router = APIRouter(prefix="/api/v1/youtube/web", tags=["youtube_web"])

@router.get("/get_video_info")
async def get_video_info(
    video_id: str,
    request: Request,
    url_access: str | None = None,
    lang: str | None = None,
    videos: str | None = None,
    audios: str | None = None,
    subtitles: bool | None = None,
    related: bool | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取视频信息 V1/Get video information V1"""
    params: dict[str, Any] = {}
    if video_id is not None:
        params["video_id"] = video_id
    if url_access is not None:
        params["url_access"] = url_access
    if lang is not None:
        params["lang"] = lang
    if videos is not None:
        params["videos"] = videos
    if audios is not None:
        params["audios"] = audios
    if subtitles is not None:
        params["subtitles"] = subtitles
    if related is not None:
        params["related"] = related
    return await proxy_request("youtube", "/api/v1/youtube/web/get_video_info", params=params)

@router.get("/get_video_info_v2")
async def get_video_info_v2(
    video_id: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取视频信息 V2/Get video information V2"""
    params: dict[str, Any] = {}
    if video_id is not None:
        params["video_id"] = video_id
    return await proxy_request("youtube", "/api/v1/youtube/web/get_video_info_v2", params=params)

@router.get("/get_video_info_v3")
async def get_video_info_v3(
    video_id: str,
    request: Request,
    language_code: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取视频详情 V3/Get video information V3"""
    params: dict[str, Any] = {}
    if video_id is not None:
        params["video_id"] = video_id
    if language_code is not None:
        params["language_code"] = language_code
    return await proxy_request("youtube", "/api/v1/youtube/web/get_video_info_v3", params=params)

@router.get("/get_video_subtitles")
async def get_video_subtitles(
    subtitle_url: str,
    request: Request,
    format: str | None = None,
    fix_overlap: bool | None = None,
    target_lang: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取视频字幕/Get video subtitles"""
    params: dict[str, Any] = {}
    if subtitle_url is not None:
        params["subtitle_url"] = subtitle_url
    if format is not None:
        params["format"] = format
    if fix_overlap is not None:
        params["fix_overlap"] = fix_overlap
    if target_lang is not None:
        params["target_lang"] = target_lang
    return await proxy_request("youtube", "/api/v1/youtube/web/get_video_subtitles", params=params)

@router.get("/get_video_comments")
async def get_video_comments(
    video_id: str,
    request: Request,
    language_code: str | None = None,
    country_code: str | None = None,
    sort_by: str | None = None,
    continuation_token: str | None = None,
    need_format: bool | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取视频评论/Get video comments"""
    params: dict[str, Any] = {}
    if video_id is not None:
        params["video_id"] = video_id
    if language_code is not None:
        params["language_code"] = language_code
    if country_code is not None:
        params["country_code"] = country_code
    if sort_by is not None:
        params["sort_by"] = sort_by
    if continuation_token is not None:
        params["continuation_token"] = continuation_token
    if need_format is not None:
        params["need_format"] = need_format
    return await proxy_request("youtube", "/api/v1/youtube/web/get_video_comments", params=params)

@router.get("/get_video_comment_replies")
async def get_video_comment_replies(
    continuation_token: str,
    request: Request,
    language_code: str | None = None,
    country_code: str | None = None,
    need_format: bool | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取视频二级评论/Get video sub comments"""
    params: dict[str, Any] = {}
    if continuation_token is not None:
        params["continuation_token"] = continuation_token
    if language_code is not None:
        params["language_code"] = language_code
    if country_code is not None:
        params["country_code"] = country_code
    if need_format is not None:
        params["need_format"] = need_format
    return await proxy_request("youtube", "/api/v1/youtube/web/get_video_comment_replies", params=params)

@router.get("/get_channel_description")
async def get_channel_description(
    request: Request,
    channel_id: str | None = None,
    continuation_token: str | None = None,
    language_code: str | None = None,
    country_code: str | None = None,
    need_format: bool | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取频道描述信息/Get channel description"""
    params: dict[str, Any] = {}
    if channel_id is not None:
        params["channel_id"] = channel_id
    if continuation_token is not None:
        params["continuation_token"] = continuation_token
    if language_code is not None:
        params["language_code"] = language_code
    if country_code is not None:
        params["country_code"] = country_code
    if need_format is not None:
        params["need_format"] = need_format
    return await proxy_request("youtube", "/api/v1/youtube/web/get_channel_description", params=params)

@router.get("/get_relate_video")
async def get_relate_video(
    video_id: str,
    request: Request,
    continuation_token: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取推荐视频/Get related videos"""
    params: dict[str, Any] = {}
    if video_id is not None:
        params["video_id"] = video_id
    if continuation_token is not None:
        params["continuation_token"] = continuation_token
    return await proxy_request("youtube", "/api/v1/youtube/web/get_relate_video", params=params)

@router.get("/search_video")
async def search_video(
    search_query: str,
    request: Request,
    language_code: str | None = None,
    order_by: str | None = None,
    country_code: str | None = None,
    continuation_token: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """搜索视频/Search video"""
    params: dict[str, Any] = {}
    if search_query is not None:
        params["search_query"] = search_query
    if language_code is not None:
        params["language_code"] = language_code
    if order_by is not None:
        params["order_by"] = order_by
    if country_code is not None:
        params["country_code"] = country_code
    if continuation_token is not None:
        params["continuation_token"] = continuation_token
    return await proxy_request("youtube", "/api/v1/youtube/web/search_video", params=params)

@router.get("/get_general_search")
async def get_general_search(
    search_query: str,
    request: Request,
    language_code: str | None = None,
    country_code: str | None = None,
    time_zone: str | None = None,
    upload_time: str | None = None,
    duration: str | None = None,
    content_type: str | None = None,
    feature: str | None = None,
    sort_by: str | None = None,
    continuation_token: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """综合搜索（支持过滤条件）/General search with filters"""
    params: dict[str, Any] = {}
    if search_query is not None:
        params["search_query"] = search_query
    if language_code is not None:
        params["language_code"] = language_code
    if country_code is not None:
        params["country_code"] = country_code
    if time_zone is not None:
        params["time_zone"] = time_zone
    if upload_time is not None:
        params["upload_time"] = upload_time
    if duration is not None:
        params["duration"] = duration
    if content_type is not None:
        params["content_type"] = content_type
    if feature is not None:
        params["feature"] = feature
    if sort_by is not None:
        params["sort_by"] = sort_by
    if continuation_token is not None:
        params["continuation_token"] = continuation_token
    return await proxy_request("youtube", "/api/v1/youtube/web/get_general_search", params=params)

@router.get("/get_shorts_search")
async def get_shorts_search(
    search_query: str,
    request: Request,
    language_code: str | None = None,
    country_code: str | None = None,
    time_zone: str | None = None,
    upload_time: str | None = None,
    sort_by: str | None = None,
    continuation_token: str | None = None,
    filter_mixed_content: bool | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """YouTube Shorts短视频搜索/YouTube Shorts search"""
    params: dict[str, Any] = {}
    if search_query is not None:
        params["search_query"] = search_query
    if language_code is not None:
        params["language_code"] = language_code
    if country_code is not None:
        params["country_code"] = country_code
    if time_zone is not None:
        params["time_zone"] = time_zone
    if upload_time is not None:
        params["upload_time"] = upload_time
    if sort_by is not None:
        params["sort_by"] = sort_by
    if continuation_token is not None:
        params["continuation_token"] = continuation_token
    if filter_mixed_content is not None:
        params["filter_mixed_content"] = filter_mixed_content
    return await proxy_request("youtube", "/api/v1/youtube/web/get_shorts_search", params=params)

@router.get("/get_channel_id")
async def get_channel_id(
    channel_name: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取频道ID/Get channel ID"""
    params: dict[str, Any] = {}
    if channel_name is not None:
        params["channel_name"] = channel_name
    return await proxy_request("youtube", "/api/v1/youtube/web/get_channel_id", params=params)

@router.get("/get_channel_id_v2")
async def get_channel_id_v2(
    channel_url: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """从频道URL获取频道ID V2/Get channel ID from URL V2"""
    params: dict[str, Any] = {}
    if channel_url is not None:
        params["channel_url"] = channel_url
    return await proxy_request("youtube", "/api/v1/youtube/web/get_channel_id_v2", params=params)

@router.get("/get_channel_url")
async def get_channel_url(
    channel_id: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """从频道ID获取频道URL/Get channel URL from channel ID"""
    params: dict[str, Any] = {}
    if channel_id is not None:
        params["channel_id"] = channel_id
    return await proxy_request("youtube", "/api/v1/youtube/web/get_channel_url", params=params)

@router.get("/get_channel_info")
async def get_channel_info(
    channel_id: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取频道信息/Get channel information"""
    params: dict[str, Any] = {}
    if channel_id is not None:
        params["channel_id"] = channel_id
    return await proxy_request("youtube", "/api/v1/youtube/web/get_channel_info", params=params)

@router.get("/get_channel_videos")
async def get_channel_videos(
    channel_id: str,
    request: Request,
    continuation_token: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取频道视频 V1（即将过时，优先使用 V2）/Get channel videos V1 (deprecated soon, use V2 first)"""
    params: dict[str, Any] = {}
    if channel_id is not None:
        params["channel_id"] = channel_id
    if continuation_token is not None:
        params["continuation_token"] = continuation_token
    return await proxy_request("youtube", "/api/v1/youtube/web/get_channel_videos", params=params)

@router.get("/get_channel_videos_v2")
async def get_channel_videos_v2(
    channel_id: str,
    request: Request,
    lang: str | None = None,
    sortBy: str | None = None,
    contentType: str | None = None,
    nextToken: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取频道视频 V2/Get channel videos V2"""
    params: dict[str, Any] = {}
    if channel_id is not None:
        params["channel_id"] = channel_id
    if lang is not None:
        params["lang"] = lang
    if sortBy is not None:
        params["sortBy"] = sortBy
    if contentType is not None:
        params["contentType"] = contentType
    if nextToken is not None:
        params["nextToken"] = nextToken
    return await proxy_request("youtube", "/api/v1/youtube/web/get_channel_videos_v2", params=params)

@router.get("/get_channel_videos_v3")
async def get_channel_videos_v3(
    channel_id: str,
    request: Request,
    language_code: str | None = None,
    country_code: str | None = None,
    continuation_token: str | None = None,
    need_format: bool | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取频道视频 V3/Get channel videos V3"""
    params: dict[str, Any] = {}
    if channel_id is not None:
        params["channel_id"] = channel_id
    if language_code is not None:
        params["language_code"] = language_code
    if country_code is not None:
        params["country_code"] = country_code
    if continuation_token is not None:
        params["continuation_token"] = continuation_token
    if need_format is not None:
        params["need_format"] = need_format
    return await proxy_request("youtube", "/api/v1/youtube/web/get_channel_videos_v3", params=params)

@router.get("/get_channel_short_videos")
async def get_channel_short_videos(
    channel_id: str,
    request: Request,
    continuation_token: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取频道短视频/Get channel short videos"""
    params: dict[str, Any] = {}
    if channel_id is not None:
        params["channel_id"] = channel_id
    if continuation_token is not None:
        params["continuation_token"] = continuation_token
    return await proxy_request("youtube", "/api/v1/youtube/web/get_channel_short_videos", params=params)

@router.get("/search_channel")
async def search_channel(
    channel_id: str,
    search_query: str,
    request: Request,
    language_code: str | None = None,
    country_code: str | None = None,
    continuation_token: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """搜索频道/Search channel"""
    params: dict[str, Any] = {}
    if channel_id is not None:
        params["channel_id"] = channel_id
    if search_query is not None:
        params["search_query"] = search_query
    if language_code is not None:
        params["language_code"] = language_code
    if country_code is not None:
        params["country_code"] = country_code
    if continuation_token is not None:
        params["continuation_token"] = continuation_token
    return await proxy_request("youtube", "/api/v1/youtube/web/search_channel", params=params)

@router.get("/get_trending_videos")
async def get_trending_videos(
    request: Request,
    language_code: str | None = None,
    country_code: str | None = None,
    section: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取趋势视频/Get trending videos"""
    params: dict[str, Any] = {}
    if language_code is not None:
        params["language_code"] = language_code
    if country_code is not None:
        params["country_code"] = country_code
    if section is not None:
        params["section"] = section
    return await proxy_request("youtube", "/api/v1/youtube/web/get_trending_videos", params=params)
