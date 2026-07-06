"""Auto-generated routes for Kuaishou-App-API."""

from __future__ import annotations

from typing import Any

from fastapi import APIRouter, Depends, Request

from socialmedia_hub.server._core import proxy_request, verify_api_key

router = APIRouter(prefix="/api/v1/kuaishou/app", tags=["kuaishou_app"])

@router.get("/fetch_one_video")
async def fetch_one_video(
    photo_id: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """视频详情V1/Video detailsV1"""
    body = await request.json()
    params: dict[str, Any] = {}
    if photo_id is not None:
        params["photo_id"] = photo_id
    return await proxy_request("kuaishou", "/api/v1/kuaishou/app/fetch_one_video", params=params, json_body=body)

@router.get("/fetch_videos_batch")
async def fetch_videos_batch(
    photo_ids: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """快手批量视频查询接口/Kuaishou batch video query API"""
    body = await request.json()
    params: dict[str, Any] = {}
    if photo_ids is not None:
        params["photo_ids"] = photo_ids
    return await proxy_request("kuaishou", "/api/v1/kuaishou/app/fetch_videos_batch", params=params, json_body=body)

@router.get("/fetch_one_video_by_url")
async def fetch_one_video_by_url(
    share_text: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """根据链接获取单个作品数据/Fetch single video by URL"""
    body = await request.json()
    params: dict[str, Any] = {}
    if share_text is not None:
        params["share_text"] = share_text
    return await proxy_request("kuaishou", "/api/v1/kuaishou/app/fetch_one_video_by_url", params=params, json_body=body)

@router.get("/fetch_one_video_comment")
async def fetch_one_video_comment(
    photo_id: str,
    request: Request,
    pcursor: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取单个作品评论数据/Get single video comment data"""
    body = await request.json()
    params: dict[str, Any] = {}
    if photo_id is not None:
        params["photo_id"] = photo_id
    if pcursor is not None:
        params["pcursor"] = pcursor
    return await proxy_request("kuaishou", "/api/v1/kuaishou/app/fetch_one_video_comment", params=params, json_body=body)

@router.get("/fetch_one_user_v2")
async def fetch_one_user_v2(
    user_id: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取单个用户数据V2/Get single user data V2"""
    body = await request.json()
    params: dict[str, Any] = {}
    if user_id is not None:
        params["user_id"] = user_id
    return await proxy_request("kuaishou", "/api/v1/kuaishou/app/fetch_one_user_v2", params=params, json_body=body)

@router.get("/fetch_user_live_info")
async def fetch_user_live_info(
    user_id: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户直播信息/Get user live info"""
    body = await request.json()
    params: dict[str, Any] = {}
    if user_id is not None:
        params["user_id"] = user_id
    return await proxy_request("kuaishou", "/api/v1/kuaishou/app/fetch_user_live_info", params=params, json_body=body)

@router.get("/fetch_user_hot_post")
async def fetch_user_hot_post(
    user_id: str,
    request: Request,
    pcursor: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户热门作品数据/Get user hot post data"""
    body = await request.json()
    params: dict[str, Any] = {}
    if user_id is not None:
        params["user_id"] = user_id
    if pcursor is not None:
        params["pcursor"] = pcursor
    return await proxy_request("kuaishou", "/api/v1/kuaishou/app/fetch_user_hot_post", params=params, json_body=body)

@router.get("/fetch_user_post_v2")
async def fetch_user_post_v2(
    user_id: str,
    request: Request,
    pcursor: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """用户视频列表V2/User video list V2"""
    body = await request.json()
    params: dict[str, Any] = {}
    if user_id is not None:
        params["user_id"] = user_id
    if pcursor is not None:
        params["pcursor"] = pcursor
    return await proxy_request("kuaishou", "/api/v1/kuaishou/app/fetch_user_post_v2", params=params, json_body=body)

@router.get("/search_comprehensive")
async def search_comprehensive(
    keyword: str,
    request: Request,
    pcursor: str | None = None,
    sort_type: str | None = None,
    publish_time: str | None = None,
    duration: str | None = None,
    search_scope: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """综合搜索/Comprehensive search"""
    body = await request.json()
    params: dict[str, Any] = {}
    if keyword is not None:
        params["keyword"] = keyword
    if pcursor is not None:
        params["pcursor"] = pcursor
    if sort_type is not None:
        params["sort_type"] = sort_type
    if publish_time is not None:
        params["publish_time"] = publish_time
    if duration is not None:
        params["duration"] = duration
    if search_scope is not None:
        params["search_scope"] = search_scope
    return await proxy_request("kuaishou", "/api/v1/kuaishou/app/search_comprehensive", params=params, json_body=body)

@router.get("/search_video_v2")
async def search_video_v2(
    keyword: str,
    request: Request,
    page: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """搜索视频V2/Search video V2"""
    body = await request.json()
    params: dict[str, Any] = {}
    if keyword is not None:
        params["keyword"] = keyword
    if page is not None:
        params["page"] = page
    return await proxy_request("kuaishou", "/api/v1/kuaishou/app/search_video_v2", params=params, json_body=body)

@router.get("/search_user_v2")
async def search_user_v2(
    keyword: str,
    request: Request,
    page: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """搜索用户V2/Search user V2"""
    body = await request.json()
    params: dict[str, Any] = {}
    if keyword is not None:
        params["keyword"] = keyword
    if page is not None:
        params["page"] = page
    return await proxy_request("kuaishou", "/api/v1/kuaishou/app/search_user_v2", params=params, json_body=body)

@router.get("/fetch_hot_board_categories")
async def fetch_hot_board_categories(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """快手热榜分类/Kuaishou hot categories"""
    body = await request.json()
    return await proxy_request("kuaishou", "/api/v1/kuaishou/app/fetch_hot_board_categories", json_body=body)

@router.get("/fetch_hot_board_detail")
async def fetch_hot_board_detail(
    request: Request,
    boardType: int | None = None,
    boardId: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """快手热榜详情/Kuaishou hot board detail"""
    body = await request.json()
    params: dict[str, Any] = {}
    if boardType is not None:
        params["boardType"] = boardType
    if boardId is not None:
        params["boardId"] = boardId
    return await proxy_request("kuaishou", "/api/v1/kuaishou/app/fetch_hot_board_detail", params=params, json_body=body)

@router.get("/fetch_hot_search_person")
async def fetch_hot_search_person(
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """快手热搜人物榜单/Kuaishou hot search person board"""
    body = await request.json()
    return await proxy_request("kuaishou", "/api/v1/kuaishou/app/fetch_hot_search_person", json_body=body)

@router.get("/fetch_live_top_list")
async def fetch_live_top_list(
    request: Request,
    subTabId: int | None = None,
    subTabName: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """快手直播榜单/Kuaishou live top list"""
    body = await request.json()
    params: dict[str, Any] = {}
    if subTabId is not None:
        params["subTabId"] = subTabId
    if subTabName is not None:
        params["subTabName"] = subTabName
    return await proxy_request("kuaishou", "/api/v1/kuaishou/app/fetch_live_top_list", params=params, json_body=body)

@router.get("/fetch_shopping_top_list")
async def fetch_shopping_top_list(
    request: Request,
    subTabId: int | None = None,
    subTabName: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """快手购物榜单/Kuaishou shopping top list"""
    body = await request.json()
    params: dict[str, Any] = {}
    if subTabId is not None:
        params["subTabId"] = subTabId
    if subTabName is not None:
        params["subTabName"] = subTabName
    return await proxy_request("kuaishou", "/api/v1/kuaishou/app/fetch_shopping_top_list", params=params, json_body=body)

@router.get("/fetch_brand_top_list")
async def fetch_brand_top_list(
    request: Request,
    subTabId: int | None = None,
    subTabName: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """快手品牌榜单/Kuaishou brand top list"""
    body = await request.json()
    params: dict[str, Any] = {}
    if subTabId is not None:
        params["subTabId"] = subTabId
    if subTabName is not None:
        params["subTabName"] = subTabName
    return await proxy_request("kuaishou", "/api/v1/kuaishou/app/fetch_brand_top_list", params=params, json_body=body)

@router.get("/generate_kuaishou_share_link")
async def generate_kuaishou_share_link(
    shareObjectId: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """生成快手分享链接/Generate Kuaishou share link"""
    body = await request.json()
    params: dict[str, Any] = {}
    if shareObjectId is not None:
        params["shareObjectId"] = shareObjectId
    return await proxy_request("kuaishou", "/api/v1/kuaishou/app/generate_kuaishou_share_link", params=params, json_body=body)

@router.get("/fetch_magic_face_usage")
async def fetch_magic_face_usage(
    magic_face_id: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取魔法表情使用人数/Fetch magic face usage count"""
    body = await request.json()
    params: dict[str, Any] = {}
    if magic_face_id is not None:
        params["magic_face_id"] = magic_face_id
    return await proxy_request("kuaishou", "/api/v1/kuaishou/app/fetch_magic_face_usage", params=params, json_body=body)

@router.get("/fetch_magic_face_hot")
async def fetch_magic_face_hot(
    magic_face_id: str,
    request: Request,
    pcursor: str | None = None,
    count: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取魔法表情热门视频/Fetch magic face hot videos"""
    body = await request.json()
    params: dict[str, Any] = {}
    if magic_face_id is not None:
        params["magic_face_id"] = magic_face_id
    if pcursor is not None:
        params["pcursor"] = pcursor
    if count is not None:
        params["count"] = count
    return await proxy_request("kuaishou", "/api/v1/kuaishou/app/fetch_magic_face_hot", params=params, json_body=body)
