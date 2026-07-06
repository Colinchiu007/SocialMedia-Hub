"""Auto-generated routes for Bilibili-Web-API."""

from __future__ import annotations

from typing import Any

from fastapi import APIRouter, Depends, Request

from socialmedia_hub.server._core import proxy_request, verify_api_key

router = APIRouter(prefix="/api/v1/bilibili/web", tags=["bilibili_web"])

@router.get("/fetch_one_video")
async def fetch_one_video(
    bv_id: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取单个视频详情信息/Get single video data"""
    params: dict[str, Any] = {}
    if bv_id is not None:
        params["bv_id"] = bv_id
    return await proxy_request("bilibili", "/api/v1/bilibili/web/fetch_one_video", params=params)

@router.get("/fetch_one_video_v2")
async def fetch_one_video_v2(
    a_id: str,
    c_id: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取单个视频详情信息V2/Get single video data V2"""
    params: dict[str, Any] = {}
    if a_id is not None:
        params["a_id"] = a_id
    if c_id is not None:
        params["c_id"] = c_id
    return await proxy_request("bilibili", "/api/v1/bilibili/web/fetch_one_video_v2", params=params)

@router.get("/fetch_one_video_v3")
async def fetch_one_video_v3(
    url: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取单个视频详情信息V3/Get single video data V3"""
    params: dict[str, Any] = {}
    if url is not None:
        params["url"] = url
    return await proxy_request("bilibili", "/api/v1/bilibili/web/fetch_one_video_v3", params=params)

@router.get("/fetch_video_detail")
async def fetch_video_detail(
    aid: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取单个视频详情/Get single video detail"""
    params: dict[str, Any] = {}
    if aid is not None:
        params["aid"] = aid
    return await proxy_request("bilibili", "/api/v1/bilibili/web/fetch_video_detail", params=params)

@router.get("/fetch_video_play_info")
async def fetch_video_play_info(
    url: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取单个视频播放信息/Get single video play info"""
    params: dict[str, Any] = {}
    if url is not None:
        params["url"] = url
    return await proxy_request("bilibili", "/api/v1/bilibili/web/fetch_video_play_info", params=params)

@router.get("/fetch_video_subtitle")
async def fetch_video_subtitle(
    a_id: str,
    c_id: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取视频字幕信息/Get video subtitle info"""
    params: dict[str, Any] = {}
    if a_id is not None:
        params["a_id"] = a_id
    if c_id is not None:
        params["c_id"] = c_id
    return await proxy_request("bilibili", "/api/v1/bilibili/web/fetch_video_subtitle", params=params)

@router.get("/fetch_hot_search")
async def fetch_hot_search(
    limit: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取热门搜索信息/Get hot search data"""
    params: dict[str, Any] = {}
    if limit is not None:
        params["limit"] = limit
    return await proxy_request("bilibili", "/api/v1/bilibili/web/fetch_hot_search", params=params)

@router.get("/fetch_general_search")
async def fetch_general_search(
    keyword: str,
    order: str,
    page: int,
    page_size: int,
    request: Request,
    duration: int | None = None,
    pubtime_begin_s: int | None = None,
    pubtime_end_s: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取综合搜索信息/Get general search data"""
    params: dict[str, Any] = {}
    if keyword is not None:
        params["keyword"] = keyword
    if order is not None:
        params["order"] = order
    if page is not None:
        params["page"] = page
    if page_size is not None:
        params["page_size"] = page_size
    if duration is not None:
        params["duration"] = duration
    if pubtime_begin_s is not None:
        params["pubtime_begin_s"] = pubtime_begin_s
    if pubtime_end_s is not None:
        params["pubtime_end_s"] = pubtime_end_s
    return await proxy_request("bilibili", "/api/v1/bilibili/web/fetch_general_search", params=params)

@router.get("/fetch_video_playurl")
async def fetch_video_playurl(
    bv_id: str,
    cid: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取视频流地址/Get video playurl"""
    params: dict[str, Any] = {}
    if bv_id is not None:
        params["bv_id"] = bv_id
    if cid is not None:
        params["cid"] = cid
    return await proxy_request("bilibili", "/api/v1/bilibili/web/fetch_video_playurl", params=params)

@router.post("/fetch_vip_video_playurl")
async def fetch_vip_video_playurl(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取大会员清晰度视频流地址/Get VIP video playurl"""
    body = await request.json()
    return await proxy_request("bilibili", "/api/v1/bilibili/web/fetch_vip_video_playurl", json_body=body)

@router.get("/fetch_user_post_videos")
async def fetch_user_post_videos(
    uid: str,
    request: Request,
    pn: int | None = None,
    order: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户主页作品数据/Get user homepage video data"""
    params: dict[str, Any] = {}
    if uid is not None:
        params["uid"] = uid
    if pn is not None:
        params["pn"] = pn
    if order is not None:
        params["order"] = order
    return await proxy_request("bilibili", "/api/v1/bilibili/web/fetch_user_post_videos", params=params)

@router.get("/fetch_collect_folders")
async def fetch_collect_folders(
    uid: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户所有收藏夹信息/Get user collection folders"""
    params: dict[str, Any] = {}
    if uid is not None:
        params["uid"] = uid
    return await proxy_request("bilibili", "/api/v1/bilibili/web/fetch_collect_folders", params=params)

@router.get("/fetch_user_collection_videos")
async def fetch_user_collection_videos(
    folder_id: str,
    request: Request,
    pn: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取指定收藏夹内视频数据/Gets video data from a collection folder"""
    params: dict[str, Any] = {}
    if folder_id is not None:
        params["folder_id"] = folder_id
    if pn is not None:
        params["pn"] = pn
    return await proxy_request("bilibili", "/api/v1/bilibili/web/fetch_user_collection_videos", params=params)

@router.get("/fetch_user_profile")
async def fetch_user_profile(
    uid: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取指定用户的信息/Get information of specified user"""
    params: dict[str, Any] = {}
    if uid is not None:
        params["uid"] = uid
    return await proxy_request("bilibili", "/api/v1/bilibili/web/fetch_user_profile", params=params)

@router.get("/fetch_user_up_stat")
async def fetch_user_up_stat(
    uid: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取UP主状态统计/Get UP stat (total likes and views)"""
    params: dict[str, Any] = {}
    if uid is not None:
        params["uid"] = uid
    return await proxy_request("bilibili", "/api/v1/bilibili/web/fetch_user_up_stat", params=params)

@router.get("/fetch_user_relation_stat")
async def fetch_user_relation_stat(
    uid: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户关系状态统计/Get user relation stat (following and followers)"""
    params: dict[str, Any] = {}
    if uid is not None:
        params["uid"] = uid
    return await proxy_request("bilibili", "/api/v1/bilibili/web/fetch_user_relation_stat", params=params)

@router.get("/fetch_com_popular")
async def fetch_com_popular(
    request: Request,
    pn: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取综合热门视频信息/Get comprehensive popular video information"""
    params: dict[str, Any] = {}
    if pn is not None:
        params["pn"] = pn
    return await proxy_request("bilibili", "/api/v1/bilibili/web/fetch_com_popular", params=params)

@router.get("/fetch_video_comments")
async def fetch_video_comments(
    bv_id: str,
    request: Request,
    pn: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取指定视频的评论/Get comments on the specified video"""
    params: dict[str, Any] = {}
    if bv_id is not None:
        params["bv_id"] = bv_id
    if pn is not None:
        params["pn"] = pn
    return await proxy_request("bilibili", "/api/v1/bilibili/web/fetch_video_comments", params=params)

@router.get("/fetch_comment_reply")
async def fetch_comment_reply(
    bv_id: str,
    rpid: str,
    request: Request,
    pn: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取视频下指定评论的回复/Get reply to the specified comment"""
    params: dict[str, Any] = {}
    if bv_id is not None:
        params["bv_id"] = bv_id
    if pn is not None:
        params["pn"] = pn
    if rpid is not None:
        params["rpid"] = rpid
    return await proxy_request("bilibili", "/api/v1/bilibili/web/fetch_comment_reply", params=params)

@router.get("/fetch_user_dynamic")
async def fetch_user_dynamic(
    uid: str,
    request: Request,
    offset: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取指定用户动态/Get dynamic information of specified user"""
    params: dict[str, Any] = {}
    if uid is not None:
        params["uid"] = uid
    if offset is not None:
        params["offset"] = offset
    return await proxy_request("bilibili", "/api/v1/bilibili/web/fetch_user_dynamic", params=params)

@router.get("/fetch_dynamic_detail")
async def fetch_dynamic_detail(
    dynamic_id: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取动态详情/Get dynamic detail"""
    params: dict[str, Any] = {}
    if dynamic_id is not None:
        params["dynamic_id"] = dynamic_id
    return await proxy_request("bilibili", "/api/v1/bilibili/web/fetch_dynamic_detail", params=params)

@router.get("/fetch_dynamic_detail_v2")
async def fetch_dynamic_detail_v2(
    dynamic_id: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取动态详情v2/Get dynamic detail v2"""
    params: dict[str, Any] = {}
    if dynamic_id is not None:
        params["dynamic_id"] = dynamic_id
    return await proxy_request("bilibili", "/api/v1/bilibili/web/fetch_dynamic_detail_v2", params=params)

@router.get("/fetch_video_danmaku")
async def fetch_video_danmaku(
    cid: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取视频实时弹幕/Get Video Danmaku"""
    params: dict[str, Any] = {}
    if cid is not None:
        params["cid"] = cid
    return await proxy_request("bilibili", "/api/v1/bilibili/web/fetch_video_danmaku", params=params)

@router.get("/fetch_live_room_detail")
async def fetch_live_room_detail(
    room_id: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取指定直播间信息/Get information of specified live room"""
    params: dict[str, Any] = {}
    if room_id is not None:
        params["room_id"] = room_id
    return await proxy_request("bilibili", "/api/v1/bilibili/web/fetch_live_room_detail", params=params)

@router.get("/fetch_live_videos")
async def fetch_live_videos(
    room_id: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取直播间视频流/Get live video data of specified room"""
    params: dict[str, Any] = {}
    if room_id is not None:
        params["room_id"] = room_id
    return await proxy_request("bilibili", "/api/v1/bilibili/web/fetch_live_videos", params=params)

@router.get("/fetch_live_streamers")
async def fetch_live_streamers(
    area_id: str,
    request: Request,
    pn: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取指定分区正在直播的主播/Get live streamers of specified live area"""
    params: dict[str, Any] = {}
    if area_id is not None:
        params["area_id"] = area_id
    if pn is not None:
        params["pn"] = pn
    return await proxy_request("bilibili", "/api/v1/bilibili/web/fetch_live_streamers", params=params)

@router.get("/fetch_all_live_areas")
async def fetch_all_live_areas(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取所有直播分区列表/Get a list of all live areas"""
    return await proxy_request("bilibili", "/api/v1/bilibili/web/fetch_all_live_areas")

@router.get("/bv_to_aid")
async def bv_to_aid(
    bv_id: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """通过bv号获得视频aid号/Generate aid by bvid"""
    params: dict[str, Any] = {}
    if bv_id is not None:
        params["bv_id"] = bv_id
    return await proxy_request("bilibili", "/api/v1/bilibili/web/bv_to_aid", params=params)

@router.get("/fetch_video_parts")
async def fetch_video_parts(
    bv_id: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """通过bv号获得视频分p信息/Get Video Parts By bvid"""
    params: dict[str, Any] = {}
    if bv_id is not None:
        params["bv_id"] = bv_id
    return await proxy_request("bilibili", "/api/v1/bilibili/web/fetch_video_parts", params=params)

@router.get("/fetch_get_user_id")
async def fetch_get_user_id(
    share_link: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """提取用户ID/Extract user ID"""
    params: dict[str, Any] = {}
    if share_link is not None:
        params["share_link"] = share_link
    return await proxy_request("bilibili", "/api/v1/bilibili/web/fetch_get_user_id", params=params)
