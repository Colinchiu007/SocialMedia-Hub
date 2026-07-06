"""Auto-generated routes for TikTok-Web-API."""

from __future__ import annotations

from typing import Any

from fastapi import APIRouter, Depends, Request

from socialmedia_hub.server._core import proxy_request, verify_api_key

router = APIRouter(prefix="/api/v1/tiktok/web", tags=["tiktok_web"])

@router.get("/fetch_post_detail")
async def fetch_post_detail(
    itemId: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取单个作品数据/Get single video data"""
        params: dict[str, Any] = {}
        if itemId is not None:
            params["itemId"] = itemId
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/web/fetch_post_detail", json_body=body)

@router.get("/fetch_post_detail_v2")
async def fetch_post_detail_v2(
    itemId: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取单个作品数据 V2/Get single video data V2"""
        params: dict[str, Any] = {}
        if itemId is not None:
            params["itemId"] = itemId
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/web/fetch_post_detail_v2", json_body=body)

@router.get("/fetch_explore_post")
async def fetch_explore_post(
    count: int | None = None,
    categoryType: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取探索作品数据/Get explore video data"""
        params: dict[str, Any] = {}
        if categoryType is not None:
            params["categoryType"] = categoryType
        if count is not None:
            params["count"] = count
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/web/fetch_explore_post", json_body=body)

@router.get("/fetch_trending_post")
async def fetch_trending_post(
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取每日热门内容作品数据/Get daily trending video data"""
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/web/fetch_trending_post", json_body=body)

@router.get("/fetch_trending_searchwords")
async def fetch_trending_searchwords(
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取每日趋势搜索关键词/Get daily trending search words"""
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/web/fetch_trending_searchwords", json_body=body)

@router.get("/fetch_user_profile")
async def fetch_user_profile(
    secUid: str | None = None,
    uniqueId: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户的个人信息/Get user profile"""
        params: dict[str, Any] = {}
        if uniqueId is not None:
            params["uniqueId"] = uniqueId
        if secUid is not None:
            params["secUid"] = secUid
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/web/fetch_user_profile", json_body=body)

@router.get("/fetch_user_post")
async def fetch_user_post(
    post_item_list_request_type: int | None = None,
    coverFormat: int | None = None,
    count: int | None = None,
    cursor: int | None = None,
    secUid: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户的作品列表/Get user posts"""
        params: dict[str, Any] = {}
        if secUid is not None:
            params["secUid"] = secUid
        if cursor is not None:
            params["cursor"] = cursor
        if count is not None:
            params["count"] = count
        if coverFormat is not None:
            params["coverFormat"] = coverFormat
        if post_item_list_request_type is not None:
            params["post_item_list_request_type"] = post_item_list_request_type
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/web/fetch_user_post", json_body=body)

@router.get("/fetch_user_repost")
async def fetch_user_repost(
    coverFormat: int | None = None,
    count: int | None = None,
    cursor: int | None = None,
    secUid: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户的转发作品列表/Get user reposts"""
        params: dict[str, Any] = {}
        if secUid is not None:
            params["secUid"] = secUid
        if cursor is not None:
            params["cursor"] = cursor
        if count is not None:
            params["count"] = count
        if coverFormat is not None:
            params["coverFormat"] = coverFormat
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/web/fetch_user_repost", json_body=body)

@router.get("/fetch_user_like")
async def fetch_user_like(
    post_item_list_request_type: int | None = None,
    coverFormat: int | None = None,
    count: int | None = None,
    cursor: int | None = None,
    secUid: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户的点赞列表/Get user likes"""
        params: dict[str, Any] = {}
        if secUid is not None:
            params["secUid"] = secUid
        if cursor is not None:
            params["cursor"] = cursor
        if count is not None:
            params["count"] = count
        if coverFormat is not None:
            params["coverFormat"] = coverFormat
        if post_item_list_request_type is not None:
            params["post_item_list_request_type"] = post_item_list_request_type
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/web/fetch_user_like", json_body=body)

@router.get("/fetch_user_collect")
async def fetch_user_collect(
    coverFormat: int | None = None,
    count: int | None = None,
    cursor: int | None = None,
    secUid: str,
    cookie: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户的收藏列表/Get user favorites"""
        params: dict[str, Any] = {}
        if cookie is not None:
            params["cookie"] = cookie
        if secUid is not None:
            params["secUid"] = secUid
        if cursor is not None:
            params["cursor"] = cursor
        if count is not None:
            params["count"] = count
        if coverFormat is not None:
            params["coverFormat"] = coverFormat
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/web/fetch_user_collect", json_body=body)

@router.get("/fetch_user_play_list")
async def fetch_user_play_list(
    count: int | None = None,
    cursor: int | None = None,
    secUid: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户的播放列表/Get user play list"""
        params: dict[str, Any] = {}
        if secUid is not None:
            params["secUid"] = secUid
        if cursor is not None:
            params["cursor"] = cursor
        if count is not None:
            params["count"] = count
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/web/fetch_user_play_list", json_body=body)

@router.get("/fetch_user_mix")
async def fetch_user_mix(
    count: int | None = None,
    cursor: int | None = None,
    mixId: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户的合辑列表/Get user mix list"""
        params: dict[str, Any] = {}
        if mixId is not None:
            params["mixId"] = mixId
        if cursor is not None:
            params["cursor"] = cursor
        if count is not None:
            params["count"] = count
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/web/fetch_user_mix", json_body=body)

@router.get("/fetch_post_comment")
async def fetch_post_comment(
    current_region: str | None = None,
    count: int | None = None,
    cursor: int | None = None,
    aweme_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取作品的评论列表/Get video comments"""
        params: dict[str, Any] = {}
        if aweme_id is not None:
            params["aweme_id"] = aweme_id
        if cursor is not None:
            params["cursor"] = cursor
        if count is not None:
            params["count"] = count
        if current_region is not None:
            params["current_region"] = current_region
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/web/fetch_post_comment", json_body=body)

@router.get("/fetch_post_comment_reply")
async def fetch_post_comment_reply(
    current_region: str | None = None,
    count: int | None = None,
    cursor: int | None = None,
    comment_id: str,
    item_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取作品的评论回复列表/Get video comment replies"""
        params: dict[str, Any] = {}
        if item_id is not None:
            params["item_id"] = item_id
        if comment_id is not None:
            params["comment_id"] = comment_id
        if cursor is not None:
            params["cursor"] = cursor
        if count is not None:
            params["count"] = count
        if current_region is not None:
            params["current_region"] = current_region
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/web/fetch_post_comment_reply", json_body=body)

@router.get("/fetch_user_fans")
async def fetch_user_fans(
    minCursor: int | None = None,
    maxCursor: int | None = None,
    count: int | None = None,
    secUid: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户的粉丝列表/Get user followers"""
        params: dict[str, Any] = {}
        if secUid is not None:
            params["secUid"] = secUid
        if count is not None:
            params["count"] = count
        if maxCursor is not None:
            params["maxCursor"] = maxCursor
        if minCursor is not None:
            params["minCursor"] = minCursor
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/web/fetch_user_fans", json_body=body)

@router.get("/fetch_user_follow")
async def fetch_user_follow(
    minCursor: int | None = None,
    maxCursor: int | None = None,
    count: int | None = None,
    secUid: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户的关注列表/Get user followings"""
        params: dict[str, Any] = {}
        if secUid is not None:
            params["secUid"] = secUid
        if count is not None:
            params["count"] = count
        if maxCursor is not None:
            params["maxCursor"] = maxCursor
        if minCursor is not None:
            params["minCursor"] = minCursor
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/web/fetch_user_follow", json_body=body)

@router.get("/fetch_user_live_detail")
async def fetch_user_live_detail(
    uniqueId: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户的直播详情/Get user live details"""
        params: dict[str, Any] = {}
        if uniqueId is not None:
            params["uniqueId"] = uniqueId
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/web/fetch_user_live_detail", json_body=body)

@router.get("/fetch_general_search")
async def fetch_general_search(
    cookie: str | None = None,
    search_id: str | None = None,
    offset: int | None = None,
    keyword: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取综合搜索列表/Get general search list"""
        params: dict[str, Any] = {}
        if keyword is not None:
            params["keyword"] = keyword
        if offset is not None:
            params["offset"] = offset
        if search_id is not None:
            params["search_id"] = search_id
        if cookie is not None:
            params["cookie"] = cookie
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/web/fetch_general_search", json_body=body)

@router.get("/fetch_search_keyword_suggest")
async def fetch_search_keyword_suggest(
    keyword: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """搜索关键字推荐/Search keyword suggest"""
        params: dict[str, Any] = {}
        if keyword is not None:
            params["keyword"] = keyword
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/web/fetch_search_keyword_suggest", json_body=body)

@router.get("/fetch_search_user")
async def fetch_search_user(
    cookie: str | None = None,
    search_id: str | None = None,
    cursor: int | None = None,
    keyword: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """搜索用户/Search user"""
        params: dict[str, Any] = {}
        if keyword is not None:
            params["keyword"] = keyword
        if cursor is not None:
            params["cursor"] = cursor
        if search_id is not None:
            params["search_id"] = search_id
        if cookie is not None:
            params["cookie"] = cookie
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/web/fetch_search_user", json_body=body)

@router.get("/fetch_search_video")
async def fetch_search_video(
    cookie: str | None = None,
    search_id: str | None = None,
    offset: int | None = None,
    count: int | None = None,
    keyword: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """搜索视频/Search video"""
        params: dict[str, Any] = {}
        if keyword is not None:
            params["keyword"] = keyword
        if count is not None:
            params["count"] = count
        if offset is not None:
            params["offset"] = offset
        if search_id is not None:
            params["search_id"] = search_id
        if cookie is not None:
            params["cookie"] = cookie
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/web/fetch_search_video", json_body=body)

@router.get("/fetch_search_live")
async def fetch_search_live(
    cookie: str | None = None,
    search_id: str | None = None,
    offset: int | None = None,
    count: int | None = None,
    keyword: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """搜索直播/Search live"""
        params: dict[str, Any] = {}
        if keyword is not None:
            params["keyword"] = keyword
        if count is not None:
            params["count"] = count
        if offset is not None:
            params["offset"] = offset
        if search_id is not None:
            params["search_id"] = search_id
        if cookie is not None:
            params["cookie"] = cookie
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/web/fetch_search_live", json_body=body)

@router.get("/fetch_search_photo")
async def fetch_search_photo(
    cookie: str | None = None,
    search_id: str | None = None,
    offset: int | None = None,
    count: int | None = None,
    keyword: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """搜索照片/Search photo"""
        params: dict[str, Any] = {}
        if keyword is not None:
            params["keyword"] = keyword
        if count is not None:
            params["count"] = count
        if offset is not None:
            params["offset"] = offset
        if search_id is not None:
            params["search_id"] = search_id
        if cookie is not None:
            params["cookie"] = cookie
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/web/fetch_search_photo", json_body=body)

@router.get("/fetch_tag_detail")
async def fetch_tag_detail(
    tag_name: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """Tag详情/Tag Detail"""
        params: dict[str, Any] = {}
        if tag_name is not None:
            params["tag_name"] = tag_name
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/web/fetch_tag_detail", json_body=body)

@router.get("/fetch_tag_post")
async def fetch_tag_post(
    cursor: int | None = None,
    count: int | None = None,
    challengeID: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """Tag作品/Tag Post"""
        params: dict[str, Any] = {}
        if challengeID is not None:
            params["challengeID"] = challengeID
        if count is not None:
            params["count"] = count
        if cursor is not None:
            params["cursor"] = cursor
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/web/fetch_tag_post", json_body=body)

@router.post("/fetch_home_feed")
async def fetch_home_feed(
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """首页推荐作品/Home Feed"""
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/web/fetch_home_feed", json_body=body)

@router.get("/generate_real_msToken")
async def generate_real_msToken(
    browser_type: str | None = None,
    random_strData: bool | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """生成真实msToken/Generate real msToken"""
        params: dict[str, Any] = {}
        if random_strData is not None:
            params["random_strData"] = random_strData
        if browser_type is not None:
            params["browser_type"] = browser_type
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/web/generate_real_msToken", json_body=body)

@router.get("/encrypt_strData")
async def encrypt_strData(
    data: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """加密strData/Encrypt strData"""
        params: dict[str, Any] = {}
        if data is not None:
            params["data"] = data
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/web/encrypt_strData", json_body=body)

@router.get("/decrypt_strData")
async def decrypt_strData(
    encrypted_data: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """解密strData/Decrypt strData"""
        params: dict[str, Any] = {}
        if encrypted_data is not None:
            params["encrypted_data"] = encrypted_data
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/web/decrypt_strData", json_body=body)

@router.get("/generate_fingerprint")
async def generate_fingerprint(
    browser_type: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """生成浏览器指纹/Generate browser fingerprint"""
        params: dict[str, Any] = {}
        if browser_type is not None:
            params["browser_type"] = browser_type
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/web/generate_fingerprint", json_body=body)

@router.get("/generate_webid")
async def generate_webid(
    app_id: int | None = None,
    user_unique_id: str | None = None,
    referer: str | None = None,
    url: str | None = None,
    user_agent: str | None = None,
    cookie: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """生成web_id/Generate web_id"""
        params: dict[str, Any] = {}
        if cookie is not None:
            params["cookie"] = cookie
        if user_agent is not None:
            params["user_agent"] = user_agent
        if url is not None:
            params["url"] = url
        if referer is not None:
            params["referer"] = referer
        if user_unique_id is not None:
            params["user_unique_id"] = user_unique_id
        if app_id is not None:
            params["app_id"] = app_id
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/web/generate_webid", json_body=body)

@router.get("/generate_ttwid")
async def generate_ttwid(
    user_agent: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """生成ttwid/Generate ttwid"""
        params: dict[str, Any] = {}
        if user_agent is not None:
            params["user_agent"] = user_agent
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/web/generate_ttwid", json_body=body)

@router.post("/generate_xbogus")
async def generate_xbogus(
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """生成 XBogus/Generate XBogus"""
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/web/generate_xbogus", json_body=body)

@router.post("/generate_xgnarly")
async def generate_xgnarly(
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """生成 XGnarly /Generate XGnarly"""
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/web/generate_xgnarly", json_body=body)

@router.post("/generate_xgnarly_and_xbogus")
async def generate_xgnarly_and_xbogus(
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """生成 XGnarly 和 XBogus /Generate XGnarly and XBogus"""
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/web/generate_xgnarly_and_xbogus", json_body=body)

@router.post("/generate_x_mssdk_info")
async def generate_x_mssdk_info(
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """生成 X-Mssdk-Info /Generate X-Mssdk-Info"""
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/web/generate_x_mssdk_info", json_body=body)

@router.get("/get_user_id")
async def get_user_id(
    url: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """提取用户user_id/Extract user user_id"""
        params: dict[str, Any] = {}
        if url is not None:
            params["url"] = url
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/web/get_user_id", json_body=body)

@router.get("/get_sec_user_id")
async def get_sec_user_id(
    url: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """提取用户sec_user_id/Extract user sec_user_id"""
        params: dict[str, Any] = {}
        if url is not None:
            params["url"] = url
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/web/get_sec_user_id", json_body=body)

@router.post("/get_all_sec_user_id")
async def get_all_sec_user_id(
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """提取列表用户sec_user_id/Extract list user sec_user_id"""
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/web/get_all_sec_user_id", json_body=body)

@router.get("/get_aweme_id")
async def get_aweme_id(
    url: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """提取单个作品id/Extract single video id"""
        params: dict[str, Any] = {}
        if url is not None:
            params["url"] = url
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/web/get_aweme_id", json_body=body)

@router.post("/get_all_aweme_id")
async def get_all_aweme_id(
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """提取列表作品id/Extract list video id"""
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/web/get_all_aweme_id", json_body=body)

@router.get("/get_unique_id")
async def get_unique_id(
    url: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户unique_id/Get user unique_id"""
        params: dict[str, Any] = {}
        if url is not None:
            params["url"] = url
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/web/get_unique_id", json_body=body)

@router.post("/get_all_unique_id")
async def get_all_unique_id(
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取列表unique_id/Get list unique_id"""
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/web/get_all_unique_id", json_body=body)

@router.get("/tiktok_live_room")
async def tiktok_live_room(
    danmaku_type: str,
    live_room_url: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """提取直播间弹幕/Extract live room danmaku"""
        params: dict[str, Any] = {}
        if live_room_url is not None:
            params["live_room_url"] = live_room_url
        if danmaku_type is not None:
            params["danmaku_type"] = danmaku_type
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/web/tiktok_live_room", json_body=body)

@router.get("/fetch_live_im_fetch")
async def fetch_live_im_fetch(
    user_unique_id: str,
    room_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """TikTok直播间弹幕参数获取/tiktok live room danmaku parameters"""
        params: dict[str, Any] = {}
        if room_id is not None:
            params["room_id"] = room_id
        if user_unique_id is not None:
            params["user_unique_id"] = user_unique_id
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/web/fetch_live_im_fetch", json_body=body)

@router.get("/get_live_room_id")
async def get_live_room_id(
    live_room_url: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """根据直播间链接提取直播间ID/Extract live room ID from live room link"""
        params: dict[str, Any] = {}
        if live_room_url is not None:
            params["live_room_url"] = live_room_url
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/web/get_live_room_id", json_body=body)

@router.get("/fetch_check_live_alive")
async def fetch_check_live_alive(
    room_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """直播间开播状态检测/Live room start status check"""
        params: dict[str, Any] = {}
        if room_id is not None:
            params["room_id"] = room_id
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/web/fetch_check_live_alive", json_body=body)

@router.get("/fetch_batch_check_live_alive")
async def fetch_batch_check_live_alive(
    room_ids: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """批量直播间开播状态检测/Batch live room start status check"""
        params: dict[str, Any] = {}
        if room_ids is not None:
            params["room_ids"] = room_ids
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/web/fetch_batch_check_live_alive", json_body=body)

@router.get("/fetch_tiktok_live_data")
async def fetch_tiktok_live_data(
    live_room_url: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """通过直播链接获取直播间信息/Get live room information via live link"""
        params: dict[str, Any] = {}
        if live_room_url is not None:
            params["live_room_url"] = live_room_url
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/web/fetch_tiktok_live_data", json_body=body)

@router.get("/fetch_live_recommend")
async def fetch_live_recommend(
    related_live_tag: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取直播间首页推荐列表/Get live room homepage recommendation list"""
        params: dict[str, Any] = {}
        if related_live_tag is not None:
            params["related_live_tag"] = related_live_tag
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/web/fetch_live_recommend", json_body=body)

@router.get("/fetch_live_gift_list")
async def fetch_live_gift_list(
    room_id: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取直播间礼物列表/Get live room gift list"""
        params: dict[str, Any] = {}
        if room_id is not None:
            params["room_id"] = room_id
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/web/fetch_live_gift_list", json_body=body)

@router.get("/fetch_sso_login_qrcode")
async def fetch_sso_login_qrcode(
    proxy: str,
    region: str,
    device_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取SSO登录二维码/Get SSO login QR code"""
        params: dict[str, Any] = {}
        if device_id is not None:
            params["device_id"] = device_id
        if region is not None:
            params["region"] = region
        if proxy is not None:
            params["proxy"] = proxy
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/web/fetch_sso_login_qrcode", json_body=body)

@router.get("/fetch_sso_login_status")
async def fetch_sso_login_status(
    proxy: str,
    region: str,
    verifyFp: str,
    device_id: str,
    token: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取SSO登录状态/Get SSO login status"""
        params: dict[str, Any] = {}
        if token is not None:
            params["token"] = token
        if device_id is not None:
            params["device_id"] = device_id
        if verifyFp is not None:
            params["verifyFp"] = verifyFp
        if region is not None:
            params["region"] = region
        if proxy is not None:
            params["proxy"] = proxy
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/web/fetch_sso_login_status", json_body=body)

@router.get("/fetch_sso_login_auth")
async def fetch_sso_login_auth(
    proxy: str,
    region: str,
    verifyFp: str,
    device_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """认证SSO登录/Authenticate SSO login"""
        params: dict[str, Any] = {}
        if device_id is not None:
            params["device_id"] = device_id
        if verifyFp is not None:
            params["verifyFp"] = verifyFp
        if region is not None:
            params["region"] = region
        if proxy is not None:
            params["proxy"] = proxy
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/web/fetch_sso_login_auth", json_body=body)

@router.get("/generate_hashed_id")
async def generate_hashed_id(
    email: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """生成哈希ID/Generate hashed ID"""
        params: dict[str, Any] = {}
        if email is not None:
            params["email"] = email
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/web/generate_hashed_id", json_body=body)

@router.post("/fetch_gift_name_by_id")
async def fetch_gift_name_by_id(
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """根据Gift ID查询礼物名称/Get gift name by gift ID"""
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/web/fetch_gift_name_by_id", json_body=body)

@router.post("/fetch_gift_names_by_ids")
async def fetch_gift_names_by_ids(
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """批量查询Gift ID对应的礼物名称($0.025/次,建议50个)/Batch get gift names by gift IDs ($0.025/call, suggest 50)"""
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/web/fetch_gift_names_by_ids", json_body=body)

@router.get("/fetch_tiktok_web_guest_cookie")
async def fetch_tiktok_web_guest_cookie(
    user_agent: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取游客 Cookie/Get the guest Cookie"""
        params: dict[str, Any] = {}
        if user_agent is not None:
            params["user_agent"] = user_agent
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/web/fetch_tiktok_web_guest_cookie", json_body=body)

@router.get("/device_register")
async def device_register(
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """设备注册/Register device for TikTok Web"""
        body = await request.json()
        return await proxy_request("tiktok", "/api/v1/tiktok/web/device_register", json_body=body)
