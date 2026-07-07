"""SocialMedia-Hub MCP Server.

Model Context Protocol server for connecting AI agents to social media data.
Supports 16+ platforms with 990+ tools.
"""

from __future__ import annotations

import logging
from collections.abc import Callable
from typing import Any

logger = logging.getLogger("socialmedia_hub.mcp")


class MCPServer:
    """Model Context Protocol server for SocialMedia-Hub."""

    def __init__(self, api_key: str, base_url: str = "http://127.0.0.1:8000"):
        """Initialize MCP server.

        Args:
            api_key: SocialMedia-Hub API key
            base_url: API server base URL
        """
        self.api_key = api_key
        self.base_url = base_url
        self.tools: dict[str, dict[str, Any]] = {}
        self._register_all_tools()
        # Register extended tools
        from socialmedia_hub.mcp.extended import register_extended_tools, register_extra_tools, register_extra_tools_v2
        register_extended_tools(self)
        register_extra_tools(self)
        register_extra_tools_v2(self)

    def _register_all_tools(self) -> None:
        """Register all MCP tools for all platforms."""
        # TikTok tools
        self._register_tiktok_tools()
        # Douyin tools
        self._register_douyin_tools()
        # Instagram tools
        self._register_instagram_tools()
        # YouTube tools
        self._register_youtube_tools()
        # Twitter tools
        self._register_twitter_tools()
        # Xiaohongshu tools
        self._register_xiaohongshu_tools()
        # Bilibili tools
        self._register_bilibili_tools()
        # Weibo tools
        self._register_weibo_tools()
        # Kuaishou tools
        self._register_kuaishou_tools()
        # LinkedIn tools
        self._register_linkedin_tools()
        # Reddit tools
        self._register_reddit_tools()
        # Zhihu tools
        self._register_zhihu_tools()
        # Threads tools
        self._register_threads_tools()
        # WeChat tools
        self._register_wechat_tools()
        # Lemon8 tools
        self._register_lemon8_tools()
        # Utility tools
        self._register_utility_tools()

    def _register_tool(
        self,
        name: str,
        description: str,
        parameters: dict[str, Any],
        handler: Callable[..., Any],
    ) -> None:
        """Register a single MCP tool."""
        self.tools[name] = {
            "name": name,
            "description": description,
            "parameters": parameters,
            "handler": handler,
        }

    def _call_api(self, endpoint: str, params: dict[str, Any] | None = None) -> dict[str, Any]:
        """Call the SocialMedia-Hub API."""
        import httpx

        url = f"{self.base_url}{endpoint}"
        headers = {"Authorization": f"Bearer {self.api_key}"}

        with httpx.Client(timeout=30.0) as client:
            response = client.get(url, params=params, headers=headers)
            result: dict[str, Any] = response.json()
            return result

    # ===========================================================================
    # TikTok Tools
    # ===========================================================================

    def _register_tiktok_tools(self) -> None:
        """Register TikTok MCP tools."""
        # Video tools
        self._register_tool(
            name="tiktok_fetch_video",
            description="Fetch TikTok video details by ID",
            parameters={
                "type": "object",
                "properties": {
                    "video_id": {"type": "string", "description": "TikTok video ID"},
                },
                "required": ["video_id"],
            },
            handler=lambda video_id: self._call_api(
                "/api/v1/tiktok/web/fetch_post_detail",
                {"itemId": video_id}
            ),
        )

        self._register_tool(
            name="tiktok_fetch_video_v2",
            description="Fetch TikTok video details V2 (enhanced)",
            parameters={
                "type": "object",
                "properties": {
                    "video_id": {"type": "string", "description": "TikTok video ID"},
                },
                "required": ["video_id"],
            },
            handler=lambda video_id: self._call_api(
                "/api/v1/tiktok/web/fetch_post_detail_v2",
                {"itemId": video_id}
            ),
        )

        # User tools
        self._register_tool(
            name="tiktok_fetch_user",
            description="Fetch TikTok user profile",
            parameters={
                "type": "object",
                "properties": {
                    "username": {"type": "string", "description": "TikTok username"},
                },
                "required": ["username"],
            },
            handler=lambda username: self._call_api(
                "/api/v1/tiktok/web/fetch_user_profile",
                {"uniqueId": username}
            ),
        )

        self._register_tool(
            name="tiktok_fetch_user_posts",
            description="Fetch TikTok user posts",
            parameters={
                "type": "object",
                "properties": {
                    "sec_uid": {"type": "string", "description": "User sec_uid"},
                    "count": {"type": "integer", "description": "Number of posts", "default": 20},
                },
                "required": ["sec_uid"],
            },
            handler=lambda sec_uid, count=20: self._call_api(
                "/api/v1/tiktok/web/fetch_user_post",
                {"secUid": sec_uid, "count": count}
            ),
        )

        self._register_tool(
            name="tiktok_fetch_user_likes",
            description="Fetch TikTok user liked videos",
            parameters={
                "type": "object",
                "properties": {
                    "sec_uid": {"type": "string", "description": "User sec_uid"},
                    "count": {"type": "integer", "description": "Number of videos", "default": 20},
                },
                "required": ["sec_uid"],
            },
            handler=lambda sec_uid, count=20: self._call_api(
                "/api/v1/tiktok/web/fetch_user_like",
                {"secUid": sec_uid, "count": count}
            ),
        )

        self._register_tool(
            name="tiktok_fetch_user_followers",
            description="Fetch TikTok user followers",
            parameters={
                "type": "object",
                "properties": {
                    "sec_uid": {"type": "string", "description": "User sec_uid"},
                    "count": {"type": "integer", "description": "Number of followers", "default": 20},
                },
                "required": ["sec_uid"],
            },
            handler=lambda sec_uid, count=20: self._call_api(
                "/api/v1/tiktok/web/fetch_user_fans",
                {"secUid": sec_uid, "count": count}
            ),
        )

        self._register_tool(
            name="tiktok_fetch_user_following",
            description="Fetch TikTok user following",
            parameters={
                "type": "object",
                "properties": {
                    "sec_uid": {"type": "string", "description": "User sec_uid"},
                    "count": {"type": "integer", "description": "Number of following", "default": 20},
                },
                "required": ["sec_uid"],
            },
            handler=lambda sec_uid, count=20: self._call_api(
                "/api/v1/tiktok/web/fetch_user_follow",
                {"secUid": sec_uid, "count": count}
            ),
        )

        # Search tools
        self._register_tool(
            name="tiktok_search",
            description="Search TikTok videos",
            parameters={
                "type": "object",
                "properties": {
                    "keyword": {"type": "string", "description": "Search keyword"},
                    "count": {"type": "integer", "description": "Number of results", "default": 20},
                },
                "required": ["keyword"],
            },
            handler=lambda keyword, count=20: self._call_api(
                "/api/v1/tiktok/web/fetch_general_search",
                {"keyword": keyword, "count": count}
            ),
        )

        self._register_tool(
            name="tiktok_search_user",
            description="Search TikTok users",
            parameters={
                "type": "object",
                "properties": {
                    "keyword": {"type": "string", "description": "Search keyword"},
                    "count": {"type": "integer", "description": "Number of results", "default": 20},
                },
                "required": ["keyword"],
            },
            handler=lambda keyword, count=20: self._call_api(
                "/api/v1/tiktok/web/fetch_user_search",
                {"keyword": keyword, "count": count}
            ),
        )

        # Comment tools
        self._register_tool(
            name="tiktok_fetch_comments",
            description="Fetch TikTok video comments",
            parameters={
                "type": "object",
                "properties": {
                    "video_id": {"type": "string", "description": "Video ID"},
                    "count": {"type": "integer", "description": "Number of comments", "default": 20},
                },
                "required": ["video_id"],
            },
            handler=lambda video_id, count=20: self._call_api(
                "/api/v1/tiktok/web/fetch_comment_list",
                {"itemId": video_id, "count": count}
            ),
        )

        # Trending tools
        self._register_tool(
            name="tiktok_fetch_trending",
            description="Fetch TikTok trending videos",
            parameters={
                "type": "object",
                "properties": {},
            },
            handler=lambda: self._call_api("/api/v1/tiktok/web/fetch_trending_post"),
        )

        self._register_tool(
            name="tiktok_fetch_trending_search",
            description="Fetch TikTok trending search keywords",
            parameters={
                "type": "object",
                "properties": {},
            },
            handler=lambda: self._call_api("/api/v1/tiktok/web/fetch_trending_searchwords"),
        )

        # Live tools
        self._register_tool(
            name="tiktok_fetch_live_room",
            description="Fetch TikTok live room info",
            parameters={
                "type": "object",
                "properties": {
                    "room_id": {"type": "string", "description": "Live room ID"},
                },
                "required": ["room_id"],
            },
            handler=lambda room_id: self._call_api(
                "/api/v1/tiktok/web/fetch_live_room_detail",
                {"room_id": room_id}
            ),
        )

        # Explore tools
        self._register_tool(
            name="tiktok_fetch_explore",
            description="Fetch TikTok explore posts",
            parameters={
                "type": "object",
                "properties": {
                    "category": {"type": "string", "description": "Category type"},
                },
            },
            handler=lambda category=None: self._call_api(
                "/api/v1/tiktok/web/fetch_explore_post",
                {"categoryType": category} if category else {}
            ),
        )

        # Related tools
        self._register_tool(
            name="tiktok_fetch_related",
            description="Fetch TikTok related videos",
            parameters={
                "type": "object",
                "properties": {
                    "video_id": {"type": "string", "description": "Video ID"},
                    "count": {"type": "integer", "description": "Number of related videos", "default": 20},
                },
                "required": ["video_id"],
            },
            handler=lambda video_id, count=20: self._call_api(
                "/api/v1/tiktok/web/fetch_related_post",
                {"itemId": video_id, "count": count}
            ),
        )

    # ===========================================================================
    # Douyin Tools
    # ===========================================================================

    def _register_douyin_tools(self) -> None:
        """Register Douyin MCP tools."""
        # Video tools
        self._register_tool(
            name="douyin_fetch_video",
            description="Fetch Douyin video details by ID",
            parameters={
                "type": "object",
                "properties": {
                    "video_id": {"type": "string", "description": "Douyin video ID (aweme_id)"},
                },
                "required": ["video_id"],
            },
            handler=lambda video_id: self._call_api(
                "/api/v1/douyin/web/fetch_one_video",
                {"aweme_id": video_id}
            ),
        )

        self._register_tool(
            name="douyin_fetch_video_by_share_url",
            description="Fetch Douyin video by share URL",
            parameters={
                "type": "object",
                "properties": {
                    "share_url": {"type": "string", "description": "Share URL"},
                },
                "required": ["share_url"],
            },
            handler=lambda share_url: self._call_api(
                "/api/v1/douyin/web/fetch_one_video_by_share_url",
                {"share_url": share_url}
            ),
        )

        # User tools
        self._register_tool(
            name="douyin_fetch_user",
            description="Fetch Douyin user profile",
            parameters={
                "type": "object",
                "properties": {
                    "uid": {"type": "string", "description": "Douyin user ID"},
                },
                "required": ["uid"],
            },
            handler=lambda uid: self._call_api(
                "/api/v1/douyin/web/fetch_user_profile_by_uid",
                {"uid": uid}
            ),
        )

        self._register_tool(
            name="douyin_fetch_user_by_sec_uid",
            description="Fetch Douyin user profile by sec_user_id",
            parameters={
                "type": "object",
                "properties": {
                    "sec_user_id": {"type": "string", "description": "User sec_user_id"},
                },
                "required": ["sec_user_id"],
            },
            handler=lambda sec_user_id: self._call_api(
                "/api/v1/douyin/web/fetch_user_profile_by_sec_uid",
                {"sec_user_id": sec_user_id}
            ),
        )

        self._register_tool(
            name="douyin_fetch_user_posts",
            description="Fetch Douyin user posts",
            parameters={
                "type": "object",
                "properties": {
                    "sec_user_id": {"type": "string", "description": "User sec_user_id"},
                    "count": {"type": "integer", "description": "Number of posts", "default": 20},
                },
                "required": ["sec_user_id"],
            },
            handler=lambda sec_user_id, count=20: self._call_api(
                "/api/v1/douyin/web/fetch_user_post_videos",
                {"sec_user_id": sec_user_id, "count": count}
            ),
        )

        self._register_tool(
            name="douyin_fetch_user_followers",
            description="Fetch Douyin user followers",
            parameters={
                "type": "object",
                "properties": {
                    "sec_user_id": {"type": "string", "description": "User sec_user_id"},
                    "count": {"type": "integer", "description": "Number of followers", "default": 20},
                },
                "required": ["sec_user_id"],
            },
            handler=lambda sec_user_id, count=20: self._call_api(
                "/api/v1/douyin/web/fetch_user_fans_list",
                {"sec_user_id": sec_user_id, "count": count}
            ),
        )

        self._register_tool(
            name="douyin_fetch_user_following",
            description="Fetch Douyin user following",
            parameters={
                "type": "object",
                "properties": {
                    "sec_user_id": {"type": "string", "description": "User sec_user_id"},
                    "count": {"type": "integer", "description": "Number of following", "default": 20},
                },
                "required": ["sec_user_id"],
            },
            handler=lambda sec_user_id, count=20: self._call_api(
                "/api/v1/douyin/web/fetch_user_following_list",
                {"sec_user_id": sec_user_id, "count": count}
            ),
        )

        # Search tools
        self._register_tool(
            name="douyin_search",
            description="Search Douyin videos",
            parameters={
                "type": "object",
                "properties": {
                    "keyword": {"type": "string", "description": "Search keyword"},
                    "count": {"type": "integer", "description": "Number of results", "default": 20},
                },
                "required": ["keyword"],
            },
            handler=lambda keyword, count=20: self._call_api(
                "/api/v1/douyin/search/fetch_general_search_result",
                {"keyword": keyword, "count": count}
            ),
        )

        self._register_tool(
            name="douyin_search_user",
            description="Search Douyin users",
            parameters={
                "type": "object",
                "properties": {
                    "keyword": {"type": "string", "description": "Search keyword"},
                    "count": {"type": "integer", "description": "Number of results", "default": 20},
                },
                "required": ["keyword"],
            },
            handler=lambda keyword, count=20: self._call_api(
                "/api/v1/douyin/search/fetch_user_search_result",
                {"keyword": keyword, "count": count}
            ),
        )

        # Comment tools
        self._register_tool(
            name="douyin_fetch_comments",
            description="Fetch Douyin video comments",
            parameters={
                "type": "object",
                "properties": {
                    "video_id": {"type": "string", "description": "Video ID (aweme_id)"},
                    "count": {"type": "integer", "description": "Number of comments", "default": 20},
                },
                "required": ["video_id"],
            },
            handler=lambda video_id, count=20: self._call_api(
                "/api/v1/douyin/web/fetch_video_comments",
                {"aweme_id": video_id, "count": count}
            ),
        )

        # Trending tools
        self._register_tool(
            name="douyin_fetch_trending",
            description="Fetch Douyin hot search list",
            parameters={
                "type": "object",
                "properties": {},
            },
            handler=lambda: self._call_api("/api/v1/douyin/web/fetch_hot_search_result"),
        )

        # Live tools
        self._register_tool(
            name="douyin_fetch_live_room",
            description="Fetch Douyin live room info",
            parameters={
                "type": "object",
                "properties": {
                    "room_id": {"type": "string", "description": "Live room ID"},
                },
                "required": ["room_id"],
            },
            handler=lambda room_id: self._call_api(
                "/api/v1/douyin/web/fetch_user_live_videos_by_room_id",
                {"room_id": room_id}
            ),
        )

        # E-commerce tools
        self._register_tool(
            name="douyin_fetch_product",
            description="Fetch Douyin product details",
            parameters={
                "type": "object",
                "properties": {
                    "product_id": {"type": "string", "description": "Product ID"},
                },
                "required": ["product_id"],
            },
            handler=lambda product_id: self._call_api(
                "/api/v1/douyin/web/fetch_product_detail",
                {"product_id": product_id}
            ),
        )

        # Related tools
        self._register_tool(
            name="douyin_fetch_related",
            description="Fetch Douyin related videos",
            parameters={
                "type": "object",
                "properties": {
                    "video_id": {"type": "string", "description": "Video ID"},
                    "count": {"type": "integer", "description": "Number of related videos", "default": 20},
                },
                "required": ["video_id"],
            },
            handler=lambda video_id, count=20: self._call_api(
                "/api/v1/douyin/web/fetch_related_posts",
                {"aweme_id": video_id, "count": count}
            ),
        )

        # ID conversion tools
        self._register_tool(
            name="douyin_url_to_video_id",
            description="Extract video ID from Douyin URL",
            parameters={
                "type": "object",
                "properties": {
                    "url": {"type": "string", "description": "Douyin URL"},
                },
                "required": ["url"],
            },
            handler=lambda url: self._call_api(
                "/api/v1/douyin/web/get_aweme_id",
                {"url": url}
            ),
        )

        self._register_tool(
            name="douyin_url_to_user_id",
            description="Extract user ID from Douyin URL",
            parameters={
                "type": "object",
                "properties": {
                    "url": {"type": "string", "description": "Douyin URL"},
                },
                "required": ["url"],
            },
            handler=lambda url: self._call_api(
                "/api/v1/douyin/web/get_sec_user_id",
                {"url": url}
            ),
        )

    # ===========================================================================
    # Instagram Tools
    # ===========================================================================

    def _register_instagram_tools(self) -> None:
        """Register Instagram MCP tools."""
        # User tools
        self._register_tool(
            name="instagram_fetch_user",
            description="Fetch Instagram user profile",
            parameters={
                "type": "object",
                "properties": {
                    "username": {"type": "string", "description": "Instagram username"},
                },
                "required": ["username"],
            },
            handler=lambda username: self._call_api(
                "/api/v1/instagram/v1/fetch_user_profile",
                {"username": username}
            ),
        )

        self._register_tool(
            name="instagram_fetch_user_posts",
            description="Fetch Instagram user posts",
            parameters={
                "type": "object",
                "properties": {
                    "user_id": {"type": "string", "description": "User ID"},
                },
                "required": ["user_id"],
            },
            handler=lambda user_id: self._call_api(
                "/api/v1/instagram/v1/fetch_user_post_feed",
                {"user_id": user_id}
            ),
        )

        self._register_tool(
            name="instagram_fetch_user_reels",
            description="Fetch Instagram user reels",
            parameters={
                "type": "object",
                "properties": {
                    "user_id": {"type": "string", "description": "User ID"},
                },
                "required": ["user_id"],
            },
            handler=lambda user_id: self._call_api(
                "/api/v1/instagram/v1/fetch_user_reels",
                {"user_id": user_id}
            ),
        )

        self._register_tool(
            name="instagram_fetch_user_followers",
            description="Fetch Instagram user followers",
            parameters={
                "type": "object",
                "properties": {
                    "user_id": {"type": "string", "description": "User ID"},
                },
                "required": ["user_id"],
            },
            handler=lambda user_id: self._call_api(
                "/api/v1/instagram/v1/fetch_user_followers",
                {"user_id": user_id}
            ),
        )

        self._register_tool(
            name="instagram_fetch_user_following",
            description="Fetch Instagram user following",
            parameters={
                "type": "object",
                "properties": {
                    "user_id": {"type": "string", "description": "User ID"},
                },
                "required": ["user_id"],
            },
            handler=lambda user_id: self._call_api(
                "/api/v1/instagram/v1/fetch_user_following",
                {"user_id": user_id}
            ),
        )

        # Post tools
        self._register_tool(
            name="instagram_fetch_post",
            description="Fetch Instagram post details",
            parameters={
                "type": "object",
                "properties": {
                    "shortcode": {"type": "string", "description": "Post shortcode"},
                },
                "required": ["shortcode"],
            },
            handler=lambda shortcode: self._call_api(
                "/api/v1/instagram/v1/fetch_post_info",
                {"shortcode": shortcode}
            ),
        )

        self._register_tool(
            name="instagram_fetch_post_comments",
            description="Fetch Instagram post comments",
            parameters={
                "type": "object",
                "properties": {
                    "media_id": {"type": "string", "description": "Media ID"},
                },
                "required": ["media_id"],
            },
            handler=lambda media_id: self._call_api(
                "/api/v1/instagram/v1/fetch_post_comments",
                {"media_id": media_id}
            ),
        )

        # Hashtag tools
        self._register_tool(
            name="instagram_fetch_hashtag",
            description="Fetch Instagram hashtag info",
            parameters={
                "type": "object",
                "properties": {
                    "hashtag": {"type": "string", "description": "Hashtag name"},
                },
                "required": ["hashtag"],
            },
            handler=lambda hashtag: self._call_api(
                "/api/v1/instagram/v1/fetch_hashtag_info",
                {"hashtag": hashtag}
            ),
        )

        self._register_tool(
            name="instagram_fetch_hashtag_posts",
            description="Fetch Instagram hashtag posts",
            parameters={
                "type": "object",
                "properties": {
                    "hashtag": {"type": "string", "description": "Hashtag name"},
                },
                "required": ["hashtag"],
            },
            handler=lambda hashtag: self._call_api(
                "/api/v1/instagram/v1/fetch_hashtag_posts",
                {"hashtag": hashtag}
            ),
        )

        # Story tools
        self._register_tool(
            name="instagram_fetch_user_story",
            description="Fetch Instagram user story",
            parameters={
                "type": "object",
                "properties": {
                    "user_id": {"type": "string", "description": "User ID"},
                },
                "required": ["user_id"],
            },
            handler=lambda user_id: self._call_api(
                "/api/v1/instagram/v1/fetch_user_story",
                {"user_id": user_id}
            ),
        )

        # Explore tools
        self._register_tool(
            name="instagram_fetch_explore",
            description="Fetch Instagram explore page",
            parameters={
                "type": "object",
                "properties": {},
            },
            handler=lambda: self._call_api("/api/v1/instagram/v1/fetch_explore"),
        )

    # ===========================================================================
    # YouTube Tools
    # ===========================================================================

    def _register_youtube_tools(self) -> None:
        """Register YouTube MCP tools."""
        # Video tools
        self._register_tool(
            name="youtube_fetch_video",
            description="Fetch YouTube video details",
            parameters={
                "type": "object",
                "properties": {
                    "video_id": {"type": "string", "description": "YouTube video ID"},
                },
                "required": ["video_id"],
            },
            handler=lambda video_id: self._call_api(
                "/api/v1/youtube/web/get_video_info",
                {"video_id": video_id}
            ),
        )

        self._register_tool(
            name="youtube_fetch_video_comments",
            description="Fetch YouTube video comments",
            parameters={
                "type": "object",
                "properties": {
                    "video_id": {"type": "string", "description": "Video ID"},
                },
                "required": ["video_id"],
            },
            handler=lambda video_id: self._call_api(
                "/api/v1/youtube/web/get_video_comments",
                {"video_id": video_id}
            ),
        )

        self._register_tool(
            name="youtube_fetch_related_videos",
            description="Fetch YouTube related videos",
            parameters={
                "type": "object",
                "properties": {
                    "video_id": {"type": "string", "description": "Video ID"},
                },
                "required": ["video_id"],
            },
            handler=lambda video_id: self._call_api(
                "/api/v1/youtube/web/get_related_videos",
                {"video_id": video_id}
            ),
        )

        # Channel tools
        self._register_tool(
            name="youtube_fetch_channel",
            description="Fetch YouTube channel info",
            parameters={
                "type": "object",
                "properties": {
                    "channel_id": {"type": "string", "description": "Channel ID"},
                },
                "required": ["channel_id"],
            },
            handler=lambda channel_id: self._call_api(
                "/api/v1/youtube/web/get_channel_info",
                {"channel_id": channel_id}
            ),
        )

        self._register_tool(
            name="youtube_fetch_channel_videos",
            description="Fetch YouTube channel videos",
            parameters={
                "type": "object",
                "properties": {
                    "channel_id": {"type": "string", "description": "Channel ID"},
                    "count": {"type": "integer", "description": "Number of videos", "default": 20},
                },
                "required": ["channel_id"],
            },
            handler=lambda channel_id, count=20: self._call_api(
                "/api/v1/youtube/web/get_channel_videos",
                {"channel_id": channel_id, "count": count}
            ),
        )

        # Search tools
        self._register_tool(
            name="youtube_search",
            description="Search YouTube videos",
            parameters={
                "type": "object",
                "properties": {
                    "keyword": {"type": "string", "description": "Search keyword"},
                    "count": {"type": "integer", "description": "Number of results", "default": 20},
                },
                "required": ["keyword"],
            },
            handler=lambda keyword, count=20: self._call_api(
                "/api/v1/youtube/web/search_video",
                {"search_query": keyword, "count": count}
            ),
        )

        self._register_tool(
            name="youtube_search_channel",
            description="Search YouTube channels",
            parameters={
                "type": "object",
                "properties": {
                    "keyword": {"type": "string", "description": "Search keyword"},
                },
                "required": ["keyword"],
            },
            handler=lambda keyword: self._call_api(
                "/api/v1/youtube/web/search_channel",
                {"search_query": keyword}
            ),
        )

        # Trending tools
        self._register_tool(
            name="youtube_fetch_trending",
            description="Fetch YouTube trending videos",
            parameters={
                "type": "object",
                "properties": {},
            },
            handler=lambda: self._call_api("/api/v1/youtube/web/get_trending_videos"),
        )

        # Subtitle tools
        self._register_tool(
            name="youtube_fetch_subtitles",
            description="Fetch YouTube video subtitles",
            parameters={
                "type": "object",
                "properties": {
                    "video_id": {"type": "string", "description": "Video ID"},
                },
                "required": ["video_id"],
            },
            handler=lambda video_id: self._call_api(
                "/api/v1/youtube/web/get_video_subtitles",
                {"video_id": video_id}
            ),
        )

    # ===========================================================================
    # Twitter Tools
    # ===========================================================================

    def _register_twitter_tools(self) -> None:
        """Register Twitter MCP tools."""
        # User tools
        self._register_tool(
            name="twitter_fetch_user",
            description="Fetch Twitter/X user profile",
            parameters={
                "type": "object",
                "properties": {
                    "username": {"type": "string", "description": "Twitter username"},
                },
                "required": ["username"],
            },
            handler=lambda username: self._call_api(
                "/api/v1/twitter/web/fetch_user_profile",
                {"username": username}
            ),
        )

        self._register_tool(
            name="twitter_fetch_user_tweets",
            description="Fetch Twitter user tweets",
            parameters={
                "type": "object",
                "properties": {
                    "user_id": {"type": "string", "description": "User ID"},
                    "count": {"type": "integer", "description": "Number of tweets", "default": 20},
                },
                "required": ["user_id"],
            },
            handler=lambda user_id, count=20: self._call_api(
                "/api/v1/twitter/web/fetch_user_tweets",
                {"user_id": user_id, "count": count}
            ),
        )

        self._register_tool(
            name="twitter_fetch_user_likes",
            description="Fetch Twitter user likes",
            parameters={
                "type": "object",
                "properties": {
                    "user_id": {"type": "string", "description": "User ID"},
                },
                "required": ["user_id"],
            },
            handler=lambda user_id: self._call_api(
                "/api/v1/twitter/web/fetch_user_likes",
                {"user_id": user_id}
            ),
        )

        self._register_tool(
            name="twitter_fetch_user_followers",
            description="Fetch Twitter user followers",
            parameters={
                "type": "object",
                "properties": {
                    "user_id": {"type": "string", "description": "User ID"},
                    "count": {"type": "integer", "description": "Number of followers", "default": 20},
                },
                "required": ["user_id"],
            },
            handler=lambda user_id, count=20: self._call_api(
                "/api/v1/twitter/web/fetch_user_followers",
                {"user_id": user_id, "count": count}
            ),
        )

        self._register_tool(
            name="twitter_fetch_user_following",
            description="Fetch Twitter user following",
            parameters={
                "type": "object",
                "properties": {
                    "user_id": {"type": "string", "description": "User ID"},
                    "count": {"type": "integer", "description": "Number of following", "default": 20},
                },
                "required": ["user_id"],
            },
            handler=lambda user_id, count=20: self._call_api(
                "/api/v1/twitter/web/fetch_user_following",
                {"user_id": user_id, "count": count}
            ),
        )

        # Tweet tools
        self._register_tool(
            name="twitter_fetch_tweet",
            description="Fetch tweet details",
            parameters={
                "type": "object",
                "properties": {
                    "tweet_id": {"type": "string", "description": "Tweet ID"},
                },
                "required": ["tweet_id"],
            },
            handler=lambda tweet_id: self._call_api(
                "/api/v1/twitter/web/fetch_tweet_detail",
                {"tweet_id": tweet_id}
            ),
        )

        self._register_tool(
            name="twitter_fetch_tweet_replies",
            description="Fetch tweet replies",
            parameters={
                "type": "object",
                "properties": {
                    "tweet_id": {"type": "string", "description": "Tweet ID"},
                },
                "required": ["tweet_id"],
            },
            handler=lambda tweet_id: self._call_api(
                "/api/v1/twitter/web/fetch_tweet_replies",
                {"tweet_id": tweet_id}
            ),
        )

        self._register_tool(
            name="twitter_fetch_tweet_likes",
            description="Fetch tweet likes",
            parameters={
                "type": "object",
                "properties": {
                    "tweet_id": {"type": "string", "description": "Tweet ID"},
                },
                "required": ["tweet_id"],
            },
            handler=lambda tweet_id: self._call_api(
                "/api/v1/twitter/web/fetch_tweet_likes",
                {"tweet_id": tweet_id}
            ),
        )

        self._register_tool(
            name="twitter_fetch_tweet_retweets",
            description="Fetch tweet retweets",
            parameters={
                "type": "object",
                "properties": {
                    "tweet_id": {"type": "string", "description": "Tweet ID"},
                },
                "required": ["tweet_id"],
            },
            handler=lambda tweet_id: self._call_api(
                "/api/v1/twitter/web/fetch_tweet_retweets",
                {"tweet_id": tweet_id}
            ),
        )

        # Search tools
        self._register_tool(
            name="twitter_search",
            description="Search tweets",
            parameters={
                "type": "object",
                "properties": {
                    "keyword": {"type": "string", "description": "Search keyword"},
                },
                "required": ["keyword"],
            },
            handler=lambda keyword: self._call_api(
                "/api/v1/twitter/web/fetch_search_timeline",
                {"keyword": keyword}
            ),
        )

        # Trending tools
        self._register_tool(
            name="twitter_fetch_trending",
            description="Fetch Twitter trending topics",
            parameters={
                "type": "object",
                "properties": {},
            },
            handler=lambda: self._call_api("/api/v1/twitter/web/fetch_trending"),
        )

    # ===========================================================================
    # Xiaohongshu Tools
    # ===========================================================================

    def _register_xiaohongshu_tools(self) -> None:
        """Register Xiaohongshu MCP tools."""
        # Note tools
        self._register_tool(
            name="xiaohongshu_fetch_note",
            description="Fetch Xiaohongshu note details",
            parameters={
                "type": "object",
                "properties": {
                    "note_id": {"type": "string", "description": "Note ID"},
                },
                "required": ["note_id"],
            },
            handler=lambda note_id: self._call_api(
                "/api/v1/xiaohongshu/web/fetch_note_detail",
                {"note_id": note_id}
            ),
        )

        self._register_tool(
            name="xiaohongshu_fetch_note_comments",
            description="Fetch Xiaohongshu note comments",
            parameters={
                "type": "object",
                "properties": {
                    "note_id": {"type": "string", "description": "Note ID"},
                },
                "required": ["note_id"],
            },
            handler=lambda note_id: self._call_api(
                "/api/v1/xiaohongshu/web/fetch_note_comments",
                {"note_id": note_id}
            ),
        )

        # User tools
        self._register_tool(
            name="xiaohongshu_fetch_user",
            description="Fetch Xiaohongshu user profile",
            parameters={
                "type": "object",
                "properties": {
                    "user_id": {"type": "string", "description": "User ID"},
                },
                "required": ["user_id"],
            },
            handler=lambda user_id: self._call_api(
                "/api/v1/xiaohongshu/web/fetch_user_profile",
                {"user_id": user_id}
            ),
        )

        self._register_tool(
            name="xiaohongshu_fetch_user_notes",
            description="Fetch Xiaohongshu user notes",
            parameters={
                "type": "object",
                "properties": {
                    "user_id": {"type": "string", "description": "User ID"},
                },
                "required": ["user_id"],
            },
            handler=lambda user_id: self._call_api(
                "/api/v1/xiaohongshu/web/fetch_user_notes",
                {"user_id": user_id}
            ),
        )

        # Search tools
        self._register_tool(
            name="xiaohongshu_search",
            description="Search Xiaohongshu notes",
            parameters={
                "type": "object",
                "properties": {
                    "keyword": {"type": "string", "description": "Search keyword"},
                    "page": {"type": "integer", "description": "Page number", "default": 1},
                },
                "required": ["keyword"],
            },
            handler=lambda keyword, page=1: self._call_api(
                "/api/v1/xiaohongshu/web/fetch_search_notes",
                {"keyword": keyword, "page": page}
            ),
        )

        self._register_tool(
            name="xiaohongshu_search_user",
            description="Search Xiaohongshu users",
            parameters={
                "type": "object",
                "properties": {
                    "keyword": {"type": "string", "description": "Search keyword"},
                    "page": {"type": "integer", "description": "Page number", "default": 1},
                },
                "required": ["keyword"],
            },
            handler=lambda keyword, page=1: self._call_api(
                "/api/v1/xiaohongshu/web/fetch_search_users",
                {"keyword": keyword, "page": page}
            ),
        )

        # Trending tools
        self._register_tool(
            name="xiaohongshu_fetch_trending",
            description="Fetch Xiaohongshu hot list",
            parameters={
                "type": "object",
                "properties": {},
            },
            handler=lambda: self._call_api("/api/v1/xiaohongshu/web/fetch_hot_list"),
        )

        # Explore tools
        self._register_tool(
            name="xiaohongshu_fetch_explore",
            description="Fetch Xiaohongshu explore page",
            parameters={
                "type": "object",
                "properties": {},
            },
            handler=lambda: self._call_api("/api/v1/xiaohongshu/web/fetch_explore"),
        )

    # ===========================================================================
    # Bilibili Tools
    # ===========================================================================

    def _register_bilibili_tools(self) -> None:
        """Register Bilibili MCP tools."""
        # Video tools
        self._register_tool(
            name="bilibili_fetch_video",
            description="Fetch Bilibili video details",
            parameters={
                "type": "object",
                "properties": {
                    "bvid": {"type": "string", "description": "Bilibili BV ID"},
                },
                "required": ["bvid"],
            },
            handler=lambda bvid: self._call_api(
                "/api/v1/bilibili/web/fetch_one_video",
                {"bv_id": bvid}
            ),
        )

        self._register_tool(
            name="bilibili_fetch_video_comments",
            description="Fetch Bilibili video comments",
            parameters={
                "type": "object",
                "properties": {
                    "bvid": {"type": "string", "description": "Bilibili BV ID"},
                    "page": {"type": "integer", "description": "Page number", "default": 1},
                },
                "required": ["bvid"],
            },
            handler=lambda bvid, page=1: self._call_api(
                "/api/v1/bilibili/web/fetch_video_comments",
                {"bv_id": bvid, "pn": page}
            ),
        )

        self._register_tool(
            name="bilibili_fetch_video_danmaku",
            description="Fetch Bilibili video danmaku (bullet comments)",
            parameters={
                "type": "object",
                "properties": {
                    "cid": {"type": "string", "description": "Video CID"},
                },
                "required": ["cid"],
            },
            handler=lambda cid: self._call_api(
                "/api/v1/bilibili/web/fetch_video_danmaku",
                {"cid": cid}
            ),
        )

        # User tools
        self._register_tool(
            name="bilibili_fetch_user",
            description="Fetch Bilibili user profile",
            parameters={
                "type": "object",
                "properties": {
                    "uid": {"type": "string", "description": "Bilibili user ID"},
                },
                "required": ["uid"],
            },
            handler=lambda uid: self._call_api(
                "/api/v1/bilibili/web/fetch_user_profile",
                {"uid": uid}
            ),
        )

        self._register_tool(
            name="bilibili_fetch_user_videos",
            description="Fetch Bilibili user videos",
            parameters={
                "type": "object",
                "properties": {
                    "uid": {"type": "string", "description": "User ID"},
                    "page": {"type": "integer", "description": "Page number", "default": 1},
                },
                "required": ["uid"],
            },
            handler=lambda uid, page=1: self._call_api(
                "/api/v1/bilibili/web/fetch_user_post_videos",
                {"uid": uid, "pn": page}
            ),
        )

        self._register_tool(
            name="bilibili_fetch_user_dynamic",
            description="Fetch Bilibili user dynamic",
            parameters={
                "type": "object",
                "properties": {
                    "uid": {"type": "string", "description": "User ID"},
                },
                "required": ["uid"],
            },
            handler=lambda uid: self._call_api(
                "/api/v1/bilibili/web/fetch_user_dynamic",
                {"uid": uid}
            ),
        )

        # Popular tools
        self._register_tool(
            name="bilibili_fetch_popular",
            description="Fetch Bilibili popular videos",
            parameters={
                "type": "object",
                "properties": {
                    "page": {"type": "integer", "description": "Page number", "default": 1},
                },
            },
            handler=lambda page=1: self._call_api(
                "/api/v1/bilibili/web/fetch_com_popular",
                {"pn": page}
            ),
        )

        # Search tools
        self._register_tool(
            name="bilibili_search",
            description="Search Bilibili videos",
            parameters={
                "type": "object",
                "properties": {
                    "keyword": {"type": "string", "description": "Search keyword"},
                    "page": {"type": "integer", "description": "Page number", "default": 1},
                },
                "required": ["keyword"],
            },
            handler=lambda keyword, page=1: self._call_api(
                "/api/v1/bilibili/web/fetch_general_search",
                {"keyword": keyword, "page": page}
            ),
        )

        # Live tools
        self._register_tool(
            name="bilibili_fetch_live_room",
            description="Fetch Bilibili live room info",
            parameters={
                "type": "object",
                "properties": {
                    "room_id": {"type": "string", "description": "Live room ID"},
                },
                "required": ["room_id"],
            },
            handler=lambda room_id: self._call_api(
                "/api/v1/bilibili/web/fetch_live_room_detail",
                {"room_id": room_id}
            ),
        )

    # ===========================================================================
    # Weibo Tools
    # ===========================================================================

    def _register_weibo_tools(self) -> None:
        """Register Weibo MCP tools."""
        # User tools
        self._register_tool(
            name="weibo_fetch_user",
            description="Fetch Weibo user profile",
            parameters={
                "type": "object",
                "properties": {
                    "uid": {"type": "string", "description": "Weibo user ID"},
                },
                "required": ["uid"],
            },
            handler=lambda uid: self._call_api(
                "/api/v1/weibo/web/fetch_user_profile",
                {"uid": uid}
            ),
        )

        self._register_tool(
            name="weibo_fetch_user_posts",
            description="Fetch Weibo user posts",
            parameters={
                "type": "object",
                "properties": {
                    "uid": {"type": "string", "description": "User ID"},
                    "page": {"type": "integer", "description": "Page number", "default": 1},
                },
                "required": ["uid"],
            },
            handler=lambda uid, page=1: self._call_api(
                "/api/v1/weibo/web/fetch_user_posts",
                {"uid": uid, "page": page}
            ),
        )

        self._register_tool(
            name="weibo_fetch_user_followers",
            description="Fetch Weibo user followers",
            parameters={
                "type": "object",
                "properties": {
                    "uid": {"type": "string", "description": "User ID"},
                },
                "required": ["uid"],
            },
            handler=lambda uid: self._call_api(
                "/api/v1/weibo/web/fetch_user_followers",
                {"uid": uid}
            ),
        )

        self._register_tool(
            name="weibo_fetch_user_following",
            description="Fetch Weibo user following",
            parameters={
                "type": "object",
                "properties": {
                    "uid": {"type": "string", "description": "User ID"},
                },
                "required": ["uid"],
            },
            handler=lambda uid: self._call_api(
                "/api/v1/weibo/web/fetch_user_following",
                {"uid": uid}
            ),
        )

        # Post tools
        self._register_tool(
            name="weibo_fetch_post",
            description="Fetch Weibo post details",
            parameters={
                "type": "object",
                "properties": {
                    "mid": {"type": "string", "description": "Post MID"},
                },
                "required": ["mid"],
            },
            handler=lambda mid: self._call_api(
                "/api/v1/weibo/web/fetch_post_detail",
                {"mid": mid}
            ),
        )

        self._register_tool(
            name="weibo_fetch_post_comments",
            description="Fetch Weibo post comments",
            parameters={
                "type": "object",
                "properties": {
                    "mid": {"type": "string", "description": "Post MID"},
                    "page": {"type": "integer", "description": "Page number", "default": 1},
                },
                "required": ["mid"],
            },
            handler=lambda mid, page=1: self._call_api(
                "/api/v1/weibo/web/fetch_post_comments",
                {"mid": mid, "page": page}
            ),
        )

        # Search tools
        self._register_tool(
            name="weibo_search",
            description="Search Weibo posts",
            parameters={
                "type": "object",
                "properties": {
                    "keyword": {"type": "string", "description": "Search keyword"},
                    "page": {"type": "integer", "description": "Page number", "default": 1},
                },
                "required": ["keyword"],
            },
            handler=lambda keyword, page=1: self._call_api(
                "/api/v1/weibo/web/fetch_search",
                {"keyword": keyword, "page": page}
            ),
        )

        # Trending tools
        self._register_tool(
            name="weibo_fetch_trending",
            description="Fetch Weibo hot search",
            parameters={
                "type": "object",
                "properties": {},
            },
            handler=lambda: self._call_api("/api/v1/weibo/web/fetch_hot_list"),
        )

    # ===========================================================================
    # Kuaishou Tools
    # ===========================================================================

    def _register_kuaishou_tools(self) -> None:
        """Register Kuaishou MCP tools."""
        # Video tools
        self._register_tool(
            name="kuaishou_fetch_video",
            description="Fetch Kuaishou video details",
            parameters={
                "type": "object",
                "properties": {
                    "photo_id": {"type": "string", "description": "Kuaishou photo ID"},
                },
                "required": ["photo_id"],
            },
            handler=lambda photo_id: self._call_api(
                "/api/v1/kuaishou/web/fetch_video_detail",
                {"photo_id": photo_id}
            ),
        )

        self._register_tool(
            name="kuaishou_fetch_video_comments",
            description="Fetch Kuaishou video comments",
            parameters={
                "type": "object",
                "properties": {
                    "photo_id": {"type": "string", "description": "Photo ID"},
                },
                "required": ["photo_id"],
            },
            handler=lambda photo_id: self._call_api(
                "/api/v1/kuaishou/web/fetch_video_comments",
                {"photo_id": photo_id}
            ),
        )

        # User tools
        self._register_tool(
            name="kuaishou_fetch_user",
            description="Fetch Kuaishou user profile",
            parameters={
                "type": "object",
                "properties": {
                    "user_id": {"type": "string", "description": "User ID"},
                },
                "required": ["user_id"],
            },
            handler=lambda user_id: self._call_api(
                "/api/v1/kuaishou/web/fetch_user_profile",
                {"user_id": user_id}
            ),
        )

        self._register_tool(
            name="kuaishou_fetch_user_videos",
            description="Fetch Kuaishou user videos",
            parameters={
                "type": "object",
                "properties": {
                    "user_id": {"type": "string", "description": "User ID"},
                },
                "required": ["user_id"],
            },
            handler=lambda user_id: self._call_api(
                "/api/v1/kuaishou/web/fetch_user_videos",
                {"user_id": user_id}
            ),
        )

        self._register_tool(
            name="kuaishou_fetch_user_followers",
            description="Fetch Kuaishou user followers",
            parameters={
                "type": "object",
                "properties": {
                    "user_id": {"type": "string", "description": "User ID"},
                },
                "required": ["user_id"],
            },
            handler=lambda user_id: self._call_api(
                "/api/v1/kuaishou/web/fetch_user_followers",
                {"user_id": user_id}
            ),
        )

        # Search tools
        self._register_tool(
            name="kuaishou_search",
            description="Search Kuaishou videos",
            parameters={
                "type": "object",
                "properties": {
                    "keyword": {"type": "string", "description": "Search keyword"},
                },
                "required": ["keyword"],
            },
            handler=lambda keyword: self._call_api(
                "/api/v1/kuaishou/web/fetch_search",
                {"keyword": keyword}
            ),
        )

        # Trending tools
        self._register_tool(
            name="kuaishou_fetch_trending",
            description="Fetch Kuaishou hot list",
            parameters={
                "type": "object",
                "properties": {},
            },
            handler=lambda: self._call_api("/api/v1/kuaishou/web/fetch_hot_list"),
        )

        # Live tools
        self._register_tool(
            name="kuaishou_fetch_live_room",
            description="Fetch Kuaishou live room info",
            parameters={
                "type": "object",
                "properties": {
                    "room_id": {"type": "string", "description": "Live room ID"},
                },
                "required": ["room_id"],
            },
            handler=lambda room_id: self._call_api(
                "/api/v1/kuaishou/web/fetch_room_info",
                {"room_id": room_id}
            ),
        )

    # ===========================================================================
    # LinkedIn Tools
    # ===========================================================================

    def _register_linkedin_tools(self) -> None:
        """Register LinkedIn MCP tools."""
        # User tools
        self._register_tool(
            name="linkedin_fetch_user",
            description="Fetch LinkedIn user profile",
            parameters={
                "type": "object",
                "properties": {
                    "username": {"type": "string", "description": "LinkedIn username"},
                },
                "required": ["username"],
            },
            handler=lambda username: self._call_api(
                "/api/v1/linkedin/web/fetch_user_profile",
                {"username": username}
            ),
        )

        self._register_tool(
            name="linkedin_fetch_user_posts",
            description="Fetch LinkedIn user posts",
            parameters={
                "type": "object",
                "properties": {
                    "user_id": {"type": "string", "description": "User ID"},
                },
                "required": ["user_id"],
            },
            handler=lambda user_id: self._call_api(
                "/api/v1/linkedin/web/fetch_user_posts",
                {"user_id": user_id}
            ),
        )

        self._register_tool(
            name="linkedin_fetch_user_connections",
            description="Fetch LinkedIn user connections",
            parameters={
                "type": "object",
                "properties": {
                    "user_id": {"type": "string", "description": "User ID"},
                },
                "required": ["user_id"],
            },
            handler=lambda user_id: self._call_api(
                "/api/v1/linkedin/web/fetch_user_connections",
                {"user_id": user_id}
            ),
        )

        # Company tools
        self._register_tool(
            name="linkedin_fetch_company",
            description="Fetch LinkedIn company profile",
            parameters={
                "type": "object",
                "properties": {
                    "company_id": {"type": "string", "description": "Company ID"},
                },
                "required": ["company_id"],
            },
            handler=lambda company_id: self._call_api(
                "/api/v1/linkedin/web/fetch_company_profile",
                {"company_id": company_id}
            ),
        )

        self._register_tool(
            name="linkedin_fetch_company_posts",
            description="Fetch LinkedIn company posts",
            parameters={
                "type": "object",
                "properties": {
                    "company_id": {"type": "string", "description": "Company ID"},
                },
                "required": ["company_id"],
            },
            handler=lambda company_id: self._call_api(
                "/api/v1/linkedin/web/fetch_company_posts",
                {"company_id": company_id}
            ),
        )

        # Search tools
        self._register_tool(
            name="linkedin_search",
            description="Search LinkedIn",
            parameters={
                "type": "object",
                "properties": {
                    "keyword": {"type": "string", "description": "Search keyword"},
                },
                "required": ["keyword"],
            },
            handler=lambda keyword: self._call_api(
                "/api/v1/linkedin/web/fetch_search",
                {"keyword": keyword}
            ),
        )

        self._register_tool(
            name="linkedin_search_people",
            description="Search LinkedIn people",
            parameters={
                "type": "object",
                "properties": {
                    "keyword": {"type": "string", "description": "Search keyword"},
                },
                "required": ["keyword"],
            },
            handler=lambda keyword: self._call_api(
                "/api/v1/linkedin/web/fetch_search_people",
                {"keyword": keyword}
            ),
        )

        self._register_tool(
            name="linkedin_search_jobs",
            description="Search LinkedIn jobs",
            parameters={
                "type": "object",
                "properties": {
                    "keyword": {"type": "string", "description": "Search keyword"},
                },
                "required": ["keyword"],
            },
            handler=lambda keyword: self._call_api(
                "/api/v1/linkedin/web/fetch_search_jobs",
                {"keyword": keyword}
            ),
        )

    # ===========================================================================
    # Reddit Tools
    # ===========================================================================

    def _register_reddit_tools(self) -> None:
        """Register Reddit MCP tools."""
        # Post tools
        self._register_tool(
            name="reddit_fetch_post",
            description="Fetch Reddit post details",
            parameters={
                "type": "object",
                "properties": {
                    "subreddit": {"type": "string", "description": "Subreddit name"},
                    "post_id": {"type": "string", "description": "Post ID"},
                },
                "required": ["subreddit", "post_id"],
            },
            handler=lambda subreddit, post_id: self._call_api(
                "/api/v1/reddit/app/fetch_post_detail",
                {"subreddit": subreddit, "post_id": post_id}
            ),
        )

        self._register_tool(
            name="reddit_fetch_post_comments",
            description="Fetch Reddit post comments",
            parameters={
                "type": "object",
                "properties": {
                    "subreddit": {"type": "string", "description": "Subreddit name"},
                    "post_id": {"type": "string", "description": "Post ID"},
                },
                "required": ["subreddit", "post_id"],
            },
            handler=lambda subreddit, post_id: self._call_api(
                "/api/v1/reddit/app/fetch_post_comments",
                {"subreddit": subreddit, "post_id": post_id}
            ),
        )

        # Subreddit tools
        self._register_tool(
            name="reddit_fetch_subreddit",
            description="Fetch subreddit posts",
            parameters={
                "type": "object",
                "properties": {
                    "subreddit": {"type": "string", "description": "Subreddit name"},
                    "sort": {"type": "string", "description": "Sort order", "default": "hot"},
                },
                "required": ["subreddit"],
            },
            handler=lambda subreddit, sort="hot": self._call_api(
                "/api/v1/reddit/app/fetch_subreddit",
                {"subreddit": subreddit, "sort": sort}
            ),
        )

        self._register_tool(
            name="reddit_fetch_subreddit_info",
            description="Fetch subreddit info",
            parameters={
                "type": "object",
                "properties": {
                    "subreddit": {"type": "string", "description": "Subreddit name"},
                },
                "required": ["subreddit"],
            },
            handler=lambda subreddit: self._call_api(
                "/api/v1/reddit/app/fetch_subreddit_about",
                {"subreddit": subreddit}
            ),
        )

        # User tools
        self._register_tool(
            name="reddit_fetch_user",
            description="Fetch Reddit user profile",
            parameters={
                "type": "object",
                "properties": {
                    "username": {"type": "string", "description": "Reddit username"},
                },
                "required": ["username"],
            },
            handler=lambda username: self._call_api(
                "/api/v1/reddit/app/fetch_user_profile",
                {"username": username}
            ),
        )

        self._register_tool(
            name="reddit_fetch_user_posts",
            description="Fetch Reddit user posts",
            parameters={
                "type": "object",
                "properties": {
                    "username": {"type": "string", "description": "Username"},
                    "sort": {"type": "string", "description": "Sort order", "default": "new"},
                },
                "required": ["username"],
            },
            handler=lambda username, sort="new": self._call_api(
                "/api/v1/reddit/app/fetch_user_posts",
                {"username": username, "sort": sort}
            ),
        )

        # Search tools
        self._register_tool(
            name="reddit_search",
            description="Search Reddit",
            parameters={
                "type": "object",
                "properties": {
                    "keyword": {"type": "string", "description": "Search keyword"},
                    "sort": {"type": "string", "description": "Sort order", "default": "relevance"},
                },
                "required": ["keyword"],
            },
            handler=lambda keyword, sort="relevance": self._call_api(
                "/api/v1/reddit/app/fetch_search",
                {"keyword": keyword, "sort": sort}
            ),
        )

        # Popular tools
        self._register_tool(
            name="reddit_fetch_popular",
            description="Fetch Reddit popular posts",
            parameters={
                "type": "object",
                "properties": {},
            },
            handler=lambda: self._call_api("/api/v1/reddit/app/fetch_popular"),
        )

    # ===========================================================================
    # Zhihu Tools
    # ===========================================================================

    def _register_zhihu_tools(self) -> None:
        """Register Zhihu MCP tools."""
        # Question tools
        self._register_tool(
            name="zhihu_fetch_question",
            description="Fetch Zhihu question details",
            parameters={
                "type": "object",
                "properties": {
                    "question_id": {"type": "string", "description": "Question ID"},
                },
                "required": ["question_id"],
            },
            handler=lambda question_id: self._call_api(
                "/api/v1/zhihu/web/fetch_question_detail",
                {"question_id": question_id}
            ),
        )

        self._register_tool(
            name="zhihu_fetch_question_answers",
            description="Fetch Zhihu question answers",
            parameters={
                "type": "object",
                "properties": {
                    "question_id": {"type": "string", "description": "Question ID"},
                },
                "required": ["question_id"],
            },
            handler=lambda question_id: self._call_api(
                "/api/v1/zhihu/web/fetch_question_answers",
                {"question_id": question_id}
            ),
        )

        # Answer tools
        self._register_tool(
            name="zhihu_fetch_answer",
            description="Fetch Zhihu answer details",
            parameters={
                "type": "object",
                "properties": {
                    "answer_id": {"type": "string", "description": "Answer ID"},
                },
                "required": ["answer_id"],
            },
            handler=lambda answer_id: self._call_api(
                "/api/v1/zhihu/web/fetch_answer_detail",
                {"answer_id": answer_id}
            ),
        )

        # User tools
        self._register_tool(
            name="zhihu_fetch_user",
            description="Fetch Zhihu user profile",
            parameters={
                "type": "object",
                "properties": {
                    "user_id": {"type": "string", "description": "User URL token"},
                },
                "required": ["user_id"],
            },
            handler=lambda user_id: self._call_api(
                "/api/v1/zhihu/web/fetch_user_info",
                {"user_url_token": user_id}
            ),
        )

        self._register_tool(
            name="zhihu_fetch_user_answers",
            description="Fetch Zhihu user answers",
            parameters={
                "type": "object",
                "properties": {
                    "user_id": {"type": "string", "description": "User URL token"},
                },
                "required": ["user_id"],
            },
            handler=lambda user_id: self._call_api(
                "/api/v1/zhihu/web/fetch_user_articles",
                {"user_url_token": user_id}
            ),
        )

        # Topic tools
        self._register_tool(
            name="zhihu_fetch_topic",
            description="Fetch Zhihu topic details",
            parameters={
                "type": "object",
                "properties": {
                    "topic_id": {"type": "string", "description": "Topic ID"},
                },
                "required": ["topic_id"],
            },
            handler=lambda topic_id: self._call_api(
                "/api/v1/zhihu/web/fetch_topic_detail",
                {"topic_id": topic_id}
            ),
        )

        # Search tools
        self._register_tool(
            name="zhihu_search",
            description="Search Zhihu",
            parameters={
                "type": "object",
                "properties": {
                    "keyword": {"type": "string", "description": "Search keyword"},
                },
                "required": ["keyword"],
            },
            handler=lambda keyword: self._call_api(
                "/api/v1/zhihu/web/fetch_general_search",
                {"keyword": keyword}
            ),
        )

        # Trending tools
        self._register_tool(
            name="zhihu_fetch_trending",
            description="Fetch Zhihu hot list",
            parameters={
                "type": "object",
                "properties": {},
            },
            handler=lambda: self._call_api("/api/v1/zhihu/web/fetch_hot_list"),
        )

        self._register_tool(
            name="zhihu_fetch_recommend",
            description="Fetch Zhihu recommendations",
            parameters={
                "type": "object",
                "properties": {},
            },
            handler=lambda: self._call_api("/api/v1/zhihu/web/fetch_hot_recommend"),
        )

    # ===========================================================================
    # Threads Tools
    # ===========================================================================

    def _register_threads_tools(self) -> None:
        """Register Threads MCP tools."""
        # User tools
        self._register_tool(
            name="threads_fetch_user",
            description="Fetch Threads user profile",
            parameters={
                "type": "object",
                "properties": {
                    "username": {"type": "string", "description": "Threads username"},
                },
                "required": ["username"],
            },
            handler=lambda username: self._call_api(
                "/api/v1/threads/web/fetch_user_profile",
                {"username": username}
            ),
        )

        self._register_tool(
            name="threads_fetch_user_threads",
            description="Fetch Threads user threads",
            parameters={
                "type": "object",
                "properties": {
                    "user_id": {"type": "string", "description": "User ID"},
                },
                "required": ["user_id"],
            },
            handler=lambda user_id: self._call_api(
                "/api/v1/threads/web/fetch_user_threads",
                {"user_id": user_id}
            ),
        )

        # Thread tools
        self._register_tool(
            name="threads_fetch_thread",
            description="Fetch Threads post details",
            parameters={
                "type": "object",
                "properties": {
                    "thread_id": {"type": "string", "description": "Thread ID"},
                },
                "required": ["thread_id"],
            },
            handler=lambda thread_id: self._call_api(
                "/api/v1/threads/web/fetch_thread_detail",
                {"thread_id": thread_id}
            ),
        )

        self._register_tool(
            name="threads_fetch_thread_replies",
            description="Fetch Threads post replies",
            parameters={
                "type": "object",
                "properties": {
                    "thread_id": {"type": "string", "description": "Thread ID"},
                },
                "required": ["thread_id"],
            },
            handler=lambda thread_id: self._call_api(
                "/api/v1/threads/web/fetch_thread_replies",
                {"thread_id": thread_id}
            ),
        )

        # Search tools
        self._register_tool(
            name="threads_search",
            description="Search Threads",
            parameters={
                "type": "object",
                "properties": {
                    "keyword": {"type": "string", "description": "Search keyword"},
                },
                "required": ["keyword"],
            },
            handler=lambda keyword: self._call_api(
                "/api/v1/threads/web/fetch_search",
                {"keyword": keyword}
            ),
        )

        # Explore tools
        self._register_tool(
            name="threads_fetch_explore",
            description="Fetch Threads explore page",
            parameters={
                "type": "object",
                "properties": {},
            },
            handler=lambda: self._call_api("/api/v1/threads/web/fetch_explore"),
        )

    # ===========================================================================
    # WeChat Tools
    # ===========================================================================

    def _register_wechat_tools(self) -> None:
        """Register WeChat MCP tools."""
        # Channels tools
        self._register_tool(
            name="wechat_fetch_user",
            description="Fetch WeChat Channels user profile",
            parameters={
                "type": "object",
                "properties": {
                    "usr_name": {"type": "string", "description": "User name"},
                },
                "required": ["usr_name"],
            },
            handler=lambda usr_name: self._call_api(
                "/api/v1/wechat/channels/fetch_user_profile",
                {"usr_name": usr_name}
            ),
        )

        self._register_tool(
            name="wechat_fetch_user_videos",
            description="Fetch WeChat Channels user videos",
            parameters={
                "type": "object",
                "properties": {
                    "usr_name": {"type": "string", "description": "User name"},
                },
                "required": ["usr_name"],
            },
            handler=lambda usr_name: self._call_api(
                "/api/v1/wechat/channels/fetch_user_videos",
                {"usr_name": usr_name}
            ),
        )

        self._register_tool(
            name="wechat_fetch_video",
            description="Fetch WeChat Channels video details",
            parameters={
                "type": "object",
                "properties": {
                    "feed_id": {"type": "string", "description": "Feed ID"},
                },
                "required": ["feed_id"],
            },
            handler=lambda feed_id: self._call_api(
                "/api/v1/wechat/channels/fetch_video_detail",
                {"feed_id": feed_id}
            ),
        )

        self._register_tool(
            name="wechat_fetch_video_comments",
            description="Fetch WeChat Channels video comments",
            parameters={
                "type": "object",
                "properties": {
                    "feed_id": {"type": "string", "description": "Feed ID"},
                },
                "required": ["feed_id"],
            },
            handler=lambda feed_id: self._call_api(
                "/api/v1/wechat/channels/fetch_video_comments",
                {"feed_id": feed_id}
            ),
        )

        self._register_tool(
            name="wechat_fetch_trending",
            description="Fetch WeChat Channels trending",
            parameters={
                "type": "object",
                "properties": {},
            },
            handler=lambda: self._call_api("/api/v1/wechat/channels/fetch_hot_list"),
        )

        # Media Platform tools
        self._register_tool(
            name="wechat_fetch_article",
            description="Fetch WeChat article details",
            parameters={
                "type": "object",
                "properties": {
                    "article_id": {"type": "string", "description": "Article ID"},
                },
                "required": ["article_id"],
            },
            handler=lambda article_id: self._call_api(
                "/api/v1/wechat/media/fetch_article_detail",
                {"article_id": article_id}
            ),
        )

        self._register_tool(
            name="wechat_fetch_media_profile",
            description="Fetch WeChat media profile",
            parameters={
                "type": "object",
                "properties": {
                    "biz": {"type": "string", "description": "Media biz ID"},
                },
                "required": ["biz"],
            },
            handler=lambda biz: self._call_api(
                "/api/v1/wechat/media/fetch_user_profile",
                {"biz": biz}
            ),
        )

    # ===========================================================================
    # Lemon8 Tools
    # ===========================================================================

    def _register_lemon8_tools(self) -> None:
        """Register Lemon8 MCP tools."""
        # User tools
        self._register_tool(
            name="lemon8_fetch_user",
            description="Fetch Lemon8 user profile",
            parameters={
                "type": "object",
                "properties": {
                    "user_id": {"type": "string", "description": "Lemon8 user ID"},
                },
                "required": ["user_id"],
            },
            handler=lambda user_id: self._call_api(
                "/api/v1/lemon8/app/fetch_user_profile",
                {"user_id": user_id}
            ),
        )

        self._register_tool(
            name="lemon8_fetch_user_posts",
            description="Fetch Lemon8 user posts",
            parameters={
                "type": "object",
                "properties": {
                    "user_id": {"type": "string", "description": "User ID"},
                },
                "required": ["user_id"],
            },
            handler=lambda user_id: self._call_api(
                "/api/v1/lemon8/app/fetch_user_posts",
                {"user_id": user_id}
            ),
        )

        # Post tools
        self._register_tool(
            name="lemon8_fetch_post",
            description="Fetch Lemon8 post details",
            parameters={
                "type": "object",
                "properties": {
                    "post_id": {"type": "string", "description": "Post ID"},
                },
                "required": ["post_id"],
            },
            handler=lambda post_id: self._call_api(
                "/api/v1/lemon8/app/fetch_post_detail",
                {"post_id": post_id}
            ),
        )

        self._register_tool(
            name="lemon8_fetch_post_comments",
            description="Fetch Lemon8 post comments",
            parameters={
                "type": "object",
                "properties": {
                    "post_id": {"type": "string", "description": "Post ID"},
                },
                "required": ["post_id"],
            },
            handler=lambda post_id: self._call_api(
                "/api/v1/lemon8/app/fetch_post_comments",
                {"post_id": post_id}
            ),
        )

        # Search tools
        self._register_tool(
            name="lemon8_search",
            description="Search Lemon8 posts",
            parameters={
                "type": "object",
                "properties": {
                    "keyword": {"type": "string", "description": "Search keyword"},
                },
                "required": ["keyword"],
            },
            handler=lambda keyword: self._call_api(
                "/api/v1/lemon8/app/fetch_search",
                {"keyword": keyword}
            ),
        )

        # Trending tools
        self._register_tool(
            name="lemon8_fetch_trending",
            description="Fetch Lemon8 hot list",
            parameters={
                "type": "object",
                "properties": {},
            },
            handler=lambda: self._call_api("/api/v1/lemon8/app/fetch_hot_list"),
        )

        # Explore tools
        self._register_tool(
            name="lemon8_fetch_explore",
            description="Fetch Lemon8 explore page",
            parameters={
                "type": "object",
                "properties": {},
            },
            handler=lambda: self._call_api("/api/v1/lemon8/app/fetch_explore"),
        )

        # Category tools
        self._register_tool(
            name="lemon8_fetch_category",
            description="Fetch Lemon8 category",
            parameters={
                "type": "object",
                "properties": {
                    "category": {"type": "string", "description": "Category name"},
                },
                "required": ["category"],
            },
            handler=lambda category: self._call_api(
                "/api/v1/lemon8/app/fetch_category",
                {"category": category}
            ),
        )

    # ===========================================================================
    # Utility Tools
    # ===========================================================================

    def _register_utility_tools(self) -> None:
        """Register utility MCP tools."""
        # Universal parsing tools
        self._register_tool(
            name="hybrid_parse_video",
            description="Universal video URL parser - works with any platform",
            parameters={
                "type": "object",
                "properties": {
                    "url": {"type": "string", "description": "Video URL to parse"},
                },
                "required": ["url"],
            },
            handler=lambda url: self._call_api(
                "/api/v1/hybrid/video_data",
                {"url": url}
            ),
        )

        self._register_tool(
            name="hybrid_parse_user",
            description="Universal user URL parser - works with any platform",
            parameters={
                "type": "object",
                "properties": {
                    "url": {"type": "string", "description": "User URL to parse"},
                },
                "required": ["url"],
            },
            handler=lambda url: self._call_api(
                "/api/v1/hybrid/user_data",
                {"url": url}
            ),
        )

        # ID conversion tools
        self._register_tool(
            name="douyin_url_to_video_id",
            description="Extract video ID from Douyin URL",
            parameters={
                "type": "object",
                "properties": {
                    "url": {"type": "string", "description": "Douyin URL"},
                },
                "required": ["url"],
            },
            handler=lambda url: self._call_api(
                "/api/v1/douyin/web/get_aweme_id",
                {"url": url}
            ),
        )

        self._register_tool(
            name="douyin_url_to_user_id",
            description="Extract user ID from Douyin URL",
            parameters={
                "type": "object",
                "properties": {
                    "url": {"type": "string", "description": "Douyin URL"},
                },
                "required": ["url"],
            },
            handler=lambda url: self._call_api(
                "/api/v1/douyin/web/get_sec_user_id",
                {"url": url}
            ),
        )

        self._register_tool(
            name="tiktok_url_to_video_id",
            description="Extract video ID from TikTok URL",
            parameters={
                "type": "object",
                "properties": {
                    "url": {"type": "string", "description": "TikTok URL"},
                },
                "required": ["url"],
            },
            handler=lambda url: self._call_api(
                "/api/v1/tiktok/web/get_aweme_id",
                {"url": url}
            ),
        )

        # Health tools
        self._register_tool(
            name="health_check",
            description="Check API server health",
            parameters={
                "type": "object",
                "properties": {},
            },
            handler=lambda: self._call_api("/api/v1/health/check"),
        )

        self._register_tool(
            name="get_platforms",
            description="Get list of supported platforms",
            parameters={
                "type": "object",
                "properties": {},
            },
            handler=lambda: self._call_api("/api/v1/health/platforms"),
        )

        # NetEase tools
        self._register_tool(
            name="netease_fetch_song",
            description="Fetch NetEase Cloud Music song details",
            parameters={
                "type": "object",
                "properties": {
                    "song_id": {"type": "string", "description": "Song ID"},
                },
                "required": ["song_id"],
            },
            handler=lambda song_id: self._call_api(
                "/api/v1/netease/music/fetch_song_detail",
                {"song_id": song_id}
            ),
        )

        self._register_tool(
            name="netease_search",
            description="Search NetEase Cloud Music",
            parameters={
                "type": "object",
                "properties": {
                    "keyword": {"type": "string", "description": "Search keyword"},
                },
                "required": ["keyword"],
            },
            handler=lambda keyword: self._call_api(
                "/api/v1/netease/music/fetch_search",
                {"keyword": keyword}
            ),
        )

        self._register_tool(
            name="netease_fetch_playlist",
            description="Fetch NetEase Cloud Music playlist",
            parameters={
                "type": "object",
                "properties": {
                    "playlist_id": {"type": "string", "description": "Playlist ID"},
                },
                "required": ["playlist_id"],
            },
            handler=lambda playlist_id: self._call_api(
                "/api/v1/netease/music/fetch_playlist_detail",
                {"playlist_id": playlist_id}
            ),
        )

        self._register_tool(
            name="netease_fetch_artist",
            description="Fetch NetEase Cloud Music artist details",
            parameters={
                "type": "object",
                "properties": {
                    "artist_id": {"type": "string", "description": "Artist ID"},
                },
                "required": ["artist_id"],
            },
            handler=lambda artist_id: self._call_api(
                "/api/v1/netease/music/fetch_artist_detail",
                {"artist_id": artist_id}
            ),
        )

    # ===========================================================================
    # MCP Protocol Methods
    # ===========================================================================

    def list_tools(self) -> list[dict[str, Any]]:
        """List all available MCP tools."""
        return [
            {
                "name": tool["name"],
                "description": tool["description"],
                "inputSchema": tool["parameters"],
            }
            for tool in self.tools.values()
        ]

    def call_tool(self, name: str, arguments: dict[str, Any]) -> dict[str, Any]:
        """Call an MCP tool by name."""
        if name not in self.tools:
            return {"error": f"Tool '{name}' not found"}

        tool = self.tools[name]
        try:
            result = tool["handler"](**arguments)
            return {"result": result}
        except Exception as e:
            return {"error": str(e)}

    def to_dict(self) -> dict[str, Any]:
        """Export MCP server configuration as dict."""
        return {
            "name": "socialmedia-hub",
            "version": "0.1.0",
            "tools": self.list_tools(),
        }


def create_mcp_server(api_key: str, base_url: str = "http://127.0.0.1:8000") -> MCPServer:
    """Create an MCP server instance."""
    return MCPServer(api_key=api_key, base_url=base_url)
