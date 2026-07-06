"""Auto-generated routes for Douyin-Xingtu-V2-API."""

from __future__ import annotations

from typing import Any

from fastapi import APIRouter, Depends, Request

from socialmedia_hub.server._core import proxy_request, verify_api_key

router = APIRouter(prefix="/api/v1/douyin/xingtu/v2", tags=["douyin_xingtu_v2"])

@router.get("/get_ranking_list_catalog")
async def get_ranking_list_catalog(
    request: Request,
    codes: str | None = None,
    biz_scene: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取星图热榜分类/Get Ranking List Catalog"""
    body = await request.json()
    params: dict[str, Any] = {}
    if codes is not None:
        params["codes"] = codes
    if biz_scene is not None:
        params["biz_scene"] = biz_scene
    return await proxy_request("douyin", "/api/v1/douyin/xingtu_v2/get_ranking_list_catalog", params=params, json_body=body)

@router.get("/get_ranking_list_data")
async def get_ranking_list_data(
    request: Request,
    code: int | None = None,
    qualifier: str | None = None,
    version: str | None = None,
    period: int | None = None,
    date: str | None = None,
    limit: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取星图达人商业榜数据/Get Ranking List Data"""
    body = await request.json()
    params: dict[str, Any] = {}
    if code is not None:
        params["code"] = code
    if qualifier is not None:
        params["qualifier"] = qualifier
    if version is not None:
        params["version"] = version
    if period is not None:
        params["period"] = period
    if date is not None:
        params["date"] = date
    if limit is not None:
        params["limit"] = limit
    return await proxy_request("douyin", "/api/v1/douyin/xingtu_v2/get_ranking_list_data", params=params, json_body=body)

@router.post("/get_playlet_actor_rank_catalog")
async def get_playlet_actor_rank_catalog(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取短剧演员热榜分类/Get Playlet Actor Rank Catalog"""
    body = await request.json()
    return await proxy_request("douyin", "/api/v1/douyin/xingtu_v2/get_playlet_actor_rank_catalog", json_body=body)

@router.get("/get_playlet_actor_rank_list")
async def get_playlet_actor_rank_list(
    request: Request,
    category: str | None = None,
    name: str | None = None,
    qualifier: str | None = None,
    period: int | None = None,
    date: str | None = None,
    limit: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取短剧演员热榜/Get Playlet Actor Rank List"""
    body = await request.json()
    params: dict[str, Any] = {}
    if category is not None:
        params["category"] = category
    if name is not None:
        params["name"] = name
    if qualifier is not None:
        params["qualifier"] = qualifier
    if period is not None:
        params["period"] = period
    if date is not None:
        params["date"] = date
    if limit is not None:
        params["limit"] = limit
    return await proxy_request("douyin", "/api/v1/douyin/xingtu_v2/get_playlet_actor_rank_list", params=params, json_body=body)

@router.get("/get_author_market_fields")
async def get_author_market_fields(
    request: Request,
    market_scene: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取达人广场筛选字段/Get Author Market Fields"""
    body = await request.json()
    params: dict[str, Any] = {}
    if market_scene is not None:
        params["market_scene"] = market_scene
    return await proxy_request("douyin", "/api/v1/douyin/xingtu_v2/get_author_market_fields", params=params, json_body=body)

@router.get("/get_author_base_info")
async def get_author_base_info(
    o_author_id: str,
    request: Request,
    platform_source: int | None = None,
    platform_channel: int | None = None,
    recommend: bool | None = None,
    need_sec_uid: bool | None = None,
    need_linkage_info: bool | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取创作者基本信息/Get Author Base Info"""
    body = await request.json()
    params: dict[str, Any] = {}
    if o_author_id is not None:
        params["o_author_id"] = o_author_id
    if platform_source is not None:
        params["platform_source"] = platform_source
    if platform_channel is not None:
        params["platform_channel"] = platform_channel
    if recommend is not None:
        params["recommend"] = recommend
    if need_sec_uid is not None:
        params["need_sec_uid"] = need_sec_uid
    if need_linkage_info is not None:
        params["need_linkage_info"] = need_linkage_info
    return await proxy_request("douyin", "/api/v1/douyin/xingtu_v2/get_author_base_info", params=params, json_body=body)

@router.get("/get_author_business_card_info")
async def get_author_business_card_info(
    o_author_id: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取创作者商业卡片信息/Get Author Business Card Info"""
    body = await request.json()
    params: dict[str, Any] = {}
    if o_author_id is not None:
        params["o_author_id"] = o_author_id
    return await proxy_request("douyin", "/api/v1/douyin/xingtu_v2/get_author_business_card_info", params=params, json_body=body)

@router.get("/get_author_local_info")
async def get_author_local_info(
    o_author_id: str,
    request: Request,
    platform_source: int | None = None,
    platform_channel: int | None = None,
    time_range: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取创作者位置信息/Get Author Local Info"""
    body = await request.json()
    params: dict[str, Any] = {}
    if o_author_id is not None:
        params["o_author_id"] = o_author_id
    if platform_source is not None:
        params["platform_source"] = platform_source
    if platform_channel is not None:
        params["platform_channel"] = platform_channel
    if time_range is not None:
        params["time_range"] = time_range
    return await proxy_request("douyin", "/api/v1/douyin/xingtu_v2/get_author_local_info", params=params, json_body=body)

@router.get("/get_author_show_items")
async def get_author_show_items(
    o_author_id: str,
    request: Request,
    platform_source: int | None = None,
    platform_channel: int | None = None,
    limit: int | None = None,
    only_assign: bool | None = None,
    flow_type: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取创作者视频列表/Get Author Show Items"""
    body = await request.json()
    params: dict[str, Any] = {}
    if o_author_id is not None:
        params["o_author_id"] = o_author_id
    if platform_source is not None:
        params["platform_source"] = platform_source
    if platform_channel is not None:
        params["platform_channel"] = platform_channel
    if limit is not None:
        params["limit"] = limit
    if only_assign is not None:
        params["only_assign"] = only_assign
    if flow_type is not None:
        params["flow_type"] = flow_type
    return await proxy_request("douyin", "/api/v1/douyin/xingtu_v2/get_author_show_items", params=params, json_body=body)

@router.get("/get_author_hot_comment_tokens")
async def get_author_hot_comment_tokens(
    author_id: str,
    request: Request,
    num: int | None = None,
    without_emoji: bool | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取创作者评论热词/Get Author Hot Comment Tokens"""
    body = await request.json()
    params: dict[str, Any] = {}
    if author_id is not None:
        params["author_id"] = author_id
    if num is not None:
        params["num"] = num
    if without_emoji is not None:
        params["without_emoji"] = without_emoji
    return await proxy_request("douyin", "/api/v1/douyin/xingtu_v2/get_author_hot_comment_tokens", params=params, json_body=body)

@router.get("/get_author_content_hot_keywords")
async def get_author_content_hot_keywords(
    author_id: str,
    request: Request,
    keyword_type: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取创作者内容热词/Get Author Content Hot Keywords"""
    body = await request.json()
    params: dict[str, Any] = {}
    if author_id is not None:
        params["author_id"] = author_id
    if keyword_type is not None:
        params["keyword_type"] = keyword_type
    return await proxy_request("douyin", "/api/v1/douyin/xingtu_v2/get_author_content_hot_keywords", params=params, json_body=body)

@router.post("/get_recommend_for_star_authors")
async def get_recommend_for_star_authors(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取相似创作者推荐/Get Recommend Similar Star Authors"""
    body = await request.json()
    return await proxy_request("douyin", "/api/v1/douyin/xingtu_v2/get_recommend_for_star_authors", json_body=body)

@router.get("/get_excellent_case_category_list")
async def get_excellent_case_category_list(
    request: Request,
    platform_source: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取优秀行业分类列表/Get Excellent Case Category List"""
    body = await request.json()
    params: dict[str, Any] = {}
    if platform_source is not None:
        params["platform_source"] = platform_source
    return await proxy_request("douyin", "/api/v1/douyin/xingtu_v2/get_excellent_case_category_list", params=params, json_body=body)

@router.get("/get_author_spread_info")
async def get_author_spread_info(
    o_author_id: str,
    request: Request,
    platform_source: int | None = None,
    platform_channel: int | None = None,
    type: int | None = None,
    flow_type: int | None = None,
    only_assign: bool | None = None,
    range: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取创作者传播价值/Get Author Spread Info"""
    body = await request.json()
    params: dict[str, Any] = {}
    if o_author_id is not None:
        params["o_author_id"] = o_author_id
    if platform_source is not None:
        params["platform_source"] = platform_source
    if platform_channel is not None:
        params["platform_channel"] = platform_channel
    if type is not None:
        params["type"] = type
    if flow_type is not None:
        params["flow_type"] = flow_type
    if only_assign is not None:
        params["only_assign"] = only_assign
    if range is not None:
        params["range"] = range
    return await proxy_request("douyin", "/api/v1/douyin/xingtu_v2/get_author_spread_info", params=params, json_body=body)

@router.get("/get_user_profile_qrcode")
async def get_user_profile_qrcode(
    request: Request,
    core_user_id: str | None = None,
    sec_uid: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户主页二维码/Get User Profile QRCode"""
    body = await request.json()
    params: dict[str, Any] = {}
    if core_user_id is not None:
        params["core_user_id"] = core_user_id
    if sec_uid is not None:
        params["sec_uid"] = sec_uid
    return await proxy_request("douyin", "/api/v1/douyin/xingtu_v2/get_user_profile_qrcode", params=params, json_body=body)

@router.get("/get_content_trend_guide")
async def get_content_trend_guide(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取内容趋势指南/Get Content Trend Guide"""
    body = await request.json()
    return await proxy_request("douyin", "/api/v1/douyin/xingtu_v2/get_content_trend_guide", json_body=body)

@router.get("/get_ip_activity_industry_list")
async def get_ip_activity_industry_list(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取星图IP日历行业列表/Get IP Activity Industry List"""
    body = await request.json()
    return await proxy_request("douyin", "/api/v1/douyin/xingtu_v2/get_ip_activity_industry_list", json_body=body)

@router.post("/get_ip_activity_list")
async def get_ip_activity_list(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取星图IP日历活动列表/Get IP Activity List"""
    body = await request.json()
    return await proxy_request("douyin", "/api/v1/douyin/xingtu_v2/get_ip_activity_list", json_body=body)

@router.get("/get_ip_activity_detail")
async def get_ip_activity_detail(
    id: int,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取星图IP活动详情/Get IP Activity Detail"""
    body = await request.json()
    params: dict[str, Any] = {}
    if id is not None:
        params["id"] = id
    return await proxy_request("douyin", "/api/v1/douyin/xingtu_v2/get_ip_activity_detail", params=params, json_body=body)

@router.get("/get_resource_list")
async def get_resource_list(
    resource_id: int,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取营销活动案例/Get Resource List"""
    body = await request.json()
    params: dict[str, Any] = {}
    if resource_id is not None:
        params["resource_id"] = resource_id
    return await proxy_request("douyin", "/api/v1/douyin/xingtu_v2/get_resource_list", params=params, json_body=body)

@router.get("/get_demander_mcn_list")
async def get_demander_mcn_list(
    request: Request,
    mcn_name: str | None = None,
    page: int | None = None,
    limit: int | None = None,
    order_by: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """搜索MCN机构列表/Get Demander MCN List"""
    body = await request.json()
    params: dict[str, Any] = {}
    if mcn_name is not None:
        params["mcn_name"] = mcn_name
    if page is not None:
        params["page"] = page
    if limit is not None:
        params["limit"] = limit
    if order_by is not None:
        params["order_by"] = order_by
    return await proxy_request("douyin", "/api/v1/douyin/xingtu_v2/get_demander_mcn_list", params=params, json_body=body)
