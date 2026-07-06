"""Auto-generated routes for TikTok-Ads-API."""

from __future__ import annotations

from typing import Any

from fastapi import APIRouter, Depends, Request

from socialmedia_hub.server._core import proxy_request, verify_api_key

router = APIRouter(prefix="/api/v1/tiktok/ads", tags=["tiktok_ads"])

@router.get("/get_ads_detail")
async def get_ads_detail(
    ads_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取单个广告详情/Get single ad detail"""
        params: dict[str, Any] = {}
        if ads_id is not None:
            params["ads_id"] = ads_id
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/ads/get_ads_detail", json_body=body)

@router.get("/search_ads")
async def search_ads(
    search_id: str | None = None,
    ad_language: str | None = None,
    ad_format: int | None = None,
    country_code: str | None = None,
    order_by: str | None = None,
    limit: int | None = None,
    page: int | None = None,
    keyword: str | None = None,
    industry: str | None = None,
    period: int | None = None,
    like: int | None = None,
    objective: int | None = None,
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
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/ads/search_ads", json_body=body)

@router.get("/get_keyword_insights")
async def get_keyword_insights(
    keyword: str | None = None,
    keyword_type: str | None = None,
    objective: str | None = None,
    industry: str | None = None,
    order_type: str | None = None,
    order_by: str | None = None,
    country_code: str | None = None,
    period: int | None = None,
    limit: int | None = None,
    page: int | None = None,
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
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/ads/get_keyword_insights", json_body=body)

@router.get("/get_top_products")
async def get_top_products(
    order_type: str | None = None,
    order_by: str | None = None,
    period_type: str | None = None,
    ecom_type: str | None = None,
    first_ecom_category_id: str | None = None,
    country_code: str | None = None,
    limit: int | None = None,
    page: int | None = None,
    last: int | None = None,
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
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/ads/get_top_products", json_body=body)

@router.get("/get_hashtag_list")
async def get_hashtag_list(
    filter_by: str | None = None,
    industry_id: str | None = None,
    sort_by: str | None = None,
    country_code: str | None = None,
    period: int | None = None,
    limit: int | None = None,
    page: int | None = None,
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
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/ads/get_hashtag_list", json_body=body)

@router.get("/get_sound_rank_list")
async def get_sound_rank_list(
    country_code: str | None = None,
    commercial_music: bool | None = None,
    new_on_board: bool | None = None,
    rank_type: str | None = None,
    limit: int | None = None,
    page: int | None = None,
    period: int | None = None,
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
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/ads/get_sound_rank_list", json_body=body)

@router.get("/get_keyword_list")
async def get_keyword_list(
    industry: str | None = None,
    country_code: str | None = None,
    limit: int | None = None,
    page: int | None = None,
    period: int | None = None,
    keyword: str | None = None,
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
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/ads/get_keyword_list", json_body=body)

@router.get("/get_top_ads_spotlight")
async def get_top_ads_spotlight(
    limit: int | None = None,
    page: int | None = None,
    industry: str | None = None,
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
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/ads/get_top_ads_spotlight", json_body=body)

@router.get("/get_ad_keyframe_analysis")
async def get_ad_keyframe_analysis(
    metric: str | None = None,
    material_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取广告关键帧分析/Get ad keyframe analysis"""
        params: dict[str, Any] = {}
        if material_id is not None:
            params["material_id"] = material_id
        if metric is not None:
            params["metric"] = metric
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/ads/get_ad_keyframe_analysis", json_body=body)

@router.get("/get_ad_percentile")
async def get_ad_percentile(
    period_type: int | None = None,
    metric: str | None = None,
    material_id: str,
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
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/ads/get_ad_percentile", json_body=body)

@router.get("/get_ad_interactive_analysis")
async def get_ad_interactive_analysis(
    period_type: int | None = None,
    metric_type: str | None = None,
    material_id: str,
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
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/ads/get_ad_interactive_analysis", json_body=body)

@router.get("/get_recommended_ads")
async def get_recommended_ads(
    country_code: str | None = None,
    industry: str | None = None,
    material_id: str,
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
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/ads/get_recommended_ads", json_body=body)

@router.get("/get_query_suggestions")
async def get_query_suggestions(
    scenario: int | None = None,
    count: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取查询建议/Get query suggestions"""
        params: dict[str, Any] = {}
        if count is not None:
            params["count"] = count
        if scenario is not None:
            params["scenario"] = scenario
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/ads/get_query_suggestions", json_body=body)

@router.get("/get_keyword_filters")
async def get_keyword_filters(
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取关键词筛选器/Get keyword filters"""
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/ads/get_keyword_filters", json_body=body)

@router.get("/get_related_keywords")
async def get_related_keywords(
    limit: int | None = None,
    page: int | None = None,
    content_type: str | None = None,
    rank_type: str | None = None,
    country_code: str | None = None,
    period: int | None = None,
    keyword: str | None = None,
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
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/ads/get_related_keywords", json_body=body)

@router.get("/get_keyword_details")
async def get_keyword_details(
    keyword_type: str | None = None,
    objective: str | None = None,
    industry: str | None = None,
    order_type: str | None = None,
    order_by: str | None = None,
    country_code: str | None = None,
    period: int | None = None,
    limit: int | None = None,
    page: int | None = None,
    keyword: str | None = None,
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
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/ads/get_keyword_details", json_body=body)

@router.get("/get_creative_patterns")
async def get_creative_patterns(
    limit: int | None = None,
    page: int | None = None,
    week: str | None = None,
    order_type: str | None = None,
    order_field: str | None = None,
    period_type: str | None = None,
    first_industry_id: str | None = None,
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
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/ads/get_creative_patterns", json_body=body)

@router.get("/get_product_filters")
async def get_product_filters(
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取产品筛选器/Get product filters"""
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/ads/get_product_filters", json_body=body)

@router.get("/get_product_metrics")
async def get_product_metrics(
    country_code: str | None = None,
    period_type: str | None = None,
    ecom_type: str | None = None,
    metrics: str | None = None,
    last: int | None = None,
    id: str,
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
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/ads/get_product_metrics", json_body=body)

@router.get("/get_product_detail")
async def get_product_detail(
    country_code: str | None = None,
    period_type: str | None = None,
    ecom_type: str | None = None,
    last: int | None = None,
    id: str,
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
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/ads/get_product_detail", json_body=body)

@router.get("/get_hashtag_filters")
async def get_hashtag_filters(
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取标签筛选器/Get hashtag filters"""
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/ads/get_hashtag_filters", json_body=body)

@router.get("/get_hashtag_creator")
async def get_hashtag_creator(
    hashtag: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取标签创作者信息/Get hashtag creator info"""
        params: dict[str, Any] = {}
        if hashtag is not None:
            params["hashtag"] = hashtag
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/ads/get_hashtag_creator", json_body=body)

@router.get("/get_sound_filters")
async def get_sound_filters(
    rank_type: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取音乐筛选器/Get sound filters"""
        params: dict[str, Any] = {}
        if rank_type is not None:
            params["rank_type"] = rank_type
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/ads/get_sound_filters", json_body=body)

@router.get("/get_sound_detail")
async def get_sound_detail(
    country_code: str | None = None,
    period: int | None = None,
    clip_id: str,
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
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/ads/get_sound_detail", json_body=body)

@router.get("/search_sound_hint")
async def search_sound_hint(
    commercial_music: bool | None = None,
    filter_by_checked: bool | None = None,
    country_code: str | None = None,
    rank_type: str | None = None,
    limit: int | None = None,
    page: int | None = None,
    period: int | None = None,
    keyword: str,
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
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/ads/search_sound_hint", json_body=body)

@router.get("/search_sound")
async def search_sound(
    country_code: str | None = None,
    commercial_music: bool | None = None,
    new_on_board: bool | None = None,
    rank_type: str | None = None,
    limit: int | None = None,
    page: int | None = None,
    period: int | None = None,
    keyword: str,
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
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/ads/search_sound", json_body=body)

@router.get("/get_sound_recommendations")
async def get_sound_recommendations(
    limit: int | None = None,
    clip_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取音乐推荐/Get sound recommendations"""
        params: dict[str, Any] = {}
        if clip_id is not None:
            params["clip_id"] = clip_id
        if limit is not None:
            params["limit"] = limit
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/ads/get_sound_recommendations", json_body=body)

@router.get("/get_creator_filters")
async def get_creator_filters(
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取创作者筛选器/Get creator filters"""
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/ads/get_creator_filters", json_body=body)

@router.get("/get_creator_list")
async def get_creator_list(
    keyword: str | None = None,
    audience_count: int | None = None,
    audience_country: str | None = None,
    creator_country: str | None = None,
    sort_by: str | None = None,
    limit: int | None = None,
    page: int | None = None,
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
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/ads/get_creator_list", json_body=body)

@router.get("/search_creators")
async def search_creators(
    creator_country: str | None = None,
    sort_by: str | None = None,
    limit: int | None = None,
    page: int | None = None,
    keyword: str,
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
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/ads/search_creators", json_body=body)

@router.get("/get_popular_trends")
async def get_popular_trends(
    country_code: str | None = None,
    order_by: str | None = None,
    limit: int | None = None,
    page: int | None = None,
    period: int | None = None,
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
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/ads/get_popular_trends", json_body=body)
