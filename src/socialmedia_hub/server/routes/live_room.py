"""Live Room API routes — Real-time live streaming data."""

from __future__ import annotations

from typing import Any

from fastapi import APIRouter, Depends

from socialmedia_hub.server._core import proxy_request, verify_api_key

router = APIRouter(prefix="/api/v1/live", tags=["live-room"])


# ===========================================================================
# Douyin Live
# ===========================================================================


@router.get("/douyin/fetch_room_info")
async def douyin_fetch_room_info(
    room_id: str, token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取抖音直播间信息 / Get Douyin live room info."""
    return await proxy_request("douyin", "/webcast/room/web/enter/", params={"room_id": room_id})


@router.get("/douyin/fetch_room_danmaku")
async def douyin_fetch_room_danmaku(
    room_id: str, token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取抖音直播弹幕 / Get Douyin live danmaku."""
    return await proxy_request("douyin", "/webcast/im/fetch/", params={"room_id": room_id})


@router.get("/douyin/fetch_gift_ranking")
async def douyin_fetch_gift_ranking(
    room_id: str, rank_type: int = 0, token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取抖音直播礼物排行 / Get Douyin live gift ranking."""
    return await proxy_request(
        "douyin", "/webcast/rank/list/",
        params={"room_id": room_id, "rank_type": rank_type}
    )


@router.get("/douyin/fetch_room_product")
async def douyin_fetch_room_product(
    room_id: str, author_id: str, token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取抖音直播间商品 / Get Douyin live room products."""
    return await proxy_request(
        "douyin", "/webcast/gift/list/",
        params={"room_id": room_id, "author_id": author_id}
    )


@router.get("/douyin/fetch_user_live")
async def douyin_fetch_user_live(
    uid: str, token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户直播状态 / Get user live status."""
    return await proxy_request("douyin", "/webcast/room/web/enter/", params={"uid": uid})


@router.get("/douyin/fetch_live_list")
async def douyin_fetch_live_list(
    count: int = 20, token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取直播列表 / Get live list."""
    return await proxy_request("douyin", "/webcast/room/web/list/", params={"count": count})


# ===========================================================================
# TikTok Live
# ===========================================================================


@router.get("/tiktok/fetch_room_info")
async def tiktok_fetch_room_info(
    room_id: str, token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取TikTok直播间信息 / Get TikTok live room info."""
    return await proxy_request("tiktok", "/webcast/room/web/enter/", params={"room_id": room_id})


@router.get("/tiktok/fetch_room_danmaku")
async def tiktok_fetch_room_danmaku(
    room_id: str, token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取TikTok直播弹幕 / Get TikTok live danmaku."""
    return await proxy_request("tiktok", "/webcast/im/fetch/", params={"room_id": room_id})


@router.get("/tiktok/fetch_gift_ranking")
async def tiktok_fetch_gift_ranking(
    room_id: str, token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取TikTok直播礼物排行 / Get TikTok live gift ranking."""
    return await proxy_request("tiktok", "/webcast/rank/list/", params={"room_id": room_id})


@router.get("/tiktok/fetch_user_live")
async def tiktok_fetch_user_live(
    username: str, token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户直播状态 / Get user live status."""
    return await proxy_request("tiktok", "/webcast/room/web/enter/", params={"uniqueId": username})


@router.get("/tiktok/fetch_live_list")
async def tiktok_fetch_live_list(
    count: int = 20, token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取直播列表 / Get live list."""
    return await proxy_request("tiktok", "/webcast/room/web/list/", params={"count": count})


# ===========================================================================
# Bilibili Live
# ===========================================================================


@router.get("/bilibili/fetch_room_info")
async def bilibili_fetch_room_info(
    room_id: str, token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取B站直播间信息 / Get Bilibili live room info."""
    return await proxy_request("bilibili", "/x/live/web/v1/web/RoomInfo", params={"room_id": room_id})


@router.get("/bilibili/fetch_room_stream")
async def bilibili_fetch_room_stream(
    room_id: str, token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取B站直播流 / Get Bilibili live stream."""
    return await proxy_request(
        "bilibili", "/x/live/web/v1/web/playUrl",
        params={"room_id": room_id, "qn": 10000, "platform": "web"}
    )


@router.get("/bilibili/fetch_live_areas")
async def bilibili_fetch_live_areas(
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取B站直播分区 / Get Bilibili live areas."""
    return await proxy_request("bilibili", "/x/live/area/v2/Area/getList")


@router.get("/bilibili/fetch_live_streamers")
async def bilibili_fetch_live_streamers(
    area_id: str = "0", pn: int = 1, token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取分区主播列表 / Get live streamers by area."""
    return await proxy_request(
        "bilibili", "/x/live/second/getList",
        params={"platform": "web", "parent_area_id": area_id, "page": pn}
    )


# ===========================================================================
# Kuaishou Live
# ===========================================================================


@router.get("/kuaishou/fetch_room_info")
async def kuaishou_fetch_room_info(
    room_id: str, token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取快手直播间信息 / Get Kuaishou live room info."""
    return await proxy_request("kuaishou", f"/short-video/{room_id}")


@router.get("/kuaishou/fetch_live_list")
async def kuaishou_fetch_live_list(
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取快手直播列表 / Get Kuaishou live list."""
    return await proxy_request("kuaishou", "/live/list")


# ===========================================================================
# Weibo Live
# ===========================================================================


@router.get("/weibo/fetch_live_list")
async def weibo_fetch_live_list(
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取微博直播列表 / Get Weibo live list."""
    return await proxy_request("weibo", "/api/container/getIndex", params={"containerid": "231053_-_live"})


# ===========================================================================
# Generic Live Room
# ===========================================================================


@router.get("/generic/fetch_room_info")
async def generic_fetch_room_info(
    platform: str, room_id: str, token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """通用直播间信息获取 / Generic live room info."""
    return await proxy_request(platform, f"/live/room/{room_id}")


@router.get("/generic/fetch_room_danmaku")
async def generic_fetch_room_danmaku(
    platform: str, room_id: str, token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """通用直播弹幕获取 / Generic live danmaku."""
    return await proxy_request(platform, f"/live/danmaku/{room_id}")


@router.get("/generic/fetch_room_product")
async def generic_fetch_room_product(
    platform: str, room_id: str, token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """通用直播间商品获取 / Generic live room products."""
    return await proxy_request(platform, f"/live/product/{room_id}")
