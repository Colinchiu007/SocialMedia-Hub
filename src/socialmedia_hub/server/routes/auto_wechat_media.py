"""Auto-generated routes for WeChat-Media-Platform-Web-API."""

from __future__ import annotations

from typing import Any

from fastapi import APIRouter, Depends, Request

from socialmedia_hub.server._core import proxy_request, verify_api_key

router = APIRouter(prefix="/api/v1/wechat/media", tags=["wechat_media_platform_web"])

@router.get("/fetch_mp_article_detail_json")
async def fetch_mp_article_detail_json(
    url: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取微信公众号文章详情的JSON/Get Wechat MP Article Detail JSON"""
    body = await request.json()
    params: dict[str, Any] = {}
    if url is not None:
        params["url"] = url
    return await proxy_request("wechat", "/api/v1/wechat_mp/web/fetch_mp_article_detail_json", params=params, json_body=body)

@router.get("/fetch_mp_article_detail_html")
async def fetch_mp_article_detail_html(
    url: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取微信公众号文章详情的HTML/Get Wechat MP Article Detail HTML"""
    body = await request.json()
    params: dict[str, Any] = {}
    if url is not None:
        params["url"] = url
    return await proxy_request("wechat", "/api/v1/wechat_mp/web/fetch_mp_article_detail_html", params=params, json_body=body)

@router.get("/fetch_mp_article_list")
async def fetch_mp_article_list(
    ghid: str,
    request: Request,
    offset: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取微信公众号文章列表/Get Wechat MP Article List"""
    body = await request.json()
    params: dict[str, Any] = {}
    if ghid is not None:
        params["ghid"] = ghid
    if offset is not None:
        params["offset"] = offset
    return await proxy_request("wechat", "/api/v1/wechat_mp/web/fetch_mp_article_list", params=params, json_body=body)

@router.get("/fetch_mp_article_read_count")
async def fetch_mp_article_read_count(
    url: str,
    comment_id: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取微信公众号文章阅读量/Get Wechat MP Article Read Count"""
    body = await request.json()
    params: dict[str, Any] = {}
    if url is not None:
        params["url"] = url
    if comment_id is not None:
        params["comment_id"] = comment_id
    return await proxy_request("wechat", "/api/v1/wechat_mp/web/fetch_mp_article_read_count", params=params, json_body=body)

@router.get("/fetch_mp_article_url")
async def fetch_mp_article_url(
    sogou_url: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取微信公众号文章永久链接/Get Wechat MP Article URL"""
    body = await request.json()
    params: dict[str, Any] = {}
    if sogou_url is not None:
        params["sogou_url"] = sogou_url
    return await proxy_request("wechat", "/api/v1/wechat_mp/web/fetch_mp_article_url", params=params, json_body=body)

@router.get("/fetch_mp_article_comment_list")
async def fetch_mp_article_comment_list(
    url: str,
    request: Request,
    comment_id: str | None = None,
    buffer: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取微信公众号文章评论列表/Get Wechat MP Article Comment List"""
    body = await request.json()
    params: dict[str, Any] = {}
    if url is not None:
        params["url"] = url
    if comment_id is not None:
        params["comment_id"] = comment_id
    if buffer is not None:
        params["buffer"] = buffer
    return await proxy_request("wechat", "/api/v1/wechat_mp/web/fetch_mp_article_comment_list", params=params, json_body=body)

@router.get("/fetch_mp_article_comment_reply_list")
async def fetch_mp_article_comment_reply_list(
    comment_id: str,
    content_id: str,
    request: Request,
    url: str | None = None,
    offset: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取微信公众号文章评论回复列表/Get Wechat MP Article Comment Reply List"""
    body = await request.json()
    params: dict[str, Any] = {}
    if url is not None:
        params["url"] = url
    if comment_id is not None:
        params["comment_id"] = comment_id
    if content_id is not None:
        params["content_id"] = content_id
    if offset is not None:
        params["offset"] = offset
    return await proxy_request("wechat", "/api/v1/wechat_mp/web/fetch_mp_article_comment_reply_list", params=params, json_body=body)

@router.get("/fetch_mp_article_ad")
async def fetch_mp_article_ad(
    url: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取微信公众号广告/Get Wechat MP Article Ad"""
    body = await request.json()
    params: dict[str, Any] = {}
    if url is not None:
        params["url"] = url
    return await proxy_request("wechat", "/api/v1/wechat_mp/web/fetch_mp_article_ad", params=params, json_body=body)

@router.get("/fetch_mp_article_url_conversion")
async def fetch_mp_article_url_conversion(
    url: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取微信公众号长链接转短链接/Get Wechat MP Long URL to Short URL"""
    body = await request.json()
    params: dict[str, Any] = {}
    if url is not None:
        params["url"] = url
    return await proxy_request("wechat", "/api/v1/wechat_mp/web/fetch_mp_article_url_conversion", params=params, json_body=body)

@router.get("/fetch_mp_related_articles")
async def fetch_mp_related_articles(
    url: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取微信公众号关联文章/Get Wechat MP Related Articles"""
    body = await request.json()
    params: dict[str, Any] = {}
    if url is not None:
        params["url"] = url
    return await proxy_request("wechat", "/api/v1/wechat_mp/web/fetch_mp_related_articles", params=params, json_body=body)
