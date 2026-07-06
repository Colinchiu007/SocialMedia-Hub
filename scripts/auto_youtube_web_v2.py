"""Auto-generated routes for YouTube-Web-V2-API."""

from __future__ import annotations

from typing import Any

from fastapi import APIRouter, Depends, Request

from socialmedia_hub.server._core import proxy_request, verify_api_key

router = APIRouter(prefix="/api/v1/youtube/web/v2", tags=["youtube_web_v2"])

@router.get("/get_video_info")
async def get_video_info(
    need_format: bool | None = None,
    language_code: str | None = None,
    video_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取视频详情 /Get video information"""
        params: dict[str, Any] = {}
        if video_id is not None:
            params["video_id"] = video_id
        if language_code is not None:
            params["language_code"] = language_code
        if need_format is not None:
            params["need_format"] = need_format
        body = await request.json()
        return await proxy_request("youtube", "/api/v1/youtube/web_v2/get_video_info", json_body=body)

@router.get("/get_video_comments")
async def get_video_comments(
    need_format: bool | None = None,
    continuation_token: str | None = None,
    sort_by: str | None = None,
    country_code: str | None = None,
    language_code: str | None = None,
    video_id: str,
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
        body = await request.json()
        return await proxy_request("youtube", "/api/v1/youtube/web_v2/get_video_comments", json_body=body)

@router.get("/get_video_comment_replies")
async def get_video_comment_replies(
    need_format: bool | None = None,
    country_code: str | None = None,
    language_code: str | None = None,
    continuation_token: str,
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
        body = await request.json()
        return await proxy_request("youtube", "/api/v1/youtube/web_v2/get_video_comment_replies", json_body=body)

@router.get("/get_channel_description")
async def get_channel_description(
    need_format: bool | None = None,
    country_code: str | None = None,
    language_code: str | None = None,
    continuation_token: str | None = None,
    channel_id: str | None = None,
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
        body = await request.json()
        return await proxy_request("youtube", "/api/v1/youtube/web_v2/get_channel_description", json_body=body)

@router.get("/get_general_search")
async def get_general_search(
    continuation_token: str | None = None,
    sort_by: str | None = None,
    feature: str | None = None,
    content_type: str | None = None,
    duration: str | None = None,
    upload_time: str | None = None,
    time_zone: str | None = None,
    country_code: str | None = None,
    language_code: str | None = None,
    search_query: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """综合搜索（原始数据，推荐使用V2）/General search (raw data, recommend V2)"""
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
        body = await request.json()
        return await proxy_request("youtube", "/api/v1/youtube/web_v2/get_general_search", json_body=body)

@router.get("/get_general_search_v2")
async def get_general_search_v2(
    sort_by: str | None = None,
    features: str | None = None,
    duration: str | None = None,
    type: str | None = None,
    upload_date: str | None = None,
    continuation_token: str | None = None,
    keyword: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """综合搜索V2/General search V2"""
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
        body = await request.json()
        return await proxy_request("youtube", "/api/v1/youtube/web_v2/get_general_search_v2", json_body=body)

@router.get("/get_shorts_search")
async def get_shorts_search(
    filter_mixed_content: bool | None = None,
    continuation_token: str | None = None,
    sort_by: str | None = None,
    upload_time: str | None = None,
    time_zone: str | None = None,
    country_code: str | None = None,
    language_code: str | None = None,
    search_query: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """Shorts搜索（原始数据，推荐使用V2）/Shorts search (raw data, recommend V2)"""
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
        body = await request.json()
        return await proxy_request("youtube", "/api/v1/youtube/web_v2/get_shorts_search", json_body=body)

@router.get("/get_shorts_search_v2")
async def get_shorts_search_v2(
    sort_by: str | None = None,
    upload_date: str | None = None,
    continuation_token: str | None = None,
    keyword: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """Shorts搜索V2/Shorts search V2"""
        params: dict[str, Any] = {}
        if keyword is not None:
            params["keyword"] = keyword
        if continuation_token is not None:
            params["continuation_token"] = continuation_token
        if upload_date is not None:
            params["upload_date"] = upload_date
        if sort_by is not None:
            params["sort_by"] = sort_by
        body = await request.json()
        return await proxy_request("youtube", "/api/v1/youtube/web_v2/get_shorts_search_v2", json_body=body)

@router.get("/get_channel_id")
async def get_channel_id(
    channel_url: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """从频道URL获取频道ID /Get channel ID from URL"""
        params: dict[str, Any] = {}
        if channel_url is not None:
            params["channel_url"] = channel_url
        body = await request.json()
        return await proxy_request("youtube", "/api/v1/youtube/web_v2/get_channel_id", json_body=body)

@router.get("/get_channel_url")
async def get_channel_url(
    channel_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """从频道ID获取频道URL/Get channel URL from channel ID"""
        params: dict[str, Any] = {}
        if channel_id is not None:
            params["channel_id"] = channel_id
        body = await request.json()
        return await proxy_request("youtube", "/api/v1/youtube/web_v2/get_channel_url", json_body=body)

@router.get("/get_channel_videos")
async def get_channel_videos(
    need_format: bool | None = None,
    continuation_token: str | None = None,
    country_code: str | None = None,
    language_code: str | None = None,
    channel_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取频道视频 /Get channel videos"""
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
        body = await request.json()
        return await proxy_request("youtube", "/api/v1/youtube/web_v2/get_channel_videos", json_body=body)

@router.get("/get_video_streams")
async def get_video_streams(
    video_url: str | None = None,
    video_id: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取视频流信息/Get video streams info"""
        params: dict[str, Any] = {}
        if video_id is not None:
            params["video_id"] = video_id
        if video_url is not None:
            params["video_url"] = video_url
        body = await request.json()
        return await proxy_request("youtube", "/api/v1/youtube/web_v2/get_video_streams", json_body=body)

@router.get("/get_video_streams_v2")
async def get_video_streams_v2(
    video_url: str | None = None,
    video_id: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取视频流信息 V2/Get video streams info V2"""
        params: dict[str, Any] = {}
        if video_id is not None:
            params["video_id"] = video_id
        if video_url is not None:
            params["video_url"] = video_url
        body = await request.json()
        return await proxy_request("youtube", "/api/v1/youtube/web_v2/get_video_streams_v2", json_body=body)

@router.get("/get_signed_stream_url")
async def get_signed_stream_url(
    itag: int,
    video_url: str | None = None,
    video_id: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取已签名的视频流URL/Get signed video stream URL"""
        params: dict[str, Any] = {}
        if video_id is not None:
            params["video_id"] = video_id
        if video_url is not None:
            params["video_url"] = video_url
        if itag is not None:
            params["itag"] = itag
        body = await request.json()
        return await proxy_request("youtube", "/api/v1/youtube/web_v2/get_signed_stream_url", json_body=body)

@router.get("/get_video_captions")
async def get_video_captions(
    format: str | None = None,
    language_code: str | None = None,
    video_url: str | None = None,
    video_id: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取视频字幕/Get video captions"""
        params: dict[str, Any] = {}
        if video_id is not None:
            params["video_id"] = video_id
        if video_url is not None:
            params["video_url"] = video_url
        if language_code is not None:
            params["language_code"] = language_code
        if format is not None:
            params["format"] = format
        body = await request.json()
        return await proxy_request("youtube", "/api/v1/youtube/web_v2/get_video_captions", json_body=body)

@router.get("/get_related_videos")
async def get_related_videos(
    need_format: bool | None = None,
    video_url: str | None = None,
    video_id: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取视频相似内容/Get related videos"""
        params: dict[str, Any] = {}
        if video_id is not None:
            params["video_id"] = video_id
        if video_url is not None:
            params["video_url"] = video_url
        if need_format is not None:
            params["need_format"] = need_format
        body = await request.json()
        return await proxy_request("youtube", "/api/v1/youtube/web_v2/get_related_videos", json_body=body)

@router.get("/get_channel_shorts")
async def get_channel_shorts(
    need_format: bool | None = None,
    continuation_token: str | None = None,
    channel_url: str | None = None,
    channel_id: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取频道短视频列表/Get channel shorts"""
        params: dict[str, Any] = {}
        if channel_id is not None:
            params["channel_id"] = channel_id
        if channel_url is not None:
            params["channel_url"] = channel_url
        if continuation_token is not None:
            params["continuation_token"] = continuation_token
        if need_format is not None:
            params["need_format"] = need_format
        body = await request.json()
        return await proxy_request("youtube", "/api/v1/youtube/web_v2/get_channel_shorts", json_body=body)

@router.get("/get_search_suggestions")
async def get_search_suggestions(
    region: str | None = None,
    language: str | None = None,
    keyword: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取搜索推荐词/Get search suggestions"""
        params: dict[str, Any] = {}
        if keyword is not None:
            params["keyword"] = keyword
        if language is not None:
            params["language"] = language
        if region is not None:
            params["region"] = region
        body = await request.json()
        return await proxy_request("youtube", "/api/v1/youtube/web_v2/get_search_suggestions", json_body=body)

@router.get("/search_channels")
async def search_channels(
    need_format: bool | None = None,
    continuation_token: str | None = None,
    keyword: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """搜索频道/Search channels"""
        params: dict[str, Any] = {}
        if keyword is not None:
            params["keyword"] = keyword
        if continuation_token is not None:
            params["continuation_token"] = continuation_token
        if need_format is not None:
            params["need_format"] = need_format
        body = await request.json()
        return await proxy_request("youtube", "/api/v1/youtube/web_v2/search_channels", json_body=body)
