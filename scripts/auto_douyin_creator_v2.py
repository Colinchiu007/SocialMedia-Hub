"""Auto-generated routes for Douyin-Creator-V2-API."""

from __future__ import annotations

from typing import Any

from fastapi import APIRouter, Depends, Request

from socialmedia_hub.server._core import proxy_request, verify_api_key

router = APIRouter(prefix="/api/v1/douyin/creator/v2", tags=["douyin_creator_v2"])

@router.post("/fetch_item_overview_data")
async def fetch_item_overview_data(
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取作品总览数据/Fetch item overview data"""
        body = await request.json()
        return await proxy_request("douyin", "/api/v1/douyin/creator_v2/fetch_item_overview_data", json_body=body)

@router.post("/fetch_item_play_source")
async def fetch_item_play_source(
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取作品流量来源统计/Fetch item play source statistics"""
        body = await request.json()
        return await proxy_request("douyin", "/api/v1/douyin/creator_v2/fetch_item_play_source", json_body=body)

@router.post("/fetch_item_search_keyword")
async def fetch_item_search_keyword(
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取作品搜索关键词统计/Fetch item search keywords statistics"""
        body = await request.json()
        return await proxy_request("douyin", "/api/v1/douyin/creator_v2/fetch_item_search_keyword", json_body=body)

@router.post("/fetch_item_watch_trend")
async def fetch_item_watch_trend(
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取作品观看趋势分析/Fetch item watch trend analysis"""
        body = await request.json()
        return await proxy_request("douyin", "/api/v1/douyin/creator_v2/fetch_item_watch_trend", json_body=body)

@router.post("/fetch_item_danmaku_analysis")
async def fetch_item_danmaku_analysis(
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取作品弹幕分析/Fetch item bullet analysis"""
        body = await request.json()
        return await proxy_request("douyin", "/api/v1/douyin/creator_v2/fetch_item_danmaku_analysis", json_body=body)

@router.post("/fetch_item_audience_portrait")
async def fetch_item_audience_portrait(
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取作品观众数据分析/Fetch item audience portrait"""
        body = await request.json()
        return await proxy_request("douyin", "/api/v1/douyin/creator_v2/fetch_item_audience_portrait", json_body=body)

@router.post("/fetch_item_audience_others")
async def fetch_item_audience_others(
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取作品观众其他数据分析/Fetch item audience others analysis"""
        body = await request.json()
        return await proxy_request("douyin", "/api/v1/douyin/creator_v2/fetch_item_audience_others", json_body=body)

@router.post("/fetch_item_analysis_involved_vertical")
async def fetch_item_analysis_involved_vertical(
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取作品垂类标签/Fetch item analysis involved vertical"""
        body = await request.json()
        return await proxy_request("douyin", "/api/v1/douyin/creator_v2/fetch_item_analysis_involved_vertical", json_body=body)

@router.post("/fetch_item_analysis_overview")
async def fetch_item_analysis_overview(
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取投稿分析概览/Fetch item analysis overview"""
        body = await request.json()
        return await proxy_request("douyin", "/api/v1/douyin/creator_v2/fetch_item_analysis_overview", json_body=body)

@router.post("/fetch_item_analysis_item_performance")
async def fetch_item_analysis_item_performance(
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取投稿表现数据/Fetch item analysis item performance"""
        body = await request.json()
        return await proxy_request("douyin", "/api/v1/douyin/creator_v2/fetch_item_analysis_item_performance", json_body=body)

@router.post("/fetch_item_list")
async def fetch_item_list(
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取投稿作品列表/Fetch item list"""
        body = await request.json()
        return await proxy_request("douyin", "/api/v1/douyin/creator_v2/fetch_item_list", json_body=body)

@router.post("/fetch_item_list_download")
async def fetch_item_list_download(
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """导出投稿作品列表/Download item list"""
        body = await request.json()
        return await proxy_request("douyin", "/api/v1/douyin/creator_v2/fetch_item_list_download", json_body=body)

@router.post("/fetch_live_room_history_list")
async def fetch_live_room_history_list(
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取直播场次历史记录/Fetch live room history list"""
        body = await request.json()
        return await proxy_request("douyin", "/api/v1/douyin/creator_v2/fetch_live_room_history_list", json_body=body)

@router.post("/fetch_author_diagnosis")
async def fetch_author_diagnosis(
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取创作者账号诊断/Fetch author diagnosis"""
        body = await request.json()
        return await proxy_request("douyin", "/api/v1/douyin/creator_v2/fetch_author_diagnosis", json_body=body)
