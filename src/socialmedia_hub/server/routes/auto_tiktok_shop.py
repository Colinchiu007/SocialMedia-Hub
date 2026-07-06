"""Auto-generated routes for TikTok-Shop-Web-API."""

from __future__ import annotations

from typing import Any

from fastapi import APIRouter, Depends, Request

from socialmedia_hub.server._core import proxy_request, verify_api_key

router = APIRouter(prefix="/api/v1/tiktok/shop", tags=["tiktok_shop_web"])

@router.get("/fetch_product_detail")
async def fetch_product_detail(
    product_id: str,
    request: Request,
    seller_id: str | None = None,
    region: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取商品详情V1(桌面端-数据完整)/Get product detail V1(Full data)"""
    body = await request.json()
    params: dict[str, Any] = {}
    if product_id is not None:
        params["product_id"] = product_id
    if seller_id is not None:
        params["seller_id"] = seller_id
    if region is not None:
        params["region"] = region
    return await proxy_request("tiktok", "/api/v1/tiktok/shop/web/fetch_product_detail", params=params, json_body=body)

@router.get("/fetch_product_detail_v2")
async def fetch_product_detail_v2(
    product_id: str,
    request: Request,
    seller_id: str | None = None,
    region: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取商品详情V2(移动端-数据少)/Get product detail V2 (Less Data)"""
    body = await request.json()
    params: dict[str, Any] = {}
    if product_id is not None:
        params["product_id"] = product_id
    if seller_id is not None:
        params["seller_id"] = seller_id
    if region is not None:
        params["region"] = region
    return await proxy_request("tiktok", "/api/v1/tiktok/shop/web/fetch_product_detail_v2", params=params, json_body=body)

@router.get("/fetch_product_detail_v3")
async def fetch_product_detail_v3(
    product_id: str,
    request: Request,
    region: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取商品详情V3(移动端-数据完整)/Get product detail V3 (Full Data)"""
    body = await request.json()
    params: dict[str, Any] = {}
    if product_id is not None:
        params["product_id"] = product_id
    if region is not None:
        params["region"] = region
    return await proxy_request("tiktok", "/api/v1/tiktok/shop/web/fetch_product_detail_v3", params=params, json_body=body)

@router.get("/fetch_product_reviews_v1")
async def fetch_product_reviews_v1(
    product_id: str,
    request: Request,
    sort_type: int | None = None,
    filter_id: str | None = None,
    offset: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取商品评论V1/Get product reviews V1"""
    body = await request.json()
    params: dict[str, Any] = {}
    if product_id is not None:
        params["product_id"] = product_id
    if sort_type is not None:
        params["sort_type"] = sort_type
    if filter_id is not None:
        params["filter_id"] = filter_id
    if offset is not None:
        params["offset"] = offset
    return await proxy_request("tiktok", "/api/v1/tiktok/shop/web/fetch_product_reviews_v1", params=params, json_body=body)

@router.get("/fetch_product_reviews_v2")
async def fetch_product_reviews_v2(
    product_id: str,
    request: Request,
    page_start: int | None = None,
    sort_rule: int | None = None,
    filter_type: int | None = None,
    filter_value: int | None = None,
    region: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取商品评论V2/Get product reviews V2"""
    body = await request.json()
    params: dict[str, Any] = {}
    if product_id is not None:
        params["product_id"] = product_id
    if page_start is not None:
        params["page_start"] = page_start
    if sort_rule is not None:
        params["sort_rule"] = sort_rule
    if filter_type is not None:
        params["filter_type"] = filter_type
    if filter_value is not None:
        params["filter_value"] = filter_value
    if region is not None:
        params["region"] = region
    return await proxy_request("tiktok", "/api/v1/tiktok/shop/web/fetch_product_reviews_v2", params=params, json_body=body)

@router.get("/fetch_seller_products_list")
async def fetch_seller_products_list(
    seller_id: str,
    request: Request,
    search_params: str | None = None,
    region: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取商家商品列表V1/Get seller products list V1"""
    body = await request.json()
    params: dict[str, Any] = {}
    if seller_id is not None:
        params["seller_id"] = seller_id
    if search_params is not None:
        params["search_params"] = search_params
    if region is not None:
        params["region"] = region
    return await proxy_request("tiktok", "/api/v1/tiktok/shop/web/fetch_seller_products_list", params=params, json_body=body)

@router.get("/fetch_seller_products_list_v2")
async def fetch_seller_products_list_v2(
    seller_id: str,
    request: Request,
    searchParams: str | None = None,
    region: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取商家商品列表V2(移动端)/Get seller products list V2 (Mobile)"""
    body = await request.json()
    params: dict[str, Any] = {}
    if seller_id is not None:
        params["seller_id"] = seller_id
    if searchParams is not None:
        params["searchParams"] = searchParams
    if region is not None:
        params["region"] = region
    return await proxy_request("tiktok", "/api/v1/tiktok/shop/web/fetch_seller_products_list_v2", params=params, json_body=body)

@router.get("/fetch_search_word_suggestion")
async def fetch_search_word_suggestion(
    search_word: str,
    request: Request,
    lang: str | None = None,
    region: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取搜索关键词建议V1/Get search keyword suggestions V1"""
    body = await request.json()
    params: dict[str, Any] = {}
    if search_word is not None:
        params["search_word"] = search_word
    if lang is not None:
        params["lang"] = lang
    if region is not None:
        params["region"] = region
    return await proxy_request("tiktok", "/api/v1/tiktok/shop/web/fetch_search_word_suggestion", params=params, json_body=body)

@router.get("/fetch_search_word_suggestion_v2")
async def fetch_search_word_suggestion_v2(
    search_word: str,
    request: Request,
    lang: str | None = None,
    region: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取搜索关键词建议V2(移动端)/Get search keyword suggestions V2 (Mobile)"""
    body = await request.json()
    params: dict[str, Any] = {}
    if search_word is not None:
        params["search_word"] = search_word
    if lang is not None:
        params["lang"] = lang
    if region is not None:
        params["region"] = region
    return await proxy_request("tiktok", "/api/v1/tiktok/shop/web/fetch_search_word_suggestion_v2", params=params, json_body=body)

@router.get("/fetch_search_products_list")
async def fetch_search_products_list(
    search_word: str,
    request: Request,
    offset: int | None = None,
    page_token: str | None = None,
    region: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """搜索商品列表V1/Search products list V1"""
    body = await request.json()
    params: dict[str, Any] = {}
    if search_word is not None:
        params["search_word"] = search_word
    if offset is not None:
        params["offset"] = offset
    if page_token is not None:
        params["page_token"] = page_token
    if region is not None:
        params["region"] = region
    return await proxy_request("tiktok", "/api/v1/tiktok/shop/web/fetch_search_products_list", params=params, json_body=body)

@router.get("/fetch_search_products_list_v2")
async def fetch_search_products_list_v2(
    search_word: str,
    request: Request,
    offset: int | None = None,
    page_token: str | None = None,
    region: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """搜索商品列表V2(移动端)/Search products list V2 (Mobile)"""
    body = await request.json()
    params: dict[str, Any] = {}
    if search_word is not None:
        params["search_word"] = search_word
    if offset is not None:
        params["offset"] = offset
    if page_token is not None:
        params["page_token"] = page_token
    if region is not None:
        params["region"] = region
    return await proxy_request("tiktok", "/api/v1/tiktok/shop/web/fetch_search_products_list_v2", params=params, json_body=body)

@router.get("/fetch_search_products_list_v3")
async def fetch_search_products_list_v3(
    keyword: str,
    request: Request,
    offset: int | None = None,
    region: str | None = None,
    sort_by: str | None = None,
    filters_data: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """搜索商品列表V3/Search products list V3"""
    body = await request.json()
    params: dict[str, Any] = {}
    if keyword is not None:
        params["keyword"] = keyword
    if offset is not None:
        params["offset"] = offset
    if region is not None:
        params["region"] = region
    if sort_by is not None:
        params["sort_by"] = sort_by
    if filters_data is not None:
        params["filters_data"] = filters_data
    return await proxy_request("tiktok", "/api/v1/tiktok/shop/web/fetch_search_products_list_v3", params=params, json_body=body)

@router.get("/fetch_products_category_list")
async def fetch_products_category_list(
    request: Request,
    region: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取商品分类列表/Get product category list"""
    body = await request.json()
    params: dict[str, Any] = {}
    if region is not None:
        params["region"] = region
    return await proxy_request("tiktok", "/api/v1/tiktok/shop/web/fetch_products_category_list", params=params, json_body=body)

@router.get("/fetch_products_by_category_id")
async def fetch_products_by_category_id(
    category_id: int,
    request: Request,
    offset: int | None = None,
    region: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """根据分类ID获取商品列表/Get products by category ID"""
    body = await request.json()
    params: dict[str, Any] = {}
    if category_id is not None:
        params["category_id"] = category_id
    if offset is not None:
        params["offset"] = offset
    if region is not None:
        params["region"] = region
    return await proxy_request("tiktok", "/api/v1/tiktok/shop/web/fetch_products_by_category_id", params=params, json_body=body)

@router.get("/fetch_hot_selling_products_list")
async def fetch_hot_selling_products_list(
    request: Request,
    region: str | None = None,
    count: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取热卖商品列表/Get hot selling products list"""
    body = await request.json()
    params: dict[str, Any] = {}
    if region is not None:
        params["region"] = region
    if count is not None:
        params["count"] = count
    return await proxy_request("tiktok", "/api/v1/tiktok/shop/web/fetch_hot_selling_products_list", params=params, json_body=body)
