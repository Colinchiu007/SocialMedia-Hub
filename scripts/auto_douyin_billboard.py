"""Auto-generated routes for Douyin-Billboard-API."""

from __future__ import annotations

from typing import Any

from fastapi import APIRouter, Depends, Request

from socialmedia_hub.server._core import proxy_request, verify_api_key

router = APIRouter(prefix="/api/v1/douyin/billboard", tags=["douyin_billboard"])

@router.get("/fetch_city_list")
async def fetch_city_list(
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取中国城市列表/Fetch Chinese city list"""
        body = await request.json()
        return await proxy_request("douyin", "/api/v1/douyin/billboard/fetch_city_list", json_body=body)

@router.get("/fetch_content_tag")
async def fetch_content_tag(
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取垂类内容标签/Fetch vertical content tags"""
        body = await request.json()
        return await proxy_request("douyin", "/api/v1/douyin/billboard/fetch_content_tag", json_body=body)

@router.get("/fetch_hot_category_list")
async def fetch_hot_category_list(
    keyword: str | None = None,
    end_date: str | None = None,
    start_date: str | None = None,
    snapshot_time: str | None = None,
    billboard_type: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取热点榜分类/Fetch hot list category"""
        params: dict[str, Any] = {}
        if billboard_type is not None:
            params["billboard_type"] = billboard_type
        if snapshot_time is not None:
            params["snapshot_time"] = snapshot_time
        if start_date is not None:
            params["start_date"] = start_date
        if end_date is not None:
            params["end_date"] = end_date
        if keyword is not None:
            params["keyword"] = keyword
        body = await request.json()
        return await proxy_request("douyin", "/api/v1/douyin/billboard/fetch_hot_category_list", json_body=body)

@router.get("/fetch_hot_rise_list")
async def fetch_hot_rise_list(
    keyword: str | None = None,
    sentence_tag: str | None = None,
    order: str,
    page_size: int,
    page: int,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取上升热点榜/Fetch rising hot list"""
        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if page_size is not None:
            params["page_size"] = page_size
        if order is not None:
            params["order"] = order
        if sentence_tag is not None:
            params["sentence_tag"] = sentence_tag
        if keyword is not None:
            params["keyword"] = keyword
        body = await request.json()
        return await proxy_request("douyin", "/api/v1/douyin/billboard/fetch_hot_rise_list", json_body=body)

@router.get("/fetch_hot_city_list")
async def fetch_hot_city_list(
    keyword: str | None = None,
    sentence_tag: str | None = None,
    city_code: str | None = None,
    order: str,
    page_size: int,
    page: int,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取同城热点榜/Fetch city hot list"""
        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if page_size is not None:
            params["page_size"] = page_size
        if order is not None:
            params["order"] = order
        if city_code is not None:
            params["city_code"] = city_code
        if sentence_tag is not None:
            params["sentence_tag"] = sentence_tag
        if keyword is not None:
            params["keyword"] = keyword
        body = await request.json()
        return await proxy_request("douyin", "/api/v1/douyin/billboard/fetch_hot_city_list", json_body=body)

@router.get("/fetch_hot_challenge_list")
async def fetch_hot_challenge_list(
    keyword: str | None = None,
    page_size: int,
    page: int,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取挑战热榜/Fetch hot challenge list"""
        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if page_size is not None:
            params["page_size"] = page_size
        if keyword is not None:
            params["keyword"] = keyword
        body = await request.json()
        return await proxy_request("douyin", "/api/v1/douyin/billboard/fetch_hot_challenge_list", json_body=body)

@router.get("/fetch_hot_total_list")
async def fetch_hot_total_list(
    keyword: str | None = None,
    sentence_tag: str | None = None,
    end_date: str | None = None,
    start_date: str | None = None,
    snapshot_time: str | None = None,
    type: str,
    page_size: int,
    page: int,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取热点总榜/Fetch total hot list"""
        params: dict[str, Any] = {}
        if page is not None:
            params["page"] = page
        if page_size is not None:
            params["page_size"] = page_size
        if type is not None:
            params["type"] = type
        if snapshot_time is not None:
            params["snapshot_time"] = snapshot_time
        if start_date is not None:
            params["start_date"] = start_date
        if end_date is not None:
            params["end_date"] = end_date
        if sentence_tag is not None:
            params["sentence_tag"] = sentence_tag
        if keyword is not None:
            params["keyword"] = keyword
        body = await request.json()
        return await proxy_request("douyin", "/api/v1/douyin/billboard/fetch_hot_total_list", json_body=body)

@router.post("/fetch_hot_calendar_list")
async def fetch_hot_calendar_list(
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取活动日历/Fetch activity calendar"""
        body = await request.json()
        return await proxy_request("douyin", "/api/v1/douyin/billboard/fetch_hot_calendar_list", json_body=body)

@router.get("/fetch_hot_calendar_detail")
async def fetch_hot_calendar_detail(
    calendar_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取活动日历详情/Fetch activity calendar detail"""
        params: dict[str, Any] = {}
        if calendar_id is not None:
            params["calendar_id"] = calendar_id
        body = await request.json()
        return await proxy_request("douyin", "/api/v1/douyin/billboard/fetch_hot_calendar_detail", json_body=body)

@router.get("/fetch_hot_user_portrait_list")
async def fetch_hot_user_portrait_list(
    option: int | None = None,
    aweme_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取作品点赞观众画像-仅限热门榜/Fetch work like audience portrait - hot list only"""
        params: dict[str, Any] = {}
        if aweme_id is not None:
            params["aweme_id"] = aweme_id
        if option is not None:
            params["option"] = option
        body = await request.json()
        return await proxy_request("douyin", "/api/v1/douyin/billboard/fetch_hot_user_portrait_list", json_body=body)

@router.get("/fetch_hot_comment_word_list")
async def fetch_hot_comment_word_list(
    aweme_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取作品评论分析-词云权重/Fetch work comment analysis word cloud weight"""
        params: dict[str, Any] = {}
        if aweme_id is not None:
            params["aweme_id"] = aweme_id
        body = await request.json()
        return await proxy_request("douyin", "/api/v1/douyin/billboard/fetch_hot_comment_word_list", json_body=body)

@router.get("/fetch_hot_item_trends_list")
async def fetch_hot_item_trends_list(
    date_window: int | None = None,
    option: int | None = None,
    aweme_id: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取作品数据趋势/Fetch post data trend"""
        params: dict[str, Any] = {}
        if aweme_id is not None:
            params["aweme_id"] = aweme_id
        if option is not None:
            params["option"] = option
        if date_window is not None:
            params["date_window"] = date_window
        body = await request.json()
        return await proxy_request("douyin", "/api/v1/douyin/billboard/fetch_hot_item_trends_list", json_body=body)

@router.post("/fetch_hot_account_list")
async def fetch_hot_account_list(
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取热门账号/Fetch hot account list"""
        body = await request.json()
        return await proxy_request("douyin", "/api/v1/douyin/billboard/fetch_hot_account_list", json_body=body)

@router.get("/fetch_hot_account_search_list")
async def fetch_hot_account_search_list(
    cursor: int,
    keyword: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """搜索用户名或抖音号/Fetch account search list"""
        params: dict[str, Any] = {}
        if keyword is not None:
            params["keyword"] = keyword
        if cursor is not None:
            params["cursor"] = cursor
        body = await request.json()
        return await proxy_request("douyin", "/api/v1/douyin/billboard/fetch_hot_account_search_list", json_body=body)

@router.get("/fetch_hot_account_trends_list")
async def fetch_hot_account_trends_list(
    date_window: int | None = None,
    option: int | None = None,
    sec_uid: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取账号粉丝数据趋势/Fetch account fan data trend"""
        params: dict[str, Any] = {}
        if sec_uid is not None:
            params["sec_uid"] = sec_uid
        if option is not None:
            params["option"] = option
        if date_window is not None:
            params["date_window"] = date_window
        body = await request.json()
        return await proxy_request("douyin", "/api/v1/douyin/billboard/fetch_hot_account_trends_list", json_body=body)

@router.get("/fetch_hot_account_item_analysis_list")
async def fetch_hot_account_item_analysis_list(
    sec_uid: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取账号作品分析-上周/Fetch account work analysis - last week"""
        params: dict[str, Any] = {}
        if sec_uid is not None:
            params["sec_uid"] = sec_uid
        body = await request.json()
        return await proxy_request("douyin", "/api/v1/douyin/billboard/fetch_hot_account_item_analysis_list", json_body=body)

@router.get("/fetch_hot_account_fans_portrait_list")
async def fetch_hot_account_fans_portrait_list(
    option: int | None = None,
    sec_uid: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取粉丝画像/Fetch fan portrait"""
        params: dict[str, Any] = {}
        if sec_uid is not None:
            params["sec_uid"] = sec_uid
        if option is not None:
            params["option"] = option
        body = await request.json()
        return await proxy_request("douyin", "/api/v1/douyin/billboard/fetch_hot_account_fans_portrait_list", json_body=body)

@router.get("/fetch_hot_account_fans_interest_account_list")
async def fetch_hot_account_fans_interest_account_list(
    sec_uid: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取粉丝兴趣作者 20个用户/Fetch fan interest author 20 users"""
        params: dict[str, Any] = {}
        if sec_uid is not None:
            params["sec_uid"] = sec_uid
        body = await request.json()
        return await proxy_request("douyin", "/api/v1/douyin/billboard/fetch_hot_account_fans_interest_account_list", json_body=body)

@router.get("/fetch_hot_account_fans_interest_topic_list")
async def fetch_hot_account_fans_interest_topic_list(
    sec_uid: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取粉丝近3天感兴趣的话题 10个话题/Fetch fan interest topic in the last 3 days 10 topics"""
        params: dict[str, Any] = {}
        if sec_uid is not None:
            params["sec_uid"] = sec_uid
        body = await request.json()
        return await proxy_request("douyin", "/api/v1/douyin/billboard/fetch_hot_account_fans_interest_topic_list", json_body=body)

@router.get("/fetch_hot_account_fans_interest_search_list")
async def fetch_hot_account_fans_interest_search_list(
    sec_uid: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取粉丝近3天搜索词 10个搜索词/Fetch fan interest search term in the last 3 days 10 search terms"""
        params: dict[str, Any] = {}
        if sec_uid is not None:
            params["sec_uid"] = sec_uid
        body = await request.json()
        return await proxy_request("douyin", "/api/v1/douyin/billboard/fetch_hot_account_fans_interest_search_list", json_body=body)

@router.post("/fetch_hot_total_video_list")
async def fetch_hot_total_video_list(
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取视频热榜/Fetch video hot list"""
        body = await request.json()
        return await proxy_request("douyin", "/api/v1/douyin/billboard/fetch_hot_total_video_list", json_body=body)

@router.post("/fetch_hot_total_low_fan_list")
async def fetch_hot_total_low_fan_list(
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取低粉爆款榜/Fetch low fan explosion list"""
        body = await request.json()
        return await proxy_request("douyin", "/api/v1/douyin/billboard/fetch_hot_total_low_fan_list", json_body=body)

@router.post("/fetch_hot_total_high_play_list")
async def fetch_hot_total_high_play_list(
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取高完播率榜/Fetch high completion rate list"""
        body = await request.json()
        return await proxy_request("douyin", "/api/v1/douyin/billboard/fetch_hot_total_high_play_list", json_body=body)

@router.post("/fetch_hot_total_high_like_list")
async def fetch_hot_total_high_like_list(
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取高点赞率榜/Fetch high like rate list"""
        body = await request.json()
        return await proxy_request("douyin", "/api/v1/douyin/billboard/fetch_hot_total_high_like_list", json_body=body)

@router.post("/fetch_hot_total_high_fan_list")
async def fetch_hot_total_high_fan_list(
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取高涨粉率榜/Fetch high fan rate list"""
        body = await request.json()
        return await proxy_request("douyin", "/api/v1/douyin/billboard/fetch_hot_total_high_fan_list", json_body=body)

@router.post("/fetch_hot_total_topic_list")
async def fetch_hot_total_topic_list(
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取话题热榜/Fetch topic hot list"""
        body = await request.json()
        return await proxy_request("douyin", "/api/v1/douyin/billboard/fetch_hot_total_topic_list", json_body=body)

@router.post("/fetch_hot_total_high_topic_list")
async def fetch_hot_total_high_topic_list(
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取热度飙升的话题榜/Fetch topic list with rising popularity"""
        body = await request.json()
        return await proxy_request("douyin", "/api/v1/douyin/billboard/fetch_hot_total_high_topic_list", json_body=body)

@router.post("/fetch_hot_total_search_list")
async def fetch_hot_total_search_list(
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取搜索热榜/Fetch search hot list"""
        body = await request.json()
        return await proxy_request("douyin", "/api/v1/douyin/billboard/fetch_hot_total_search_list", json_body=body)

@router.post("/fetch_hot_total_high_search_list")
async def fetch_hot_total_high_search_list(
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取热度飙升的搜索榜/Fetch search list with rising popularity"""
        body = await request.json()
        return await proxy_request("douyin", "/api/v1/douyin/billboard/fetch_hot_total_high_search_list", json_body=body)

@router.post("/fetch_hot_total_hot_word_list")
async def fetch_hot_total_hot_word_list(
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取全部热门内容词/Fetch all hot content words"""
        body = await request.json()
        return await proxy_request("douyin", "/api/v1/douyin/billboard/fetch_hot_total_hot_word_list", json_body=body)

@router.get("/fetch_hot_total_hot_word_detail_list")
async def fetch_hot_total_hot_word_detail_list(
    query_day: int,
    word_id: str,
    keyword: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取内容词详情/Fetch content word details"""
        params: dict[str, Any] = {}
        if keyword is not None:
            params["keyword"] = keyword
        if word_id is not None:
            params["word_id"] = word_id
        if query_day is not None:
            params["query_day"] = query_day
        body = await request.json()
        return await proxy_request("douyin", "/api/v1/douyin/billboard/fetch_hot_total_hot_word_detail_list", json_body=body)
