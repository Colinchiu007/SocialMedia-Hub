"""Auto-generated routes for Zhihu-Web-API."""

from __future__ import annotations

from typing import Any

from fastapi import APIRouter, Depends, Request

from socialmedia_hub.server._core import proxy_request, verify_api_key

router = APIRouter(prefix="/api/v1/zhihu/web", tags=["zhihu_web"])

@router.get("/fetch_column_articles")
async def fetch_column_articles(
    column_id: str,
    request: Request,
    limit: str | None = None,
    offset: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取知乎专栏文章列表/Get Zhihu Column Articles"""
    params: dict[str, Any] = {}
    if column_id is not None:
        params["column_id"] = column_id
    if limit is not None:
        params["limit"] = limit
    if offset is not None:
        params["offset"] = offset
    return await proxy_request("zhihu", "/api/v1/zhihu/web/fetch_column_articles", params=params)

@router.get("/fetch_column_article_detail")
async def fetch_column_article_detail(
    article_id: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取知乎专栏文章详情/Get Zhihu Column Article Detail"""
    params: dict[str, Any] = {}
    if article_id is not None:
        params["article_id"] = article_id
    return await proxy_request("zhihu", "/api/v1/zhihu/web/fetch_column_article_detail", params=params)

@router.get("/fetch_column_recommend")
async def fetch_column_recommend(
    article_id: str,
    request: Request,
    limit: str | None = None,
    offset: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取知乎相似专栏推荐/Get Zhihu Similar Column Recommend"""
    params: dict[str, Any] = {}
    if article_id is not None:
        params["article_id"] = article_id
    if limit is not None:
        params["limit"] = limit
    if offset is not None:
        params["offset"] = offset
    return await proxy_request("zhihu", "/api/v1/zhihu/web/fetch_column_recommend", params=params)

@router.get("/fetch_column_relationship")
async def fetch_column_relationship(
    article_id: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取知乎专栏文章互动关系/Get Zhihu Column Article Relationship"""
    params: dict[str, Any] = {}
    if article_id is not None:
        params["article_id"] = article_id
    return await proxy_request("zhihu", "/api/v1/zhihu/web/fetch_column_relationship", params=params)

@router.get("/fetch_column_comment_config")
async def fetch_column_comment_config(
    article_id: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取知乎专栏评论区配置/Get Zhihu Column Comment Config"""
    params: dict[str, Any] = {}
    if article_id is not None:
        params["article_id"] = article_id
    return await proxy_request("zhihu", "/api/v1/zhihu/web/fetch_column_comment_config", params=params)

@router.get("/fetch_hot_recommend")
async def fetch_hot_recommend(
    request: Request,
    offset: str | None = None,
    page_number: str | None = None,
    session_token: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取知乎首页推荐/Get Zhihu Hot Recommend"""
    params: dict[str, Any] = {}
    if offset is not None:
        params["offset"] = offset
    if page_number is not None:
        params["page_number"] = page_number
    if session_token is not None:
        params["session_token"] = session_token
    return await proxy_request("zhihu", "/api/v1/zhihu/web/fetch_hot_recommend", params=params)

@router.get("/fetch_hot_list")
async def fetch_hot_list(
    request: Request,
    limit: str | None = None,
    desktop: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取知乎首页热榜/Get Zhihu Hot List"""
    params: dict[str, Any] = {}
    if limit is not None:
        params["limit"] = limit
    if desktop is not None:
        params["desktop"] = desktop
    return await proxy_request("zhihu", "/api/v1/zhihu/web/fetch_hot_list", params=params)

@router.get("/fetch_video_list")
async def fetch_video_list(
    request: Request,
    offset: str | None = None,
    limit: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取知乎首页视频榜/Get Zhihu Video List"""
    params: dict[str, Any] = {}
    if offset is not None:
        params["offset"] = offset
    if limit is not None:
        params["limit"] = limit
    return await proxy_request("zhihu", "/api/v1/zhihu/web/fetch_video_list", params=params)

@router.get("/fetch_article_search_v3")
async def fetch_article_search_v3(
    keyword: str,
    request: Request,
    offset: str | None = None,
    limit: str | None = None,
    show_all_topics: int | None = None,
    search_source: str | None = None,
    search_hash_id: str | None = None,
    vertical: str | None = None,
    sort: str | None = None,
    time_interval: str | None = None,
    vertical_info: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取知乎文章搜索V3/Get Zhihu Article Search V3"""
    params: dict[str, Any] = {}
    if keyword is not None:
        params["keyword"] = keyword
    if offset is not None:
        params["offset"] = offset
    if limit is not None:
        params["limit"] = limit
    if show_all_topics is not None:
        params["show_all_topics"] = show_all_topics
    if search_source is not None:
        params["search_source"] = search_source
    if search_hash_id is not None:
        params["search_hash_id"] = search_hash_id
    if vertical is not None:
        params["vertical"] = vertical
    if sort is not None:
        params["sort"] = sort
    if time_interval is not None:
        params["time_interval"] = time_interval
    if vertical_info is not None:
        params["vertical_info"] = vertical_info
    return await proxy_request("zhihu", "/api/v1/zhihu/web/fetch_article_search_v3", params=params)

@router.get("/fetch_user_search_v3")
async def fetch_user_search_v3(
    keyword: str,
    request: Request,
    offset: str | None = None,
    limit: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取知乎用户搜索V3/Get Zhihu User Search V3"""
    params: dict[str, Any] = {}
    if keyword is not None:
        params["keyword"] = keyword
    if offset is not None:
        params["offset"] = offset
    if limit is not None:
        params["limit"] = limit
    return await proxy_request("zhihu", "/api/v1/zhihu/web/fetch_user_search_v3", params=params)

@router.get("/fetch_topic_search_v3")
async def fetch_topic_search_v3(
    keyword: str,
    request: Request,
    offset: str | None = None,
    limit: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取知乎话题搜索V3/Get Zhihu Topic Search V3"""
    params: dict[str, Any] = {}
    if keyword is not None:
        params["keyword"] = keyword
    if offset is not None:
        params["offset"] = offset
    if limit is not None:
        params["limit"] = limit
    return await proxy_request("zhihu", "/api/v1/zhihu/web/fetch_topic_search_v3", params=params)

@router.post("/fetch_scholar_search_v3")
async def fetch_scholar_search_v3(
    keyword: str,
    request: Request,
    offset: str | None = None,
    limit: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取知乎论文搜索V3/Get Zhihu Scholar Search V3"""
    body = await request.json()
    params: dict[str, Any] = {}
    if keyword is not None:
        params["keyword"] = keyword
    if offset is not None:
        params["offset"] = offset
    if limit is not None:
        params["limit"] = limit
    return await proxy_request("zhihu", "/api/v1/zhihu/web/fetch_scholar_search_v3", params=params, json_body=body)

@router.get("/fetch_ai_search")
async def fetch_ai_search(
    message_content: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取知乎AI搜索/Get Zhihu AI Search"""
    params: dict[str, Any] = {}
    if message_content is not None:
        params["message_content"] = message_content
    return await proxy_request("zhihu", "/api/v1/zhihu/web/fetch_ai_search", params=params)

@router.get("/fetch_ai_search_result")
async def fetch_ai_search_result(
    message_id: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取知乎AI搜索结果/Get Zhihu AI Search Result"""
    params: dict[str, Any] = {}
    if message_id is not None:
        params["message_id"] = message_id
    return await proxy_request("zhihu", "/api/v1/zhihu/web/fetch_ai_search_result", params=params)

@router.get("/fetch_video_search_v3")
async def fetch_video_search_v3(
    keyword: str,
    request: Request,
    limit: str | None = None,
    offset: str | None = None,
    search_hash_id: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取知乎视频搜索V3/Get Zhihu Video Search V3"""
    params: dict[str, Any] = {}
    if keyword is not None:
        params["keyword"] = keyword
    if limit is not None:
        params["limit"] = limit
    if offset is not None:
        params["offset"] = offset
    if search_hash_id is not None:
        params["search_hash_id"] = search_hash_id
    return await proxy_request("zhihu", "/api/v1/zhihu/web/fetch_video_search_v3", params=params)

@router.get("/fetch_column_search_v3")
async def fetch_column_search_v3(
    keyword: str,
    request: Request,
    offset: str | None = None,
    limit: str | None = None,
    search_hash_id: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取知乎专栏搜索V3/Get Zhihu Column Search V3"""
    params: dict[str, Any] = {}
    if keyword is not None:
        params["keyword"] = keyword
    if offset is not None:
        params["offset"] = offset
    if limit is not None:
        params["limit"] = limit
    if search_hash_id is not None:
        params["search_hash_id"] = search_hash_id
    return await proxy_request("zhihu", "/api/v1/zhihu/web/fetch_column_search_v3", params=params)

@router.get("/fetch_salt_search_v3")
async def fetch_salt_search_v3(
    keyword: str,
    request: Request,
    offset: str | None = None,
    limit: str | None = None,
    search_hash_id: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取知乎盐选内容搜索V3/Get Zhihu Salt Search V3"""
    params: dict[str, Any] = {}
    if keyword is not None:
        params["keyword"] = keyword
    if offset is not None:
        params["offset"] = offset
    if limit is not None:
        params["limit"] = limit
    if search_hash_id is not None:
        params["search_hash_id"] = search_hash_id
    return await proxy_request("zhihu", "/api/v1/zhihu/web/fetch_salt_search_v3", params=params)

@router.get("/fetch_ebook_search_v3")
async def fetch_ebook_search_v3(
    keyword: str,
    request: Request,
    offset: str | None = None,
    limit: str | None = None,
    search_hash_id: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取知乎电子书搜索V3/Get Zhihu Ebook Search V3"""
    params: dict[str, Any] = {}
    if keyword is not None:
        params["keyword"] = keyword
    if offset is not None:
        params["offset"] = offset
    if limit is not None:
        params["limit"] = limit
    if search_hash_id is not None:
        params["search_hash_id"] = search_hash_id
    return await proxy_request("zhihu", "/api/v1/zhihu/web/fetch_ebook_search_v3", params=params)

@router.get("/fetch_preset_search")
async def fetch_preset_search(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取知乎搜索预设词/Get Zhihu Preset Search"""
    return await proxy_request("zhihu", "/api/v1/zhihu/web/fetch_preset_search")

@router.get("/fetch_search_recommend")
async def fetch_search_recommend(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取知乎搜索发现/Get Zhihu Search Recommend"""
    return await proxy_request("zhihu", "/api/v1/zhihu/web/fetch_search_recommend")

@router.get("/fetch_search_suggest")
async def fetch_search_suggest(
    keyword: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """知乎搜索预测词/Get Zhihu Search Suggest"""
    params: dict[str, Any] = {}
    if keyword is not None:
        params["keyword"] = keyword
    return await proxy_request("zhihu", "/api/v1/zhihu/web/fetch_search_suggest", params=params)

@router.get("/fetch_comment_v5")
async def fetch_comment_v5(
    answer_id: str,
    request: Request,
    order_by: str | None = None,
    limit: str | None = None,
    offset: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取知乎评论区V5/Get Zhihu Comment V5"""
    params: dict[str, Any] = {}
    if answer_id is not None:
        params["answer_id"] = answer_id
    if order_by is not None:
        params["order_by"] = order_by
    if limit is not None:
        params["limit"] = limit
    if offset is not None:
        params["offset"] = offset
    return await proxy_request("zhihu", "/api/v1/zhihu/web/fetch_comment_v5", params=params)

@router.get("/fetch_sub_comment_v5")
async def fetch_sub_comment_v5(
    comment_id: str,
    request: Request,
    order_by: str | None = None,
    limit: str | None = None,
    offset: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取知乎子评论区V5/Get Zhihu Sub Comment V5"""
    params: dict[str, Any] = {}
    if comment_id is not None:
        params["comment_id"] = comment_id
    if order_by is not None:
        params["order_by"] = order_by
    if limit is not None:
        params["limit"] = limit
    if offset is not None:
        params["offset"] = offset
    return await proxy_request("zhihu", "/api/v1/zhihu/web/fetch_sub_comment_v5", params=params)

@router.get("/fetch_user_info")
async def fetch_user_info(
    user_url_token: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取知乎用户信息/Get Zhihu User Info"""
    params: dict[str, Any] = {}
    if user_url_token is not None:
        params["user_url_token"] = user_url_token
    return await proxy_request("zhihu", "/api/v1/zhihu/web/fetch_user_info", params=params)

@router.get("/fetch_user_followees")
async def fetch_user_followees(
    user_url_token: str,
    request: Request,
    offset: str | None = None,
    limit: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取知乎用户关注列表/Get Zhihu User Following"""
    params: dict[str, Any] = {}
    if user_url_token is not None:
        params["user_url_token"] = user_url_token
    if offset is not None:
        params["offset"] = offset
    if limit is not None:
        params["limit"] = limit
    return await proxy_request("zhihu", "/api/v1/zhihu/web/fetch_user_followees", params=params)

@router.get("/fetch_user_followers")
async def fetch_user_followers(
    user_url_token: str,
    request: Request,
    offset: str | None = None,
    limit: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取知乎用户粉丝列表/Get Zhihu User Followers"""
    params: dict[str, Any] = {}
    if user_url_token is not None:
        params["user_url_token"] = user_url_token
    if offset is not None:
        params["offset"] = offset
    if limit is not None:
        params["limit"] = limit
    return await proxy_request("zhihu", "/api/v1/zhihu/web/fetch_user_followers", params=params)

@router.get("/fetch_user_articles")
async def fetch_user_articles(
    user_url_token: str,
    request: Request,
    offset: str | None = None,
    limit: str | None = None,
    sort_type: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取知乎用户的文章列表/Get Zhihu User Articles"""
    params: dict[str, Any] = {}
    if user_url_token is not None:
        params["user_url_token"] = user_url_token
    if offset is not None:
        params["offset"] = offset
    if limit is not None:
        params["limit"] = limit
    if sort_type is not None:
        params["sort_type"] = sort_type
    return await proxy_request("zhihu", "/api/v1/zhihu/web/fetch_user_articles", params=params)

@router.get("/fetch_user_included_articles")
async def fetch_user_included_articles(
    user_url_token: str,
    request: Request,
    offset: str | None = None,
    limit: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取知乎用户的被收录文章列表/Get Zhihu User Included Articles"""
    params: dict[str, Any] = {}
    if user_url_token is not None:
        params["user_url_token"] = user_url_token
    if offset is not None:
        params["offset"] = offset
    if limit is not None:
        params["limit"] = limit
    return await proxy_request("zhihu", "/api/v1/zhihu/web/fetch_user_included_articles", params=params)

@router.get("/fetch_user_follow_columns")
async def fetch_user_follow_columns(
    user_url_token: str,
    request: Request,
    offset: str | None = None,
    limit: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取知乎用户订阅的专栏/Get Zhihu User Columns"""
    params: dict[str, Any] = {}
    if user_url_token is not None:
        params["user_url_token"] = user_url_token
    if offset is not None:
        params["offset"] = offset
    if limit is not None:
        params["limit"] = limit
    return await proxy_request("zhihu", "/api/v1/zhihu/web/fetch_user_follow_columns", params=params)

@router.get("/fetch_user_follow_questions")
async def fetch_user_follow_questions(
    user_url_token: str,
    request: Request,
    offset: str | None = None,
    limit: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取知乎用户关注的问题/Get Zhihu User Follow Questions"""
    params: dict[str, Any] = {}
    if user_url_token is not None:
        params["user_url_token"] = user_url_token
    if offset is not None:
        params["offset"] = offset
    if limit is not None:
        params["limit"] = limit
    return await proxy_request("zhihu", "/api/v1/zhihu/web/fetch_user_follow_questions", params=params)

@router.get("/fetch_user_follow_collections")
async def fetch_user_follow_collections(
    user_url_token: str,
    request: Request,
    offset: str | None = None,
    limit: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取知乎用户关注的收藏/Get Zhihu User Follow Collections"""
    params: dict[str, Any] = {}
    if user_url_token is not None:
        params["user_url_token"] = user_url_token
    if offset is not None:
        params["offset"] = offset
    if limit is not None:
        params["limit"] = limit
    return await proxy_request("zhihu", "/api/v1/zhihu/web/fetch_user_follow_collections", params=params)

@router.get("/fetch_user_follow_topics")
async def fetch_user_follow_topics(
    user_url_token: str,
    request: Request,
    offset: str | None = None,
    limit: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取知乎用户关注的话题/Get Zhihu User Follow Topics"""
    params: dict[str, Any] = {}
    if user_url_token is not None:
        params["user_url_token"] = user_url_token
    if offset is not None:
        params["offset"] = offset
    if limit is not None:
        params["limit"] = limit
    return await proxy_request("zhihu", "/api/v1/zhihu/web/fetch_user_follow_topics", params=params)

@router.get("/fetch_recommend_followees")
async def fetch_recommend_followees(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取知乎推荐关注列表/Get Zhihu Recommend Followees"""
    return await proxy_request("zhihu", "/api/v1/zhihu/web/fetch_recommend_followees")

@router.get("/fetch_question_answers")
async def fetch_question_answers(
    question_id: str,
    request: Request,
    cursor: str | None = None,
    limit: int | None = None,
    offset: int | None = None,
    order: str | None = None,
    session_id: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取知乎问题回答列表/Get Zhihu Question Answers"""
    params: dict[str, Any] = {}
    if question_id is not None:
        params["question_id"] = question_id
    if cursor is not None:
        params["cursor"] = cursor
    if limit is not None:
        params["limit"] = limit
    if offset is not None:
        params["offset"] = offset
    if order is not None:
        params["order"] = order
    if session_id is not None:
        params["session_id"] = session_id
    return await proxy_request("zhihu", "/api/v1/zhihu/web/fetch_question_answers", params=params)
