"""Auto-generated routes for TikHub-User-API."""

from __future__ import annotations

from typing import Any

from fastapi import APIRouter, Depends, Request

from socialmedia_hub.server._core import proxy_request, verify_api_key

router = APIRouter(prefix="/api/v1/tikhub/user", tags=["tikhub_user"])

@router.get("/get_user_info")
async def get_user_info(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取TikHub用户信息/Get TikHub user info"""
    return await proxy_request("tikhub", "/api/v1/tikhub/user/get_user_info")

@router.get("/get_user_daily_usage")
async def get_user_daily_usage(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户每日使用情况/Get user daily usage"""
    return await proxy_request("tikhub", "/api/v1/tikhub/user/get_user_daily_usage")

@router.get("/calculate_price")
async def calculate_price(
    endpoint: str,
    request: Request,
    request_per_day: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """计算价格/Calculate price"""
    params: dict[str, Any] = {}
    if endpoint is not None:
        params["endpoint"] = endpoint
    if request_per_day is not None:
        params["request_per_day"] = request_per_day
    return await proxy_request("tikhub", "/api/v1/tikhub/user/calculate_price", params=params)

@router.get("/get_tiered_discount_info")
async def get_tiered_discount_info(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取阶梯式折扣百分比信息/Get tiered discount percentage information"""
    return await proxy_request("tikhub", "/api/v1/tikhub/user/get_tiered_discount_info")

@router.get("/get_endpoint_info")
async def get_endpoint_info(
    endpoint: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取一个端点的信息/Get information of an endpoint"""
    params: dict[str, Any] = {}
    if endpoint is not None:
        params["endpoint"] = endpoint
    return await proxy_request("tikhub", "/api/v1/tikhub/user/get_endpoint_info", params=params)

@router.get("/get_all_endpoints_info")
async def get_all_endpoints_info(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取所有端点信息/Get all endpoints information"""
    return await proxy_request("tikhub", "/api/v1/tikhub/user/get_all_endpoints_info")
