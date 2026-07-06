"""Auto-generated routes for TikHub-User-API."""

from __future__ import annotations

from typing import Any

from fastapi import APIRouter, Depends, Request

from socialmedia_hub.server._core import proxy_request, verify_api_key

router = APIRouter(prefix="/api/v1/tikhub/user", tags=["tikhub_user"])

@router.get("/get_user_info")
async def get_user_info(
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取TikHub用户信息/Get TikHub user info"""
        body = await request.json()
        return await proxy_request("tikhub", "/api/v1/tikhub/user/get_user_info", json_body=body)

@router.get("/get_user_daily_usage")
async def get_user_daily_usage(
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户每日使用情况/Get user daily usage"""
        body = await request.json()
        return await proxy_request("tikhub", "/api/v1/tikhub/user/get_user_daily_usage", json_body=body)

@router.get("/calculate_price")
async def calculate_price(
    request_per_day: int | None = None,
    endpoint: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """计算价格/Calculate price"""
        params: dict[str, Any] = {}
        if endpoint is not None:
            params["endpoint"] = endpoint
        if request_per_day is not None:
            params["request_per_day"] = request_per_day
        body = await request.json()
        return await proxy_request("tikhub", "/api/v1/tikhub/user/calculate_price", json_body=body)

@router.get("/get_tiered_discount_info")
async def get_tiered_discount_info(
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取阶梯式折扣百分比信息/Get tiered discount percentage information"""
        body = await request.json()
        return await proxy_request("tikhub", "/api/v1/tikhub/user/get_tiered_discount_info", json_body=body)

@router.get("/get_endpoint_info")
async def get_endpoint_info(
    endpoint: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取一个端点的信息/Get information of an endpoint"""
        params: dict[str, Any] = {}
        if endpoint is not None:
            params["endpoint"] = endpoint
        body = await request.json()
        return await proxy_request("tikhub", "/api/v1/tikhub/user/get_endpoint_info", json_body=body)

@router.get("/get_all_endpoints_info")
async def get_all_endpoints_info(
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取所有端点信息/Get all endpoints information"""
        body = await request.json()
        return await proxy_request("tikhub", "/api/v1/tikhub/user/get_all_endpoints_info", json_body=body)
