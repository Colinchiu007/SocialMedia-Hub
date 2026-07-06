"""Auto-generated routes for Xiaohongshu-App-V2-API."""

from __future__ import annotations

from typing import Any

from fastapi import APIRouter, Depends, Request

from socialmedia_hub.server._core import proxy_request, verify_api_key

router = APIRouter(prefix="/api/v1/xiaohongshu/app/v2", tags=["xiaohongshu_app_v2"])

@router.get("/get_image_note_detail")
async def get_image_note_detail(
    request: Request,
    note_id: str | None = None,
    share_text: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取图文笔记详情/Get image note detail"""
    body = await request.json()
    params: dict[str, Any] = {}
    if note_id is not None:
        params["note_id"] = note_id
    if share_text is not None:
        params["share_text"] = share_text
    return await proxy_request("xiaohongshu", "/api/v1/xiaohongshu/app_v2/get_image_note_detail", params=params, json_body=body)

@router.get("/get_video_note_detail")
async def get_video_note_detail(
    request: Request,
    note_id: str | None = None,
    share_text: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取视频笔记详情/Get video note detail"""
    body = await request.json()
    params: dict[str, Any] = {}
    if note_id is not None:
        params["note_id"] = note_id
    if share_text is not None:
        params["share_text"] = share_text
    return await proxy_request("xiaohongshu", "/api/v1/xiaohongshu/app_v2/get_video_note_detail", params=params, json_body=body)

@router.get("/get_mixed_note_detail")
async def get_mixed_note_detail(
    request: Request,
    note_id: str | None = None,
    share_text: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取首页推荐流笔记详情/Get mixed note detail from feed"""
    body = await request.json()
    params: dict[str, Any] = {}
    if note_id is not None:
        params["note_id"] = note_id
    if share_text is not None:
        params["share_text"] = share_text
    return await proxy_request("xiaohongshu", "/api/v1/xiaohongshu/app_v2/get_mixed_note_detail", params=params, json_body=body)

@router.get("/get_note_comments")
async def get_note_comments(
    request: Request,
    note_id: str | None = None,
    share_text: str | None = None,
    cursor: str | None = None,
    index: int | None = None,
    pageArea: str | None = None,
    sort_strategy: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取笔记评论列表/Get note comments"""
    body = await request.json()
    params: dict[str, Any] = {}
    if note_id is not None:
        params["note_id"] = note_id
    if share_text is not None:
        params["share_text"] = share_text
    if cursor is not None:
        params["cursor"] = cursor
    if index is not None:
        params["index"] = index
    if pageArea is not None:
        params["pageArea"] = pageArea
    if sort_strategy is not None:
        params["sort_strategy"] = sort_strategy
    return await proxy_request("xiaohongshu", "/api/v1/xiaohongshu/app_v2/get_note_comments", params=params, json_body=body)

@router.get("/get_note_sub_comments")
async def get_note_sub_comments(
    comment_id: str,
    request: Request,
    note_id: str | None = None,
    share_text: str | None = None,
    cursor: str | None = None,
    index: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取笔记二级评论列表/Get note sub comments"""
    body = await request.json()
    params: dict[str, Any] = {}
    if note_id is not None:
        params["note_id"] = note_id
    if share_text is not None:
        params["share_text"] = share_text
    if comment_id is not None:
        params["comment_id"] = comment_id
    if cursor is not None:
        params["cursor"] = cursor
    if index is not None:
        params["index"] = index
    return await proxy_request("xiaohongshu", "/api/v1/xiaohongshu/app_v2/get_note_sub_comments", params=params, json_body=body)

@router.get("/get_user_info")
async def get_user_info(
    request: Request,
    user_id: str | None = None,
    share_text: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户信息/Get user info"""
    body = await request.json()
    params: dict[str, Any] = {}
    if user_id is not None:
        params["user_id"] = user_id
    if share_text is not None:
        params["share_text"] = share_text
    return await proxy_request("xiaohongshu", "/api/v1/xiaohongshu/app_v2/get_user_info", params=params, json_body=body)

@router.get("/get_user_posted_notes")
async def get_user_posted_notes(
    request: Request,
    user_id: str | None = None,
    share_text: str | None = None,
    cursor: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户笔记列表/Get user posted notes"""
    body = await request.json()
    params: dict[str, Any] = {}
    if user_id is not None:
        params["user_id"] = user_id
    if share_text is not None:
        params["share_text"] = share_text
    if cursor is not None:
        params["cursor"] = cursor
    return await proxy_request("xiaohongshu", "/api/v1/xiaohongshu/app_v2/get_user_posted_notes", params=params, json_body=body)

@router.get("/get_user_faved_notes")
async def get_user_faved_notes(
    request: Request,
    user_id: str | None = None,
    share_text: str | None = None,
    cursor: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户收藏笔记列表/Get user faved notes"""
    body = await request.json()
    params: dict[str, Any] = {}
    if user_id is not None:
        params["user_id"] = user_id
    if share_text is not None:
        params["share_text"] = share_text
    if cursor is not None:
        params["cursor"] = cursor
    return await proxy_request("xiaohongshu", "/api/v1/xiaohongshu/app_v2/get_user_faved_notes", params=params, json_body=body)

@router.get("/search_notes")
async def search_notes(
    keyword: str,
    request: Request,
    page: int | None = None,
    sort_type: str | None = None,
    note_type: str | None = None,
    time_filter: str | None = None,
    search_id: str | None = None,
    search_session_id: str | None = None,
    source: str | None = None,
    ai_mode: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """搜索笔记/Search notes"""
    body = await request.json()
    params: dict[str, Any] = {}
    if keyword is not None:
        params["keyword"] = keyword
    if page is not None:
        params["page"] = page
    if sort_type is not None:
        params["sort_type"] = sort_type
    if note_type is not None:
        params["note_type"] = note_type
    if time_filter is not None:
        params["time_filter"] = time_filter
    if search_id is not None:
        params["search_id"] = search_id
    if search_session_id is not None:
        params["search_session_id"] = search_session_id
    if source is not None:
        params["source"] = source
    if ai_mode is not None:
        params["ai_mode"] = ai_mode
    return await proxy_request("xiaohongshu", "/api/v1/xiaohongshu/app_v2/search_notes", params=params, json_body=body)

@router.get("/search_users")
async def search_users(
    keyword: str,
    request: Request,
    page: int | None = None,
    search_id: str | None = None,
    source: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """搜索用户/Search users"""
    body = await request.json()
    params: dict[str, Any] = {}
    if keyword is not None:
        params["keyword"] = keyword
    if page is not None:
        params["page"] = page
    if search_id is not None:
        params["search_id"] = search_id
    if source is not None:
        params["source"] = source
    return await proxy_request("xiaohongshu", "/api/v1/xiaohongshu/app_v2/search_users", params=params, json_body=body)

@router.get("/search_images")
async def search_images(
    keyword: str,
    request: Request,
    page: int | None = None,
    search_id: str | None = None,
    search_session_id: str | None = None,
    word_request_id: str | None = None,
    source: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """搜索图片/Search images"""
    body = await request.json()
    params: dict[str, Any] = {}
    if keyword is not None:
        params["keyword"] = keyword
    if page is not None:
        params["page"] = page
    if search_id is not None:
        params["search_id"] = search_id
    if search_session_id is not None:
        params["search_session_id"] = search_session_id
    if word_request_id is not None:
        params["word_request_id"] = word_request_id
    if source is not None:
        params["source"] = source
    return await proxy_request("xiaohongshu", "/api/v1/xiaohongshu/app_v2/search_images", params=params, json_body=body)

@router.get("/search_products")
async def search_products(
    keyword: str,
    request: Request,
    page: int | None = None,
    search_id: str | None = None,
    source: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """搜索商品/Search products"""
    body = await request.json()
    params: dict[str, Any] = {}
    if keyword is not None:
        params["keyword"] = keyword
    if page is not None:
        params["page"] = page
    if search_id is not None:
        params["search_id"] = search_id
    if source is not None:
        params["source"] = source
    return await proxy_request("xiaohongshu", "/api/v1/xiaohongshu/app_v2/search_products", params=params, json_body=body)

@router.get("/search_groups")
async def search_groups(
    keyword: str,
    request: Request,
    page_no: int | None = None,
    search_id: str | None = None,
    source: str | None = None,
    is_recommend: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """搜索群聊/Search groups"""
    body = await request.json()
    params: dict[str, Any] = {}
    if keyword is not None:
        params["keyword"] = keyword
    if page_no is not None:
        params["page_no"] = page_no
    if search_id is not None:
        params["search_id"] = search_id
    if source is not None:
        params["source"] = source
    if is_recommend is not None:
        params["is_recommend"] = is_recommend
    return await proxy_request("xiaohongshu", "/api/v1/xiaohongshu/app_v2/search_groups", params=params, json_body=body)

@router.get("/get_product_detail")
async def get_product_detail(
    sku_id: str,
    request: Request,
    source: str | None = None,
    pre_page: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取商品详情/Get product detail"""
    body = await request.json()
    params: dict[str, Any] = {}
    if sku_id is not None:
        params["sku_id"] = sku_id
    if source is not None:
        params["source"] = source
    if pre_page is not None:
        params["pre_page"] = pre_page
    return await proxy_request("xiaohongshu", "/api/v1/xiaohongshu/app_v2/get_product_detail", params=params, json_body=body)

@router.get("/get_product_review_overview")
async def get_product_review_overview(
    sku_id: str,
    request: Request,
    tab: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取商品评论总览/Get product review overview"""
    body = await request.json()
    params: dict[str, Any] = {}
    if sku_id is not None:
        params["sku_id"] = sku_id
    if tab is not None:
        params["tab"] = tab
    return await proxy_request("xiaohongshu", "/api/v1/xiaohongshu/app_v2/get_product_review_overview", params=params, json_body=body)

@router.get("/get_product_reviews")
async def get_product_reviews(
    sku_id: str,
    request: Request,
    page: int | None = None,
    sort_strategy_type: int | None = None,
    share_pics_only: int | None = None,
    from_page: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取商品评论列表/Get product reviews"""
    body = await request.json()
    params: dict[str, Any] = {}
    if sku_id is not None:
        params["sku_id"] = sku_id
    if page is not None:
        params["page"] = page
    if sort_strategy_type is not None:
        params["sort_strategy_type"] = sort_strategy_type
    if share_pics_only is not None:
        params["share_pics_only"] = share_pics_only
    if from_page is not None:
        params["from_page"] = from_page
    return await proxy_request("xiaohongshu", "/api/v1/xiaohongshu/app_v2/get_product_reviews", params=params, json_body=body)

@router.get("/get_product_recommendations")
async def get_product_recommendations(
    sku_id: str,
    request: Request,
    cursor_score: str | None = None,
    region: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取商品推荐列表/Get product recommendations"""
    body = await request.json()
    params: dict[str, Any] = {}
    if sku_id is not None:
        params["sku_id"] = sku_id
    if cursor_score is not None:
        params["cursor_score"] = cursor_score
    if region is not None:
        params["region"] = region
    return await proxy_request("xiaohongshu", "/api/v1/xiaohongshu/app_v2/get_product_recommendations", params=params, json_body=body)

@router.get("/get_topic_info")
async def get_topic_info(
    page_id: str,
    request: Request,
    source: str | None = None,
    note_id: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取话题详情/Get topic info"""
    body = await request.json()
    params: dict[str, Any] = {}
    if page_id is not None:
        params["page_id"] = page_id
    if source is not None:
        params["source"] = source
    if note_id is not None:
        params["note_id"] = note_id
    return await proxy_request("xiaohongshu", "/api/v1/xiaohongshu/app_v2/get_topic_info", params=params, json_body=body)

@router.get("/get_topic_feed")
async def get_topic_feed(
    page_id: str,
    request: Request,
    sort: str | None = None,
    cursor_score: str | None = None,
    last_note_id: str | None = None,
    last_note_ct: str | None = None,
    session_id: str | None = None,
    first_load_time: str | None = None,
    source: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取话题笔记列表/Get topic feed"""
    body = await request.json()
    params: dict[str, Any] = {}
    if page_id is not None:
        params["page_id"] = page_id
    if sort is not None:
        params["sort"] = sort
    if cursor_score is not None:
        params["cursor_score"] = cursor_score
    if last_note_id is not None:
        params["last_note_id"] = last_note_id
    if last_note_ct is not None:
        params["last_note_ct"] = last_note_ct
    if session_id is not None:
        params["session_id"] = session_id
    if first_load_time is not None:
        params["first_load_time"] = first_load_time
    if source is not None:
        params["source"] = source
    return await proxy_request("xiaohongshu", "/api/v1/xiaohongshu/app_v2/get_topic_feed", params=params, json_body=body)

@router.get("/get_creator_inspiration_feed")
async def get_creator_inspiration_feed(
    request: Request,
    cursor: str | None = None,
    tab: int | None = None,
    source: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取创作者推荐灵感列表/Get creator inspiration feed"""
    body = await request.json()
    params: dict[str, Any] = {}
    if cursor is not None:
        params["cursor"] = cursor
    if tab is not None:
        params["tab"] = tab
    if source is not None:
        params["source"] = source
    return await proxy_request("xiaohongshu", "/api/v1/xiaohongshu/app_v2/get_creator_inspiration_feed", params=params, json_body=body)

@router.get("/get_creator_hot_inspiration_feed")
async def get_creator_hot_inspiration_feed(
    request: Request,
    cursor: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取创作者热点灵感列表/Get creator hot inspiration feed"""
    body = await request.json()
    params: dict[str, Any] = {}
    if cursor is not None:
        params["cursor"] = cursor
    return await proxy_request("xiaohongshu", "/api/v1/xiaohongshu/app_v2/get_creator_hot_inspiration_feed", params=params, json_body=body)
