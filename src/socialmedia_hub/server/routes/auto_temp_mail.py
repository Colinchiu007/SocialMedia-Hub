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
    return await proxy_request("temp_mail", "/api/v1/temp_mail/v1/get_temp_email_address")

@router.get("/get_emails_inbox")
async def get_emails_inbox(
    mail_token: str | None = None,
    request: Request = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """Get Emails"""
    params: dict[str, Any] = {}
    if mail_token is not None:
        params["token"] = mail_token
    return await proxy_request("temp_mail", "/api/v1/temp_mail/v1/get_emails_inbox", params=params)

@router.get("/get_email_by_id")
async def get_email_by_id(
    mail_token: str | None = None,
    message_id: str | None = None,
    request: Request = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """Get Email By Id"""
    params: dict[str, Any] = {}
    if mail_token is not None:
        params["token"] = mail_token
    if message_id is not None:
        params["message_id"] = message_id
    return await proxy_request("temp_mail", "/api/v1/temp_mail/v1/get_email_by_id", params=params)
