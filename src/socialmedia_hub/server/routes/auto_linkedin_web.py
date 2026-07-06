"""Auto-generated routes for LinkedIn-Web-API."""

from __future__ import annotations

from typing import Any

from fastapi import APIRouter, Depends, Request

from socialmedia_hub.server._core import proxy_request, verify_api_key

router = APIRouter(prefix="/api/v1/linkedin/web", tags=["linkedin_web"])

@router.get("/get_user_profile")
async def get_user_profile(
    username: str,
    request: Request,
    include_follower_and_connection: str | None = None,
    include_experiences: str | None = None,
    include_skills: str | None = None,
    include_certifications: str | None = None,
    include_publications: str | None = None,
    include_educations: str | None = None,
    include_volunteers: str | None = None,
    include_honors: str | None = None,
    include_interests: str | None = None,
    include_bio: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户资料/Get user profile"""
    body = await request.json()
    params: dict[str, Any] = {}
    if username is not None:
        params["username"] = username
    if include_follower_and_connection is not None:
        params["include_follower_and_connection"] = include_follower_and_connection
    if include_experiences is not None:
        params["include_experiences"] = include_experiences
    if include_skills is not None:
        params["include_skills"] = include_skills
    if include_certifications is not None:
        params["include_certifications"] = include_certifications
    if include_publications is not None:
        params["include_publications"] = include_publications
    if include_educations is not None:
        params["include_educations"] = include_educations
    if include_volunteers is not None:
        params["include_volunteers"] = include_volunteers
    if include_honors is not None:
        params["include_honors"] = include_honors
    if include_interests is not None:
        params["include_interests"] = include_interests
    if include_bio is not None:
        params["include_bio"] = include_bio
    return await proxy_request("linkedin", "/api/v1/linkedin/web/get_user_profile", params=params, json_body=body)

@router.get("/get_user_posts")
async def get_user_posts(
    urn: str,
    request: Request,
    page: str | None = None,
    pagination_token: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户帖子/Get user posts"""
    body = await request.json()
    params: dict[str, Any] = {}
    if urn is not None:
        params["urn"] = urn
    if page is not None:
        params["page"] = page
    if pagination_token is not None:
        params["pagination_token"] = pagination_token
    return await proxy_request("linkedin", "/api/v1/linkedin/web/get_user_posts", params=params, json_body=body)

@router.get("/get_user_comments")
async def get_user_comments(
    urn: str,
    request: Request,
    page: str | None = None,
    pagination_token: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户评论/Get user comments"""
    body = await request.json()
    params: dict[str, Any] = {}
    if urn is not None:
        params["urn"] = urn
    if page is not None:
        params["page"] = page
    if pagination_token is not None:
        params["pagination_token"] = pagination_token
    return await proxy_request("linkedin", "/api/v1/linkedin/web/get_user_comments", params=params, json_body=body)

@router.get("/get_user_contact")
async def get_user_contact(
    username: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户联系信息/Get user contact information"""
    body = await request.json()
    params: dict[str, Any] = {}
    if username is not None:
        params["username"] = username
    return await proxy_request("linkedin", "/api/v1/linkedin/web/get_user_contact", params=params, json_body=body)

@router.get("/get_user_recommendations")
async def get_user_recommendations(
    urn: str,
    request: Request,
    page: str | None = None,
    type: str | None = None,
    pagination_token: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户推荐信/Get user recommendations"""
    body = await request.json()
    params: dict[str, Any] = {}
    if urn is not None:
        params["urn"] = urn
    if page is not None:
        params["page"] = page
    if type is not None:
        params["type"] = type
    if pagination_token is not None:
        params["pagination_token"] = pagination_token
    return await proxy_request("linkedin", "/api/v1/linkedin/web/get_user_recommendations", params=params, json_body=body)

@router.get("/get_user_videos")
async def get_user_videos(
    urn: str,
    request: Request,
    page: str | None = None,
    pagination_token: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户视频/Get user videos"""
    body = await request.json()
    params: dict[str, Any] = {}
    if urn is not None:
        params["urn"] = urn
    if page is not None:
        params["page"] = page
    if pagination_token is not None:
        params["pagination_token"] = pagination_token
    return await proxy_request("linkedin", "/api/v1/linkedin/web/get_user_videos", params=params, json_body=body)

@router.get("/get_user_images")
async def get_user_images(
    urn: str,
    request: Request,
    page: str | None = None,
    pagination_token: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户图片/Get user images"""
    body = await request.json()
    params: dict[str, Any] = {}
    if urn is not None:
        params["urn"] = urn
    if page is not None:
        params["page"] = page
    if pagination_token is not None:
        params["pagination_token"] = pagination_token
    return await proxy_request("linkedin", "/api/v1/linkedin/web/get_user_images", params=params, json_body=body)

@router.get("/get_company_profile")
async def get_company_profile(
    request: Request,
    company: str | None = None,
    company_id: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取公司资料/Get company profile"""
    body = await request.json()
    params: dict[str, Any] = {}
    if company is not None:
        params["company"] = company
    if company_id is not None:
        params["company_id"] = company_id
    return await proxy_request("linkedin", "/api/v1/linkedin/web/get_company_profile", params=params, json_body=body)

@router.get("/get_company_people")
async def get_company_people(
    company_id: str,
    request: Request,
    page: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取公司员工/Get company people"""
    body = await request.json()
    params: dict[str, Any] = {}
    if company_id is not None:
        params["company_id"] = company_id
    if page is not None:
        params["page"] = page
    return await proxy_request("linkedin", "/api/v1/linkedin/web/get_company_people", params=params, json_body=body)

@router.get("/get_company_posts")
async def get_company_posts(
    company_id: str,
    request: Request,
    page: str | None = None,
    sort_by: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取公司帖子/Get company posts"""
    body = await request.json()
    params: dict[str, Any] = {}
    if company_id is not None:
        params["company_id"] = company_id
    if page is not None:
        params["page"] = page
    if sort_by is not None:
        params["sort_by"] = sort_by
    return await proxy_request("linkedin", "/api/v1/linkedin/web/get_company_posts", params=params, json_body=body)

@router.get("/get_company_jobs")
async def get_company_jobs(
    company_id: str,
    request: Request,
    page: str | None = None,
    sort_by: str | None = None,
    date_posted: str | None = None,
    experience_level: str | None = None,
    remote: str | None = None,
    job_type: str | None = None,
    easy_apply: str | None = None,
    under_10_applicants: str | None = None,
    fair_chance_employer: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取公司职位/Get company jobs"""
    body = await request.json()
    params: dict[str, Any] = {}
    if company_id is not None:
        params["company_id"] = company_id
    if page is not None:
        params["page"] = page
    if sort_by is not None:
        params["sort_by"] = sort_by
    if date_posted is not None:
        params["date_posted"] = date_posted
    if experience_level is not None:
        params["experience_level"] = experience_level
    if remote is not None:
        params["remote"] = remote
    if job_type is not None:
        params["job_type"] = job_type
    if easy_apply is not None:
        params["easy_apply"] = easy_apply
    if under_10_applicants is not None:
        params["under_10_applicants"] = under_10_applicants
    if fair_chance_employer is not None:
        params["fair_chance_employer"] = fair_chance_employer
    return await proxy_request("linkedin", "/api/v1/linkedin/web/get_company_jobs", params=params, json_body=body)

@router.get("/get_company_job_count")
async def get_company_job_count(
    company_id: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取公司职位数量/Get company job count"""
    body = await request.json()
    params: dict[str, Any] = {}
    if company_id is not None:
        params["company_id"] = company_id
    return await proxy_request("linkedin", "/api/v1/linkedin/web/get_company_job_count", params=params, json_body=body)

@router.get("/get_user_about")
async def get_user_about(
    urn: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户简介/Get user about"""
    body = await request.json()
    params: dict[str, Any] = {}
    if urn is not None:
        params["urn"] = urn
    return await proxy_request("linkedin", "/api/v1/linkedin/web/get_user_about", params=params, json_body=body)

@router.get("/get_user_follower_and_connection")
async def get_user_follower_and_connection(
    username: str,
    request: Request,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户粉丝和连接数/Get user follower and connection"""
    body = await request.json()
    params: dict[str, Any] = {}
    if username is not None:
        params["username"] = username
    return await proxy_request("linkedin", "/api/v1/linkedin/web/get_user_follower_and_connection", params=params, json_body=body)

@router.get("/get_user_experience")
async def get_user_experience(
    urn: str,
    request: Request,
    page: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户工作经历/Get user experience"""
    body = await request.json()
    params: dict[str, Any] = {}
    if urn is not None:
        params["urn"] = urn
    if page is not None:
        params["page"] = page
    return await proxy_request("linkedin", "/api/v1/linkedin/web/get_user_experience", params=params, json_body=body)

@router.get("/get_user_skills")
async def get_user_skills(
    urn: str,
    request: Request,
    page: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户技能/Get user skills"""
    body = await request.json()
    params: dict[str, Any] = {}
    if urn is not None:
        params["urn"] = urn
    if page is not None:
        params["page"] = page
    return await proxy_request("linkedin", "/api/v1/linkedin/web/get_user_skills", params=params, json_body=body)

@router.get("/get_user_educations")
async def get_user_educations(
    urn: str,
    request: Request,
    page: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户教育背景/Get user educations"""
    body = await request.json()
    params: dict[str, Any] = {}
    if urn is not None:
        params["urn"] = urn
    if page is not None:
        params["page"] = page
    return await proxy_request("linkedin", "/api/v1/linkedin/web/get_user_educations", params=params, json_body=body)

@router.get("/get_user_publications")
async def get_user_publications(
    urn: str,
    request: Request,
    page: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户出版物/Get user publications"""
    body = await request.json()
    params: dict[str, Any] = {}
    if urn is not None:
        params["urn"] = urn
    if page is not None:
        params["page"] = page
    return await proxy_request("linkedin", "/api/v1/linkedin/web/get_user_publications", params=params, json_body=body)

@router.get("/get_user_certifications")
async def get_user_certifications(
    urn: str,
    request: Request,
    page: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户认证/Get user certifications"""
    body = await request.json()
    params: dict[str, Any] = {}
    if urn is not None:
        params["urn"] = urn
    if page is not None:
        params["page"] = page
    return await proxy_request("linkedin", "/api/v1/linkedin/web/get_user_certifications", params=params, json_body=body)

@router.get("/get_user_honors")
async def get_user_honors(
    urn: str,
    request: Request,
    page: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户荣誉奖项/Get user honors"""
    body = await request.json()
    params: dict[str, Any] = {}
    if urn is not None:
        params["urn"] = urn
    if page is not None:
        params["page"] = page
    return await proxy_request("linkedin", "/api/v1/linkedin/web/get_user_honors", params=params, json_body=body)

@router.get("/get_user_interests_groups")
async def get_user_interests_groups(
    urn: str,
    request: Request,
    page: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户感兴趣的群组/Get user interests groups"""
    body = await request.json()
    params: dict[str, Any] = {}
    if urn is not None:
        params["urn"] = urn
    if page is not None:
        params["page"] = page
    return await proxy_request("linkedin", "/api/v1/linkedin/web/get_user_interests_groups", params=params, json_body=body)

@router.get("/get_user_interests_companies")
async def get_user_interests_companies(
    urn: str,
    request: Request,
    page: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户感兴趣的公司/Get user interests companies"""
    body = await request.json()
    params: dict[str, Any] = {}
    if urn is not None:
        params["urn"] = urn
    if page is not None:
        params["page"] = page
    return await proxy_request("linkedin", "/api/v1/linkedin/web/get_user_interests_companies", params=params, json_body=body)

@router.get("/get_job_detail")
async def get_job_detail(
    job_id: str,
    request: Request,
    include_skills: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取职位详情/Get job detail"""
    body = await request.json()
    params: dict[str, Any] = {}
    if job_id is not None:
        params["job_id"] = job_id
    if include_skills is not None:
        params["include_skills"] = include_skills
    return await proxy_request("linkedin", "/api/v1/linkedin/web/get_job_detail", params=params, json_body=body)

@router.get("/search_jobs")
async def search_jobs(
    keyword: str,
    request: Request,
    page: str | None = None,
    sort_by: str | None = None,
    date_posted: str | None = None,
    geocode: str | None = None,
    company: str | None = None,
    experience_level: str | None = None,
    remote: str | None = None,
    job_type: str | None = None,
    easy_apply: str | None = None,
    has_verifications: str | None = None,
    under_10_applicants: str | None = None,
    fair_chance_employer: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """搜索职位/Search jobs"""
    body = await request.json()
    params: dict[str, Any] = {}
    if keyword is not None:
        params["keyword"] = keyword
    if page is not None:
        params["page"] = page
    if sort_by is not None:
        params["sort_by"] = sort_by
    if date_posted is not None:
        params["date_posted"] = date_posted
    if geocode is not None:
        params["geocode"] = geocode
    if company is not None:
        params["company"] = company
    if experience_level is not None:
        params["experience_level"] = experience_level
    if remote is not None:
        params["remote"] = remote
    if job_type is not None:
        params["job_type"] = job_type
    if easy_apply is not None:
        params["easy_apply"] = easy_apply
    if has_verifications is not None:
        params["has_verifications"] = has_verifications
    if under_10_applicants is not None:
        params["under_10_applicants"] = under_10_applicants
    if fair_chance_employer is not None:
        params["fair_chance_employer"] = fair_chance_employer
    return await proxy_request("linkedin", "/api/v1/linkedin/web/search_jobs", params=params, json_body=body)

@router.get("/search_people")
async def search_people(
    request: Request,
    name: str | None = None,
    first_name: str | None = None,
    last_name: str | None = None,
    title: str | None = None,
    company: str | None = None,
    school: str | None = None,
    page: str | None = None,
    geocode_location: str | None = None,
    current_company: str | None = None,
    profile_language: str | None = None,
    industry: str | None = None,
    service_category: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """搜索用户/Search people"""
    body = await request.json()
    params: dict[str, Any] = {}
    if name is not None:
        params["name"] = name
    if first_name is not None:
        params["first_name"] = first_name
    if last_name is not None:
        params["last_name"] = last_name
    if title is not None:
        params["title"] = title
    if company is not None:
        params["company"] = company
    if school is not None:
        params["school"] = school
    if page is not None:
        params["page"] = page
    if geocode_location is not None:
        params["geocode_location"] = geocode_location
    if current_company is not None:
        params["current_company"] = current_company
    if profile_language is not None:
        params["profile_language"] = profile_language
    if industry is not None:
        params["industry"] = industry
    if service_category is not None:
        params["service_category"] = service_category
    return await proxy_request("linkedin", "/api/v1/linkedin/web/search_people", params=params, json_body=body)
