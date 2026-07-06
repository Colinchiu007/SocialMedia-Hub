"""Auto-generated routes for Weibo-Web-V2-API."""

from __future__ import annotations

from typing import Any

from fastapi import APIRouter, Depends, Request

from socialmedia_hub.server._core import proxy_request, verify_api_key

router = APIRouter(prefix="/api/v1/weibo/web/v2", tags=["weibo_web_v2"])

@router.get("/check_allow_comment_with_pic")
async def check_allow_comment_with_pic(
    id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """检查微博是否允许带图评论/Check if Weibo allows image comments"""
        params: dict[str, Any] = {}
        if id is not None:
            params["id"] = id
        body = await request.json()
        return await proxy_request("weibo", "/api/v1/weibo/web_v2/check_allow_comment_with_pic", json_body=body)

@router.get("/fetch_post_detail")
async def fetch_post_detail(
    is_get_long_text: str | None = None,
    id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取单个作品数据/Get single post data"""
        params: dict[str, Any] = {}
        if id is not None:
            params["id"] = id
        if is_get_long_text is not None:
            params["is_get_long_text"] = is_get_long_text
        body = await request.json()
        return await proxy_request("weibo", "/api/v1/weibo/web_v2/fetch_post_detail", json_body=body)

@router.get("/fetch_user_info")
async def fetch_user_info(
    custom: str | None = None,
    uid: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户信息/Get user information"""
        params: dict[str, Any] = {}
        if uid is not None:
            params["uid"] = uid
        if custom is not None:
            params["custom"] = custom
        body = await request.json()
        return await proxy_request("weibo", "/api/v1/weibo/web_v2/fetch_user_info", json_body=body)

@router.get("/fetch_user_basic_info")
async def fetch_user_basic_info(
    uid: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户基本信息/Get user basic information"""
        params: dict[str, Any] = {}
        if uid is not None:
            params["uid"] = uid
        body = await request.json()
        return await proxy_request("weibo", "/api/v1/weibo/web_v2/fetch_user_basic_info", json_body=body)

@router.get("/fetch_user_posts")
async def fetch_user_posts(
    since_id: str | None = None,
    feature: int | None = None,
    page: int | None = None,
    uid: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取微博用户文章数据/Get Weibo user posts"""
        params: dict[str, Any] = {}
        if uid is not None:
            params["uid"] = uid
        if page is not None:
            params["page"] = page
        if feature is not None:
            params["feature"] = feature
        if since_id is not None:
            params["since_id"] = since_id
        body = await request.json()
        return await proxy_request("weibo", "/api/v1/weibo/web_v2/fetch_user_posts", json_body=body)

@router.get("/fetch_user_original_posts")
async def fetch_user_original_posts(
    since_id: str | None = None,
    page: int | None = None,
    uid: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取微博用户原创微博数据/Get Weibo user original posts"""
        params: dict[str, Any] = {}
        if uid is not None:
            params["uid"] = uid
        if page is not None:
            params["page"] = page
        if since_id is not None:
            params["since_id"] = since_id
        body = await request.json()
        return await proxy_request("weibo", "/api/v1/weibo/web_v2/fetch_user_original_posts", json_body=body)

@router.get("/fetch_post_comments")
async def fetch_post_comments(
    max_id: str | None = None,
    count: int | None = None,
    id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取微博评论/Get Weibo comments"""
        params: dict[str, Any] = {}
        if id is not None:
            params["id"] = id
        if count is not None:
            params["count"] = count
        if max_id is not None:
            params["max_id"] = max_id
        body = await request.json()
        return await proxy_request("weibo", "/api/v1/weibo/web_v2/fetch_post_comments", json_body=body)

@router.get("/fetch_post_sub_comments")
async def fetch_post_sub_comments(
    max_id: str | None = None,
    count: int | None = None,
    id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取微博子评论/Get Weibo sub-comments"""
        params: dict[str, Any] = {}
        if id is not None:
            params["id"] = id
        if count is not None:
            params["count"] = count
        if max_id is not None:
            params["max_id"] = max_id
        body = await request.json()
        return await proxy_request("weibo", "/api/v1/weibo/web_v2/fetch_post_sub_comments", json_body=body)

@router.get("/search_user_posts")
async def search_user_posts(
    hasmusic: int | None = None,
    hasvideo: int | None = None,
    haspic: int | None = None,
    hastext: int | None = None,
    hasret: int | None = None,
    hasori: int | None = None,
    endtime: str | None = None,
    starttime: str | None = None,
    page: int | None = None,
    q: str | None = None,
    uid: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """搜索用户微博/Search user posts"""
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
        body = await request.json()
        return await proxy_request("weibo", "/api/v1/weibo/web_v2/search_user_posts", json_body=body)

@router.get("/fetch_user_video_collection_list")
async def fetch_user_video_collection_list(
    uid: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户微博视频收藏夹列表/Get user video collection list"""
        params: dict[str, Any] = {}
        if uid is not None:
            params["uid"] = uid
        body = await request.json()
        return await proxy_request("weibo", "/api/v1/weibo/web_v2/fetch_user_video_collection_list", json_body=body)

@router.get("/fetch_user_video_collection_detail")
async def fetch_user_video_collection_detail(
    tab_code: int | None = None,
    cursor: str | None = None,
    cid: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户微博视频收藏夹详情/Get user video collection detail"""
        params: dict[str, Any] = {}
        if cid is not None:
            params["cid"] = cid
        if cursor is not None:
            params["cursor"] = cursor
        if tab_code is not None:
            params["tab_code"] = tab_code
        body = await request.json()
        return await proxy_request("weibo", "/api/v1/weibo/web_v2/fetch_user_video_collection_detail", json_body=body)

@router.get("/fetch_user_video_list")
async def fetch_user_video_list(
    cursor: str | None = None,
    uid: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取微博用户全部视频/Get user all videos"""
        params: dict[str, Any] = {}
        if uid is not None:
            params["uid"] = uid
        if cursor is not None:
            params["cursor"] = cursor
        body = await request.json()
        return await proxy_request("weibo", "/api/v1/weibo/web_v2/fetch_user_video_list", json_body=body)

@router.get("/fetch_user_following")
async def fetch_user_following(
    page: int | None = None,
    uid: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户关注列表/Get user following list"""
        params: dict[str, Any] = {}
        if uid is not None:
            params["uid"] = uid
        if page is not None:
            params["page"] = page
        body = await request.json()
        return await proxy_request("weibo", "/api/v1/weibo/web_v2/fetch_user_following", json_body=body)

@router.get("/fetch_user_fans")
async def fetch_user_fans(
    page: int | None = None,
    uid: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户粉丝列表/Get user fans list"""
        params: dict[str, Any] = {}
        if uid is not None:
            params["uid"] = uid
        if page is not None:
            params["page"] = page
        body = await request.json()
        return await proxy_request("weibo", "/api/v1/weibo/web_v2/fetch_user_fans", json_body=body)

@router.get("/fetch_all_groups")
async def fetch_all_groups(
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取所有分组信息/Get all groups information"""
        body = await request.json()
        return await proxy_request("weibo", "/api/v1/weibo/web_v2/fetch_all_groups", json_body=body)

@router.get("/fetch_user_recommend_timeline")
async def fetch_user_recommend_timeline(
    count: int | None = None,
    max_id: str | None = None,
    extparam: str | None = None,
    containerid: str | None = None,
    group_id: str | None = None,
    refresh: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取微博主页推荐时间轴/Get user recommend timeline"""
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
        body = await request.json()
        return await proxy_request("weibo", "/api/v1/weibo/web_v2/fetch_user_recommend_timeline", json_body=body)

@router.get("/fetch_hot_ranking_timeline")
async def fetch_hot_ranking_timeline(
    count: int | None = None,
    max_id: str | None = None,
    since_id: str | None = None,
    ranking_type: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取微博热门榜单时间轴/Get hot ranking timeline"""
        params: dict[str, Any] = {}
        if ranking_type is not None:
            params["ranking_type"] = ranking_type
        if since_id is not None:
            params["since_id"] = since_id
        if max_id is not None:
            params["max_id"] = max_id
        if count is not None:
            params["count"] = count
        body = await request.json()
        return await proxy_request("weibo", "/api/v1/weibo/web_v2/fetch_hot_ranking_timeline", json_body=body)

@router.get("/fetch_hot_search_index")
async def fetch_hot_search_index(
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取微博热搜词条(10条)/Get Weibo hot search index (10 items)"""
        body = await request.json()
        return await proxy_request("weibo", "/api/v1/weibo/web_v2/fetch_hot_search_index", json_body=body)

@router.get("/fetch_hot_search_summary")
async def fetch_hot_search_summary(
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取微博完整热搜榜单(50条)/Get Weibo complete hot search ranking (50 items)"""
        body = await request.json()
        return await proxy_request("weibo", "/api/v1/weibo/web_v2/fetch_hot_search_summary", json_body=body)

@router.get("/fetch_hot_search")
async def fetch_hot_search(
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取微博热搜榜单/Get Weibo hot search ranking"""
        body = await request.json()
        return await proxy_request("weibo", "/api/v1/weibo/web_v2/fetch_hot_search", json_body=body)

@router.get("/fetch_entertainment_ranking")
async def fetch_entertainment_ranking(
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取微博文娱榜单/Get Weibo entertainment ranking"""
        body = await request.json()
        return await proxy_request("weibo", "/api/v1/weibo/web_v2/fetch_entertainment_ranking", json_body=body)

@router.get("/fetch_life_ranking")
async def fetch_life_ranking(
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取微博生活榜单/Get Weibo life ranking"""
        body = await request.json()
        return await proxy_request("weibo", "/api/v1/weibo/web_v2/fetch_life_ranking", json_body=body)

@router.get("/fetch_social_ranking")
async def fetch_social_ranking(
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取微博社会榜单/Get Weibo social ranking"""
        body = await request.json()
        return await proxy_request("weibo", "/api/v1/weibo/web_v2/fetch_social_ranking", json_body=body)

@router.get("/fetch_similar_search")
async def fetch_similar_search(
    keyword: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取微博相似搜索词推荐/Get Weibo similar search recommendations"""
        params: dict[str, Any] = {}
        if keyword is not None:
            params["keyword"] = keyword
        body = await request.json()
        return await proxy_request("weibo", "/api/v1/weibo/web_v2/fetch_similar_search", json_body=body)

@router.get("/fetch_ai_search")
async def fetch_ai_search(
    query: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """微博智能搜索/Weibo AI Search"""
        params: dict[str, Any] = {}
        if query is not None:
            params["query"] = query
        body = await request.json()
        return await proxy_request("weibo", "/api/v1/weibo/web_v2/fetch_ai_search", json_body=body)

@router.get("/fetch_ai_related_search")
async def fetch_ai_related_search(
    keyword: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """微博AI搜索内容扩展/Weibo AI Search Content Extension"""
        params: dict[str, Any] = {}
        if keyword is not None:
            params["keyword"] = keyword
        body = await request.json()
        return await proxy_request("weibo", "/api/v1/weibo/web_v2/fetch_ai_related_search", json_body=body)

@router.get("/fetch_advanced_search")
async def fetch_advanced_search(
    page: int | None = None,
    timescope: str | None = None,
    include_type: str | None = None,
    search_type: str | None = None,
    q: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """微博高级搜索/Weibo Advanced Search"""
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
        body = await request.json()
        return await proxy_request("weibo", "/api/v1/weibo/web_v2/fetch_advanced_search", json_body=body)

@router.get("/fetch_city_list")
async def fetch_city_list(
    normalized: bool | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """地区省市映射/Region City List"""
        params: dict[str, Any] = {}
        if normalized is not None:
            params["normalized"] = normalized
        body = await request.json()
        return await proxy_request("weibo", "/api/v1/weibo/web_v2/fetch_city_list", json_body=body)

@router.get("/fetch_realtime_search")
async def fetch_realtime_search(
    page: int | None = None,
    query: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """实时搜索/Weibo Realtime Search"""
        params: dict[str, Any] = {}
        if query is not None:
            params["query"] = query
        if page is not None:
            params["page"] = page
        body = await request.json()
        return await proxy_request("weibo", "/api/v1/weibo/web_v2/fetch_realtime_search", json_body=body)

@router.get("/fetch_user_search")
async def fetch_user_search(
    work: str | None = None,
    school: str | None = None,
    tag: str | None = None,
    nickname: str | None = None,
    age: str | None = None,
    gender: str | None = None,
    auth: str | None = None,
    region: str | None = None,
    page: int | None = None,
    query: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """用户搜索/User search"""
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
        body = await request.json()
        return await proxy_request("weibo", "/api/v1/weibo/web_v2/fetch_user_search", json_body=body)

@router.get("/fetch_video_search")
async def fetch_video_search(
    page: int | None = None,
    mode: str | None = None,
    query: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """视频搜索（热门/全部）/Weibo video search (hot/all)"""
        params: dict[str, Any] = {}
        if query is not None:
            params["query"] = query
        if mode is not None:
            params["mode"] = mode
        if page is not None:
            params["page"] = page
        body = await request.json()
        return await proxy_request("weibo", "/api/v1/weibo/web_v2/fetch_video_search", json_body=body)

@router.get("/fetch_pic_search")
async def fetch_pic_search(
    page: int | None = None,
    query: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """图片搜索/Weibo picture search"""
        params: dict[str, Any] = {}
        if query is not None:
            params["query"] = query
        if page is not None:
            params["page"] = page
        body = await request.json()
        return await proxy_request("weibo", "/api/v1/weibo/web_v2/fetch_pic_search", json_body=body)

@router.get("/fetch_topic_search")
async def fetch_topic_search(
    page: int | None = None,
    query: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """话题搜索/Weibo topic search"""
        params: dict[str, Any] = {}
        if query is not None:
            params["query"] = query
        if page is not None:
            params["page"] = page
        body = await request.json()
        return await proxy_request("weibo", "/api/v1/weibo/web_v2/fetch_topic_search", json_body=body)
