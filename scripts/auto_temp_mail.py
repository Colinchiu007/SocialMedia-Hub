"""Auto-generated routes for Temp-Mail-API."""

from __future__ import annotations

from typing import Any

from fastapi import APIRouter, Depends, Request

from socialmedia_hub.server._core import proxy_request, verify_api_key

router = APIRouter(prefix="/api/v1/temp_mail", tags=["temp_mail"])

@router.get("/get_temp_email_address")
async def get_temp_email_address(
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """Get Temp Email"""
        body = await request.json()
        return await proxy_request("temp_mail", "/api/v1/temp_mail/v1/get_temp_email_address", json_body=body)

@router.get("/get_emails_inbox")
async def get_emails_inbox(
    token: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """Get Emails"""
        params: dict[str, Any] = {}
        if token is not None:
            params["token"] = token
        body = await request.json()
        return await proxy_request("temp_mail", "/api/v1/temp_mail/v1/get_emails_inbox", json_body=body)

@router.get("/get_email_by_id")
async def get_email_by_id(
    message_id: str,
    token: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """Get Email By Id"""
        params: dict[str, Any] = {}
        if token is not None:
            params["token"] = token
        if message_id is not None:
            params["message_id"] = message_id
        body = await request.json()
        return await proxy_request("temp_mail", "/api/v1/temp_mail/v1/get_email_by_id", json_body=body)
