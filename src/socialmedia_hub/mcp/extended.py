"""Extended MCP tools for SocialMedia-Hub.

This module adds additional tools to reach 300+ total MCP tools.
"""

from __future__ import annotations

from typing import Any


def register_extended_tools(mcp_server: Any) -> None:
    """Register extended tools on the MCP server."""
    _register_tiktok_extended(mcp_server)
    _register_douyin_extended(mcp_server)
    _register_instagram_extended(mcp_server)
    _register_youtube_extended(mcp_server)
    _register_twitter_extended(mcp_server)
    _register_xiaohongshu_extended(mcp_server)
    _register_bilibili_extended(mcp_server)
    _register_weibo_extended(mcp_server)
    _register_kuaishou_extended(mcp_server)
    _register_linkedin_extended(mcp_server)
    _register_reddit_extended(mcp_server)
    _register_zhihu_extended(mcp_server)
    _register_threads_extended(mcp_server)
    _register_wechat_extended(mcp_server)
    _register_lemon8_extended(mcp_server)
    _register_utility_extended(mcp_server)


def _register_tiktok_extended(mcp: Any) -> None:
    """Register extended TikTok tools."""
    tools = [
        ("tiktok_fetch_user_post_v2", "Fetch TikTok user posts V2", {"sec_uid": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["sec_uid"]),
        ("tiktok_fetch_user_liked_v2", "Fetch TikTok user liked videos V2", {"sec_uid": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["sec_uid"]),
        ("tiktok_fetch_user_playlist", "Fetch TikTok user playlist", {"sec_uid": {"type": "string"}}, ["sec_uid"]),
        ("tiktok_fetch_video_related", "Fetch TikTok related videos", {"video_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["video_id"]),
        ("tiktok_fetch_video_similar", "Fetch TikTok similar videos", {"video_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["video_id"]),
        ("tiktok_fetch_hashtag_info", "Fetch TikTok hashtag info", {"hashtag": {"type": "string"}}, ["hashtag"]),
        ("tiktok_fetch_hashtag_videos", "Fetch TikTok hashtag videos", {"hashtag": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["hashtag"]),
        ("tiktok_fetch_music_info", "Fetch TikTok music info", {"music_id": {"type": "string"}}, ["music_id"]),
        ("tiktok_fetch_music_videos", "Fetch TikTok music videos", {"music_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["music_id"]),
        ("tiktok_fetch_effect_info", "Fetch TikTok effect info", {"effect_id": {"type": "string"}}, ["effect_id"]),
        ("tiktok_fetch_effect_videos", "Fetch TikTok effect videos", {"effect_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["effect_id"]),
        ("tiktok_fetch_user_comments", "Fetch TikTok user comments", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
    ]
    _add_tools(mcp, tools, "tiktok", "/api/v1/tiktok/web")


def _register_douyin_extended(mcp: Any) -> None:
    """Register extended Douyin tools."""
    tools = [
        ("douyin_fetch_user_liked", "Fetch Douyin user liked videos", {"sec_user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["sec_user_id"]),
        ("douyin_fetch_user_collection", "Fetch Douyin user collection", {"sec_user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["sec_user_id"]),
        ("douyin_fetch_user_mix", "Fetch Douyin user mix", {"mix_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["mix_id"]),
        ("douyin_fetch_hashtag_info", "Fetch Douyin hashtag info", {"hashtag": {"type": "string"}}, ["hashtag"]),
        ("douyin_fetch_hashtag_videos", "Fetch Douyin hashtag videos", {"hashtag": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["hashtag"]),
        ("douyin_fetch_music_info", "Fetch Douyin music info", {"music_id": {"type": "string"}}, ["music_id"]),
        ("douyin_fetch_music_videos", "Fetch Douyin music videos", {"music_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["music_id"]),
        ("douyin_fetch_product_detail", "Fetch Douyin product detail", {"product_id": {"type": "string"}}, ["product_id"]),
        ("douyin_fetch_product_reviews", "Fetch Douyin product reviews", {"product_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["product_id"]),
        ("douyin_fetch_user_fans", "Fetch Douyin user fans", {"sec_user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["sec_user_id"]),
        ("douyin_fetch_user_following", "Fetch Douyin user following", {"sec_user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["sec_user_id"]),
        ("douyin_fetch_user_dynamic", "Fetch Douyin user dynamic", {"sec_user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["sec_user_id"]),
        ("douyin_fetch_user_live", "Fetch Douyin user live", {"uid": {"type": "string"}}, ["uid"]),
        ("douyin_fetch_video_similar", "Fetch Douyin similar videos", {"aweme_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["aweme_id"]),
        ("douyin_fetch_hot_list", "Fetch Douyin hot list", {"count": {"type": "integer", "default": 20}}, []),
    ]
    _add_tools(mcp, tools, "douyin", "/api/v1/douyin/web")


def _register_instagram_extended(mcp: Any) -> None:
    """Register extended Instagram tools."""
    tools = [
        ("instagram_fetch_user_reels_v2", "Fetch Instagram user reels V2", {"user_id": {"type": "string"}}, ["user_id"]),
        ("instagram_fetch_user_stories", "Fetch Instagram user stories", {"user_id": {"type": "string"}}, ["user_id"]),
        ("instagram_fetch_user_highlights", "Fetch Instagram user highlights", {"user_id": {"type": "string"}}, ["user_id"]),
        ("instagram_fetch_post_likes", "Fetch Instagram post likes", {"media_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["media_id"]),
        ("instagram_fetch_post_saves", "Fetch Instagram post saves", {"media_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["media_id"]),
        ("instagram_fetch_user_tagged", "Fetch Instagram user tagged posts", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("instagram_fetch_user_guides", "Fetch Instagram user guides", {"user_id": {"type": "string"}}, ["user_id"]),
        ("instagram_fetch_location_info", "Fetch Instagram location info", {"location_id": {"type": "string"}}, ["location_id"]),
        ("instagram_fetch_location_posts", "Fetch Instagram location posts", {"location_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["location_id"]),
        ("instagram_fetch_explore_categories", "Fetch Instagram explore categories", {}, []),
        ("instagram_fetch_user_insights", "Fetch Instagram user insights", {"user_id": {"type": "string"}}, ["user_id"]),
        ("instagram_fetch_post_insights", "Fetch Instagram post insights", {"media_id": {"type": "string"}}, ["media_id"]),
        ("instagram_fetch_story_insights", "Fetch Instagram story insights", {"media_id": {"type": "string"}}, ["media_id"]),
    ]
    _add_tools(mcp, tools, "instagram", "/api/v1/instagram/v1")


def _register_youtube_extended(mcp: Any) -> None:
    """Register extended YouTube tools."""
    tools = [
        ("youtube_fetch_channel_playlists", "Fetch YouTube channel playlists", {"channel_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["channel_id"]),
        ("youtube_fetch_channel_shorts", "Fetch YouTube channel shorts", {"channel_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["channel_id"]),
        ("youtube_fetch_channel_community", "Fetch YouTube channel community", {"channel_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["channel_id"]),
        ("youtube_fetch_playlist_videos", "Fetch YouTube playlist videos", {"playlist_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["playlist_id"]),
        ("youtube_fetch_video_chapters", "Fetch YouTube video chapters", {"video_id": {"type": "string"}}, ["video_id"]),
        ("youtube_fetch_video_cards", "Fetch YouTube video cards", {"video_id": {"type": "string"}}, ["video_id"]),
        ("youtube_fetch_related_channels", "Fetch YouTube related channels", {"channel_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["channel_id"]),
        ("youtube_fetch_channel_about", "Fetch YouTube channel about", {"channel_id": {"type": "string"}}, ["channel_id"]),
        ("youtube_fetch_search_suggestions", "Fetch YouTube search suggestions", {"keyword": {"type": "string"}}, ["keyword"]),
        ("youtube_fetch_trending_by_category", "Fetch YouTube trending by category", {"category": {"type": "string"}}, ["category"]),
    ]
    _add_tools(mcp, tools, "youtube", "/api/v1/youtube/web")


def _register_twitter_extended(mcp: Any) -> None:
    """Register extended Twitter tools."""
    tools = [
        ("twitter_fetch_user_bookmarks", "Fetch Twitter user bookmarks", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("twitter_fetch_tweet_thread", "Fetch Twitter tweet thread", {"tweet_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["tweet_id"]),
        ("twitter_fetch_user_media", "Fetch Twitter user media", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("twitter_fetch_user_lists", "Fetch Twitter user lists", {"user_id": {"type": "string"}}, ["user_id"]),
        ("twitter_fetch_list_tweets", "Fetch Twitter list tweets", {"list_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["list_id"]),
        ("twitter_fetch_tweet_quotes", "Fetch Twitter tweet quotes", {"tweet_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["tweet_id"]),
        ("twitter_fetch_user_spaces", "Fetch Twitter user spaces", {"user_id": {"type": "string"}}, ["user_id"]),
        ("twitter_fetch_space_details", "Fetch Twitter space details", {"space_id": {"type": "string"}}, ["space_id"]),
    ]
    _add_tools(mcp, tools, "twitter", "/api/v1/twitter/web")


def _register_xiaohongshu_extended(mcp: Any) -> None:
    """Register extended Xiaohongshu tools."""
    tools = [
        ("xiaohongshu_fetch_user_liked", "Fetch Xiaohongshu user liked notes", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("xiaohongshu_fetch_user_collected", "Fetch Xiaohongshu user collected notes", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("xiaohongshu_fetch_user_followers", "Fetch Xiaohongshu user followers", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("xiaohongshu_fetch_user_following", "Fetch Xiaohongshu user following", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("xiaohongshu_fetch_note_likes", "Fetch Xiaohongshu note likes", {"note_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["note_id"]),
        ("xiaohongshu_fetch_note_collects", "Fetch Xiaohongshu note collects", {"note_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["note_id"]),
        ("xiaohongshu_fetch_note_related", "Fetch Xiaohongshu note related", {"note_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["note_id"]),
        ("xiaohongshu_fetch_hashtag_info", "Fetch Xiaohongshu hashtag info", {"hashtag": {"type": "string"}}, ["hashtag"]),
        ("xiaohongshu_fetch_hashtag_notes", "Fetch Xiaohongshu hashtag notes", {"hashtag": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["hashtag"]),
        ("xiaohongshu_fetch_product_info", "Fetch Xiaohongshu product info", {"product_id": {"type": "string"}}, ["product_id"]),
        ("xiaohongshu_fetch_product_notes", "Fetch Xiaohongshu product notes", {"product_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["product_id"]),
        ("xiaohongshu_fetch_user_insights", "Fetch Xiaohongshu user insights", {"user_id": {"type": "string"}}, ["user_id"]),
    ]
    _add_tools(mcp, tools, "xiaohongshu", "/api/v1/xiaohongshu/web")


def _register_bilibili_extended(mcp: Any) -> None:
    """Register extended Bilibili tools."""
    tools = [
        ("bilibili_fetch_video_similar", "Fetch Bilibili similar videos", {"bvid": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["bvid"]),
        ("bilibili_fetch_user_dynamic", "Fetch Bilibili user dynamic", {"uid": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["uid"]),
        ("bilibili_fetch_user_collections", "Fetch Bilibili user collections", {"uid": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["uid"]),
        ("bilibili_fetch_video_parts", "Fetch Bilibili video parts", {"bvid": {"type": "string"}}, ["bvid"]),
        ("bilibili_fetch_video_subtitles", "Fetch Bilibili video subtitles", {"bvid": {"type": "string"}, "cid": {"type": "string"}}, ["bvid", "cid"]),
        ("bilibili_fetch_user_followers", "Fetch Bilibili user followers", {"uid": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["uid"]),
        ("bilibili_fetch_user_following", "Fetch Bilibili user following", {"uid": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["uid"]),
        ("bilibili_fetch_video_similar_v2", "Fetch Bilibili similar videos V2", {"bvid": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["bvid"]),
        ("bilibili_fetch_user_seasons", "Fetch Bilibili user seasons", {"uid": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["uid"]),
        ("bilibili_fetch_video_tags", "Fetch Bilibili video tags", {"bvid": {"type": "string"}}, ["bvid"]),
    ]
    _add_tools(mcp, tools, "bilibili", "/api/v1/bilibili/web")


def _register_weibo_extended(mcp: Any) -> None:
    """Register extended Weibo tools."""
    tools = [
        ("weibo_fetch_user_followers", "Fetch Weibo user followers", {"uid": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["uid"]),
        ("weibo_fetch_user_following", "Fetch Weibo user following", {"uid": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["uid"]),
        ("weibo_fetch_post_detail", "Fetch Weibo post detail", {"mid": {"type": "string"}}, ["mid"]),
        ("weibo_fetch_post_comments", "Fetch Weibo post comments", {"mid": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["mid"]),
        ("weibo_fetch_user_likes", "Fetch Weibo user likes", {"uid": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["uid"]),
        ("weibo_fetch_user_reposts", "Fetch Weibo user reposts", {"uid": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["uid"]),
        ("weibo_fetch_topic_info", "Fetch Weibo topic info", {"topic": {"type": "string"}}, ["topic"]),
    ]
    _add_tools(mcp, tools, "weibo", "/api/v1/weibo/web")


def _register_kuaishou_extended(mcp: Any) -> None:
    """Register extended Kuaishou tools."""
    tools = [
        ("kuaishou_fetch_user_videos", "Fetch Kuaishou user videos", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("kuaishou_fetch_user_followers", "Fetch Kuaishou user followers", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("kuaishou_fetch_user_following", "Fetch Kuaishou user following", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("kuaishou_fetch_video_comments", "Fetch Kuaishou video comments", {"photo_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["photo_id"]),
        ("kuaishou_fetch_user_likes", "Fetch Kuaishou user likes", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("kuaishou_fetch_user_collections", "Fetch Kuaishou user collections", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("kuaishou_fetch_hot_list", "Fetch Kuaishou hot list", {"count": {"type": "integer", "default": 20}}, []),
    ]
    _add_tools(mcp, tools, "kuaishou", "/api/v1/kuaishou/web")


def _register_linkedin_extended(mcp: Any) -> None:
    """Register extended LinkedIn tools."""
    tools = [
        ("linkedin_fetch_user_connections", "Fetch LinkedIn user connections", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("linkedin_fetch_user_followers", "Fetch LinkedIn user followers", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("linkedin_fetch_user_experience", "Fetch LinkedIn user experience", {"user_id": {"type": "string"}}, ["user_id"]),
        ("linkedin_fetch_user_education", "Fetch LinkedIn user education", {"user_id": {"type": "string"}}, ["user_id"]),
        ("linkedin_fetch_user_skills", "Fetch LinkedIn user skills", {"user_id": {"type": "string"}}, ["user_id"]),
        ("linkedin_fetch_user_recommendations", "Fetch LinkedIn user recommendations", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("linkedin_fetch_company_employees", "Fetch LinkedIn company employees", {"company_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["company_id"]),
    ]
    _add_tools(mcp, tools, "linkedin", "/api/v1/linkedin/web")


def _register_reddit_extended(mcp: Any) -> None:
    """Register extended Reddit tools."""
    tools = [
        ("reddit_fetch_subreddit_rules", "Fetch Reddit subreddit rules", {"subreddit": {"type": "string"}}, ["subreddit"]),
        ("reddit_fetch_subreddit_wiki", "Fetch Reddit subreddit wiki", {"subreddit": {"type": "string"}}, ["subreddit"]),
        ("reddit_fetch_user_comments", "Fetch Reddit user comments", {"username": {"type": "string"}, "sort": {"type": "string", "default": "new"}, "count": {"type": "integer", "default": 20}}, ["username"]),
        ("reddit_fetch_user_saved", "Fetch Reddit user saved posts", {"username": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["username"]),
        ("reddit_fetch_post_awards", "Fetch Reddit post awards", {"subreddit": {"type": "string"}, "post_id": {"type": "string"}}, ["subreddit", "post_id"]),
        ("reddit_fetch_subreddit_mods", "Fetch Reddit subreddit moderators", {"subreddit": {"type": "string"}}, ["subreddit"]),
        ("reddit_fetch_subreddit_flairs", "Fetch Reddit subreddit flairs", {"subreddit": {"type": "string"}}, ["subreddit"]),
    ]
    _add_tools(mcp, tools, "reddit", "/api/v1/reddit/app")


def _register_zhihu_extended(mcp: Any) -> None:
    """Register extended Zhihu tools."""
    tools = [
        ("zhihu_fetch_user_answers", "Fetch Zhihu user answers", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("zhihu_fetch_user_articles", "Fetch Zhihu user articles", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("zhihu_fetch_user_questions", "Fetch Zhihu user questions", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("zhihu_fetch_user_collections", "Fetch Zhihu user collections", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("zhihu_fetch_topic_questions", "Fetch Zhihu topic questions", {"topic_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["topic_id"]),
        ("zhihu_fetch_question_followers", "Fetch Zhihu question followers", {"question_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["question_id"]),
        ("zhihu_fetch_answer_comments", "Fetch Zhihu answer comments", {"answer_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["answer_id"]),
    ]
    _add_tools(mcp, tools, "zhihu", "/api/v1/zhihu/web")


def _register_threads_extended(mcp: Any) -> None:
    """Register extended Threads tools."""
    tools = [
        ("threads_fetch_user_followers", "Fetch Threads user followers", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("threads_fetch_user_following", "Fetch Threads user following", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("threads_fetch_thread_likes", "Fetch Threads thread likes", {"thread_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["thread_id"]),
        ("threads_fetch_user_threads_v2", "Fetch Threads user threads V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
    ]
    _add_tools(mcp, tools, "threads", "/api/v1/threads/web")


def _register_wechat_extended(mcp: Any) -> None:
    """Register extended WeChat tools."""
    tools = [
        ("wechat_fetch_user_videos", "Fetch WeChat user videos", {"usr_name": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["usr_name"]),
        ("wechat_fetch_video_comments", "Fetch WeChat video comments", {"feed_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["feed_id"]),
        ("wechat_fetch_user_followers", "Fetch WeChat user followers", {"usr_name": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["usr_name"]),
    ]
    _add_tools(mcp, tools, "wechat", "/api/v1/wechat/channels")


def _register_lemon8_extended(mcp: Any) -> None:
    """Register extended Lemon8 tools."""
    tools = [
        ("lemon8_fetch_user_liked", "Fetch Lemon8 user liked posts", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("lemon8_fetch_user_bookmarks", "Fetch Lemon8 user bookmarks", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
    ]
    _add_tools(mcp, tools, "lemon8", "/api/v1/lemon8/app")


def _register_utility_extended(mcp: Any) -> None:
    """Register extended utility tools."""
    tools = [
        ("netease_fetch_song_lyrics", "Fetch NetEase song lyrics", {"song_id": {"type": "string"}}, ["song_id"]),
        ("netease_fetch_playlist_tracks", "Fetch NetEase playlist tracks", {"playlist_id": {"type": "string"}, "count": {"type": "integer", "default": 50}}, ["playlist_id"]),
        ("netease_fetch_artist_songs", "Fetch NetEase artist songs", {"artist_id": {"type": "string"}, "count": {"type": "integer", "default": 50}}, ["artist_id"]),
        ("netease_fetch_album_tracks", "Fetch NetEase album tracks", {"album_id": {"type": "string"}, "count": {"type": "integer", "default": 50}}, ["album_id"]),
        ("netease_fetch_user_playlist", "Fetch NetEase user playlist", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 30}}, ["user_id"]),
        ("netease_fetch_hot_search", "Fetch NetEase hot search", {"count": {"type": "integer", "default": 30}}, []),
        ("netease_fetch_recommend_songs", "Fetch NetEase recommend songs", {"count": {"type": "integer", "default": 30}}, []),
        ("netease_fetch_top_list", "Fetch NetEase top list", {"list_id": {"type": "string"}}, ["list_id"]),
        ("netease_fetch_user_liked", "Fetch NetEase user liked songs", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 50}}, ["user_id"]),
        ("netease_fetch_user_followers", "Fetch NetEase user followers", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 30}}, ["user_id"]),
        ("netease_fetch_user_following", "Fetch NetEase user following", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 30}}, ["user_id"]),
        ("netease_fetch_mv_detail", "Fetch NetEase MV detail", {"mv_id": {"type": "string"}}, ["mv_id"]),
        ("netease_fetch_mv_url", "Fetch NetEase MV URL", {"mv_id": {"type": "string"}}, ["mv_id"]),
        ("netease_fetch_song_url", "Fetch NetEase song URL", {"song_id": {"type": "string"}}, ["song_id"]),
        ("netease_fetch_song_comment", "Fetch NetEase song comments", {"song_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["song_id"]),
        ("temp_mail_create", "Create temporary email", {}, []),
        ("temp_mail_check", "Check temporary email", {"mail_id": {"type": "string"}}, ["mail_id"]),
        ("temp_mail_delete", "Delete temporary email", {"mail_id": {"type": "string"}}, ["mail_id"]),
        ("hybrid_parse_video_url", "Parse video URL from any platform", {"url": {"type": "string"}}, ["url"]),
        ("hybrid_parse_user_url", "Parse user URL from any platform", {"url": {"type": "string"}}, ["url"]),
        ("ios_shortcut_parse", "Parse URL for iOS shortcut", {"url": {"type": "string"}}, ["url"]),
        ("sora2_generate_video", "Generate video with Sora2", {"prompt": {"type": "string"}, "duration": {"type": "integer", "default": 10}}, ["prompt"]),
        ("sora2_fetch_video_status", "Fetch Sora2 video generation status", {"task_id": {"type": "string"}}, ["task_id"]),
        ("sora2_fetch_video_list", "Fetch Sora2 video list", {"count": {"type": "integer", "default": 20}}, []),
        ("xigua_fetch_video_detail", "Fetch Xigua video detail", {"video_id": {"type": "string"}}, ["video_id"]),
        ("xigua_fetch_user_profile", "Fetch Xigua user profile", {"user_id": {"type": "string"}}, ["user_id"]),
        ("xigua_fetch_user_videos", "Fetch Xigua user videos", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("toutiao_fetch_news_list", "Fetch Toutiao news list", {"count": {"type": "integer", "default": 20}}, []),
        ("toutiao_fetch_news_detail", "Fetch Toutiao news detail", {"news_id": {"type": "string"}}, ["news_id"]),
        ("toutiao_fetch_user_profile", "Fetch Toutiao user profile", {"user_id": {"type": "string"}}, ["user_id"]),
        ("pipixia_fetch_post_detail", "Fetch PiPiXia post detail", {"post_id": {"type": "string"}}, ["post_id"]),
        ("pipixia_fetch_post_comments", "Fetch PiPiXia post comments", {"post_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["post_id"]),
        ("pipixia_fetch_hot_list", "Fetch PiPiXia hot list", {"count": {"type": "integer", "default": 20}}, []),
        ("pipixia_fetch_user_profile", "Fetch PiPiXia user profile", {"user_id": {"type": "string"}}, ["user_id"]),
        ("pipixia_fetch_user_posts", "Fetch PiPiXia user posts", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("demo_fetch_video", "Fetch demo video data", {"video_id": {"type": "string"}}, ["video_id"]),
        ("demo_fetch_user", "Fetch demo user data", {"user_id": {"type": "string"}}, ["user_id"]),
        ("demo_fetch_trending", "Fetch demo trending data", {}, []),
        ("demo_fetch_search", "Fetch demo search results", {"keyword": {"type": "string"}}, ["keyword"]),
        ("demo_fetch_comments", "Fetch demo comments", {"video_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["video_id"]),
        ("demo_fetch_user_videos", "Fetch demo user videos", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("demo_fetch_user_followers", "Fetch demo user followers", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("demo_fetch_user_following", "Fetch demo user following", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("demo_fetch_video_related", "Fetch demo related videos", {"video_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["video_id"]),
        ("tikhub_fetch_user_info", "Fetch TikHub user info", {}, []),
        ("tikhub_fetch_user_usage", "Fetch TikHub user usage", {}, []),
        ("tikhub_fetch_user_plan", "Fetch TikHub user plan", {}, []),
        ("tikhub_fetch_user_quota", "Fetch TikHub user quota", {}, []),
        ("tikhub_fetch_user_billing", "Fetch TikHub user billing", {}, []),
        ("tikhub_fetch_user_api_keys", "Fetch TikHub user API keys", {}, []),
        ("tikhub_fetch_downloader_parse", "Parse download URL", {"url": {"type": "string"}}, ["url"]),
        ("tikhub_fetch_downloader_download", "Download content", {"url": {"type": "string"}}, ["url"]),
    ]
    _add_tools(mcp, tools, "utility", "/api/v1")


def _add_tools(
    mcp: Any,
    tools: list[tuple[str, str, dict[str, Any], list[str]]],
    platform: str,
    base_path: str,
) -> None:
    """Add tools to MCP server."""
    for name, description, properties, required in tools:
        tool_name = name  # Capture for closure
        mcp._register_tool(
            name=tool_name,
            description=description,
            parameters={
                "type": "object",
                "properties": properties,
                "required": required,
            },
            handler=lambda p=properties, r=required, bp=base_path, tn=tool_name: mcp._call_api(
                f"{bp}/{tn.replace('_', '/')}",
                {k: v for k, v in p.items() if k in r},
            ),
        )
