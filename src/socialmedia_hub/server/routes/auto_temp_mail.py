"""Auto-generated routes for Temp-Mail-API."""

from __future__ import annotations

from typing import Any

from fastapi import APIRouter, Depends, Request

from socialmedia_hub.server._core import proxy_request, verify_api_key

router = APIRouter(prefix="/api/v1/temp_mail", tags=["temp_mail"])

@router.get("/get_temp_email_address")
async def get_temp_email_address(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """Get Temp Email"""
    body = await request.json()
    return await proxy_request("temp_mail", "/api/v1/temp_mail/v1/get_temp_email_address", json_body=body)

@router.get("/get_emails_inbox")
async def get_emails_inbox(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """Get Emails"""
    body = await request.json()
    params: dict[str, Any] = {}
    if token is not None:
        params["token"] = token
    return await proxy_request("temp_mail", "/api/v1/temp_mail/v1/get_emails_inbox", params=params, json_body=body)


@router.get("/get_email_by_id")
async def get_email_by_id(
    message_id: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """Get Email By Id"""
    body = await request.json()
    params: dict[str, Any] = {}
    if message_id is not None:
        params["message_id"] = message_id
    return await proxy_request("temp_mail", "/api/v1/temp_mail/v1/get_email_by_id", params=params, json_body=body)
