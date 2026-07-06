"""Auto-generated routes for Douyin-Web-API."""

from __future__ import annotations

from typing import Any

from fastapi import APIRouter, Depends, Request

from socialmedia_hub.server._core import proxy_request, verify_api_key

router = APIRouter(prefix="/api/v1/douyin/web", tags=["douyin_web"])

@router.get("/fetch_one_video")
async def fetch_one_video(
    aweme_id: str,
    request: Request,
    need_anchor_info: bool | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取单个作品数据/Get single video data"""
    params: dict[str, Any] = {}
    if aweme_id is not None:
        params["aweme_id"] = aweme_id
    if need_anchor_info is not None:
        params["need_anchor_info"] = need_anchor_info
    return await proxy_request("douyin", "/api/v1/douyin/web/fetch_one_video", params=params)

@router.get("/fetch_one_video_v2")
async def fetch_one_video_v2(
    aweme_id: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取单个作品数据 V2/Get single video data V2"""
    params: dict[str, Any] = {}
    if aweme_id is not None:
        params["aweme_id"] = aweme_id
    return await proxy_request("douyin", "/api/v1/douyin/web/fetch_one_video_v2", params=params)

@router.get("/fetch_one_video_by_share_url")
async def fetch_one_video_by_share_url(
    share_url: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """根据分享链接获取单个作品数据/Get single video data by sharing link"""
    params: dict[str, Any] = {}
    if share_url is not None:
        params["share_url"] = share_url
    return await proxy_request("douyin", "/api/v1/douyin/web/fetch_one_video_by_share_url", params=params)

@router.get("/fetch_video_high_quality_play_url")
async def fetch_video_high_quality_play_url(
    request: Request,
    aweme_id: str | None = None,
    share_url: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取视频的最高画质播放链接/Get the highest quality play URL of the video"""
    params: dict[str, Any] = {}
    if aweme_id is not None:
        params["aweme_id"] = aweme_id
    if share_url is not None:
        params["share_url"] = share_url
    return await proxy_request("douyin", "/api/v1/douyin/web/fetch_video_high_quality_play_url", params=params)

@router.post("/fetch_multi_video_high_quality_play_url")
async def fetch_multi_video_high_quality_play_url(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """批量获取视频的最高画质播放链接/Batch get the highest quality play URL of videos"""
    body = await request.json()
    return await proxy_request("douyin", "/api/v1/douyin/web/fetch_multi_video_high_quality_play_url", json_body=body)

@router.post("/fetch_multi_video")
async def fetch_multi_video(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """批量获取视频信息/Batch Get Video Information"""
    body = await request.json()
    return await proxy_request("douyin", "/api/v1/douyin/web/fetch_multi_video", json_body=body)

@router.get("/fetch_one_video_danmaku")
async def fetch_one_video_danmaku(
    item_id: str,
    duration: int,
    end_time: int,
    start_time: int,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取单个作品视频弹幕数据/Get single video danmaku data"""
    params: dict[str, Any] = {}
    if item_id is not None:
        params["item_id"] = item_id
    if duration is not None:
        params["duration"] = duration
    if end_time is not None:
        params["end_time"] = end_time
    if start_time is not None:
        params["start_time"] = start_time
    return await proxy_request("douyin", "/api/v1/douyin/web/fetch_one_video_danmaku", params=params)

@router.get("/fetch_home_feed")
async def fetch_home_feed(
    request: Request,
    count: int | None = None,
    refresh_index: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取首页推荐数据/Get home feed data"""
    params: dict[str, Any] = {}
    if count is not None:
        params["count"] = count
    if refresh_index is not None:
        params["refresh_index"] = refresh_index
    return await proxy_request("douyin", "/api/v1/douyin/web/fetch_home_feed", params=params)

@router.get("/fetch_related_posts")
async def fetch_related_posts(
    aweme_id: str,
    request: Request,
    refresh_index: int | None = None,
    count: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取相关作品推荐数据/Get related posts recommendation data"""
    params: dict[str, Any] = {}
    if aweme_id is not None:
        params["aweme_id"] = aweme_id
    if refresh_index is not None:
        params["refresh_index"] = refresh_index
    if count is not None:
        params["count"] = count
    return await proxy_request("douyin", "/api/v1/douyin/web/fetch_related_posts", params=params)

@router.get("/fetch_user_post_videos")
async def fetch_user_post_videos(
    sec_user_id: str,
    request: Request,
    max_cursor: str | None = None,
    count: int | None = None,
    filter_type: str | None = None,
    cookie: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户主页作品数据/Get user homepage video data"""
    params: dict[str, Any] = {}
    if sec_user_id is not None:
        params["sec_user_id"] = sec_user_id
    if max_cursor is not None:
        params["max_cursor"] = max_cursor
    if count is not None:
        params["count"] = count
    if filter_type is not None:
        params["filter_type"] = filter_type
    if cookie is not None:
        params["cookie"] = cookie
    return await proxy_request("douyin", "/api/v1/douyin/web/fetch_user_post_videos", params=params)

@router.post("/fetch_user_like_videos")
async def fetch_user_like_videos(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户喜欢作品数据/Get user like video data"""
    body = await request.json()
    return await proxy_request("douyin", "/api/v1/douyin/web/fetch_user_like_videos", json_body=body)

@router.post("/fetch_user_collection_videos")
async def fetch_user_collection_videos(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户收藏作品数据/Get user collection video data"""
    body = await request.json()
    return await proxy_request("douyin", "/api/v1/douyin/web/fetch_user_collection_videos", json_body=body)

@router.post("/fetch_user_collects")
async def fetch_user_collects(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户收藏夹/Get user collection"""
    body = await request.json()
    return await proxy_request("douyin", "/api/v1/douyin/web/fetch_user_collects", json_body=body)

@router.get("/fetch_user_collects_videos")
async def fetch_user_collects_videos(
    collects_id: str,
    request: Request,
    max_cursor: int | None = None,
    counts: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户收藏夹数据/Get user collection data"""
    params: dict[str, Any] = {}
    if collects_id is not None:
        params["collects_id"] = collects_id
    if max_cursor is not None:
        params["max_cursor"] = max_cursor
    if counts is not None:
        params["counts"] = counts
    return await proxy_request("douyin", "/api/v1/douyin/web/fetch_user_collects_videos", params=params)

@router.get("/fetch_user_mix_videos")
async def fetch_user_mix_videos(
    mix_id: str,
    request: Request,
    max_cursor: int | None = None,
    counts: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户合辑作品数据/Get user mix video data"""
    params: dict[str, Any] = {}
    if mix_id is not None:
        params["mix_id"] = mix_id
    if max_cursor is not None:
        params["max_cursor"] = max_cursor
    if counts is not None:
        params["counts"] = counts
    return await proxy_request("douyin", "/api/v1/douyin/web/fetch_user_mix_videos", params=params)

@router.get("/fetch_user_live_videos")
async def fetch_user_live_videos(
    webcast_id: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户直播流数据/Get user live video data"""
    params: dict[str, Any] = {}
    if webcast_id is not None:
        params["webcast_id"] = webcast_id
    return await proxy_request("douyin", "/api/v1/douyin/web/fetch_user_live_videos", params=params)

@router.get("/fetch_user_live_videos_by_sec_uid")
async def fetch_user_live_videos_by_sec_uid(
    sec_uid: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """通过sec_uid获取指定用户的直播流数据/Get live video data of specified user by sec_uid"""
    params: dict[str, Any] = {}
    if sec_uid is not None:
        params["sec_uid"] = sec_uid
    return await proxy_request("douyin", "/api/v1/douyin/web/fetch_user_live_videos_by_sec_uid", params=params)

@router.get("/fetch_user_live_videos_by_room_id")
async def fetch_user_live_videos_by_room_id(
    room_id: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """通过room_id获取指定用户的直播流数据 V1/Get live video data of specified user by room_id V1"""
    params: dict[str, Any] = {}
    if room_id is not None:
        params["room_id"] = room_id
    return await proxy_request("douyin", "/api/v1/douyin/web/fetch_user_live_videos_by_room_id", params=params)

@router.get("/fetch_user_live_videos_by_room_id_v2")
async def fetch_user_live_videos_by_room_id_v2(
    room_id: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """通过room_id获取指定用户的直播流数据 V2/Gets the live stream data of the specified user by room_id V2"""
    params: dict[str, Any] = {}
    if room_id is not None:
        params["room_id"] = room_id
    return await proxy_request("douyin", "/api/v1/douyin/web/fetch_user_live_videos_by_room_id_v2", params=params)

@router.get("/fetch_live_gift_ranking")
async def fetch_live_gift_ranking(
    room_id: str,
    request: Request,
    rank_type: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取直播间送礼用户排行榜/Get live room gift user ranking"""
    params: dict[str, Any] = {}
    if room_id is not None:
        params["room_id"] = room_id
    if rank_type is not None:
        params["rank_type"] = rank_type
    return await proxy_request("douyin", "/api/v1/douyin/web/fetch_live_gift_ranking", params=params)

@router.get("/fetch_live_room_product_result")
async def fetch_live_room_product_result(
    room_id: str,
    author_id: str,
    request: Request,
    offset: int | None = None,
    limit: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """抖音直播间商品信息/Douyin live room product information"""
    params: dict[str, Any] = {}
    if room_id is not None:
        params["room_id"] = room_id
    if author_id is not None:
        params["author_id"] = author_id
    if offset is not None:
        params["offset"] = offset
    if limit is not None:
        params["limit"] = limit
    return await proxy_request("douyin", "/api/v1/douyin/web/fetch_live_room_product_result", params=params)

@router.get("/fetch_product_detail")
async def fetch_product_detail(
    product_id: str,
    request: Request,
    aweme_id: str | None = None,
    room_id: str | None = None,
    sec_user_id: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取商品详情/Get product detail"""
    params: dict[str, Any] = {}
    if product_id is not None:
        params["product_id"] = product_id
    if aweme_id is not None:
        params["aweme_id"] = aweme_id
    if room_id is not None:
        params["room_id"] = room_id
    if sec_user_id is not None:
        params["sec_user_id"] = sec_user_id
    return await proxy_request("douyin", "/api/v1/douyin/web/fetch_product_detail", params=params)

@router.get("/fetch_product_sku_list")
async def fetch_product_sku_list(
    product_id: str,
    author_id: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取商品SKU列表/Get product SKU list"""
    params: dict[str, Any] = {}
    if product_id is not None:
        params["product_id"] = product_id
    if author_id is not None:
        params["author_id"] = author_id
    return await proxy_request("douyin", "/api/v1/douyin/web/fetch_product_sku_list", params=params)

@router.get("/fetch_product_coupon")
async def fetch_product_coupon(
    product_id: str,
    shop_id: str,
    price: str,
    author_id: str,
    sec_user_id: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取商品优惠券信息/Get product coupon information"""
    params: dict[str, Any] = {}
    if product_id is not None:
        params["product_id"] = product_id
    if shop_id is not None:
        params["shop_id"] = shop_id
    if price is not None:
        params["price"] = price
    if author_id is not None:
        params["author_id"] = author_id
    if sec_user_id is not None:
        params["sec_user_id"] = sec_user_id
    return await proxy_request("douyin", "/api/v1/douyin/web/fetch_product_coupon", params=params)

@router.get("/fetch_product_review_score")
async def fetch_product_review_score(
    product_id: str,
    shop_id: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取商品评价评分/Get product review score"""
    params: dict[str, Any] = {}
    if product_id is not None:
        params["product_id"] = product_id
    if shop_id is not None:
        params["shop_id"] = shop_id
    return await proxy_request("douyin", "/api/v1/douyin/web/fetch_product_review_score", params=params)

@router.get("/fetch_product_review_list")
async def fetch_product_review_list(
    product_id: str,
    shop_id: str,
    request: Request,
    cursor: int | None = None,
    count: int | None = None,
    sort_type: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取商品评价列表/Get product review list"""
    params: dict[str, Any] = {}
    if product_id is not None:
        params["product_id"] = product_id
    if shop_id is not None:
        params["shop_id"] = shop_id
    if cursor is not None:
        params["cursor"] = cursor
    if count is not None:
        params["count"] = count
    if sort_type is not None:
        params["sort_type"] = sort_type
    return await proxy_request("douyin", "/api/v1/douyin/web/fetch_product_review_list", params=params)

@router.get("/fetch_user_profile_by_uid")
async def fetch_user_profile_by_uid(
    uid: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """使用UID获取用户信息/Get user information by UID"""
    params: dict[str, Any] = {}
    if uid is not None:
        params["uid"] = uid
    return await proxy_request("douyin", "/api/v1/douyin/web/fetch_user_profile_by_uid", params=params)

@router.get("/fetch_batch_user_profile_v1")
async def fetch_batch_user_profile_v1(
    sec_user_ids: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取批量用户信息(最多10个)/Get batch user profile (up to 10)"""
    params: dict[str, Any] = {}
    if sec_user_ids is not None:
        params["sec_user_ids"] = sec_user_ids
    return await proxy_request("douyin", "/api/v1/douyin/web/fetch_batch_user_profile_v1", params=params)

@router.get("/fetch_batch_user_profile_v2")
async def fetch_batch_user_profile_v2(
    sec_user_ids: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取批量用户信息(最多50个)/Get batch user profile (up to 50)"""
    params: dict[str, Any] = {}
    if sec_user_ids is not None:
        params["sec_user_ids"] = sec_user_ids
    return await proxy_request("douyin", "/api/v1/douyin/web/fetch_batch_user_profile_v2", params=params)

@router.get("/fetch_user_live_info_by_uid")
async def fetch_user_live_info_by_uid(
    uid: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """使用UID获取用户开播信息/Get user live information by UID"""
    params: dict[str, Any] = {}
    if uid is not None:
        params["uid"] = uid
    return await proxy_request("douyin", "/api/v1/douyin/web/fetch_user_live_info_by_uid", params=params)

@router.get("/fetch_user_profile_by_short_id")
async def fetch_user_profile_by_short_id(
    short_id: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """使用Short ID获取用户信息/Get user information by Short ID"""
    params: dict[str, Any] = {}
    if short_id is not None:
        params["short_id"] = short_id
    return await proxy_request("douyin", "/api/v1/douyin/web/fetch_user_profile_by_short_id", params=params)

@router.get("/handler_shorten_url")
async def handler_shorten_url(
    target_url: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """生成短链接"""
    params: dict[str, Any] = {}
    if target_url is not None:
        params["target_url"] = target_url
    return await proxy_request("douyin", "/api/v1/douyin/web/handler_shorten_url", params=params)

@router.get("/handler_user_profile")
async def handler_user_profile(
    sec_user_id: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """使用sec_user_id获取指定用户的信息/Get information of specified user by sec_user_id"""
    params: dict[str, Any] = {}
    if sec_user_id is not None:
        params["sec_user_id"] = sec_user_id
    return await proxy_request("douyin", "/api/v1/douyin/web/handler_user_profile", params=params)

@router.get("/handler_user_profile_v2")
async def handler_user_profile_v2(
    unique_id: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """使用unique_id（抖音号）获取指定用户的信息/Get information of specified user by unique_id"""
    params: dict[str, Any] = {}
    if unique_id is not None:
        params["unique_id"] = unique_id
    return await proxy_request("douyin", "/api/v1/douyin/web/handler_user_profile_v2", params=params)

@router.get("/encrypt_uid_to_sec_user_id")
async def encrypt_uid_to_sec_user_id(
    uid: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """加密用户uid到sec_user_id/Encrypt user uid to sec_user_id"""
    params: dict[str, Any] = {}
    if uid is not None:
        params["uid"] = uid
    return await proxy_request("douyin", "/api/v1/douyin/web/encrypt_uid_to_sec_user_id", params=params)

@router.get("/handler_user_profile_v3")
async def handler_user_profile_v3(
    uid: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """根据抖音uid获取指定用户的信息/Get information of specified user by uid"""
    params: dict[str, Any] = {}
    if uid is not None:
        params["uid"] = uid
    return await proxy_request("douyin", "/api/v1/douyin/web/handler_user_profile_v3", params=params)

@router.get("/handler_user_profile_v4")
async def handler_user_profile_v4(
    sec_user_id: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """根据sec_user_id获取指定用户的信息（性别，年龄，直播等级、牌子）/Get information of specified user by sec_user_id (gender, age, live level、brand)"""
    params: dict[str, Any] = {}
    if sec_user_id is not None:
        params["sec_user_id"] = sec_user_id
    return await proxy_request("douyin", "/api/v1/douyin/web/handler_user_profile_v4", params=params)

@router.get("/fetch_user_fans_list")
async def fetch_user_fans_list(
    request: Request,
    sec_user_id: str | None = None,
    max_time: str | None = None,
    count: int | None = None,
    source_type: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户粉丝列表/Get user fans list"""
    params: dict[str, Any] = {}
    if sec_user_id is not None:
        params["sec_user_id"] = sec_user_id
    if max_time is not None:
        params["max_time"] = max_time
    if count is not None:
        params["count"] = count
    if source_type is not None:
        params["source_type"] = source_type
    return await proxy_request("douyin", "/api/v1/douyin/web/fetch_user_fans_list", params=params)

@router.get("/fetch_user_following_list")
async def fetch_user_following_list(
    request: Request,
    sec_user_id: str | None = None,
    max_time: str | None = None,
    count: int | None = None,
    source_type: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户关注列表/Get user following list"""
    params: dict[str, Any] = {}
    if sec_user_id is not None:
        params["sec_user_id"] = sec_user_id
    if max_time is not None:
        params["max_time"] = max_time
    if count is not None:
        params["count"] = count
    if source_type is not None:
        params["source_type"] = source_type
    return await proxy_request("douyin", "/api/v1/douyin/web/fetch_user_following_list", params=params)

@router.get("/fetch_video_comments")
async def fetch_video_comments(
    aweme_id: str,
    request: Request,
    cursor: int | None = None,
    count: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取单个视频评论数据/Get single video comments data"""
    params: dict[str, Any] = {}
    if aweme_id is not None:
        params["aweme_id"] = aweme_id
    if cursor is not None:
        params["cursor"] = cursor
    if count is not None:
        params["count"] = count
    return await proxy_request("douyin", "/api/v1/douyin/web/fetch_video_comments", params=params)

@router.get("/fetch_video_comment_replies")
async def fetch_video_comment_replies(
    item_id: str,
    comment_id: str,
    request: Request,
    cursor: int | None = None,
    count: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取指定视频的评论回复数据/Get comment replies data of specified video"""
    params: dict[str, Any] = {}
    if item_id is not None:
        params["item_id"] = item_id
    if comment_id is not None:
        params["comment_id"] = comment_id
    if cursor is not None:
        params["cursor"] = cursor
    if count is not None:
        params["count"] = count
    return await proxy_request("douyin", "/api/v1/douyin/web/fetch_video_comment_replies", params=params)

@router.get("/fetch_general_search_result")
async def fetch_general_search_result(
    keyword: str,
    request: Request,
    offset: int | None = None,
    count: int | None = None,
    sort_type: str | None = None,
    publish_time: str | None = None,
    filter_duration: str | None = None,
    search_range: str | None = None,
    content_type: str | None = None,
    search_id: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """[已弃用/Deprecated] 获取指定关键词的综合搜索结果/Get comprehensive search results of specified keywords"""
    params: dict[str, Any] = {}
    if keyword is not None:
        params["keyword"] = keyword
    if offset is not None:
        params["offset"] = offset
    if count is not None:
        params["count"] = count
    if sort_type is not None:
        params["sort_type"] = sort_type
    if publish_time is not None:
        params["publish_time"] = publish_time
    if filter_duration is not None:
        params["filter_duration"] = filter_duration
    if search_range is not None:
        params["search_range"] = search_range
    if content_type is not None:
        params["content_type"] = content_type
    if search_id is not None:
        params["search_id"] = search_id
    return await proxy_request("douyin", "/api/v1/douyin/web/fetch_general_search_result", params=params)

@router.get("/fetch_video_search_result")
async def fetch_video_search_result(
    keyword: str,
    request: Request,
    offset: int | None = None,
    count: int | None = None,
    sort_type: str | None = None,
    publish_time: str | None = None,
    filter_duration: str | None = None,
    search_id: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """[已弃用/Deprecated] 获取指定关键词的视频搜索结果/Get video search results of specified keywords"""
    params: dict[str, Any] = {}
    if keyword is not None:
        params["keyword"] = keyword
    if offset is not None:
        params["offset"] = offset
    if count is not None:
        params["count"] = count
    if sort_type is not None:
        params["sort_type"] = sort_type
    if publish_time is not None:
        params["publish_time"] = publish_time
    if filter_duration is not None:
        params["filter_duration"] = filter_duration
    if search_id is not None:
        params["search_id"] = search_id
    return await proxy_request("douyin", "/api/v1/douyin/web/fetch_video_search_result", params=params)

@router.get("/fetch_video_search_result_v2")
async def fetch_video_search_result_v2(
    keyword: str,
    request: Request,
    sort_type: str | None = None,
    publish_time: str | None = None,
    filter_duration: str | None = None,
    page: int | None = None,
    search_id: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取指定关键词的视频搜索结果 V2 （废弃，替代接口请参考下方文档）/Get video search results of specified keywords V2 (Deprecated, please refer to the following document for replacement interface)"""
    params: dict[str, Any] = {}
    if keyword is not None:
        params["keyword"] = keyword
    if sort_type is not None:
        params["sort_type"] = sort_type
    if publish_time is not None:
        params["publish_time"] = publish_time
    if filter_duration is not None:
        params["filter_duration"] = filter_duration
    if page is not None:
        params["page"] = page
    if search_id is not None:
        params["search_id"] = search_id
    return await proxy_request("douyin", "/api/v1/douyin/web/fetch_video_search_result_v2", params=params)

@router.get("/fetch_user_search_result")
async def fetch_user_search_result(
    keyword: str,
    request: Request,
    offset: int | None = None,
    count: int | None = None,
    douyin_user_fans: str | None = None,
    douyin_user_type: str | None = None,
    search_id: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取指定关键词的用户搜索结果(废弃，替代接口请参考下方文档)/Get user search results of specified keywords (deprecated, please refer to the following document for replacement interface)"""
    params: dict[str, Any] = {}
    if keyword is not None:
        params["keyword"] = keyword
    if offset is not None:
        params["offset"] = offset
    if count is not None:
        params["count"] = count
    if douyin_user_fans is not None:
        params["douyin_user_fans"] = douyin_user_fans
    if douyin_user_type is not None:
        params["douyin_user_type"] = douyin_user_type
    if search_id is not None:
        params["search_id"] = search_id
    return await proxy_request("douyin", "/api/v1/douyin/web/fetch_user_search_result", params=params)

@router.get("/fetch_user_search_result_v2")
async def fetch_user_search_result_v2(
    keyword: str,
    request: Request,
    cursor: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取指定关键词的用户搜索结果 V2 (已弃用，替代接口请参考下方文档)/Get user search results of specified keywords V2 (deprecated, please refer to the following document for replacement interface)"""
    params: dict[str, Any] = {}
    if keyword is not None:
        params["keyword"] = keyword
    if cursor is not None:
        params["cursor"] = cursor
    return await proxy_request("douyin", "/api/v1/douyin/web/fetch_user_search_result_v2", params=params)

@router.get("/fetch_user_search_result_v3")
async def fetch_user_search_result_v3(
    keyword: str,
    request: Request,
    cursor: str | None = None,
    douyin_user_type: str | None = None,
    douyin_user_fans: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取指定关键词的用户搜索结果 V3 (已弃用，替代接口请参考下方文档)/Get user search results of specified keywords V3 (deprecated, please refer to the following document for replacement interface)"""
    params: dict[str, Any] = {}
    if keyword is not None:
        params["keyword"] = keyword
    if cursor is not None:
        params["cursor"] = cursor
    if douyin_user_type is not None:
        params["douyin_user_type"] = douyin_user_type
    if douyin_user_fans is not None:
        params["douyin_user_fans"] = douyin_user_fans
    return await proxy_request("douyin", "/api/v1/douyin/web/fetch_user_search_result_v3", params=params)

@router.get("/fetch_live_search_result")
async def fetch_live_search_result(
    keyword: str,
    request: Request,
    offset: int | None = None,
    count: int | None = None,
    search_id: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """[已弃用/Deprecated] 获取指定关键词的直播搜索结果/Get live search results of specified keywords"""
    params: dict[str, Any] = {}
    if keyword is not None:
        params["keyword"] = keyword
    if offset is not None:
        params["offset"] = offset
    if count is not None:
        params["count"] = count
    if search_id is not None:
        params["search_id"] = search_id
    return await proxy_request("douyin", "/api/v1/douyin/web/fetch_live_search_result", params=params)

@router.post("/fetch_search_challenge")
async def fetch_search_challenge(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """[已弃用/Deprecated] 搜索话题/Search Challenge"""
    body = await request.json()
    return await proxy_request("douyin", "/api/v1/douyin/web/fetch_search_challenge", json_body=body)

@router.post("/fetch_challenge_posts")
async def fetch_challenge_posts(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """话题作品/Challenge Posts"""
    body = await request.json()
    return await proxy_request("douyin", "/api/v1/douyin/web/fetch_challenge_posts", json_body=body)

@router.get("/fetch_hot_search_result")
async def fetch_hot_search_result(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取抖音热榜数据/Get Douyin hot search results"""
    return await proxy_request("douyin", "/api/v1/douyin/web/fetch_hot_search_result")

@router.get("/fetch_video_channel_result")
async def fetch_video_channel_result(
    tag_id: int,
    request: Request,
    count: int | None = None,
    refresh_index: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """抖音视频频道数据/Douyin video channel data"""
    params: dict[str, Any] = {}
    if tag_id is not None:
        params["tag_id"] = tag_id
    if count is not None:
        params["count"] = count
    if refresh_index is not None:
        params["refresh_index"] = refresh_index
    return await proxy_request("douyin", "/api/v1/douyin/web/fetch_video_channel_result", params=params)

@router.get("/fetch_douyin_web_guest_cookie")
async def fetch_douyin_web_guest_cookie(
    user_agent: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取抖音Web的游客Cookie/Get the guest Cookie of Douyin Web"""
    params: dict[str, Any] = {}
    if user_agent is not None:
        params["user_agent"] = user_agent
    return await proxy_request("douyin", "/api/v1/douyin/web/fetch_douyin_web_guest_cookie", params=params)

@router.get("/generate_real_msToken")
async def generate_real_msToken(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """生成真实msToken/Generate real msToken"""
    return await proxy_request("douyin", "/api/v1/douyin/web/generate_real_msToken")

@router.get("/generate_ttwid")
async def generate_ttwid(
    request: Request,
    user_agent: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """生成ttwid/Generate ttwid"""
    params: dict[str, Any] = {}
    if user_agent is not None:
        params["user_agent"] = user_agent
    return await proxy_request("douyin", "/api/v1/douyin/web/generate_ttwid", params=params)

@router.post("/fetch_query_user")
async def fetch_query_user(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """查询抖音用户基本信息/Query Douyin user basic information"""
    body = await request.json()
    return await proxy_request("douyin", "/api/v1/douyin/web/fetch_query_user", json_body=body)

@router.get("/generate_verify_fp")
async def generate_verify_fp(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """生成verify_fp/Generate verify_fp"""
    return await proxy_request("douyin", "/api/v1/douyin/web/generate_verify_fp")

@router.get("/generate_s_v_web_id")
async def generate_s_v_web_id(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """生成s_v_web_id/Generate s_v_web_id"""
    return await proxy_request("douyin", "/api/v1/douyin/web/generate_s_v_web_id")

@router.get("/generate_wss_xb_signature")
async def generate_wss_xb_signature(
    user_agent: str,
    room_id: str,
    user_unique_id: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """生成弹幕xb签名/Generate barrage xb signature"""
    params: dict[str, Any] = {}
    if user_agent is not None:
        params["user_agent"] = user_agent
    if room_id is not None:
        params["room_id"] = room_id
    if user_unique_id is not None:
        params["user_unique_id"] = user_unique_id
    return await proxy_request("douyin", "/api/v1/douyin/web/generate_wss_xb_signature", params=params)

@router.post("/generate_x_bogus")
async def generate_x_bogus(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """使用接口网址生成X-Bogus参数/Generate X-Bogus parameter using API URL"""
    body = await request.json()
    return await proxy_request("douyin", "/api/v1/douyin/web/generate_x_bogus", json_body=body)

@router.post("/generate_a_bogus")
async def generate_a_bogus(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """使用接口网址生成A-Bogus参数/Generate A-Bogus parameter using API URL"""
    body = await request.json()
    return await proxy_request("douyin", "/api/v1/douyin/web/generate_a_bogus", json_body=body)

@router.get("/get_sec_user_id")
async def get_sec_user_id(
    url: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """提取单个用户id/Extract single user id"""
    params: dict[str, Any] = {}
    if url is not None:
        params["url"] = url
    return await proxy_request("douyin", "/api/v1/douyin/web/get_sec_user_id", params=params)

@router.post("/get_all_sec_user_id")
async def get_all_sec_user_id(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """提取列表用户id/Extract list user id"""
    body = await request.json()
    return await proxy_request("douyin", "/api/v1/douyin/web/get_all_sec_user_id", json_body=body)

@router.get("/get_aweme_id")
async def get_aweme_id(
    url: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """提取单个作品id/Extract single video id"""
    params: dict[str, Any] = {}
    if url is not None:
        params["url"] = url
    return await proxy_request("douyin", "/api/v1/douyin/web/get_aweme_id", params=params)

@router.post("/get_all_aweme_id")
async def get_all_aweme_id(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """提取列表作品id/Extract list video id"""
    body = await request.json()
    return await proxy_request("douyin", "/api/v1/douyin/web/get_all_aweme_id", json_body=body)

@router.get("/get_webcast_id")
async def get_webcast_id(
    url: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """提取直播间号/Extract webcast id"""
    params: dict[str, Any] = {}
    if url is not None:
        params["url"] = url
    return await proxy_request("douyin", "/api/v1/douyin/web/get_webcast_id", params=params)

@router.post("/get_all_webcast_id")
async def get_all_webcast_id(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """提取列表直播间号/Extract list webcast id"""
    body = await request.json()
    return await proxy_request("douyin", "/api/v1/douyin/web/get_all_webcast_id", json_body=body)

@router.get("/webcast_id_2_room_id")
async def webcast_id_2_room_id(
    webcast_id: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """直播间号转房间号/Webcast id to room id"""
    params: dict[str, Any] = {}
    if webcast_id is not None:
        params["webcast_id"] = webcast_id
    return await proxy_request("douyin", "/api/v1/douyin/web/webcast_id_2_room_id", params=params)

@router.get("/douyin_live_room")
async def douyin_live_room(
    live_room_url: str,
    danmaku_type: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """提取直播间弹幕/Extract live room danmaku"""
    params: dict[str, Any] = {}
    if live_room_url is not None:
        params["live_room_url"] = live_room_url
    if danmaku_type is not None:
        params["danmaku_type"] = danmaku_type
    return await proxy_request("douyin", "/api/v1/douyin/web/douyin_live_room", params=params)

@router.get("/fetch_live_im_fetch")
async def fetch_live_im_fetch(
    room_id: str,
    user_unique_id: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """抖音直播间弹幕参数获取/Douyin live room danmaku parameters"""
    params: dict[str, Any] = {}
    if room_id is not None:
        params["room_id"] = room_id
    if user_unique_id is not None:
        params["user_unique_id"] = user_unique_id
    return await proxy_request("douyin", "/api/v1/douyin/web/fetch_live_im_fetch", params=params)

@router.get("/fetch_series_aweme")
async def fetch_series_aweme(
    offset: int,
    count: int,
    content_type: int,
    request: Request,
    cookie: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """短剧作品/Series Video"""
    params: dict[str, Any] = {}
    if offset is not None:
        params["offset"] = offset
    if count is not None:
        params["count"] = count
    if content_type is not None:
        params["content_type"] = content_type
    if cookie is not None:
        params["cookie"] = cookie
    return await proxy_request("douyin", "/api/v1/douyin/web/fetch_series_aweme", params=params)

@router.get("/fetch_knowledge_aweme")
async def fetch_knowledge_aweme(
    count: int,
    request: Request,
    refresh_index: int | None = None,
    cookie: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """知识作品推荐/Knowledge Video"""
    params: dict[str, Any] = {}
    if count is not None:
        params["count"] = count
    if refresh_index is not None:
        params["refresh_index"] = refresh_index
    if cookie is not None:
        params["cookie"] = cookie
    return await proxy_request("douyin", "/api/v1/douyin/web/fetch_knowledge_aweme", params=params)

@router.get("/fetch_game_aweme")
async def fetch_game_aweme(
    count: int,
    request: Request,
    refresh_index: int | None = None,
    cookie: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """游戏作品推荐/Game Video"""
    params: dict[str, Any] = {}
    if count is not None:
        params["count"] = count
    if refresh_index is not None:
        params["refresh_index"] = refresh_index
    if cookie is not None:
        params["cookie"] = cookie
    return await proxy_request("douyin", "/api/v1/douyin/web/fetch_game_aweme", params=params)

@router.get("/fetch_cartoon_aweme")
async def fetch_cartoon_aweme(
    count: int,
    request: Request,
    refresh_index: int | None = None,
    cookie: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """二次元作品推荐/Anime Video"""
    params: dict[str, Any] = {}
    if count is not None:
        params["count"] = count
    if refresh_index is not None:
        params["refresh_index"] = refresh_index
    if cookie is not None:
        params["cookie"] = cookie
    return await proxy_request("douyin", "/api/v1/douyin/web/fetch_cartoon_aweme", params=params)

@router.get("/fetch_music_aweme")
async def fetch_music_aweme(
    count: int,
    request: Request,
    refresh_index: int | None = None,
    cookie: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """音乐作品推荐/Music Video"""
    params: dict[str, Any] = {}
    if count is not None:
        params["count"] = count
    if refresh_index is not None:
        params["refresh_index"] = refresh_index
    if cookie is not None:
        params["cookie"] = cookie
    return await proxy_request("douyin", "/api/v1/douyin/web/fetch_music_aweme", params=params)

@router.get("/fetch_food_aweme")
async def fetch_food_aweme(
    count: int,
    request: Request,
    refresh_index: int | None = None,
    cookie: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """美食作品推荐/Food Video"""
    params: dict[str, Any] = {}
    if count is not None:
        params["count"] = count
    if refresh_index is not None:
        params["refresh_index"] = refresh_index
    if cookie is not None:
        params["cookie"] = cookie
    return await proxy_request("douyin", "/api/v1/douyin/web/fetch_food_aweme", params=params)
