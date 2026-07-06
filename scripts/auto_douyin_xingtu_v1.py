"""Auto-generated routes for Douyin-Xingtu-API."""

from __future__ import annotations

from typing import Any

from fastapi import APIRouter, Depends, Request

from socialmedia_hub.server._core import proxy_request, verify_api_key

router = APIRouter(prefix="/api/v1/douyin/xingtu/v1", tags=["douyin_xingtu"])

@router.get("/get_sign_image")
async def get_sign_image(
    format: str | None = None,
    durationTS: int | None = None,
    uri: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取加密图片解析/Get Sign Image"""
        params: dict[str, Any] = {}
        if uri is not None:
            params["uri"] = uri
        if durationTS is not None:
            params["durationTS"] = durationTS
        if format is not None:
            params["format"] = format
        body = await request.json()
        return await proxy_request("douyin", "/api/v1/douyin/xingtu/get_sign_image", json_body=body)

@router.get("/get_xingtu_kolid_by_uid")
async def get_xingtu_kolid_by_uid(
    uid: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """根据抖音用户ID获取游客星图kolid/Get XingTu kolid by Douyin User ID"""
        params: dict[str, Any] = {}
        if uid is not None:
            params["uid"] = uid
        body = await request.json()
        return await proxy_request("douyin", "/api/v1/douyin/xingtu/get_xingtu_kolid_by_uid", json_body=body)

@router.get("/get_xingtu_kolid_by_sec_user_id")
async def get_xingtu_kolid_by_sec_user_id(
    sec_user_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """根据抖音sec_user_id获取游客星图kolid/Get XingTu kolid by Douyin sec_user_id"""
        params: dict[str, Any] = {}
        if sec_user_id is not None:
            params["sec_user_id"] = sec_user_id
        body = await request.json()
        return await proxy_request("douyin", "/api/v1/douyin/xingtu/get_xingtu_kolid_by_sec_user_id", json_body=body)

@router.get("/get_xingtu_kolid_by_unique_id")
async def get_xingtu_kolid_by_unique_id(
    unique_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """根据抖音号获取游客星图kolid/Get XingTu kolid by Douyin unique_id"""
        params: dict[str, Any] = {}
        if unique_id is not None:
            params["unique_id"] = unique_id
        body = await request.json()
        return await proxy_request("douyin", "/api/v1/douyin/xingtu/get_xingtu_kolid_by_unique_id", json_body=body)

@router.get("/kol_base_info_v1")
async def kol_base_info_v1(
    platformChannel: str,
    kolId: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取kol基本信息V1/Get kol Base Info V1"""
        params: dict[str, Any] = {}
        if kolId is not None:
            params["kolId"] = kolId
        if platformChannel is not None:
            params["platformChannel"] = platformChannel
        body = await request.json()
        return await proxy_request("douyin", "/api/v1/douyin/xingtu/kol_base_info_v1", json_body=body)

@router.get("/kol_audience_portrait_v1")
async def kol_audience_portrait_v1(
    kolId: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取kol观众画像V1/Get kol Audience Portrait V1"""
        params: dict[str, Any] = {}
        if kolId is not None:
            params["kolId"] = kolId
        body = await request.json()
        return await proxy_request("douyin", "/api/v1/douyin/xingtu/kol_audience_portrait_v1", json_body=body)

@router.get("/kol_fans_portrait_v1")
async def kol_fans_portrait_v1(
    fansType: str | None = None,
    kolId: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取kol粉丝画像V1/Get kol Fans Portrait V1"""
        params: dict[str, Any] = {}
        if kolId is not None:
            params["kolId"] = kolId
        if fansType is not None:
            params["fansType"] = fansType
        body = await request.json()
        return await proxy_request("douyin", "/api/v1/douyin/xingtu/kol_fans_portrait_v1", json_body=body)

@router.get("/kol_service_price_v1")
async def kol_service_price_v1(
    platformChannel: str,
    kolId: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取kol服务报价V1/Get kol Service Price V1"""
        params: dict[str, Any] = {}
        if kolId is not None:
            params["kolId"] = kolId
        if platformChannel is not None:
            params["platformChannel"] = platformChannel
        body = await request.json()
        return await proxy_request("douyin", "/api/v1/douyin/xingtu/kol_service_price_v1", json_body=body)

@router.get("/kol_data_overview_v1")
async def kol_data_overview_v1(
    onlyAssign: bool | None = None,
    flowType: int,
    _range: str,
    _type: str,
    kolId: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取kol数据概览V1/Get kol Data Overview V1"""
        params: dict[str, Any] = {}
        if kolId is not None:
            params["kolId"] = kolId
        if _type is not None:
            params["_type"] = _type
        if _range is not None:
            params["_range"] = _range
        if flowType is not None:
            params["flowType"] = flowType
        if onlyAssign is not None:
            params["onlyAssign"] = onlyAssign
        body = await request.json()
        return await proxy_request("douyin", "/api/v1/douyin/xingtu/kol_data_overview_v1", json_body=body)

@router.get("/search_kol_v1")
async def search_kol_v1(
    page: int,
    platformSource: str,
    keyword: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """关键词搜索kol V1/Search Kol V1"""
        params: dict[str, Any] = {}
        if keyword is not None:
            params["keyword"] = keyword
        if platformSource is not None:
            params["platformSource"] = platformSource
        if page is not None:
            params["page"] = page
        body = await request.json()
        return await proxy_request("douyin", "/api/v1/douyin/xingtu/search_kol_v1", json_body=body)

@router.get("/search_kol_v2")
async def search_kol_v2(
    contentTag: str | None = None,
    followerRange: str | None = None,
    keyword: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """高级搜索kol V2/Search Kol Advanced V2"""
        params: dict[str, Any] = {}
        if keyword is not None:
            params["keyword"] = keyword
        if followerRange is not None:
            params["followerRange"] = followerRange
        if contentTag is not None:
            params["contentTag"] = contentTag
        body = await request.json()
        return await proxy_request("douyin", "/api/v1/douyin/xingtu/search_kol_v2", json_body=body)

@router.get("/kol_conversion_ability_analysis_v1")
async def kol_conversion_ability_analysis_v1(
    _range: str,
    kolId: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取kol转化能力分析V1/Get kol Conversion Ability Analysis V1"""
        params: dict[str, Any] = {}
        if kolId is not None:
            params["kolId"] = kolId
        if _range is not None:
            params["_range"] = _range
        body = await request.json()
        return await proxy_request("douyin", "/api/v1/douyin/xingtu/kol_conversion_ability_analysis_v1", json_body=body)

@router.get("/kol_video_performance_v1")
async def kol_video_performance_v1(
    onlyAssign: bool,
    kolId: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取kol视频表现V1/Get kol Video Performance V1"""
        params: dict[str, Any] = {}
        if kolId is not None:
            params["kolId"] = kolId
        if onlyAssign is not None:
            params["onlyAssign"] = onlyAssign
        body = await request.json()
        return await proxy_request("douyin", "/api/v1/douyin/xingtu/kol_video_performance_v1", json_body=body)

@router.get("/kol_xingtu_index_v1")
async def kol_xingtu_index_v1(
    kolId: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取kol星图指数V1/Get kol Xingtu Index V1"""
        params: dict[str, Any] = {}
        if kolId is not None:
            params["kolId"] = kolId
        body = await request.json()
        return await proxy_request("douyin", "/api/v1/douyin/xingtu/kol_xingtu_index_v1", json_body=body)

@router.get("/kol_convert_video_display_v1")
async def kol_convert_video_display_v1(
    page: int,
    detailType: str,
    kolId: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取kol转化视频展示V1/Get kol Convert Video Display V1"""
        params: dict[str, Any] = {}
        if kolId is not None:
            params["kolId"] = kolId
        if detailType is not None:
            params["detailType"] = detailType
        if page is not None:
            params["page"] = page
        body = await request.json()
        return await proxy_request("douyin", "/api/v1/douyin/xingtu/kol_convert_video_display_v1", json_body=body)

@router.get("/kol_link_struct_v1")
async def kol_link_struct_v1(
    kolId: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取kol连接用户V1/Get kol Link Struct V1"""
        params: dict[str, Any] = {}
        if kolId is not None:
            params["kolId"] = kolId
        body = await request.json()
        return await proxy_request("douyin", "/api/v1/douyin/xingtu/kol_link_struct_v1", json_body=body)

@router.get("/kol_touch_distribution_v1")
async def kol_touch_distribution_v1(
    kolId: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取kol连接用户来源V1/Get kol Touch Distribution V1"""
        params: dict[str, Any] = {}
        if kolId is not None:
            params["kolId"] = kolId
        body = await request.json()
        return await proxy_request("douyin", "/api/v1/douyin/xingtu/kol_touch_distribution_v1", json_body=body)

@router.get("/kol_cp_info_v1")
async def kol_cp_info_v1(
    kolId: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取kol性价比能力分析V1/Get kol Cp Info V1"""
        params: dict[str, Any] = {}
        if kolId is not None:
            params["kolId"] = kolId
        body = await request.json()
        return await proxy_request("douyin", "/api/v1/douyin/xingtu/kol_cp_info_v1", json_body=body)

@router.get("/kol_rec_videos_v1")
async def kol_rec_videos_v1(
    kolId: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取kol内容表现V1/Get kol Rec Videos V1"""
        params: dict[str, Any] = {}
        if kolId is not None:
            params["kolId"] = kolId
        body = await request.json()
        return await proxy_request("douyin", "/api/v1/douyin/xingtu/kol_rec_videos_v1", json_body=body)

@router.get("/kol_daily_fans_v1")
async def kol_daily_fans_v1(
    endDate: str,
    startDate: str,
    kolId: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取kol粉丝趋势V1/Get kol Daily Fans V1"""
        params: dict[str, Any] = {}
        if kolId is not None:
            params["kolId"] = kolId
        if startDate is not None:
            params["startDate"] = startDate
        if endDate is not None:
            params["endDate"] = endDate
        body = await request.json()
        return await proxy_request("douyin", "/api/v1/douyin/xingtu/kol_daily_fans_v1", json_body=body)

@router.get("/author_hot_comment_tokens_v1")
async def author_hot_comment_tokens_v1(
    kolId: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取kol热词分析评论V1/Get Author Hot Comment Tokens V1"""
        params: dict[str, Any] = {}
        if kolId is not None:
            params["kolId"] = kolId
        body = await request.json()
        return await proxy_request("douyin", "/api/v1/douyin/xingtu/author_hot_comment_tokens_v1", json_body=body)

@router.get("/author_content_hot_comment_keywords_v1")
async def author_content_hot_comment_keywords_v1(
    kolId: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取kol热词分析内容V1/Get Author Content Hot Comment Keywords V1"""
        params: dict[str, Any] = {}
        if kolId is not None:
            params["kolId"] = kolId
        body = await request.json()
        return await proxy_request("douyin", "/api/v1/douyin/xingtu/author_content_hot_comment_keywords_v1", json_body=body)
