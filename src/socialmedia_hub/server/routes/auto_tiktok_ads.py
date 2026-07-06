"""Auto-generated routes for TikTok-Ads-API."""

from __future__ import annotations

from typing import Any

from fastapi import APIRouter, Depends, Request

from socialmedia_hub.server._core import proxy_request, verify_api_key

router = APIRouter(prefix="/api/v1/tiktok/ads", tags=["tiktok_ads"])

@router.get("/get_ads_detail")
async def get_ads_detail(
    ads_id: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取单个广告详情/Get single ad detail"""
    params: dict[str, Any] = {}
    if ads_id is not None:
        params["ads_id"] = ads_id
    return await proxy_request("tiktok", "/api/v1/tiktok/ads/get_ads_detail", params=params)

@router.get("/search_ads")
async def search_ads(
    request: Request,
    objective: int | None = None,
    like: int | None = None,
    period: int | None = None,
    industry: str | None = None,
    keyword: str | None = None,
    page: int | None = None,
    limit: int | None = None,
    order_by: str | None = None,
    country_code: str | None = None,
    ad_format: int | None = None,
    ad_language: str | None = None,
    search_id: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """搜索广告/Search ads"""
    params: dict[str, Any] = {}
    if objective is not None:
        params["objective"] = objective
    if like is not None:
        params["like"] = like
    if period is not None:
        params["period"] = period
    if industry is not None:
        params["industry"] = industry
    if keyword is not None:
        params["keyword"] = keyword
    if page is not None:
        params["page"] = page
    if limit is not None:
        params["limit"] = limit
    if order_by is not None:
        params["order_by"] = order_by
    if country_code is not None:
        params["country_code"] = country_code
    if ad_format is not None:
        params["ad_format"] = ad_format
    if ad_language is not None:
        params["ad_language"] = ad_language
    if search_id is not None:
        params["search_id"] = search_id
    return await proxy_request("tiktok", "/api/v1/tiktok/ads/search_ads", params=params)

@router.get("/get_keyword_insights")
async def get_keyword_insights(
    request: Request,
    page: int | None = None,
    limit: int | None = None,
    period: int | None = None,
    country_code: str | None = None,
    order_by: str | None = None,
    order_type: str | None = None,
    industry: str | None = None,
    objective: str | None = None,
    keyword_type: str | None = None,
    keyword: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取关键词洞察数据/Get keyword insights data"""
    params: dict[str, Any] = {}
    if page is not None:
        params["page"] = page
    if limit is not None:
        params["limit"] = limit
    if period is not None:
        params["period"] = period
    if country_code is not None:
        params["country_code"] = country_code
    if order_by is not None:
        params["order_by"] = order_by
    if order_type is not None:
        params["order_type"] = order_type
    if industry is not None:
        params["industry"] = industry
    if objective is not None:
        params["objective"] = objective
    if keyword_type is not None:
        params["keyword_type"] = keyword_type
    if keyword is not None:
        params["keyword"] = keyword
    return await proxy_request("tiktok", "/api/v1/tiktok/ads/get_keyword_insights", params=params)

@router.get("/get_top_products")
async def get_top_products(
    request: Request,
    last: int | None = None,
    page: int | None = None,
    limit: int | None = None,
    country_code: str | None = None,
    first_ecom_category_id: str | None = None,
    ecom_type: str | None = None,
    period_type: str | None = None,
    order_by: str | None = None,
    order_type: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取热门产品列表/Get top products list"""
    params: dict[str, Any] = {}
    if last is not None:
        params["last"] = last
    if page is not None:
        params["page"] = page
    if limit is not None:
        params["limit"] = limit
    if country_code is not None:
        params["country_code"] = country_code
    if first_ecom_category_id is not None:
        params["first_ecom_category_id"] = first_ecom_category_id
    if ecom_type is not None:
        params["ecom_type"] = ecom_type
    if period_type is not None:
        params["period_type"] = period_type
    if order_by is not None:
        params["order_by"] = order_by
    if order_type is not None:
        params["order_type"] = order_type
    return await proxy_request("tiktok", "/api/v1/tiktok/ads/get_top_products", params=params)

@router.get("/get_hashtag_list")
async def get_hashtag_list(
    request: Request,
    page: int | None = None,
    limit: int | None = None,
    period: int | None = None,
    country_code: str | None = None,
    sort_by: str | None = None,
    industry_id: str | None = None,
    filter_by: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取热门标签列表/Get popular hashtags list"""
    params: dict[str, Any] = {}
    if page is not None:
        params["page"] = page
    if limit is not None:
        params["limit"] = limit
    if period is not None:
        params["period"] = period
    if country_code is not None:
        params["country_code"] = country_code
    if sort_by is not None:
        params["sort_by"] = sort_by
    if industry_id is not None:
        params["industry_id"] = industry_id
    if filter_by is not None:
        params["filter_by"] = filter_by
    return await proxy_request("tiktok", "/api/v1/tiktok/ads/get_hashtag_list", params=params)

@router.get("/get_sound_rank_list")
async def get_sound_rank_list(
    request: Request,
    period: int | None = None,
    page: int | None = None,
    limit: int | None = None,
    rank_type: str | None = None,
    new_on_board: bool | None = None,
    commercial_music: bool | None = None,
    country_code: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取热门音乐排行榜/Get popular sound rankings"""
    params: dict[str, Any] = {}
    if period is not None:
        params["period"] = period
    if page is not None:
        params["page"] = page
    if limit is not None:
        params["limit"] = limit
    if rank_type is not None:
        params["rank_type"] = rank_type
    if new_on_board is not None:
        params["new_on_board"] = new_on_board
    if commercial_music is not None:
        params["commercial_music"] = commercial_music
    if country_code is not None:
        params["country_code"] = country_code
    return await proxy_request("tiktok", "/api/v1/tiktok/ads/get_sound_rank_list", params=params)

@router.get("/get_keyword_list")
async def get_keyword_list(
    request: Request,
    keyword: str | None = None,
    period: int | None = None,
    page: int | None = None,
    limit: int | None = None,
    country_code: str | None = None,
    industry: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取关键词列表/Get keyword list"""
    params: dict[str, Any] = {}
    if keyword is not None:
        params["keyword"] = keyword
    if period is not None:
        params["period"] = period
    if page is not None:
        params["page"] = page
    if limit is not None:
        params["limit"] = limit
    if country_code is not None:
        params["country_code"] = country_code
    if industry is not None:
        params["industry"] = industry
    return await proxy_request("tiktok", "/api/v1/tiktok/ads/get_keyword_list", params=params)

@router.get("/get_top_ads_spotlight")
async def get_top_ads_spotlight(
    request: Request,
    industry: str | None = None,
    page: int | None = None,
    limit: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取热门广告聚光灯/Get top ads spotlight"""
    params: dict[str, Any] = {}
    if industry is not None:
        params["industry"] = industry
    if page is not None:
        params["page"] = page
    if limit is not None:
        params["limit"] = limit
    return await proxy_request("tiktok", "/api/v1/tiktok/ads/get_top_ads_spotlight", params=params)

@router.get("/get_ad_keyframe_analysis")
async def get_ad_keyframe_analysis(
    material_id: str,
    request: Request,
    metric: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取广告关键帧分析/Get ad keyframe analysis"""
    params: dict[str, Any] = {}
    if material_id is not None:
        params["material_id"] = material_id
    if metric is not None:
        params["metric"] = metric
    return await proxy_request("tiktok", "/api/v1/tiktok/ads/get_ad_keyframe_analysis", params=params)

@router.get("/get_ad_percentile")
async def get_ad_percentile(
    material_id: str,
    request: Request,
    metric: str | None = None,
    period_type: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取广告百分位数据/Get ad percentile data"""
    params: dict[str, Any] = {}
    if material_id is not None:
        params["material_id"] = material_id
    if metric is not None:
        params["metric"] = metric
    if period_type is not None:
        params["period_type"] = period_type
    return await proxy_request("tiktok", "/api/v1/tiktok/ads/get_ad_percentile", params=params)

@router.get("/get_ad_interactive_analysis")
async def get_ad_interactive_analysis(
    material_id: str,
    request: Request,
    metric_type: str | None = None,
    period_type: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取广告互动分析/Get ad interactive analysis"""
    params: dict[str, Any] = {}
    if material_id is not None:
        params["material_id"] = material_id
    if metric_type is not None:
        params["metric_type"] = metric_type
    if period_type is not None:
        params["period_type"] = period_type
    return await proxy_request("tiktok", "/api/v1/tiktok/ads/get_ad_interactive_analysis", params=params)

@router.get("/get_recommended_ads")
async def get_recommended_ads(
    material_id: str,
    request: Request,
    industry: str | None = None,
    country_code: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取推荐广告/Get recommended ads"""
    params: dict[str, Any] = {}
    if material_id is not None:
        params["material_id"] = material_id
    if industry is not None:
        params["industry"] = industry
    if country_code is not None:
        params["country_code"] = country_code
    return await proxy_request("tiktok", "/api/v1/tiktok/ads/get_recommended_ads", params=params)

@router.get("/get_query_suggestions")
async def get_query_suggestions(
    request: Request,
    count: int | None = None,
    scenario: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取查询建议/Get query suggestions"""
    params: dict[str, Any] = {}
    if count is not None:
        params["count"] = count
    if scenario is not None:
        params["scenario"] = scenario
    return await proxy_request("tiktok", "/api/v1/tiktok/ads/get_query_suggestions", params=params)

@router.get("/get_keyword_filters")
async def get_keyword_filters(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取关键词筛选器/Get keyword filters"""
    return await proxy_request("tiktok", "/api/v1/tiktok/ads/get_keyword_filters")

@router.get("/get_related_keywords")
async def get_related_keywords(
    request: Request,
    keyword: str | None = None,
    period: int | None = None,
    country_code: str | None = None,
    rank_type: str | None = None,
    content_type: str | None = None,
    page: int | None = None,
    limit: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取相关关键词/Get related keywords"""
    params: dict[str, Any] = {}
    if keyword is not None:
        params["keyword"] = keyword
    if period is not None:
        params["period"] = period
    if country_code is not None:
        params["country_code"] = country_code
    if rank_type is not None:
        params["rank_type"] = rank_type
    if content_type is not None:
        params["content_type"] = content_type
    if page is not None:
        params["page"] = page
    if limit is not None:
        params["limit"] = limit
    return await proxy_request("tiktok", "/api/v1/tiktok/ads/get_related_keywords", params=params)

@router.get("/get_keyword_details")
async def get_keyword_details(
    request: Request,
    keyword: str | None = None,
    page: int | None = None,
    limit: int | None = None,
    period: int | None = None,
    country_code: str | None = None,
    order_by: str | None = None,
    order_type: str | None = None,
    industry: str | None = None,
    objective: str | None = None,
    keyword_type: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取关键词详细信息/Get keyword details"""
    params: dict[str, Any] = {}
    if keyword is not None:
        params["keyword"] = keyword
    if page is not None:
        params["page"] = page
    if limit is not None:
        params["limit"] = limit
    if period is not None:
        params["period"] = period
    if country_code is not None:
        params["country_code"] = country_code
    if order_by is not None:
        params["order_by"] = order_by
    if order_type is not None:
        params["order_type"] = order_type
    if industry is not None:
        params["industry"] = industry
    if objective is not None:
        params["objective"] = objective
    if keyword_type is not None:
        params["keyword_type"] = keyword_type
    return await proxy_request("tiktok", "/api/v1/tiktok/ads/get_keyword_details", params=params)

@router.get("/get_creative_patterns")
async def get_creative_patterns(
    request: Request,
    first_industry_id: str | None = None,
    period_type: str | None = None,
    order_field: str | None = None,
    order_type: str | None = None,
    week: str | None = None,
    page: int | None = None,
    limit: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取创意模式排行榜/Get creative pattern rankings"""
    params: dict[str, Any] = {}
    if first_industry_id is not None:
        params["first_industry_id"] = first_industry_id
    if period_type is not None:
        params["period_type"] = period_type
    if order_field is not None:
        params["order_field"] = order_field
    if order_type is not None:
        params["order_type"] = order_type
    if week is not None:
        params["week"] = week
    if page is not None:
        params["page"] = page
    if limit is not None:
        params["limit"] = limit
    return await proxy_request("tiktok", "/api/v1/tiktok/ads/get_creative_patterns", params=params)

@router.get("/get_product_filters")
async def get_product_filters(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取产品筛选器/Get product filters"""
    return await proxy_request("tiktok", "/api/v1/tiktok/ads/get_product_filters")

@router.get("/get_product_metrics")
async def get_product_metrics(
    id: str,
    request: Request,
    last: int | None = None,
    metrics: str | None = None,
    ecom_type: str | None = None,
    period_type: str | None = None,
    country_code: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取产品指标数据/Get product metrics"""
    params: dict[str, Any] = {}
    if id is not None:
        params["id"] = id
    if last is not None:
        params["last"] = last
    if metrics is not None:
        params["metrics"] = metrics
    if ecom_type is not None:
        params["ecom_type"] = ecom_type
    if period_type is not None:
        params["period_type"] = period_type
    if country_code is not None:
        params["country_code"] = country_code
    return await proxy_request("tiktok", "/api/v1/tiktok/ads/get_product_metrics", params=params)

@router.get("/get_product_detail")
async def get_product_detail(
    id: str,
    request: Request,
    last: int | None = None,
    ecom_type: str | None = None,
    period_type: str | None = None,
    country_code: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取产品详细信息/Get product detail"""
    params: dict[str, Any] = {}
    if id is not None:
        params["id"] = id
    if last is not None:
        params["last"] = last
    if ecom_type is not None:
        params["ecom_type"] = ecom_type
    if period_type is not None:
        params["period_type"] = period_type
    if country_code is not None:
        params["country_code"] = country_code
    return await proxy_request("tiktok", "/api/v1/tiktok/ads/get_product_detail", params=params)

@router.get("/get_hashtag_filters")
async def get_hashtag_filters(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取标签筛选器/Get hashtag filters"""
    return await proxy_request("tiktok", "/api/v1/tiktok/ads/get_hashtag_filters")

@router.get("/get_hashtag_creator")
async def get_hashtag_creator(
    hashtag: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取标签创作者信息/Get hashtag creator info"""
    params: dict[str, Any] = {}
    if hashtag is not None:
        params["hashtag"] = hashtag
    return await proxy_request("tiktok", "/api/v1/tiktok/ads/get_hashtag_creator", params=params)

@router.get("/get_sound_filters")
async def get_sound_filters(
    request: Request,
    rank_type: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取音乐筛选器/Get sound filters"""
    params: dict[str, Any] = {}
    if rank_type is not None:
        params["rank_type"] = rank_type
    return await proxy_request("tiktok", "/api/v1/tiktok/ads/get_sound_filters", params=params)

@router.get("/get_sound_detail")
async def get_sound_detail(
    clip_id: str,
    request: Request,
    period: int | None = None,
    country_code: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取音乐详情/Get sound detail"""
    params: dict[str, Any] = {}
    if clip_id is not None:
        params["clip_id"] = clip_id
    if period is not None:
        params["period"] = period
    if country_code is not None:
        params["country_code"] = country_code
    return await proxy_request("tiktok", "/api/v1/tiktok/ads/get_sound_detail", params=params)

@router.get("/search_sound_hint")
async def search_sound_hint(
    keyword: str,
    request: Request,
    period: int | None = None,
    page: int | None = None,
    limit: int | None = None,
    rank_type: str | None = None,
    country_code: str | None = None,
    filter_by_checked: bool | None = None,
    commercial_music: bool | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """搜索音乐提示/Search sound hints"""
    params: dict[str, Any] = {}
    if keyword is not None:
        params["keyword"] = keyword
    if period is not None:
        params["period"] = period
    if page is not None:
        params["page"] = page
    if limit is not None:
        params["limit"] = limit
    if rank_type is not None:
        params["rank_type"] = rank_type
    if country_code is not None:
        params["country_code"] = country_code
    if filter_by_checked is not None:
        params["filter_by_checked"] = filter_by_checked
    if commercial_music is not None:
        params["commercial_music"] = commercial_music
    return await proxy_request("tiktok", "/api/v1/tiktok/ads/search_sound_hint", params=params)

@router.get("/search_sound")
async def search_sound(
    keyword: str,
    request: Request,
    period: int | None = None,
    page: int | None = None,
    limit: int | None = None,
    rank_type: str | None = None,
    new_on_board: bool | None = None,
    commercial_music: bool | None = None,
    country_code: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """搜索音乐/Search sounds"""
    params: dict[str, Any] = {}
    if keyword is not None:
        params["keyword"] = keyword
    if period is not None:
        params["period"] = period
    if page is not None:
        params["page"] = page
    if limit is not None:
        params["limit"] = limit
    if rank_type is not None:
        params["rank_type"] = rank_type
    if new_on_board is not None:
        params["new_on_board"] = new_on_board
    if commercial_music is not None:
        params["commercial_music"] = commercial_music
    if country_code is not None:
        params["country_code"] = country_code
    return await proxy_request("tiktok", "/api/v1/tiktok/ads/search_sound", params=params)

@router.get("/get_sound_recommendations")
async def get_sound_recommendations(
    clip_id: str,
    request: Request,
    limit: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取音乐推荐/Get sound recommendations"""
    params: dict[str, Any] = {}
    if clip_id is not None:
        params["clip_id"] = clip_id
    if limit is not None:
        params["limit"] = limit
    return await proxy_request("tiktok", "/api/v1/tiktok/ads/get_sound_recommendations", params=params)

@router.get("/get_creator_filters")
async def get_creator_filters(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取创作者筛选器/Get creator filters"""
    return await proxy_request("tiktok", "/api/v1/tiktok/ads/get_creator_filters")

@router.get("/get_creator_list")
async def get_creator_list(
    request: Request,
    page: int | None = None,
    limit: int | None = None,
    sort_by: str | None = None,
    creator_country: str | None = None,
    audience_country: str | None = None,
    audience_count: int | None = None,
    keyword: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取创作者列表/Get creator list"""
    params: dict[str, Any] = {}
    if page is not None:
        params["page"] = page
    if limit is not None:
        params["limit"] = limit
    if sort_by is not None:
        params["sort_by"] = sort_by
    if creator_country is not None:
        params["creator_country"] = creator_country
    if audience_country is not None:
        params["audience_country"] = audience_country
    if audience_count is not None:
        params["audience_count"] = audience_count
    if keyword is not None:
        params["keyword"] = keyword
    return await proxy_request("tiktok", "/api/v1/tiktok/ads/get_creator_list", params=params)

@router.get("/search_creators")
async def search_creators(
    keyword: str,
    request: Request,
    page: int | None = None,
    limit: int | None = None,
    sort_by: str | None = None,
    creator_country: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """搜索创作者/Search creators"""
    params: dict[str, Any] = {}
    if keyword is not None:
        params["keyword"] = keyword
    if page is not None:
        params["page"] = page
    if limit is not None:
        params["limit"] = limit
    if sort_by is not None:
        params["sort_by"] = sort_by
    if creator_country is not None:
        params["creator_country"] = creator_country
    return await proxy_request("tiktok", "/api/v1/tiktok/ads/search_creators", params=params)

@router.get("/get_popular_trends")
async def get_popular_trends(
    request: Request,
    period: int | None = None,
    page: int | None = None,
    limit: int | None = None,
    order_by: str | None = None,
    country_code: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取流行趋势视频/Get popular trend videos"""
    params: dict[str, Any] = {}
    if period is not None:
        params["period"] = period
    if page is not None:
        params["page"] = page
    if limit is not None:
        params["limit"] = limit
    if order_by is not None:
        params["order_by"] = order_by
    if country_code is not None:
        params["country_code"] = country_code
    return await proxy_request("tiktok", "/api/v1/tiktok/ads/get_popular_trends", params=params)
