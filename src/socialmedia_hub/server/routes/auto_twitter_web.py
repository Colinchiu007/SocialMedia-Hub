"""Auto-generated routes for Twitter-Web-API."""

from __future__ import annotations

from typing import Any

from fastapi import APIRouter, Depends, Request

from socialmedia_hub.server._core import proxy_request, verify_api_key

router = APIRouter(prefix="/api/v1/twitter/web", tags=["twitter_web"])

@router.get("/fetch_tweet_detail")
async def fetch_tweet_detail(
    tweet_id: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取单个推文数据/Get single tweet data"""
    body = await request.json()
    params: dict[str, Any] = {}
    if tweet_id is not None:
        params["tweet_id"] = tweet_id
    return await proxy_request("twitter", "/api/v1/twitter/web/fetch_tweet_detail", params=params, json_body=body)

@router.get("/fetch_user_profile")
async def fetch_user_profile(
    request: Request,
    screen_name: str | None = None,
    rest_id: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户资料/Get user profile"""
    body = await request.json()
    params: dict[str, Any] = {}
    if screen_name is not None:
        params["screen_name"] = screen_name
    if rest_id is not None:
        params["rest_id"] = rest_id
    return await proxy_request("twitter", "/api/v1/twitter/web/fetch_user_profile", params=params, json_body=body)

@router.get("/fetch_user_post_tweet")
async def fetch_user_post_tweet(
    request: Request,
    screen_name: str | None = None,
    rest_id: int | None = None,
    cursor: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户发帖/Get user post"""
    body = await request.json()
    params: dict[str, Any] = {}
    if screen_name is not None:
        params["screen_name"] = screen_name
    if rest_id is not None:
        params["rest_id"] = rest_id
    if cursor is not None:
        params["cursor"] = cursor
    return await proxy_request("twitter", "/api/v1/twitter/web/fetch_user_post_tweet", params=params, json_body=body)

@router.get("/fetch_search_timeline")
async def fetch_search_timeline(
    keyword: str,
    request: Request,
    search_type: str | None = None,
    cursor: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """搜索/Search"""
    body = await request.json()
    params: dict[str, Any] = {}
    if keyword is not None:
        params["keyword"] = keyword
    if search_type is not None:
        params["search_type"] = search_type
    if cursor is not None:
        params["cursor"] = cursor
    return await proxy_request("twitter", "/api/v1/twitter/web/fetch_search_timeline", params=params, json_body=body)

@router.get("/fetch_post_comments")
async def fetch_post_comments(
    tweet_id: str,
    request: Request,
    cursor: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取评论/Get comments"""
    body = await request.json()
    params: dict[str, Any] = {}
    if tweet_id is not None:
        params["tweet_id"] = tweet_id
    if cursor is not None:
        params["cursor"] = cursor
    return await proxy_request("twitter", "/api/v1/twitter/web/fetch_post_comments", params=params, json_body=body)

@router.get("/fetch_latest_post_comments")
async def fetch_latest_post_comments(
    tweet_id: str,
    request: Request,
    cursor: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取最新的推文评论/Get the latest tweet comments"""
    body = await request.json()
    params: dict[str, Any] = {}
    if tweet_id is not None:
        params["tweet_id"] = tweet_id
    if cursor is not None:
        params["cursor"] = cursor
    return await proxy_request("twitter", "/api/v1/twitter/web/fetch_latest_post_comments", params=params, json_body=body)

@router.get("/fetch_user_tweet_replies")
async def fetch_user_tweet_replies(
    screen_name: str,
    request: Request,
    cursor: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户推文回复/Get user tweet replies"""
    body = await request.json()
    params: dict[str, Any] = {}
    if screen_name is not None:
        params["screen_name"] = screen_name
    if cursor is not None:
        params["cursor"] = cursor
    return await proxy_request("twitter", "/api/v1/twitter/web/fetch_user_tweet_replies", params=params, json_body=body)

@router.get("/fetch_user_highlights_tweets")
async def fetch_user_highlights_tweets(
    userId: str,
    request: Request,
    count: int | None = None,
    cursor: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户高光推文/Get user highlights tweets"""
    body = await request.json()
    params: dict[str, Any] = {}
    if userId is not None:
        params["userId"] = userId
    if count is not None:
        params["count"] = count
    if cursor is not None:
        params["cursor"] = cursor
    return await proxy_request("twitter", "/api/v1/twitter/web/fetch_user_highlights_tweets", params=params, json_body=body)

@router.get("/fetch_user_media")
async def fetch_user_media(
    screen_name: str,
    request: Request,
    rest_id: int | None = None,
    cursor: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户媒体/Get user media"""
    body = await request.json()
    params: dict[str, Any] = {}
    if screen_name is not None:
        params["screen_name"] = screen_name
    if rest_id is not None:
        params["rest_id"] = rest_id
    if cursor is not None:
        params["cursor"] = cursor
    return await proxy_request("twitter", "/api/v1/twitter/web/fetch_user_media", params=params, json_body=body)

@router.get("/fetch_retweet_user_list")
async def fetch_retweet_user_list(
    tweet_id: str,
    request: Request,
    cursor: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """转推用户列表/ReTweet User list"""
    body = await request.json()
    params: dict[str, Any] = {}
    if tweet_id is not None:
        params["tweet_id"] = tweet_id
    if cursor is not None:
        params["cursor"] = cursor
    return await proxy_request("twitter", "/api/v1/twitter/web/fetch_retweet_user_list", params=params, json_body=body)

@router.get("/fetch_trending")
async def fetch_trending(
    request: Request,
    country: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """趋势/Trending"""
    body = await request.json()
    params: dict[str, Any] = {}
    if country is not None:
        params["country"] = country
    return await proxy_request("twitter", "/api/v1/twitter/web/fetch_trending", params=params, json_body=body)

@router.get("/fetch_user_followings")
async def fetch_user_followings(
    screen_name: str,
    request: Request,
    cursor: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """用户关注/User Followings"""
    body = await request.json()
    params: dict[str, Any] = {}
    if screen_name is not None:
        params["screen_name"] = screen_name
    if cursor is not None:
        params["cursor"] = cursor
    return await proxy_request("twitter", "/api/v1/twitter/web/fetch_user_followings", params=params, json_body=body)

@router.get("/fetch_user_followers")
async def fetch_user_followers(
    screen_name: str,
    request: Request,
    cursor: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """用户粉丝/User Followers"""
    body = await request.json()
    params: dict[str, Any] = {}
    if screen_name is not None:
        params["screen_name"] = screen_name
    if cursor is not None:
        params["cursor"] = cursor
    return await proxy_request("twitter", "/api/v1/twitter/web/fetch_user_followers", params=params, json_body=body)
