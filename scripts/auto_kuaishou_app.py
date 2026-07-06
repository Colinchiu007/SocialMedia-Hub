"""Auto-generated routes for Kuaishou-App-API."""

from __future__ import annotations

from typing import Any

from fastapi import APIRouter, Depends, Request

from socialmedia_hub.server._core import proxy_request, verify_api_key

router = APIRouter(prefix="/api/v1/kuaishou/app", tags=["kuaishou_app"])

@router.get("/fetch_one_video")
async def fetch_one_video(
    photo_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """视频详情V1/Video detailsV1"""
        params: dict[str, Any] = {}
        if photo_id is not None:
            params["photo_id"] = photo_id
        body = await request.json()
        return await proxy_request("kuaishou", "/api/v1/kuaishou/app/fetch_one_video", json_body=body)

@router.get("/fetch_videos_batch")
async def fetch_videos_batch(
    photo_ids: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """快手批量视频查询接口/Kuaishou batch video query API"""
        params: dict[str, Any] = {}
        if photo_ids is not None:
            params["photo_ids"] = photo_ids
        body = await request.json()
        return await proxy_request("kuaishou", "/api/v1/kuaishou/app/fetch_videos_batch", json_body=body)

@router.get("/fetch_one_video_by_url")
async def fetch_one_video_by_url(
    share_text: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """根据链接获取单个作品数据/Fetch single video by URL"""
        params: dict[str, Any] = {}
        if share_text is not None:
            params["share_text"] = share_text
        body = await request.json()
        return await proxy_request("kuaishou", "/api/v1/kuaishou/app/fetch_one_video_by_url", json_body=body)

@router.get("/fetch_one_video_comment")
async def fetch_one_video_comment(
    pcursor: str | None = None,
    photo_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取单个作品评论数据/Get single video comment data"""
        params: dict[str, Any] = {}
        if photo_id is not None:
            params["photo_id"] = photo_id
        if pcursor is not None:
            params["pcursor"] = pcursor
        body = await request.json()
        return await proxy_request("kuaishou", "/api/v1/kuaishou/app/fetch_one_video_comment", json_body=body)

@router.get("/fetch_one_user_v2")
async def fetch_one_user_v2(
    user_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取单个用户数据V2/Get single user data V2"""
        params: dict[str, Any] = {}
        if user_id is not None:
            params["user_id"] = user_id
        body = await request.json()
        return await proxy_request("kuaishou", "/api/v1/kuaishou/app/fetch_one_user_v2", json_body=body)

@router.get("/fetch_user_live_info")
async def fetch_user_live_info(
    user_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户直播信息/Get user live info"""
        params: dict[str, Any] = {}
        if user_id is not None:
            params["user_id"] = user_id
        body = await request.json()
        return await proxy_request("kuaishou", "/api/v1/kuaishou/app/fetch_user_live_info", json_body=body)

@router.get("/fetch_user_hot_post")
async def fetch_user_hot_post(
    pcursor: str | None = None,
    user_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户热门作品数据/Get user hot post data"""
        params: dict[str, Any] = {}
        if user_id is not None:
            params["user_id"] = user_id
        if pcursor is not None:
            params["pcursor"] = pcursor
        body = await request.json()
        return await proxy_request("kuaishou", "/api/v1/kuaishou/app/fetch_user_hot_post", json_body=body)

@router.get("/fetch_user_post_v2")
async def fetch_user_post_v2(
    pcursor: str | None = None,
    user_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """用户视频列表V2/User video list V2"""
        params: dict[str, Any] = {}
        if user_id is not None:
            params["user_id"] = user_id
        if pcursor is not None:
            params["pcursor"] = pcursor
        body = await request.json()
        return await proxy_request("kuaishou", "/api/v1/kuaishou/app/fetch_user_post_v2", json_body=body)

@router.get("/search_comprehensive")
async def search_comprehensive(
    search_scope: str | None = None,
    duration: str | None = None,
    publish_time: str | None = None,
    sort_type: str | None = None,
    pcursor: str | None = None,
    keyword: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """综合搜索/Comprehensive search"""
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
        body = await request.json()
        return await proxy_request("kuaishou", "/api/v1/kuaishou/app/search_comprehensive", json_body=body)

@router.get("/search_video_v2")
async def search_video_v2(
    page: str | None = None,
    keyword: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """搜索视频V2/Search video V2"""
        params: dict[str, Any] = {}
        if keyword is not None:
            params["keyword"] = keyword
        if page is not None:
            params["page"] = page
        body = await request.json()
        return await proxy_request("kuaishou", "/api/v1/kuaishou/app/search_video_v2", json_body=body)

@router.get("/search_user_v2")
async def search_user_v2(
    page: str | None = None,
    keyword: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """搜索用户V2/Search user V2"""
        params: dict[str, Any] = {}
        if keyword is not None:
            params["keyword"] = keyword
        if page is not None:
            params["page"] = page
        body = await request.json()
        return await proxy_request("kuaishou", "/api/v1/kuaishou/app/search_user_v2", json_body=body)

@router.get("/fetch_hot_board_categories")
async def fetch_hot_board_categories(
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """快手热榜分类/Kuaishou hot categories"""
        body = await request.json()
        return await proxy_request("kuaishou", "/api/v1/kuaishou/app/fetch_hot_board_categories", json_body=body)

@router.get("/fetch_hot_board_detail")
async def fetch_hot_board_detail(
    boardId: int | None = None,
    boardType: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """快手热榜详情/Kuaishou hot board detail"""
        params: dict[str, Any] = {}
        if boardType is not None:
            params["boardType"] = boardType
        if boardId is not None:
            params["boardId"] = boardId
        body = await request.json()
        return await proxy_request("kuaishou", "/api/v1/kuaishou/app/fetch_hot_board_detail", json_body=body)

@router.get("/fetch_hot_search_person")
async def fetch_hot_search_person(
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """快手热搜人物榜单/Kuaishou hot search person board"""
        body = await request.json()
        return await proxy_request("kuaishou", "/api/v1/kuaishou/app/fetch_hot_search_person", json_body=body)

@router.get("/fetch_live_top_list")
async def fetch_live_top_list(
    subTabName: str | None = None,
    subTabId: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """快手直播榜单/Kuaishou live top list"""
        params: dict[str, Any] = {}
        if subTabId is not None:
            params["subTabId"] = subTabId
        if subTabName is not None:
            params["subTabName"] = subTabName
        body = await request.json()
        return await proxy_request("kuaishou", "/api/v1/kuaishou/app/fetch_live_top_list", json_body=body)

@router.get("/fetch_shopping_top_list")
async def fetch_shopping_top_list(
    subTabName: str | None = None,
    subTabId: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """快手购物榜单/Kuaishou shopping top list"""
        params: dict[str, Any] = {}
        if subTabId is not None:
            params["subTabId"] = subTabId
        if subTabName is not None:
            params["subTabName"] = subTabName
        body = await request.json()
        return await proxy_request("kuaishou", "/api/v1/kuaishou/app/fetch_shopping_top_list", json_body=body)

@router.get("/fetch_brand_top_list")
async def fetch_brand_top_list(
    subTabName: str | None = None,
    subTabId: int | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """快手品牌榜单/Kuaishou brand top list"""
        params: dict[str, Any] = {}
        if subTabId is not None:
            params["subTabId"] = subTabId
        if subTabName is not None:
            params["subTabName"] = subTabName
        body = await request.json()
        return await proxy_request("kuaishou", "/api/v1/kuaishou/app/fetch_brand_top_list", json_body=body)

@router.get("/generate_kuaishou_share_link")
async def generate_kuaishou_share_link(
    shareObjectId: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """生成快手分享链接/Generate Kuaishou share link"""
        params: dict[str, Any] = {}
        if shareObjectId is not None:
            params["shareObjectId"] = shareObjectId
        body = await request.json()
        return await proxy_request("kuaishou", "/api/v1/kuaishou/app/generate_kuaishou_share_link", json_body=body)

@router.get("/fetch_magic_face_usage")
async def fetch_magic_face_usage(
    magic_face_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取魔法表情使用人数/Fetch magic face usage count"""
        params: dict[str, Any] = {}
        if magic_face_id is not None:
            params["magic_face_id"] = magic_face_id
        body = await request.json()
        return await proxy_request("kuaishou", "/api/v1/kuaishou/app/fetch_magic_face_usage", json_body=body)

@router.get("/fetch_magic_face_hot")
async def fetch_magic_face_hot(
    count: int | None = None,
    pcursor: str | None = None,
    magic_face_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取魔法表情热门视频/Fetch magic face hot videos"""
        params: dict[str, Any] = {}
        if magic_face_id is not None:
            params["magic_face_id"] = magic_face_id
        if pcursor is not None:
            params["pcursor"] = pcursor
        if count is not None:
            params["count"] = count
        body = await request.json()
        return await proxy_request("kuaishou", "/api/v1/kuaishou/app/fetch_magic_face_hot", json_body=body)
