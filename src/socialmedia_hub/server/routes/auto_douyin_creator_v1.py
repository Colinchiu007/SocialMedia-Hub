"""Auto-generated routes for Douyin-Creator-API."""

from __future__ import annotations

from typing import Any

from fastapi import APIRouter, Depends, Request

from socialmedia_hub.server._core import proxy_request, verify_api_key

router = APIRouter(prefix="/api/v1/douyin/creator/v1", tags=["douyin_creator"])

@router.get("/fetch_creator_activity_list")
async def fetch_creator_activity_list(
    start_time: int,
    end_time: int,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取创作者活动列表/Get creator activity list"""
    params: dict[str, Any] = {}
    if start_time is not None:
        params["start_time"] = start_time
    if end_time is not None:
        params["end_time"] = end_time
    return await proxy_request("douyin", "/api/v1/douyin/creator/fetch_creator_activity_list", params=params)

@router.get("/fetch_creator_activity_detail")
async def fetch_creator_activity_detail(
    activity_id: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取创作者活动详情/Get creator activity detail"""
    params: dict[str, Any] = {}
    if activity_id is not None:
        params["activity_id"] = activity_id
    return await proxy_request("douyin", "/api/v1/douyin/creator/fetch_creator_activity_detail", params=params)

@router.get("/fetch_creator_material_center_config")
async def fetch_creator_material_center_config(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取创作者中心配置/Get creator material center config"""
    return await proxy_request("douyin", "/api/v1/douyin/creator/fetch_creator_material_center_config")

@router.get("/fetch_creator_material_center_billboard")
async def fetch_creator_material_center_billboard(
    request: Request,
    billboard_tag: int | None = None,
    order_key: int | None = None,
    time_filter: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取创作者中心热门视频榜单/Get creator material center billboard"""
    params: dict[str, Any] = {}
    if billboard_tag is not None:
        params["billboard_tag"] = billboard_tag
    if order_key is not None:
        params["order_key"] = order_key
    if time_filter is not None:
        params["time_filter"] = time_filter
    return await proxy_request("douyin", "/api/v1/douyin/creator/fetch_creator_material_center_billboard", params=params)

@router.get("/fetch_creator_hot_spot_billboard")
async def fetch_creator_hot_spot_billboard(
    request: Request,
    billboard_tag: str | None = None,
    hot_search_type: int | None = None,
    city_code: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取创作者中心创作热点/Get creator hot spot billboard"""
    params: dict[str, Any] = {}
    if billboard_tag is not None:
        params["billboard_tag"] = billboard_tag
    if hot_search_type is not None:
        params["hot_search_type"] = hot_search_type
    if city_code is not None:
        params["city_code"] = city_code
    return await proxy_request("douyin", "/api/v1/douyin/creator/fetch_creator_hot_spot_billboard", params=params)

@router.get("/fetch_creator_hot_topic_billboard")
async def fetch_creator_hot_topic_billboard(
    request: Request,
    billboard_tag: int | None = None,
    order_key: int | None = None,
    time_filter: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取创作者热门话题榜单/Get creator hot topic billboard"""
    params: dict[str, Any] = {}
    if billboard_tag is not None:
        params["billboard_tag"] = billboard_tag
    if order_key is not None:
        params["order_key"] = order_key
    if time_filter is not None:
        params["time_filter"] = time_filter
    return await proxy_request("douyin", "/api/v1/douyin/creator/fetch_creator_hot_topic_billboard", params=params)

@router.get("/fetch_creator_hot_props_billboard")
async def fetch_creator_hot_props_billboard(
    request: Request,
    billboard_tag: int | None = None,
    order_key: int | None = None,
    time_filter: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取创作者热门道具榜单/Get creator hot props billboard"""
    params: dict[str, Any] = {}
    if billboard_tag is not None:
        params["billboard_tag"] = billboard_tag
    if order_key is not None:
        params["order_key"] = order_key
    if time_filter is not None:
        params["time_filter"] = time_filter
    return await proxy_request("douyin", "/api/v1/douyin/creator/fetch_creator_hot_props_billboard", params=params)

@router.get("/fetch_creator_hot_challenge_billboard")
async def fetch_creator_hot_challenge_billboard(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取创作者热门挑战榜单/Get creator hot challenge billboard"""
    return await proxy_request("douyin", "/api/v1/douyin/creator/fetch_creator_hot_challenge_billboard")

@router.get("/fetch_creator_hot_music_billboard")
async def fetch_creator_hot_music_billboard(
    request: Request,
    billboard_tag: int | None = None,
    order_key: int | None = None,
    time_filter: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取创作者热门音乐榜单/Get creator hot music billboard"""
    params: dict[str, Any] = {}
    if billboard_tag is not None:
        params["billboard_tag"] = billboard_tag
    if order_key is not None:
        params["order_key"] = order_key
    if time_filter is not None:
        params["time_filter"] = time_filter
    return await proxy_request("douyin", "/api/v1/douyin/creator/fetch_creator_hot_music_billboard", params=params)

@router.get("/fetch_creator_hot_course")
async def fetch_creator_hot_course(
    request: Request,
    order: int | None = None,
    limit: int | None = None,
    offset: int | None = None,
    category_id: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取创作者热门课程/Get creator hot course"""
    params: dict[str, Any] = {}
    if order is not None:
        params["order"] = order
    if limit is not None:
        params["limit"] = limit
    if offset is not None:
        params["offset"] = offset
    if category_id is not None:
        params["category_id"] = category_id
    return await proxy_request("douyin", "/api/v1/douyin/creator/fetch_creator_hot_course", params=params)

@router.get("/fetch_creator_content_category")
async def fetch_creator_content_category(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取创作者内容创作合集分类/Get creator content creation category"""
    return await proxy_request("douyin", "/api/v1/douyin/creator/fetch_creator_content_category")

@router.get("/fetch_creator_content_course")
async def fetch_creator_content_course(
    category_id: int,
    request: Request,
    order: int | None = None,
    limit: int | None = None,
    offset: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取创作者内容创作课程/Get creator content creation course"""
    params: dict[str, Any] = {}
    if category_id is not None:
        params["category_id"] = category_id
    if order is not None:
        params["order"] = order
    if limit is not None:
        params["limit"] = limit
    if offset is not None:
        params["offset"] = offset
    return await proxy_request("douyin", "/api/v1/douyin/creator/fetch_creator_content_course", params=params)

@router.get("/fetch_video_danmaku_list")
async def fetch_video_danmaku_list(
    item_id: str,
    request: Request,
    count: int | None = None,
    offset: int | None = None,
    order_type: int | None = None,
    is_blocked: bool | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取作品弹幕列表/Get video danmaku list"""
    params: dict[str, Any] = {}
    if item_id is not None:
        params["item_id"] = item_id
    if count is not None:
        params["count"] = count
    if offset is not None:
        params["offset"] = offset
    if order_type is not None:
        params["order_type"] = order_type
    if is_blocked is not None:
        params["is_blocked"] = is_blocked
    return await proxy_request("douyin", "/api/v1/douyin/creator/fetch_video_danmaku_list", params=params)

@router.get("/fetch_user_search")
async def fetch_user_search(
    user_name: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """搜索用户/Search users"""
    params: dict[str, Any] = {}
    if user_name is not None:
        params["user_name"] = user_name
    return await proxy_request("douyin", "/api/v1/douyin/creator/fetch_user_search", params=params)

@router.get("/fetch_mission_task_list")
async def fetch_mission_task_list(
    request: Request,
    cursor: int | None = None,
    limit: int | None = None,
    mission_type: int | None = None,
    tab_scene: int | None = None,
    industry_lv1: int | None = None,
    industry_lv2: int | None = None,
    platform_channel: str | None = None,
    pay_type: str | None = None,
    greater_than_cost_progress: str | None = None,
    publish_time_start: str | None = None,
    quick_selector_scene: str | None = None,
    keyword: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取商单任务列表/Get mission task list"""
    params: dict[str, Any] = {}
    if cursor is not None:
        params["cursor"] = cursor
    if limit is not None:
        params["limit"] = limit
    if mission_type is not None:
        params["mission_type"] = mission_type
    if tab_scene is not None:
        params["tab_scene"] = tab_scene
    if industry_lv1 is not None:
        params["industry_lv1"] = industry_lv1
    if industry_lv2 is not None:
        params["industry_lv2"] = industry_lv2
    if platform_channel is not None:
        params["platform_channel"] = platform_channel
    if pay_type is not None:
        params["pay_type"] = pay_type
    if greater_than_cost_progress is not None:
        params["greater_than_cost_progress"] = greater_than_cost_progress
    if publish_time_start is not None:
        params["publish_time_start"] = publish_time_start
    if quick_selector_scene is not None:
        params["quick_selector_scene"] = quick_selector_scene
    if keyword is not None:
        params["keyword"] = keyword
    return await proxy_request("douyin", "/api/v1/douyin/creator/fetch_mission_task_list", params=params)

@router.get("/fetch_industry_category_config")
async def fetch_industry_category_config(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取行业分类配置/Get industry category config"""
    return await proxy_request("douyin", "/api/v1/douyin/creator/fetch_industry_category_config")
