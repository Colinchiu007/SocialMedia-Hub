"""Auto-generated routes for YouTube-Web-V2-API."""

from __future__ import annotations

from typing import Any

from fastapi import APIRouter, Depends, Request

from socialmedia_hub.server._core import proxy_request, verify_api_key

router = APIRouter(prefix="/api/v1/youtube/web/v2", tags=["youtube_web_v2"])

@router.get("/get_video_info")
async def get_video_info(
    video_id: str,
    request: Request,
    language_code: str | None = None,
    need_format: bool | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取视频详情 /Get video information"""
    body = await request.json()
    params: dict[str, Any] = {}
    if video_id is not None:
        params["video_id"] = video_id
    if language_code is not None:
        params["language_code"] = language_code
    if need_format is not None:
        params["need_format"] = need_format
    return await proxy_request("youtube", "/api/v1/youtube/web_v2/get_video_info", params=params, json_body=body)

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
    body = await request.json()
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
    return await proxy_request("youtube", "/api/v1/youtube/web_v2/get_video_comments", params=params, json_body=body)

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
    body = await request.json()
    params: dict[str, Any] = {}
    if continuation_token is not None:
        params["continuation_token"] = continuation_token
    if language_code is not None:
        params["language_code"] = language_code
    if country_code is not None:
        params["country_code"] = country_code
    if need_format is not None:
        params["need_format"] = need_format
    return await proxy_request("youtube", "/api/v1/youtube/web_v2/get_video_comment_replies", params=params, json_body=body)

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
    body = await request.json()
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
    return await proxy_request("youtube", "/api/v1/youtube/web_v2/get_channel_description", params=params, json_body=body)

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
    """综合搜索（原始数据，推荐使用V2）/General search (raw data, recommend V2)"""
    body = await request.json()
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
    return await proxy_request("youtube", "/api/v1/youtube/web_v2/get_general_search", params=params, json_body=body)

@router.get("/get_general_search_v2")
async def get_general_search_v2(
    request: Request,
    keyword: str | None = None,
    continuation_token: str | None = None,
    upload_date: str | None = None,
    type: str | None = None,
    duration: str | None = None,
    features: str | None = None,
    sort_by: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """综合搜索V2/General search V2"""
    body = await request.json()
    params: dict[str, Any] = {}
    if keyword is not None:
        params["keyword"] = keyword
    if continuation_token is not None:
        params["continuation_token"] = continuation_token
    if upload_date is not None:
        params["upload_date"] = upload_date
    if type is not None:
        params["type"] = type
    if duration is not None:
        params["duration"] = duration
    if features is not None:
        params["features"] = features
    if sort_by is not None:
        params["sort_by"] = sort_by
    return await proxy_request("youtube", "/api/v1/youtube/web_v2/get_general_search_v2", params=params, json_body=body)

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
    """Shorts搜索（原始数据，推荐使用V2）/Shorts search (raw data, recommend V2)"""
    body = await request.json()
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
    return await proxy_request("youtube", "/api/v1/youtube/web_v2/get_shorts_search", params=params, json_body=body)

@router.get("/get_shorts_search_v2")
async def get_shorts_search_v2(
    request: Request,
    keyword: str | None = None,
    continuation_token: str | None = None,
    upload_date: str | None = None,
    sort_by: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """Shorts搜索V2/Shorts search V2"""
    body = await request.json()
    params: dict[str, Any] = {}
    if keyword is not None:
        params["keyword"] = keyword
    if continuation_token is not None:
        params["continuation_token"] = continuation_token
    if upload_date is not None:
        params["upload_date"] = upload_date
    if sort_by is not None:
        params["sort_by"] = sort_by
    return await proxy_request("youtube", "/api/v1/youtube/web_v2/get_shorts_search_v2", params=params, json_body=body)

@router.get("/get_channel_id")
async def get_channel_id(
    channel_url: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """从频道URL获取频道ID /Get channel ID from URL"""
    body = await request.json()
    params: dict[str, Any] = {}
    if channel_url is not None:
        params["channel_url"] = channel_url
    return await proxy_request("youtube", "/api/v1/youtube/web_v2/get_channel_id", params=params, json_body=body)

@router.get("/get_channel_url")
async def get_channel_url(
    channel_id: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """从频道ID获取频道URL/Get channel URL from channel ID"""
    body = await request.json()
    params: dict[str, Any] = {}
    if channel_id is not None:
        params["channel_id"] = channel_id
    return await proxy_request("youtube", "/api/v1/youtube/web_v2/get_channel_url", params=params, json_body=body)

@router.get("/get_channel_videos")
async def get_channel_videos(
    channel_id: str,
    request: Request,
    language_code: str | None = None,
    country_code: str | None = None,
    continuation_token: str | None = None,
    need_format: bool | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取频道视频 /Get channel videos"""
    body = await request.json()
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
    return await proxy_request("youtube", "/api/v1/youtube/web_v2/get_channel_videos", params=params, json_body=body)

@router.get("/get_video_streams")
async def get_video_streams(
    request: Request,
    video_id: str | None = None,
    video_url: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取视频流信息/Get video streams info"""
    body = await request.json()
    params: dict[str, Any] = {}
    if video_id is not None:
        params["video_id"] = video_id
    if video_url is not None:
        params["video_url"] = video_url
    return await proxy_request("youtube", "/api/v1/youtube/web_v2/get_video_streams", params=params, json_body=body)

@router.get("/get_video_streams_v2")
async def get_video_streams_v2(
    request: Request,
    video_id: str | None = None,
    video_url: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取视频流信息 V2/Get video streams info V2"""
    body = await request.json()
    params: dict[str, Any] = {}
    if video_id is not None:
        params["video_id"] = video_id
    if video_url is not None:
        params["video_url"] = video_url
    return await proxy_request("youtube", "/api/v1/youtube/web_v2/get_video_streams_v2", params=params, json_body=body)

@router.get("/get_signed_stream_url")
async def get_signed_stream_url(
    itag: int,
    request: Request,
    video_id: str | None = None,
    video_url: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取已签名的视频流URL/Get signed video stream URL"""
    body = await request.json()
    params: dict[str, Any] = {}
    if video_id is not None:
        params["video_id"] = video_id
    if video_url is not None:
        params["video_url"] = video_url
    if itag is not None:
        params["itag"] = itag
    return await proxy_request("youtube", "/api/v1/youtube/web_v2/get_signed_stream_url", params=params, json_body=body)

@router.get("/get_video_captions")
async def get_video_captions(
    request: Request,
    video_id: str | None = None,
    video_url: str | None = None,
    language_code: str | None = None,
    format: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取视频字幕/Get video captions"""
    body = await request.json()
    params: dict[str, Any] = {}
    if video_id is not None:
        params["video_id"] = video_id
    if video_url is not None:
        params["video_url"] = video_url
    if language_code is not None:
        params["language_code"] = language_code
    if format is not None:
        params["format"] = format
    return await proxy_request("youtube", "/api/v1/youtube/web_v2/get_video_captions", params=params, json_body=body)

@router.get("/get_related_videos")
async def get_related_videos(
    request: Request,
    video_id: str | None = None,
    video_url: str | None = None,
    need_format: bool | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取视频相似内容/Get related videos"""
    body = await request.json()
    params: dict[str, Any] = {}
    if video_id is not None:
        params["video_id"] = video_id
    if video_url is not None:
        params["video_url"] = video_url
    if need_format is not None:
        params["need_format"] = need_format
    return await proxy_request("youtube", "/api/v1/youtube/web_v2/get_related_videos", params=params, json_body=body)

@router.get("/get_channel_shorts")
async def get_channel_shorts(
    request: Request,
    channel_id: str | None = None,
    channel_url: str | None = None,
    continuation_token: str | None = None,
    need_format: bool | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取频道短视频列表/Get channel shorts"""
    body = await request.json()
    params: dict[str, Any] = {}
    if channel_id is not None:
        params["channel_id"] = channel_id
    if channel_url is not None:
        params["channel_url"] = channel_url
    if continuation_token is not None:
        params["continuation_token"] = continuation_token
    if need_format is not None:
        params["need_format"] = need_format
    return await proxy_request("youtube", "/api/v1/youtube/web_v2/get_channel_shorts", params=params, json_body=body)

@router.get("/get_search_suggestions")
async def get_search_suggestions(
    keyword: str,
    request: Request,
    language: str | None = None,
    region: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取搜索推荐词/Get search suggestions"""
    body = await request.json()
    params: dict[str, Any] = {}
    if keyword is not None:
        params["keyword"] = keyword
    if language is not None:
        params["language"] = language
    if region is not None:
        params["region"] = region
    return await proxy_request("youtube", "/api/v1/youtube/web_v2/get_search_suggestions", params=params, json_body=body)

@router.get("/search_channels")
async def search_channels(
    request: Request,
    keyword: str | None = None,
    continuation_token: str | None = None,
    need_format: bool | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """搜索频道/Search channels"""
    body = await request.json()
    params: dict[str, Any] = {}
    if keyword is not None:
        params["keyword"] = keyword
    if continuation_token is not None:
        params["continuation_token"] = continuation_token
    if need_format is not None:
        params["need_format"] = need_format
    return await proxy_request("youtube", "/api/v1/youtube/web_v2/search_channels", params=params, json_body=body)
