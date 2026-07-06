"""Auto-generated routes for Weibo-Web-V2-API."""

from __future__ import annotations

from typing import Any

from fastapi import APIRouter, Depends, Request

from socialmedia_hub.server._core import proxy_request, verify_api_key

router = APIRouter(prefix="/api/v1/weibo/web/v2", tags=["weibo_web_v2"])

@router.get("/check_allow_comment_with_pic")
async def check_allow_comment_with_pic(
    id: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """检查微博是否允许带图评论/Check if Weibo allows image comments"""
    body = await request.json()
    params: dict[str, Any] = {}
    if id is not None:
        params["id"] = id
    return await proxy_request("weibo", "/api/v1/weibo/web_v2/check_allow_comment_with_pic", params=params, json_body=body)

@router.get("/fetch_post_detail")
async def fetch_post_detail(
    id: str,
    request: Request,
    is_get_long_text: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取单个作品数据/Get single post data"""
    body = await request.json()
    params: dict[str, Any] = {}
    if id is not None:
        params["id"] = id
    if is_get_long_text is not None:
        params["is_get_long_text"] = is_get_long_text
    return await proxy_request("weibo", "/api/v1/weibo/web_v2/fetch_post_detail", params=params, json_body=body)

@router.get("/fetch_user_info")
async def fetch_user_info(
    request: Request,
    uid: str | None = None,
    custom: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户信息/Get user information"""
    body = await request.json()
    params: dict[str, Any] = {}
    if uid is not None:
        params["uid"] = uid
    if custom is not None:
        params["custom"] = custom
    return await proxy_request("weibo", "/api/v1/weibo/web_v2/fetch_user_info", params=params, json_body=body)

@router.get("/fetch_user_basic_info")
async def fetch_user_basic_info(
    uid: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户基本信息/Get user basic information"""
    body = await request.json()
    params: dict[str, Any] = {}
    if uid is not None:
        params["uid"] = uid
    return await proxy_request("weibo", "/api/v1/weibo/web_v2/fetch_user_basic_info", params=params, json_body=body)

@router.get("/fetch_user_posts")
async def fetch_user_posts(
    uid: str,
    request: Request,
    page: int | None = None,
    feature: int | None = None,
    since_id: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取微博用户文章数据/Get Weibo user posts"""
    body = await request.json()
    params: dict[str, Any] = {}
    if uid is not None:
        params["uid"] = uid
    if page is not None:
        params["page"] = page
    if feature is not None:
        params["feature"] = feature
    if since_id is not None:
        params["since_id"] = since_id
    return await proxy_request("weibo", "/api/v1/weibo/web_v2/fetch_user_posts", params=params, json_body=body)

@router.get("/fetch_user_original_posts")
async def fetch_user_original_posts(
    uid: str,
    request: Request,
    page: int | None = None,
    since_id: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取微博用户原创微博数据/Get Weibo user original posts"""
    body = await request.json()
    params: dict[str, Any] = {}
    if uid is not None:
        params["uid"] = uid
    if page is not None:
        params["page"] = page
    if since_id is not None:
        params["since_id"] = since_id
    return await proxy_request("weibo", "/api/v1/weibo/web_v2/fetch_user_original_posts", params=params, json_body=body)

@router.get("/fetch_post_comments")
async def fetch_post_comments(
    id: str,
    request: Request,
    count: int | None = None,
    max_id: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取微博评论/Get Weibo comments"""
    body = await request.json()
    params: dict[str, Any] = {}
    if id is not None:
        params["id"] = id
    if count is not None:
        params["count"] = count
    if max_id is not None:
        params["max_id"] = max_id
    return await proxy_request("weibo", "/api/v1/weibo/web_v2/fetch_post_comments", params=params, json_body=body)

@router.get("/fetch_post_sub_comments")
async def fetch_post_sub_comments(
    id: str,
    request: Request,
    count: int | None = None,
    max_id: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取微博子评论/Get Weibo sub-comments"""
    body = await request.json()
    params: dict[str, Any] = {}
    if id is not None:
        params["id"] = id
    if count is not None:
        params["count"] = count
    if max_id is not None:
        params["max_id"] = max_id
    return await proxy_request("weibo", "/api/v1/weibo/web_v2/fetch_post_sub_comments", params=params, json_body=body)

@router.get("/search_user_posts")
async def search_user_posts(
    uid: str,
    request: Request,
    q: str | None = None,
    page: int | None = None,
    starttime: str | None = None,
    endtime: str | None = None,
    hasori: int | None = None,
    hasret: int | None = None,
    hastext: int | None = None,
    haspic: int | None = None,
    hasvideo: int | None = None,
    hasmusic: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """搜索用户微博/Search user posts"""
    body = await request.json()
    params: dict[str, Any] = {}
    if uid is not None:
        params["uid"] = uid
    if q is not None:
        params["q"] = q
    if page is not None:
        params["page"] = page
    if starttime is not None:
        params["starttime"] = starttime
    if endtime is not None:
        params["endtime"] = endtime
    if hasori is not None:
        params["hasori"] = hasori
    if hasret is not None:
        params["hasret"] = hasret
    if hastext is not None:
        params["hastext"] = hastext
    if haspic is not None:
        params["haspic"] = haspic
    if hasvideo is not None:
        params["hasvideo"] = hasvideo
    if hasmusic is not None:
        params["hasmusic"] = hasmusic
    return await proxy_request("weibo", "/api/v1/weibo/web_v2/search_user_posts", params=params, json_body=body)

@router.get("/fetch_user_video_collection_list")
async def fetch_user_video_collection_list(
    uid: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户微博视频收藏夹列表/Get user video collection list"""
    body = await request.json()
    params: dict[str, Any] = {}
    if uid is not None:
        params["uid"] = uid
    return await proxy_request("weibo", "/api/v1/weibo/web_v2/fetch_user_video_collection_list", params=params, json_body=body)

@router.get("/fetch_user_video_collection_detail")
async def fetch_user_video_collection_detail(
    cid: str,
    request: Request,
    cursor: str | None = None,
    tab_code: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户微博视频收藏夹详情/Get user video collection detail"""
    body = await request.json()
    params: dict[str, Any] = {}
    if cid is not None:
        params["cid"] = cid
    if cursor is not None:
        params["cursor"] = cursor
    if tab_code is not None:
        params["tab_code"] = tab_code
    return await proxy_request("weibo", "/api/v1/weibo/web_v2/fetch_user_video_collection_detail", params=params, json_body=body)

@router.get("/fetch_user_video_list")
async def fetch_user_video_list(
    uid: str,
    request: Request,
    cursor: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取微博用户全部视频/Get user all videos"""
    body = await request.json()
    params: dict[str, Any] = {}
    if uid is not None:
        params["uid"] = uid
    if cursor is not None:
        params["cursor"] = cursor
    return await proxy_request("weibo", "/api/v1/weibo/web_v2/fetch_user_video_list", params=params, json_body=body)

@router.get("/fetch_user_following")
async def fetch_user_following(
    uid: str,
    request: Request,
    page: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户关注列表/Get user following list"""
    body = await request.json()
    params: dict[str, Any] = {}
    if uid is not None:
        params["uid"] = uid
    if page is not None:
        params["page"] = page
    return await proxy_request("weibo", "/api/v1/weibo/web_v2/fetch_user_following", params=params, json_body=body)

@router.get("/fetch_user_fans")
async def fetch_user_fans(
    uid: str,
    request: Request,
    page: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户粉丝列表/Get user fans list"""
    body = await request.json()
    params: dict[str, Any] = {}
    if uid is not None:
        params["uid"] = uid
    if page is not None:
        params["page"] = page
    return await proxy_request("weibo", "/api/v1/weibo/web_v2/fetch_user_fans", params=params, json_body=body)

@router.get("/fetch_all_groups")
async def fetch_all_groups(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取所有分组信息/Get all groups information"""
    body = await request.json()
    return await proxy_request("weibo", "/api/v1/weibo/web_v2/fetch_all_groups", json_body=body)

@router.get("/fetch_user_recommend_timeline")
async def fetch_user_recommend_timeline(
    request: Request,
    refresh: int | None = None,
    group_id: str | None = None,
    containerid: str | None = None,
    extparam: str | None = None,
    max_id: str | None = None,
    count: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取微博主页推荐时间轴/Get user recommend timeline"""
    body = await request.json()
    params: dict[str, Any] = {}
    if refresh is not None:
        params["refresh"] = refresh
    if group_id is not None:
        params["group_id"] = group_id
    if containerid is not None:
        params["containerid"] = containerid
    if extparam is not None:
        params["extparam"] = extparam
    if max_id is not None:
        params["max_id"] = max_id
    if count is not None:
        params["count"] = count
    return await proxy_request("weibo", "/api/v1/weibo/web_v2/fetch_user_recommend_timeline", params=params, json_body=body)

@router.get("/fetch_hot_ranking_timeline")
async def fetch_hot_ranking_timeline(
    ranking_type: str,
    request: Request,
    since_id: str | None = None,
    max_id: str | None = None,
    count: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取微博热门榜单时间轴/Get hot ranking timeline"""
    body = await request.json()
    params: dict[str, Any] = {}
    if ranking_type is not None:
        params["ranking_type"] = ranking_type
    if since_id is not None:
        params["since_id"] = since_id
    if max_id is not None:
        params["max_id"] = max_id
    if count is not None:
        params["count"] = count
    return await proxy_request("weibo", "/api/v1/weibo/web_v2/fetch_hot_ranking_timeline", params=params, json_body=body)

@router.get("/fetch_hot_search_index")
async def fetch_hot_search_index(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取微博热搜词条(10条)/Get Weibo hot search index (10 items)"""
    body = await request.json()
    return await proxy_request("weibo", "/api/v1/weibo/web_v2/fetch_hot_search_index", json_body=body)

@router.get("/fetch_hot_search_summary")
async def fetch_hot_search_summary(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取微博完整热搜榜单(50条)/Get Weibo complete hot search ranking (50 items)"""
    body = await request.json()
    return await proxy_request("weibo", "/api/v1/weibo/web_v2/fetch_hot_search_summary", json_body=body)

@router.get("/fetch_hot_search")
async def fetch_hot_search(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取微博热搜榜单/Get Weibo hot search ranking"""
    body = await request.json()
    return await proxy_request("weibo", "/api/v1/weibo/web_v2/fetch_hot_search", json_body=body)

@router.get("/fetch_entertainment_ranking")
async def fetch_entertainment_ranking(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取微博文娱榜单/Get Weibo entertainment ranking"""
    body = await request.json()
    return await proxy_request("weibo", "/api/v1/weibo/web_v2/fetch_entertainment_ranking", json_body=body)

@router.get("/fetch_life_ranking")
async def fetch_life_ranking(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取微博生活榜单/Get Weibo life ranking"""
    body = await request.json()
    return await proxy_request("weibo", "/api/v1/weibo/web_v2/fetch_life_ranking", json_body=body)

@router.get("/fetch_social_ranking")
async def fetch_social_ranking(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取微博社会榜单/Get Weibo social ranking"""
    body = await request.json()
    return await proxy_request("weibo", "/api/v1/weibo/web_v2/fetch_social_ranking", json_body=body)

@router.get("/fetch_similar_search")
async def fetch_similar_search(
    keyword: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取微博相似搜索词推荐/Get Weibo similar search recommendations"""
    body = await request.json()
    params: dict[str, Any] = {}
    if keyword is not None:
        params["keyword"] = keyword
    return await proxy_request("weibo", "/api/v1/weibo/web_v2/fetch_similar_search", params=params, json_body=body)

@router.get("/fetch_ai_search")
async def fetch_ai_search(
    query: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """微博智能搜索/Weibo AI Search"""
    body = await request.json()
    params: dict[str, Any] = {}
    if query is not None:
        params["query"] = query
    return await proxy_request("weibo", "/api/v1/weibo/web_v2/fetch_ai_search", params=params, json_body=body)

@router.get("/fetch_ai_related_search")
async def fetch_ai_related_search(
    keyword: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """微博AI搜索内容扩展/Weibo AI Search Content Extension"""
    body = await request.json()
    params: dict[str, Any] = {}
    if keyword is not None:
        params["keyword"] = keyword
    return await proxy_request("weibo", "/api/v1/weibo/web_v2/fetch_ai_related_search", params=params, json_body=body)

@router.get("/fetch_advanced_search")
async def fetch_advanced_search(
    q: str,
    request: Request,
    search_type: str | None = None,
    include_type: str | None = None,
    timescope: str | None = None,
    page: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """微博高级搜索/Weibo Advanced Search"""
    body = await request.json()
    params: dict[str, Any] = {}
    if q is not None:
        params["q"] = q
    if search_type is not None:
        params["search_type"] = search_type
    if include_type is not None:
        params["include_type"] = include_type
    if timescope is not None:
        params["timescope"] = timescope
    if page is not None:
        params["page"] = page
    return await proxy_request("weibo", "/api/v1/weibo/web_v2/fetch_advanced_search", params=params, json_body=body)

@router.get("/fetch_city_list")
async def fetch_city_list(
    request: Request,
    normalized: bool | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """地区省市映射/Region City List"""
    body = await request.json()
    params: dict[str, Any] = {}
    if normalized is not None:
        params["normalized"] = normalized
    return await proxy_request("weibo", "/api/v1/weibo/web_v2/fetch_city_list", params=params, json_body=body)

@router.get("/fetch_realtime_search")
async def fetch_realtime_search(
    query: str,
    request: Request,
    page: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """实时搜索/Weibo Realtime Search"""
    body = await request.json()
    params: dict[str, Any] = {}
    if query is not None:
        params["query"] = query
    if page is not None:
        params["page"] = page
    return await proxy_request("weibo", "/api/v1/weibo/web_v2/fetch_realtime_search", params=params, json_body=body)

@router.get("/fetch_user_search")
async def fetch_user_search(
    request: Request,
    query: str | None = None,
    page: int | None = None,
    region: str | None = None,
    auth: str | None = None,
    gender: str | None = None,
    age: str | None = None,
    nickname: str | None = None,
    tag: str | None = None,
    school: str | None = None,
    work: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """用户搜索/User search"""
    body = await request.json()
    params: dict[str, Any] = {}
    if query is not None:
        params["query"] = query
    if page is not None:
        params["page"] = page
    if region is not None:
        params["region"] = region
    if auth is not None:
        params["auth"] = auth
    if gender is not None:
        params["gender"] = gender
    if age is not None:
        params["age"] = age
    if nickname is not None:
        params["nickname"] = nickname
    if tag is not None:
        params["tag"] = tag
    if school is not None:
        params["school"] = school
    if work is not None:
        params["work"] = work
    return await proxy_request("weibo", "/api/v1/weibo/web_v2/fetch_user_search", params=params, json_body=body)

@router.get("/fetch_video_search")
async def fetch_video_search(
    query: str,
    request: Request,
    mode: str | None = None,
    page: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """视频搜索（热门/全部）/Weibo video search (hot/all)"""
    body = await request.json()
    params: dict[str, Any] = {}
    if query is not None:
        params["query"] = query
    if mode is not None:
        params["mode"] = mode
    if page is not None:
        params["page"] = page
    return await proxy_request("weibo", "/api/v1/weibo/web_v2/fetch_video_search", params=params, json_body=body)

@router.get("/fetch_pic_search")
async def fetch_pic_search(
    query: str,
    request: Request,
    page: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """图片搜索/Weibo picture search"""
    body = await request.json()
    params: dict[str, Any] = {}
    if query is not None:
        params["query"] = query
    if page is not None:
        params["page"] = page
    return await proxy_request("weibo", "/api/v1/weibo/web_v2/fetch_pic_search", params=params, json_body=body)

@router.get("/fetch_topic_search")
async def fetch_topic_search(
    query: str,
    request: Request,
    page: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """话题搜索/Weibo topic search"""
    body = await request.json()
    params: dict[str, Any] = {}
    if query is not None:
        params["query"] = query
    if page is not None:
        params["page"] = page
    return await proxy_request("weibo", "/api/v1/weibo/web_v2/fetch_topic_search", params=params, json_body=body)
