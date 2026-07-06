"""Auto-generated routes for Twitter-Web-API."""

from __future__ import annotations

from typing import Any

from fastapi import APIRouter, Depends, Request

from socialmedia_hub.server._core import proxy_request, verify_api_key

router = APIRouter(prefix="/api/v1/twitter/web", tags=["twitter_web"])

@router.get("/fetch_tweet_detail")
async def fetch_tweet_detail(
    tweet_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取单个推文数据/Get single tweet data"""
        params: dict[str, Any] = {}
        if tweet_id is not None:
            params["tweet_id"] = tweet_id
        body = await request.json()
        return await proxy_request("twitter", "/api/v1/twitter/web/fetch_tweet_detail", json_body=body)

@router.get("/fetch_user_profile")
async def fetch_user_profile(
    rest_id: int | None = None,
    screen_name: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户资料/Get user profile"""
        params: dict[str, Any] = {}
        if screen_name is not None:
            params["screen_name"] = screen_name
        if rest_id is not None:
            params["rest_id"] = rest_id
        body = await request.json()
        return await proxy_request("twitter", "/api/v1/twitter/web/fetch_user_profile", json_body=body)

@router.get("/fetch_user_post_tweet")
async def fetch_user_post_tweet(
    cursor: str | None = None,
    rest_id: int | None = None,
    screen_name: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户发帖/Get user post"""
        params: dict[str, Any] = {}
        if screen_name is not None:
            params["screen_name"] = screen_name
        if rest_id is not None:
            params["rest_id"] = rest_id
        if cursor is not None:
            params["cursor"] = cursor
        body = await request.json()
        return await proxy_request("twitter", "/api/v1/twitter/web/fetch_user_post_tweet", json_body=body)

@router.get("/fetch_search_timeline")
async def fetch_search_timeline(
    cursor: str | None = None,
    search_type: str | None = None,
    keyword: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """搜索/Search"""
        params: dict[str, Any] = {}
        if keyword is not None:
            params["keyword"] = keyword
        if search_type is not None:
            params["search_type"] = search_type
        if cursor is not None:
            params["cursor"] = cursor
        body = await request.json()
        return await proxy_request("twitter", "/api/v1/twitter/web/fetch_search_timeline", json_body=body)

@router.get("/fetch_post_comments")
async def fetch_post_comments(
    cursor: str | None = None,
    tweet_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取评论/Get comments"""
        params: dict[str, Any] = {}
        if tweet_id is not None:
            params["tweet_id"] = tweet_id
        if cursor is not None:
            params["cursor"] = cursor
        body = await request.json()
        return await proxy_request("twitter", "/api/v1/twitter/web/fetch_post_comments", json_body=body)

@router.get("/fetch_latest_post_comments")
async def fetch_latest_post_comments(
    cursor: str | None = None,
    tweet_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取最新的推文评论/Get the latest tweet comments"""
        params: dict[str, Any] = {}
        if tweet_id is not None:
            params["tweet_id"] = tweet_id
        if cursor is not None:
            params["cursor"] = cursor
        body = await request.json()
        return await proxy_request("twitter", "/api/v1/twitter/web/fetch_latest_post_comments", json_body=body)

@router.get("/fetch_user_tweet_replies")
async def fetch_user_tweet_replies(
    cursor: str | None = None,
    screen_name: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户推文回复/Get user tweet replies"""
        params: dict[str, Any] = {}
        if screen_name is not None:
            params["screen_name"] = screen_name
        if cursor is not None:
            params["cursor"] = cursor
        body = await request.json()
        return await proxy_request("twitter", "/api/v1/twitter/web/fetch_user_tweet_replies", json_body=body)

@router.get("/fetch_user_highlights_tweets")
async def fetch_user_highlights_tweets(
    cursor: str | None = None,
    count: int | None = None,
    userId: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户高光推文/Get user highlights tweets"""
        params: dict[str, Any] = {}
        if userId is not None:
            params["userId"] = userId
        if count is not None:
            params["count"] = count
        if cursor is not None:
            params["cursor"] = cursor
        body = await request.json()
        return await proxy_request("twitter", "/api/v1/twitter/web/fetch_user_highlights_tweets", json_body=body)

@router.get("/fetch_user_media")
async def fetch_user_media(
    cursor: str | None = None,
    rest_id: int | None = None,
    screen_name: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户媒体/Get user media"""
        params: dict[str, Any] = {}
        if screen_name is not None:
            params["screen_name"] = screen_name
        if rest_id is not None:
            params["rest_id"] = rest_id
        if cursor is not None:
            params["cursor"] = cursor
        body = await request.json()
        return await proxy_request("twitter", "/api/v1/twitter/web/fetch_user_media", json_body=body)

@router.get("/fetch_retweet_user_list")
async def fetch_retweet_user_list(
    cursor: str | None = None,
    tweet_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """转推用户列表/ReTweet User list"""
        params: dict[str, Any] = {}
        if tweet_id is not None:
            params["tweet_id"] = tweet_id
        if cursor is not None:
            params["cursor"] = cursor
        body = await request.json()
        return await proxy_request("twitter", "/api/v1/twitter/web/fetch_retweet_user_list", json_body=body)

@router.get("/fetch_trending")
async def fetch_trending(
    country: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """趋势/Trending"""
        params: dict[str, Any] = {}
        if country is not None:
            params["country"] = country
        body = await request.json()
        return await proxy_request("twitter", "/api/v1/twitter/web/fetch_trending", json_body=body)

@router.get("/fetch_user_followings")
async def fetch_user_followings(
    cursor: str | None = None,
    screen_name: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """用户关注/User Followings"""
        params: dict[str, Any] = {}
        if screen_name is not None:
            params["screen_name"] = screen_name
        if cursor is not None:
            params["cursor"] = cursor
        body = await request.json()
        return await proxy_request("twitter", "/api/v1/twitter/web/fetch_user_followings", json_body=body)

@router.get("/fetch_user_followers")
async def fetch_user_followers(
    cursor: str | None = None,
    screen_name: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """用户粉丝/User Followers"""
        params: dict[str, Any] = {}
        if screen_name is not None:
            params["screen_name"] = screen_name
        if cursor is not None:
            params["cursor"] = cursor
        body = await request.json()
        return await proxy_request("twitter", "/api/v1/twitter/web/fetch_user_followers", json_body=body)
