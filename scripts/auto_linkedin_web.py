"""Auto-generated routes for LinkedIn-Web-API."""

from __future__ import annotations

from typing import Any

from fastapi import APIRouter, Depends, Request

from socialmedia_hub.server._core import proxy_request, verify_api_key

router = APIRouter(prefix="/api/v1/linkedin/web", tags=["linkedin_web"])

@router.get("/get_user_profile")
async def get_user_profile(
    include_bio: str | None = None,
    include_interests: str | None = None,
    include_honors: str | None = None,
    include_volunteers: str | None = None,
    include_educations: str | None = None,
    include_publications: str | None = None,
    include_certifications: str | None = None,
    include_skills: str | None = None,
    include_experiences: str | None = None,
    include_follower_and_connection: str | None = None,
    username: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户资料/Get user profile"""
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
        body = await request.json()
        return await proxy_request("linkedin", "/api/v1/linkedin/web/get_user_profile", json_body=body)

@router.get("/get_user_posts")
async def get_user_posts(
    pagination_token: str | None = None,
    page: str | None = None,
    urn: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户帖子/Get user posts"""
        params: dict[str, Any] = {}
        if urn is not None:
            params["urn"] = urn
        if page is not None:
            params["page"] = page
        if pagination_token is not None:
            params["pagination_token"] = pagination_token
        body = await request.json()
        return await proxy_request("linkedin", "/api/v1/linkedin/web/get_user_posts", json_body=body)

@router.get("/get_user_comments")
async def get_user_comments(
    pagination_token: str | None = None,
    page: str | None = None,
    urn: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户评论/Get user comments"""
        params: dict[str, Any] = {}
        if urn is not None:
            params["urn"] = urn
        if page is not None:
            params["page"] = page
        if pagination_token is not None:
            params["pagination_token"] = pagination_token
        body = await request.json()
        return await proxy_request("linkedin", "/api/v1/linkedin/web/get_user_comments", json_body=body)

@router.get("/get_user_contact")
async def get_user_contact(
    username: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户联系信息/Get user contact information"""
        params: dict[str, Any] = {}
        if username is not None:
            params["username"] = username
        body = await request.json()
        return await proxy_request("linkedin", "/api/v1/linkedin/web/get_user_contact", json_body=body)

@router.get("/get_user_recommendations")
async def get_user_recommendations(
    pagination_token: str | None = None,
    type: str | None = None,
    page: str | None = None,
    urn: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户推荐信/Get user recommendations"""
        params: dict[str, Any] = {}
        if urn is not None:
            params["urn"] = urn
        if page is not None:
            params["page"] = page
        if type is not None:
            params["type"] = type
        if pagination_token is not None:
            params["pagination_token"] = pagination_token
        body = await request.json()
        return await proxy_request("linkedin", "/api/v1/linkedin/web/get_user_recommendations", json_body=body)

@router.get("/get_user_videos")
async def get_user_videos(
    pagination_token: str | None = None,
    page: str | None = None,
    urn: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户视频/Get user videos"""
        params: dict[str, Any] = {}
        if urn is not None:
            params["urn"] = urn
        if page is not None:
            params["page"] = page
        if pagination_token is not None:
            params["pagination_token"] = pagination_token
        body = await request.json()
        return await proxy_request("linkedin", "/api/v1/linkedin/web/get_user_videos", json_body=body)

@router.get("/get_user_images")
async def get_user_images(
    pagination_token: str | None = None,
    page: str | None = None,
    urn: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户图片/Get user images"""
        params: dict[str, Any] = {}
        if urn is not None:
            params["urn"] = urn
        if page is not None:
            params["page"] = page
        if pagination_token is not None:
            params["pagination_token"] = pagination_token
        body = await request.json()
        return await proxy_request("linkedin", "/api/v1/linkedin/web/get_user_images", json_body=body)

@router.get("/get_company_profile")
async def get_company_profile(
    company_id: str | None = None,
    company: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取公司资料/Get company profile"""
        params: dict[str, Any] = {}
        if company is not None:
            params["company"] = company
        if company_id is not None:
            params["company_id"] = company_id
        body = await request.json()
        return await proxy_request("linkedin", "/api/v1/linkedin/web/get_company_profile", json_body=body)

@router.get("/get_company_people")
async def get_company_people(
    page: str | None = None,
    company_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取公司员工/Get company people"""
        params: dict[str, Any] = {}
        if company_id is not None:
            params["company_id"] = company_id
        if page is not None:
            params["page"] = page
        body = await request.json()
        return await proxy_request("linkedin", "/api/v1/linkedin/web/get_company_people", json_body=body)

@router.get("/get_company_posts")
async def get_company_posts(
    sort_by: str | None = None,
    page: str | None = None,
    company_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取公司帖子/Get company posts"""
        params: dict[str, Any] = {}
        if company_id is not None:
            params["company_id"] = company_id
        if page is not None:
            params["page"] = page
        if sort_by is not None:
            params["sort_by"] = sort_by
        body = await request.json()
        return await proxy_request("linkedin", "/api/v1/linkedin/web/get_company_posts", json_body=body)

@router.get("/get_company_jobs")
async def get_company_jobs(
    fair_chance_employer: str | None = None,
    under_10_applicants: str | None = None,
    easy_apply: str | None = None,
    job_type: str | None = None,
    remote: str | None = None,
    experience_level: str | None = None,
    date_posted: str | None = None,
    sort_by: str | None = None,
    page: str | None = None,
    company_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取公司职位/Get company jobs"""
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
        body = await request.json()
        return await proxy_request("linkedin", "/api/v1/linkedin/web/get_company_jobs", json_body=body)

@router.get("/get_company_job_count")
async def get_company_job_count(
    company_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取公司职位数量/Get company job count"""
        params: dict[str, Any] = {}
        if company_id is not None:
            params["company_id"] = company_id
        body = await request.json()
        return await proxy_request("linkedin", "/api/v1/linkedin/web/get_company_job_count", json_body=body)

@router.get("/get_user_about")
async def get_user_about(
    urn: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户简介/Get user about"""
        params: dict[str, Any] = {}
        if urn is not None:
            params["urn"] = urn
        body = await request.json()
        return await proxy_request("linkedin", "/api/v1/linkedin/web/get_user_about", json_body=body)

@router.get("/get_user_follower_and_connection")
async def get_user_follower_and_connection(
    username: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户粉丝和连接数/Get user follower and connection"""
        params: dict[str, Any] = {}
        if username is not None:
            params["username"] = username
        body = await request.json()
        return await proxy_request("linkedin", "/api/v1/linkedin/web/get_user_follower_and_connection", json_body=body)

@router.get("/get_user_experience")
async def get_user_experience(
    page: str | None = None,
    urn: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户工作经历/Get user experience"""
        params: dict[str, Any] = {}
        if urn is not None:
            params["urn"] = urn
        if page is not None:
            params["page"] = page
        body = await request.json()
        return await proxy_request("linkedin", "/api/v1/linkedin/web/get_user_experience", json_body=body)

@router.get("/get_user_skills")
async def get_user_skills(
    page: str | None = None,
    urn: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户技能/Get user skills"""
        params: dict[str, Any] = {}
        if urn is not None:
            params["urn"] = urn
        if page is not None:
            params["page"] = page
        body = await request.json()
        return await proxy_request("linkedin", "/api/v1/linkedin/web/get_user_skills", json_body=body)

@router.get("/get_user_educations")
async def get_user_educations(
    page: str | None = None,
    urn: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户教育背景/Get user educations"""
        params: dict[str, Any] = {}
        if urn is not None:
            params["urn"] = urn
        if page is not None:
            params["page"] = page
        body = await request.json()
        return await proxy_request("linkedin", "/api/v1/linkedin/web/get_user_educations", json_body=body)

@router.get("/get_user_publications")
async def get_user_publications(
    page: str | None = None,
    urn: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户出版物/Get user publications"""
        params: dict[str, Any] = {}
        if urn is not None:
            params["urn"] = urn
        if page is not None:
            params["page"] = page
        body = await request.json()
        return await proxy_request("linkedin", "/api/v1/linkedin/web/get_user_publications", json_body=body)

@router.get("/get_user_certifications")
async def get_user_certifications(
    page: str | None = None,
    urn: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户认证/Get user certifications"""
        params: dict[str, Any] = {}
        if urn is not None:
            params["urn"] = urn
        if page is not None:
            params["page"] = page
        body = await request.json()
        return await proxy_request("linkedin", "/api/v1/linkedin/web/get_user_certifications", json_body=body)

@router.get("/get_user_honors")
async def get_user_honors(
    page: str | None = None,
    urn: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户荣誉奖项/Get user honors"""
        params: dict[str, Any] = {}
        if urn is not None:
            params["urn"] = urn
        if page is not None:
            params["page"] = page
        body = await request.json()
        return await proxy_request("linkedin", "/api/v1/linkedin/web/get_user_honors", json_body=body)

@router.get("/get_user_interests_groups")
async def get_user_interests_groups(
    page: str | None = None,
    urn: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户感兴趣的群组/Get user interests groups"""
        params: dict[str, Any] = {}
        if urn is not None:
            params["urn"] = urn
        if page is not None:
            params["page"] = page
        body = await request.json()
        return await proxy_request("linkedin", "/api/v1/linkedin/web/get_user_interests_groups", json_body=body)

@router.get("/get_user_interests_companies")
async def get_user_interests_companies(
    page: str | None = None,
    urn: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户感兴趣的公司/Get user interests companies"""
        params: dict[str, Any] = {}
        if urn is not None:
            params["urn"] = urn
        if page is not None:
            params["page"] = page
        body = await request.json()
        return await proxy_request("linkedin", "/api/v1/linkedin/web/get_user_interests_companies", json_body=body)

@router.get("/get_job_detail")
async def get_job_detail(
    include_skills: str | None = None,
    job_id: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取职位详情/Get job detail"""
        params: dict[str, Any] = {}
        if job_id is not None:
            params["job_id"] = job_id
        if include_skills is not None:
            params["include_skills"] = include_skills
        body = await request.json()
        return await proxy_request("linkedin", "/api/v1/linkedin/web/get_job_detail", json_body=body)

@router.get("/search_jobs")
async def search_jobs(
    fair_chance_employer: str | None = None,
    under_10_applicants: str | None = None,
    has_verifications: str | None = None,
    easy_apply: str | None = None,
    job_type: str | None = None,
    remote: str | None = None,
    experience_level: str | None = None,
    company: str | None = None,
    geocode: str | None = None,
    date_posted: str | None = None,
    sort_by: str | None = None,
    page: str | None = None,
    keyword: str,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """搜索职位/Search jobs"""
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
        body = await request.json()
        return await proxy_request("linkedin", "/api/v1/linkedin/web/search_jobs", json_body=body)

@router.get("/search_people")
async def search_people(
    service_category: str | None = None,
    industry: str | None = None,
    profile_language: str | None = None,
    current_company: str | None = None,
    geocode_location: str | None = None,
    page: str | None = None,
    school: str | None = None,
    company: str | None = None,
    title: str | None = None,
    last_name: str | None = None,
    first_name: str | None = None,
    name: str | None = None,
    token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """搜索用户/Search people"""
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
        body = await request.json()
        return await proxy_request("linkedin", "/api/v1/linkedin/web/search_people", json_body=body)
