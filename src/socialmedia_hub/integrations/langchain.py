"""LangChain integration for SocialMedia-Hub."""

from __future__ import annotations

import json
import logging
from typing import Any, Type

logger = logging.getLogger("socialmedia_hub.integrations.langchain")


def create_langchain_tools(
    api_key: str,
    base_url: str = "http://127.0.0.1:8000",
    platforms: list[str] | None = None,
) -> list[Any]:
    """Create LangChain tools for SocialMedia-Hub.

    Args:
        api_key: SocialMedia-Hub API key
        base_url: API server base URL
        platforms: List of platforms to include (None for all)

    Returns:
        List of LangChain Tool objects
    """
    try:
        from langchain_core.tools import StructuredTool
    except ImportError:
        raise ImportError("langchain-core is required. Install with: pip install langchain-core")

    from socialmedia_hub.server._core import proxy_request

    tools = []
    platform_list = platforms or [
        "douyin", "tiktok", "instagram", "youtube", "twitter",
        "xiaohongshu", "bilibili", "weibo", "kuaishou", "linkedin",
        "reddit", "zhihu", "threads", "wechat", "lemon8"
    ]

    for platform in platform_list:
        tools.extend(_create_platform_tools(platform, api_key, base_url))

    return tools


def _create_platform_tools(
    platform: str,
    api_key: str,
    base_url: str,
) -> list[Any]:
    """Create tools for a specific platform."""
    try:
        from langchain_core.tools import StructuredTool
    except ImportError:
        return []

    tools = []

    # Fetch video tool
    tools.append(StructuredTool(
        name=f"{platform}_fetch_video",
        description=f"Fetch {platform} video details",
        func=lambda video_id, _platform=platform, _base=base_url, _key=api_key: _fetch_video(
            _platform, video_id, _base, _key
        ),
        args_schema=None,
    ))

    # Fetch user tool
    tools.append(StructuredTool(
        name=f"{platform}_fetch_user",
        description=f"Fetch {platform} user profile",
        func=lambda user_id, _platform=platform, _base=base_url, _key=api_key: _fetch_user(
            _platform, user_id, _base, _key
        ),
        args_schema=None,
    ))

    # Search tool
    tools.append(StructuredTool(
        name=f"{platform}_search",
        description=f"Search {platform} content",
        func=lambda keyword, _platform=platform, _base=base_url, _key=api_key: _search(
            _platform, keyword, _base, _key
        ),
        args_schema=None,
    ))

    return tools


def _fetch_video(platform: str, video_id: str, base_url: str, api_key: str) -> str:
    """Fetch video details."""
    import httpx

    url = f"{base_url}/api/v1/{platform}/fetch_video"
    headers = {"Authorization": f"Bearer {api_key}"}

    with httpx.Client(timeout=30.0) as client:
        response = client.get(url, params={"video_id": video_id}, headers=headers)
        return json.dumps(response.json(), indent=2, ensure_ascii=False)


def _fetch_user(platform: str, user_id: str, base_url: str, api_key: str) -> str:
    """Fetch user profile."""
    import httpx

    url = f"{base_url}/api/v1/{platform}/fetch_user"
    headers = {"Authorization": f"Bearer {api_key}"}

    with httpx.Client(timeout=30.0) as client:
        response = client.get(url, params={"user_id": user_id}, headers=headers)
        return json.dumps(response.json(), indent=2, ensure_ascii=False)


def _search(platform: str, keyword: str, base_url: str, api_key: str) -> str:
    """Search content."""
    import httpx

    url = f"{base_url}/api/v1/{platform}/search"
    headers = {"Authorization": f"Bearer {api_key}"}

    with httpx.Client(timeout=30.0) as client:
        response = client.get(url, params={"keyword": keyword}, headers=headers)
        return json.dumps(response.json(), indent=2, ensure_ascii=False)
