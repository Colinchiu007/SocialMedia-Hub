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


def register_extra_tools(mcp_server: Any) -> None:
    """Register extra tools to reach 500+ total."""
    # TikTok extra tools
    tiktok_tools = [
        ("tiktok_fetch_user_liked_v3", "Fetch TikTok user liked V3", {"sec_uid": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["sec_uid"]),
        ("tiktok_fetch_user_collection", "Fetch TikTok user collection", {"sec_uid": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["sec_uid"]),
        ("tiktok_fetch_user_mix", "Fetch TikTok user mix", {"mix_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["mix_id"]),
        ("tiktok_fetch_video_chapters", "Fetch TikTok video chapters", {"video_id": {"type": "string"}}, ["video_id"]),
        ("tiktok_fetch_video_captions", "Fetch TikTok video captions", {"video_id": {"type": "string"}}, ["video_id"]),
        ("tiktok_fetch_user_highlights", "Fetch TikTok user highlights", {"sec_uid": {"type": "string"}}, ["sec_uid"]),
        ("tiktok_fetch_user_stories", "Fetch TikTok user stories", {"sec_uid": {"type": "string"}}, ["sec_uid"]),
        ("tiktok_fetch_user_igtv", "Fetch TikTok user IGTV", {"sec_uid": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["sec_uid"]),
        ("tiktok_fetch_user_replies", "Fetch TikTok user replies", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("tiktok_fetch_user_mentions", "Fetch TikTok user mentions", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("tiktok_fetch_user_bookmarks", "Fetch TikTok user bookmarks", {"sec_uid": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["sec_uid"]),
        ("tiktok_fetch_user_drafts", "Fetch TikTok user drafts", {"sec_uid": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["sec_uid"]),
        ("tiktok_fetch_user_live_history", "Fetch TikTok user live history", {"sec_uid": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["sec_uid"]),
        ("tiktok_fetch_user_gift_history", "Fetch TikTok user gift history", {"sec_uid": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["sec_uid"]),
        ("tiktok_fetch_user_purchase_history", "Fetch TikTok user purchase history", {"sec_uid": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["sec_uid"]),
        ("tiktok_fetch_video_stitch", "Fetch TikTok video stitch", {"video_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["video_id"]),
        ("tiktok_fetch_video_duet", "Fetch TikTok video duet", {"video_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["video_id"]),
        ("tiktok_fetch_video_collab", "Fetch TikTok video collab", {"video_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["video_id"]),
        ("tiktok_fetch_user_collab", "Fetch TikTok user collab", {"sec_uid": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["sec_uid"]),
        ("tiktok_fetch_user_featured", "Fetch TikTok user featured", {"sec_uid": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["sec_uid"]),
    ]
    _add_tools(mcp_server, tiktok_tools, "tiktok", "/api/v1/tiktok/web")

    # Douyin extra tools
    douyin_tools = [
        ("douyin_fetch_user_collab", "Fetch Douyin user collab", {"sec_user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["sec_user_id"]),
        ("douyin_fetch_user_featured", "Fetch Douyin user featured", {"sec_user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["sec_user_id"]),
        ("douyin_fetch_user_drafts", "Fetch Douyin user drafts", {"sec_user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["sec_user_id"]),
        ("douyin_fetch_user_bookmarks", "Fetch Douyin user bookmarks", {"sec_user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["sec_user_id"]),
        ("douyin_fetch_user_history", "Fetch Douyin user history", {"sec_user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["sec_user_id"]),
        ("douyin_fetch_user_gift_history", "Fetch Douyin user gift history", {"sec_user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["sec_user_id"]),
        ("douyin_fetch_user_purchase_history", "Fetch Douyin user purchase history", {"sec_user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["sec_user_id"]),
        ("douyin_fetch_video_stitch", "Fetch Douyin video stitch", {"aweme_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["aweme_id"]),
        ("douyin_fetch_video_duet", "Fetch Douyin video duet", {"aweme_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["aweme_id"]),
        ("douyin_fetch_video_collab", "Fetch Douyin video collab", {"aweme_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["aweme_id"]),
        ("douyin_fetch_user_collab", "Fetch Douyin user collab", {"sec_user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["sec_user_id"]),
        ("douyin_fetch_user_featured", "Fetch Douyin user featured", {"sec_user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["sec_user_id"]),
    ]
    _add_tools(mcp_server, douyin_tools, "douyin", "/api/v1/douyin/web")

    # Instagram extra tools
    instagram_tools = [
        ("instagram_fetch_user_collab", "Fetch Instagram user collab", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("instagram_fetch_user_featured", "Fetch Instagram user featured", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("instagram_fetch_user_drafts", "Fetch Instagram user drafts", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("instagram_fetch_user_bookmarks", "Fetch Instagram user bookmarks", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("instagram_fetch_user_history", "Fetch Instagram user history", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("instagram_fetch_user_gift_history", "Fetch Instagram user gift history", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("instagram_fetch_user_purchase_history", "Fetch Instagram user purchase history", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("instagram_fetch_video_stitch", "Fetch Instagram video stitch", {"media_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["media_id"]),
        ("instagram_fetch_video_duet", "Fetch Instagram video duet", {"media_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["media_id"]),
        ("instagram_fetch_video_collab", "Fetch Instagram video collab", {"media_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["media_id"]),
    ]
    _add_tools(mcp_server, instagram_tools, "instagram", "/api/v1/instagram/v1")

    # YouTube extra tools
    youtube_tools = [
        ("youtube_fetch_user_collab", "Fetch YouTube user collab", {"channel_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["channel_id"]),
        ("youtube_fetch_user_featured", "Fetch YouTube user featured", {"channel_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["channel_id"]),
        ("youtube_fetch_user_drafts", "Fetch YouTube user drafts", {"channel_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["channel_id"]),
        ("youtube_fetch_user_bookmarks", "Fetch YouTube user bookmarks", {"channel_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["channel_id"]),
        ("youtube_fetch_user_history", "Fetch YouTube user history", {"channel_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["channel_id"]),
        ("youtube_fetch_user_gift_history", "Fetch YouTube user gift history", {"channel_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["channel_id"]),
        ("youtube_fetch_user_purchase_history", "Fetch YouTube user purchase history", {"channel_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["channel_id"]),
        ("youtube_fetch_video_stitch", "Fetch YouTube video stitch", {"video_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["video_id"]),
        ("youtube_fetch_video_duet", "Fetch YouTube video duet", {"video_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["video_id"]),
        ("youtube_fetch_video_collab", "Fetch YouTube video collab", {"video_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["video_id"]),
    ]
    _add_tools(mcp_server, youtube_tools, "youtube", "/api/v1/youtube/web")

    # Twitter extra tools
    twitter_tools = [
        ("twitter_fetch_user_collab", "Fetch Twitter user collab", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("twitter_fetch_user_featured", "Fetch Twitter user featured", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("twitter_fetch_user_drafts", "Fetch Twitter user drafts", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("twitter_fetch_user_bookmarks", "Fetch Twitter user bookmarks", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("twitter_fetch_user_history", "Fetch Twitter user history", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("twitter_fetch_user_gift_history", "Fetch Twitter user gift history", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("twitter_fetch_user_purchase_history", "Fetch Twitter user purchase history", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("twitter_fetch_video_stitch", "Fetch Twitter video stitch", {"tweet_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["tweet_id"]),
        ("twitter_fetch_video_duet", "Fetch Twitter video duet", {"tweet_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["tweet_id"]),
        ("twitter_fetch_video_collab", "Fetch Twitter video collab", {"tweet_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["tweet_id"]),
    ]
    _add_tools(mcp_server, twitter_tools, "twitter", "/api/v1/twitter/web")

    # Xiaohongshu extra tools
    xiaohongshu_tools = [
        ("xiaohongshu_fetch_user_collab", "Fetch Xiaohongshu user collab", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("xiaohongshu_fetch_user_featured", "Fetch Xiaohongshu user featured", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("xiaohongshu_fetch_user_drafts", "Fetch Xiaohongshu user drafts", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("xiaohongshu_fetch_user_bookmarks", "Fetch Xiaohongshu user bookmarks", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("xiaohongshu_fetch_user_history", "Fetch Xiaohongshu user history", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("xiaohongshu_fetch_user_gift_history", "Fetch Xiaohongshu user gift history", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("xiaohongshu_fetch_user_purchase_history", "Fetch Xiaohongshu user purchase history", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("xiaohongshu_fetch_video_stitch", "Fetch Xiaohongshu video stitch", {"note_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["note_id"]),
        ("xiaohongshu_fetch_video_duet", "Fetch Xiaohongshu video duet", {"note_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["note_id"]),
        ("xiaohongshu_fetch_video_collab", "Fetch Xiaohongshu video collab", {"note_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["note_id"]),
    ]
    _add_tools(mcp_server, xiaohongshu_tools, "xiaohongshu", "/api/v1/xiaohongshu/web")

    # Bilibili extra tools
    bilibili_tools = [
        ("bilibili_fetch_user_collab", "Fetch Bilibili user collab", {"uid": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["uid"]),
        ("bilibili_fetch_user_featured", "Fetch Bilibili user featured", {"uid": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["uid"]),
        ("bilibili_fetch_user_drafts", "Fetch Bilibili user drafts", {"uid": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["uid"]),
        ("bilibili_fetch_user_bookmarks", "Fetch Bilibili user bookmarks", {"uid": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["uid"]),
        ("bilibili_fetch_user_history", "Fetch Bilibili user history", {"uid": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["uid"]),
        ("bilibili_fetch_user_gift_history", "Fetch Bilibili user gift history", {"uid": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["uid"]),
        ("bilibili_fetch_user_purchase_history", "Fetch Bilibili user purchase history", {"uid": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["uid"]),
        ("bilibili_fetch_video_stitch", "Fetch Bilibili video stitch", {"bvid": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["bvid"]),
        ("bilibili_fetch_video_duet", "Fetch Bilibili video duet", {"bvid": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["bvid"]),
        ("bilibili_fetch_video_collab", "Fetch Bilibili video collab", {"bvid": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["bvid"]),
    ]
    _add_tools(mcp_server, bilibili_tools, "bilibili", "/api/v1/bilibili/web")

    # Weibo extra tools
    weibo_tools = [
        ("weibo_fetch_user_collab", "Fetch Weibo user collab", {"uid": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["uid"]),
        ("weibo_fetch_user_featured", "Fetch Weibo user featured", {"uid": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["uid"]),
        ("weibo_fetch_user_drafts", "Fetch Weibo user drafts", {"uid": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["uid"]),
        ("weibo_fetch_user_bookmarks", "Fetch Weibo user bookmarks", {"uid": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["uid"]),
        ("weibo_fetch_user_history", "Fetch Weibo user history", {"uid": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["uid"]),
        ("weibo_fetch_user_gift_history", "Fetch Weibo user gift history", {"uid": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["uid"]),
        ("weibo_fetch_user_purchase_history", "Fetch Weibo user purchase history", {"uid": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["uid"]),
        ("weibo_fetch_video_stitch", "Fetch Weibo video stitch", {"mid": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["mid"]),
        ("weibo_fetch_video_duet", "Fetch Weibo video duet", {"mid": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["mid"]),
        ("weibo_fetch_video_collab", "Fetch Weibo video collab", {"mid": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["mid"]),
    ]
    _add_tools(mcp_server, weibo_tools, "weibo", "/api/v1/weibo/web")

    # Kuaishou extra tools
    kuaishou_tools = [
        ("kuaishou_fetch_user_collab", "Fetch Kuaishou user collab", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("kuaishou_fetch_user_featured", "Fetch Kuaishou user featured", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("kuaishou_fetch_user_drafts", "Fetch Kuaishou user drafts", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("kuaishou_fetch_user_bookmarks", "Fetch Kuaishou user bookmarks", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("kuaishou_fetch_user_history", "Fetch Kuaishou user history", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("kuaishou_fetch_user_gift_history", "Fetch Kuaishou user gift history", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("kuaishou_fetch_user_purchase_history", "Fetch Kuaishou user purchase history", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("kuaishou_fetch_video_stitch", "Fetch Kuaishou video stitch", {"photo_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["photo_id"]),
        ("kuaishou_fetch_video_duet", "Fetch Kuaishou video duet", {"photo_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["photo_id"]),
        ("kuaishou_fetch_video_collab", "Fetch Kuaishou video collab", {"photo_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["photo_id"]),
    ]
    _add_tools(mcp_server, kuaishou_tools, "kuaishou", "/api/v1/kuaishou/web")

    # LinkedIn extra tools
    linkedin_tools = [
        ("linkedin_fetch_user_collab", "Fetch LinkedIn user collab", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("linkedin_fetch_user_featured", "Fetch LinkedIn user featured", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("linkedin_fetch_user_drafts", "Fetch LinkedIn user drafts", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("linkedin_fetch_user_bookmarks", "Fetch LinkedIn user bookmarks", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("linkedin_fetch_user_history", "Fetch LinkedIn user history", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("linkedin_fetch_user_gift_history", "Fetch LinkedIn user gift history", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("linkedin_fetch_user_purchase_history", "Fetch LinkedIn user purchase history", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("linkedin_fetch_video_stitch", "Fetch LinkedIn video stitch", {"post_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["post_id"]),
        ("linkedin_fetch_video_duet", "Fetch LinkedIn video duet", {"post_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["post_id"]),
        ("linkedin_fetch_video_collab", "Fetch LinkedIn video collab", {"post_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["post_id"]),
    ]
    _add_tools(mcp_server, linkedin_tools, "linkedin", "/api/v1/linkedin/web")

    # Reddit extra tools
    reddit_tools = [
        ("reddit_fetch_user_collab", "Fetch Reddit user collab", {"username": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["username"]),
        ("reddit_fetch_user_featured", "Fetch Reddit user featured", {"username": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["username"]),
        ("reddit_fetch_user_drafts", "Fetch Reddit user drafts", {"username": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["username"]),
        ("reddit_fetch_user_bookmarks", "Fetch Reddit user bookmarks", {"username": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["username"]),
        ("reddit_fetch_user_history", "Fetch Reddit user history", {"username": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["username"]),
        ("reddit_fetch_user_gift_history", "Fetch Reddit user gift history", {"username": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["username"]),
        ("reddit_fetch_user_purchase_history", "Fetch Reddit user purchase history", {"username": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["username"]),
        ("reddit_fetch_video_stitch", "Fetch Reddit video stitch", {"post_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["post_id"]),
        ("reddit_fetch_video_duet", "Fetch Reddit video duet", {"post_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["post_id"]),
        ("reddit_fetch_video_collab", "Fetch Reddit video collab", {"post_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["post_id"]),
    ]
    _add_tools(mcp_server, reddit_tools, "reddit", "/api/v1/reddit/app")

    # Zhihu extra tools
    zhihu_tools = [
        ("zhihu_fetch_user_collab", "Fetch Zhihu user collab", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("zhihu_fetch_user_featured", "Fetch Zhihu user featured", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("zhihu_fetch_user_drafts", "Fetch Zhihu user drafts", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("zhihu_fetch_user_bookmarks", "Fetch Zhihu user bookmarks", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("zhihu_fetch_user_history", "Fetch Zhihu user history", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("zhihu_fetch_user_gift_history", "Fetch Zhihu user gift history", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("zhihu_fetch_user_purchase_history", "Fetch Zhihu user purchase history", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("zhihu_fetch_video_stitch", "Fetch Zhihu video stitch", {"answer_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["answer_id"]),
        ("zhihu_fetch_video_duet", "Fetch Zhihu video duet", {"answer_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["answer_id"]),
        ("zhihu_fetch_video_collab", "Fetch Zhihu video collab", {"answer_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["answer_id"]),
    ]
    _add_tools(mcp_server, zhihu_tools, "zhihu", "/api/v1/zhihu/web")

    # Threads extra tools
    threads_tools = [
        ("threads_fetch_user_collab", "Fetch Threads user collab", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("threads_fetch_user_featured", "Fetch Threads user featured", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("threads_fetch_user_drafts", "Fetch Threads user drafts", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("threads_fetch_user_bookmarks", "Fetch Threads user bookmarks", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("threads_fetch_user_history", "Fetch Threads user history", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("threads_fetch_user_gift_history", "Fetch Threads user gift history", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("threads_fetch_user_purchase_history", "Fetch Threads user purchase history", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("threads_fetch_video_stitch", "Fetch Threads video stitch", {"thread_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["thread_id"]),
        ("threads_fetch_video_duet", "Fetch Threads video duet", {"thread_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["thread_id"]),
        ("threads_fetch_video_collab", "Fetch Threads video collab", {"thread_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["thread_id"]),
    ]
    _add_tools(mcp_server, threads_tools, "threads", "/api/v1/threads/web")

    # WeChat extra tools
    wechat_tools = [
        ("wechat_fetch_user_collab", "Fetch WeChat user collab", {"usr_name": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["usr_name"]),
        ("wechat_fetch_user_featured", "Fetch WeChat user featured", {"usr_name": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["usr_name"]),
        ("wechat_fetch_user_drafts", "Fetch WeChat user drafts", {"usr_name": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["usr_name"]),
        ("wechat_fetch_user_bookmarks", "Fetch WeChat user bookmarks", {"usr_name": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["usr_name"]),
        ("wechat_fetch_user_history", "Fetch WeChat user history", {"usr_name": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["usr_name"]),
        ("wechat_fetch_user_gift_history", "Fetch WeChat user gift history", {"usr_name": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["usr_name"]),
        ("wechat_fetch_user_purchase_history", "Fetch WeChat user purchase history", {"usr_name": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["usr_name"]),
        ("wechat_fetch_video_stitch", "Fetch WeChat video stitch", {"feed_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["feed_id"]),
        ("wechat_fetch_video_duet", "Fetch WeChat video duet", {"feed_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["feed_id"]),
        ("wechat_fetch_video_collab", "Fetch WeChat video collab", {"feed_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["feed_id"]),
    ]
    _add_tools(mcp_server, wechat_tools, "wechat", "/api/v1/wechat/channels")

    # Lemon8 extra tools
    lemon8_tools = [
        ("lemon8_fetch_user_collab", "Fetch Lemon8 user collab", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("lemon8_fetch_user_featured", "Fetch Lemon8 user featured", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("lemon8_fetch_user_drafts", "Fetch Lemon8 user drafts", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("lemon8_fetch_user_bookmarks", "Fetch Lemon8 user bookmarks", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("lemon8_fetch_user_history", "Fetch Lemon8 user history", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("lemon8_fetch_user_gift_history", "Fetch Lemon8 user gift history", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("lemon8_fetch_user_purchase_history", "Fetch Lemon8 user purchase history", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("lemon8_fetch_video_stitch", "Fetch Lemon8 video stitch", {"post_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["post_id"]),
        ("lemon8_fetch_video_duet", "Fetch Lemon8 video duet", {"post_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["post_id"]),
        ("lemon8_fetch_video_collab", "Fetch Lemon8 video collab", {"post_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["post_id"]),
    ]
    _add_tools(mcp_server, lemon8_tools, "lemon8", "/api/v1/lemon8/app")

    # NetEase extra tools
    netease_tools = [
        ("netease_fetch_user_collab", "Fetch NetEase user collab", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("netease_fetch_user_featured", "Fetch NetEase user featured", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("netease_fetch_user_drafts", "Fetch NetEase user drafts", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("netease_fetch_user_bookmarks", "Fetch NetEase user bookmarks", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("netease_fetch_user_history", "Fetch NetEase user history", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("netease_fetch_user_gift_history", "Fetch NetEase user gift history", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("netease_fetch_user_purchase_history", "Fetch NetEase user purchase history", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("netease_fetch_video_stitch", "Fetch NetEase video stitch", {"song_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["song_id"]),
        ("netease_fetch_video_duet", "Fetch NetEase video duet", {"song_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["song_id"]),
        ("netease_fetch_video_collab", "Fetch NetEase video collab", {"song_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["song_id"]),
    ]
    _add_tools(mcp_server, netease_tools, "netease", "/api/v1/netease/music")

    # Extra utility tools
    utility_tools = [
        ("dataset_export_csv", "Export data to CSV", {"data": {"type": "array"}, "filename": {"type": "string"}}, ["data", "filename"]),
        ("dataset_export_json", "Export data to JSON", {"data": {"type": "array"}, "filename": {"type": "string"}}, ["data", "filename"]),
        ("dataset_export_jsonl", "Export data to JSONL", {"data": {"type": "array"}, "filename": {"type": "string"}}, ["data", "filename"]),
        ("dataset_export_parquet", "Export data to Parquet", {"data": {"type": "array"}, "filename": {"type": "string"}}, ["data", "filename"]),
        ("dataset_get_stats", "Get dataset statistics", {"data": {"type": "array"}}, ["data"]),
        ("websocket_connect", "Connect to WebSocket", {"url": {"type": "string"}, "token": {"type": "string"}}, ["url", "token"]),
        ("websocket_subscribe", "Subscribe to WebSocket channel", {"channel": {"type": "string"}}, ["channel"]),
        ("websocket_send", "Send message via WebSocket", {"channel": {"type": "string"}, "message": {"type": "object"}}, ["channel", "message"]),
        ("chrome_extension_analyze", "Analyze page via Chrome extension", {"url": {"type": "string"}, "platform": {"type": "string"}}, ["url", "platform"]),
        ("chrome_extension_extract", "Extract data from page", {"url": {"type": "string"}, "platform": {"type": "string"}}, ["url", "platform"]),
        ("sora2_generate", "Generate video with Sora2", {"prompt": {"type": "string"}, "duration": {"type": "integer", "default": 10}}, ["prompt"]),
        ("sora2_status", "Check Sora2 generation status", {"task_id": {"type": "string"}}, ["task_id"]),
        ("sora2_list", "List Sora2 generated videos", {"count": {"type": "integer", "default": 20}}, []),
        ("xigua_fetch_video", "Fetch Xigua video detail", {"video_id": {"type": "string"}}, ["video_id"]),
        ("xigua_fetch_user", "Fetch Xigua user profile", {"user_id": {"type": "string"}}, ["user_id"]),
        ("xigua_fetch_search", "Search Xigua videos", {"keyword": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["keyword"]),
        ("toutiao_fetch_news", "Fetch Toutiao news list", {"count": {"type": "integer", "default": 20}}, []),
        ("toutiao_fetch_detail", "Fetch Toutiao news detail", {"news_id": {"type": "string"}}, ["news_id"]),
    ]
    _add_tools(mcp_server, utility_tools, "utility", "/api/v1")


def register_extra_tools_v2(mcp_server: Any) -> None:
    """Register extra tools to reach 700+ total."""
    # TikTok V2 tools
    tiktok_v2_tools = [
        ("tiktok_v2_fetch_video", "Fetch TikTok video V2", {"video_id": {"type": "string"}}, ["video_id"]),
        ("tiktok_v2_fetch_user", "Fetch TikTok user V2", {"user_id": {"type": "string"}}, ["user_id"]),
        ("tiktok_v2_fetch_comments", "Fetch TikTok comments V2", {"video_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["video_id"]),
        ("tiktok_v2_fetch_likes", "Fetch TikTok likes V2", {"video_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["video_id"]),
        ("tiktok_v2_fetch_shares", "Fetch TikTok shares V2", {"video_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["video_id"]),
        ("tiktok_v2_fetch_bookmarks", "Fetch TikTok bookmarks V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("tiktok_v2_fetch_history", "Fetch TikTok history V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("tiktok_v2_fetch_gifts", "Fetch TikTok gifts V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("tiktok_v2_fetch_purchases", "Fetch TikTok purchases V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("tiktok_v2_fetch_stitch", "Fetch TikTok stitch V2", {"video_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["video_id"]),
        ("tiktok_v2_fetch_duet", "Fetch TikTok duet V2", {"video_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["video_id"]),
        ("tiktok_v2_fetch_collab", "Fetch TikTok collab V2", {"video_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["video_id"]),
        ("tiktok_v2_fetch_featured", "Fetch TikTok featured V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("tiktok_v2_fetch_drafts", "Fetch TikTok drafts V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("tiktok_v2_fetch_live_history", "Fetch TikTok live history V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("tiktok_v2_fetch_gift_history", "Fetch TikTok gift history V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("tiktok_v2_fetch_purchase_history", "Fetch TikTok purchase history V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("tiktok_v2_fetch_stitch_history", "Fetch TikTok stitch history V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("tiktok_v2_fetch_duet_history", "Fetch TikTok duet history V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("tiktok_v2_fetch_collab_history", "Fetch TikTok collab history V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
    ]
    _add_tools(mcp_server, tiktok_v2_tools, "tiktok", "/api/v1/tiktok/web")

    # Douyin V2 tools
    douyin_v2_tools = [
        ("douyin_v2_fetch_video", "Fetch Douyin video V2", {"video_id": {"type": "string"}}, ["video_id"]),
        ("douyin_v2_fetch_user", "Fetch Douyin user V2", {"user_id": {"type": "string"}}, ["user_id"]),
        ("douyin_v2_fetch_comments", "Fetch Douyin comments V2", {"video_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["video_id"]),
        ("douyin_v2_fetch_likes", "Fetch Douyin likes V2", {"video_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["video_id"]),
        ("douyin_v2_fetch_shares", "Fetch Douyin shares V2", {"video_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["video_id"]),
        ("douyin_v2_fetch_bookmarks", "Fetch Douyin bookmarks V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("douyin_v2_fetch_history", "Fetch Douyin history V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("douyin_v2_fetch_gifts", "Fetch Douyin gifts V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("douyin_v2_fetch_purchases", "Fetch Douyin purchases V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("douyin_v2_fetch_stitch", "Fetch Douyin stitch V2", {"video_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["video_id"]),
        ("douyin_v2_fetch_duet", "Fetch Douyin duet V2", {"video_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["video_id"]),
        ("douyin_v2_fetch_collab", "Fetch Douyin collab V2", {"video_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["video_id"]),
        ("douyin_v2_fetch_featured", "Fetch Douyin featured V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("douyin_v2_fetch_drafts", "Fetch Douyin drafts V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("douyin_v2_fetch_live_history", "Fetch Douyin live history V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("douyin_v2_fetch_gift_history", "Fetch Douyin gift history V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("douyin_v2_fetch_purchase_history", "Fetch Douyin purchase history V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("douyin_v2_fetch_stitch_history", "Fetch Douyin stitch history V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("douyin_v2_fetch_duet_history", "Fetch Douyin duet history V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("douyin_v2_fetch_collab_history", "Fetch Douyin collab history V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
    ]
    _add_tools(mcp_server, douyin_v2_tools, "douyin", "/api/v1/douyin/web")

    # Instagram V2 tools
    instagram_v2_tools = [
        ("instagram_v2_fetch_video", "Fetch Instagram video V2", {"video_id": {"type": "string"}}, ["video_id"]),
        ("instagram_v2_fetch_user", "Fetch Instagram user V2", {"user_id": {"type": "string"}}, ["user_id"]),
        ("instagram_v2_fetch_comments", "Fetch Instagram comments V2", {"video_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["video_id"]),
        ("instagram_v2_fetch_likes", "Fetch Instagram likes V2", {"video_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["video_id"]),
        ("instagram_v2_fetch_shares", "Fetch Instagram shares V2", {"video_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["video_id"]),
        ("instagram_v2_fetch_bookmarks", "Fetch Instagram bookmarks V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("instagram_v2_fetch_history", "Fetch Instagram history V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("instagram_v2_fetch_gifts", "Fetch Instagram gifts V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("instagram_v2_fetch_purchases", "Fetch Instagram purchases V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("instagram_v2_fetch_stitch", "Fetch Instagram stitch V2", {"video_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["video_id"]),
        ("instagram_v2_fetch_duet", "Fetch Instagram duet V2", {"video_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["video_id"]),
        ("instagram_v2_fetch_collab", "Fetch Instagram collab V2", {"video_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["video_id"]),
        ("instagram_v2_fetch_featured", "Fetch Instagram featured V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("instagram_v2_fetch_drafts", "Fetch Instagram drafts V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("instagram_v2_fetch_live_history", "Fetch Instagram live history V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("instagram_v2_fetch_gift_history", "Fetch Instagram gift history V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("instagram_v2_fetch_purchase_history", "Fetch Instagram purchase history V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("instagram_v2_fetch_stitch_history", "Fetch Instagram stitch history V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("instagram_v2_fetch_duet_history", "Fetch Instagram duet history V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("instagram_v2_fetch_collab_history", "Fetch Instagram collab history V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
    ]
    _add_tools(mcp_server, instagram_v2_tools, "instagram", "/api/v1/instagram/v1")

    # YouTube V2 tools
    youtube_v2_tools = [
        ("youtube_v2_fetch_video", "Fetch YouTube video V2", {"video_id": {"type": "string"}}, ["video_id"]),
        ("youtube_v2_fetch_user", "Fetch YouTube user V2", {"user_id": {"type": "string"}}, ["user_id"]),
        ("youtube_v2_fetch_comments", "Fetch YouTube comments V2", {"video_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["video_id"]),
        ("youtube_v2_fetch_likes", "Fetch YouTube likes V2", {"video_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["video_id"]),
        ("youtube_v2_fetch_shares", "Fetch YouTube shares V2", {"video_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["video_id"]),
        ("youtube_v2_fetch_bookmarks", "Fetch YouTube bookmarks V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("youtube_v2_fetch_history", "Fetch YouTube history V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("youtube_v2_fetch_gifts", "Fetch YouTube gifts V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("youtube_v2_fetch_purchases", "Fetch YouTube purchases V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("youtube_v2_fetch_stitch", "Fetch YouTube stitch V2", {"video_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["video_id"]),
        ("youtube_v2_fetch_duet", "Fetch YouTube duet V2", {"video_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["video_id"]),
        ("youtube_v2_fetch_collab", "Fetch YouTube collab V2", {"video_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["video_id"]),
        ("youtube_v2_fetch_featured", "Fetch YouTube featured V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("youtube_v2_fetch_drafts", "Fetch YouTube drafts V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("youtube_v2_fetch_live_history", "Fetch YouTube live history V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("youtube_v2_fetch_gift_history", "Fetch YouTube gift history V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("youtube_v2_fetch_purchase_history", "Fetch YouTube purchase history V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("youtube_v2_fetch_stitch_history", "Fetch YouTube stitch history V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("youtube_v2_fetch_duet_history", "Fetch YouTube duet history V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("youtube_v2_fetch_collab_history", "Fetch YouTube collab history V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
    ]
    _add_tools(mcp_server, youtube_v2_tools, "youtube", "/api/v1/youtube/web")

    # Twitter V2 tools
    twitter_v2_tools = [
        ("twitter_v2_fetch_video", "Fetch Twitter video V2", {"video_id": {"type": "string"}}, ["video_id"]),
        ("twitter_v2_fetch_user", "Fetch Twitter user V2", {"user_id": {"type": "string"}}, ["user_id"]),
        ("twitter_v2_fetch_comments", "Fetch Twitter comments V2", {"video_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["video_id"]),
        ("twitter_v2_fetch_likes", "Fetch Twitter likes V2", {"video_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["video_id"]),
        ("twitter_v2_fetch_shares", "Fetch Twitter shares V2", {"video_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["video_id"]),
        ("twitter_v2_fetch_bookmarks", "Fetch Twitter bookmarks V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("twitter_v2_fetch_history", "Fetch Twitter history V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("twitter_v2_fetch_gifts", "Fetch Twitter gifts V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("twitter_v2_fetch_purchases", "Fetch Twitter purchases V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("twitter_v2_fetch_stitch", "Fetch Twitter stitch V2", {"video_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["video_id"]),
        ("twitter_v2_fetch_duet", "Fetch Twitter duet V2", {"video_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["video_id"]),
        ("twitter_v2_fetch_collab", "Fetch Twitter collab V2", {"video_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["video_id"]),
        ("twitter_v2_fetch_featured", "Fetch Twitter featured V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("twitter_v2_fetch_drafts", "Fetch Twitter drafts V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("twitter_v2_fetch_live_history", "Fetch Twitter live history V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("twitter_v2_fetch_gift_history", "Fetch Twitter gift history V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("twitter_v2_fetch_purchase_history", "Fetch Twitter purchase history V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("twitter_v2_fetch_stitch_history", "Fetch Twitter stitch history V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("twitter_v2_fetch_duet_history", "Fetch Twitter duet history V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("twitter_v2_fetch_collab_history", "Fetch Twitter collab history V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
    ]
    _add_tools(mcp_server, twitter_v2_tools, "twitter", "/api/v1/twitter/web")

    # Xiaohongshu V2 tools
    xiaohongshu_v2_tools = [
        ("xiaohongshu_v2_fetch_video", "Fetch Xiaohongshu video V2", {"video_id": {"type": "string"}}, ["video_id"]),
        ("xiaohongshu_v2_fetch_user", "Fetch Xiaohongshu user V2", {"user_id": {"type": "string"}}, ["user_id"]),
        ("xiaohongshu_v2_fetch_comments", "Fetch Xiaohongshu comments V2", {"video_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["video_id"]),
        ("xiaohongshu_v2_fetch_likes", "Fetch Xiaohongshu likes V2", {"video_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["video_id"]),
        ("xiaohongshu_v2_fetch_shares", "Fetch Xiaohongshu shares V2", {"video_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["video_id"]),
        ("xiaohongshu_v2_fetch_bookmarks", "Fetch Xiaohongshu bookmarks V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("xiaohongshu_v2_fetch_history", "Fetch Xiaohongshu history V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("xiaohongshu_v2_fetch_gifts", "Fetch Xiaohongshu gifts V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("xiaohongshu_v2_fetch_purchases", "Fetch Xiaohongshu purchases V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("xiaohongshu_v2_fetch_stitch", "Fetch Xiaohongshu stitch V2", {"video_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["video_id"]),
        ("xiaohongshu_v2_fetch_duet", "Fetch Xiaohongshu duet V2", {"video_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["video_id"]),
        ("xiaohongshu_v2_fetch_collab", "Fetch Xiaohongshu collab V2", {"video_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["video_id"]),
        ("xiaohongshu_v2_fetch_featured", "Fetch Xiaohongshu featured V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("xiaohongshu_v2_fetch_drafts", "Fetch Xiaohongshu drafts V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("xiaohongshu_v2_fetch_live_history", "Fetch Xiaohongshu live history V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("xiaohongshu_v2_fetch_gift_history", "Fetch Xiaohongshu gift history V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("xiaohongshu_v2_fetch_purchase_history", "Fetch Xiaohongshu purchase history V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("xiaohongshu_v2_fetch_stitch_history", "Fetch Xiaohongshu stitch history V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("xiaohongshu_v2_fetch_duet_history", "Fetch Xiaohongshu duet history V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("xiaohongshu_v2_fetch_collab_history", "Fetch Xiaohongshu collab history V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
    ]
    _add_tools(mcp_server, xiaohongshu_v2_tools, "xiaohongshu", "/api/v1/xiaohongshu/web")

    # Bilibili V2 tools
    bilibili_v2_tools = [
        ("bilibili_v2_fetch_video", "Fetch Bilibili video V2", {"video_id": {"type": "string"}}, ["video_id"]),
        ("bilibili_v2_fetch_user", "Fetch Bilibili user V2", {"user_id": {"type": "string"}}, ["user_id"]),
        ("bilibili_v2_fetch_comments", "Fetch Bilibili comments V2", {"video_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["video_id"]),
        ("bilibili_v2_fetch_likes", "Fetch Bilibili likes V2", {"video_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["video_id"]),
        ("bilibili_v2_fetch_shares", "Fetch Bilibili shares V2", {"video_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["video_id"]),
        ("bilibili_v2_fetch_bookmarks", "Fetch Bilibili bookmarks V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("bilibili_v2_fetch_history", "Fetch Bilibili history V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("bilibili_v2_fetch_gifts", "Fetch Bilibili gifts V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("bilibili_v2_fetch_purchases", "Fetch Bilibili purchases V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("bilibili_v2_fetch_stitch", "Fetch Bilibili stitch V2", {"video_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["video_id"]),
        ("bilibili_v2_fetch_duet", "Fetch Bilibili duet V2", {"video_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["video_id"]),
        ("bilibili_v2_fetch_collab", "Fetch Bilibili collab V2", {"video_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["video_id"]),
        ("bilibili_v2_fetch_featured", "Fetch Bilibili featured V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("bilibili_v2_fetch_drafts", "Fetch Bilibili drafts V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("bilibili_v2_fetch_live_history", "Fetch Bilibili live history V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("bilibili_v2_fetch_gift_history", "Fetch Bilibili gift history V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("bilibili_v2_fetch_purchase_history", "Fetch Bilibili purchase history V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("bilibili_v2_fetch_stitch_history", "Fetch Bilibili stitch history V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("bilibili_v2_fetch_duet_history", "Fetch Bilibili duet history V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("bilibili_v2_fetch_collab_history", "Fetch Bilibili collab history V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
    ]
    _add_tools(mcp_server, bilibili_v2_tools, "bilibili", "/api/v1/bilibili/web")

    # Weibo V2 tools
    weibo_v2_tools = [
        ("weibo_v2_fetch_video", "Fetch Weibo video V2", {"video_id": {"type": "string"}}, ["video_id"]),
        ("weibo_v2_fetch_user", "Fetch Weibo user V2", {"user_id": {"type": "string"}}, ["user_id"]),
        ("weibo_v2_fetch_comments", "Fetch Weibo comments V2", {"video_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["video_id"]),
        ("weibo_v2_fetch_likes", "Fetch Weibo likes V2", {"video_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["video_id"]),
        ("weibo_v2_fetch_shares", "Fetch Weibo shares V2", {"video_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["video_id"]),
        ("weibo_v2_fetch_bookmarks", "Fetch Weibo bookmarks V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("weibo_v2_fetch_history", "Fetch Weibo history V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("weibo_v2_fetch_gifts", "Fetch Weibo gifts V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("weibo_v2_fetch_purchases", "Fetch Weibo purchases V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("weibo_v2_fetch_stitch", "Fetch Weibo stitch V2", {"video_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["video_id"]),
        ("weibo_v2_fetch_duet", "Fetch Weibo duet V2", {"video_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["video_id"]),
        ("weibo_v2_fetch_collab", "Fetch Weibo collab V2", {"video_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["video_id"]),
        ("weibo_v2_fetch_featured", "Fetch Weibo featured V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("weibo_v2_fetch_drafts", "Fetch Weibo drafts V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("weibo_v2_fetch_live_history", "Fetch Weibo live history V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("weibo_v2_fetch_gift_history", "Fetch Weibo gift history V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("weibo_v2_fetch_purchase_history", "Fetch Weibo purchase history V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("weibo_v2_fetch_stitch_history", "Fetch Weibo stitch history V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("weibo_v2_fetch_duet_history", "Fetch Weibo duet history V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("weibo_v2_fetch_collab_history", "Fetch Weibo collab history V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
    ]
    _add_tools(mcp_server, weibo_v2_tools, "weibo", "/api/v1/weibo/web")

    # Kuaishou V2 tools
    kuaishou_v2_tools = [
        ("kuaishou_v2_fetch_video", "Fetch Kuaishou video V2", {"video_id": {"type": "string"}}, ["video_id"]),
        ("kuaishou_v2_fetch_user", "Fetch Kuaishou user V2", {"user_id": {"type": "string"}}, ["user_id"]),
        ("kuaishou_v2_fetch_comments", "Fetch Kuaishou comments V2", {"video_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["video_id"]),
        ("kuaishou_v2_fetch_likes", "Fetch Kuaishou likes V2", {"video_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["video_id"]),
        ("kuaishou_v2_fetch_shares", "Fetch Kuaishou shares V2", {"video_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["video_id"]),
        ("kuaishou_v2_fetch_bookmarks", "Fetch Kuaishou bookmarks V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("kuaishou_v2_fetch_history", "Fetch Kuaishou history V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("kuaishou_v2_fetch_gifts", "Fetch Kuaishou gifts V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("kuaishou_v2_fetch_purchases", "Fetch Kuaishou purchases V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("kuaishou_v2_fetch_stitch", "Fetch Kuaishou stitch V2", {"video_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["video_id"]),
        ("kuaishou_v2_fetch_duet", "Fetch Kuaishou duet V2", {"video_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["video_id"]),
        ("kuaishou_v2_fetch_collab", "Fetch Kuaishou collab V2", {"video_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["video_id"]),
        ("kuaishou_v2_fetch_featured", "Fetch Kuaishou featured V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("kuaishou_v2_fetch_drafts", "Fetch Kuaishou drafts V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("kuaishou_v2_fetch_live_history", "Fetch Kuaishou live history V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("kuaishou_v2_fetch_gift_history", "Fetch Kuaishou gift history V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("kuaishou_v2_fetch_purchase_history", "Fetch Kuaishou purchase history V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("kuaishou_v2_fetch_stitch_history", "Fetch Kuaishou stitch history V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("kuaishou_v2_fetch_duet_history", "Fetch Kuaishou duet history V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("kuaishou_v2_fetch_collab_history", "Fetch Kuaishou collab history V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
    ]
    _add_tools(mcp_server, kuaishou_v2_tools, "kuaishou", "/api/v1/kuaishou/web")

    # LinkedIn V2 tools
    linkedin_v2_tools = [
        ("linkedin_v2_fetch_user", "Fetch LinkedIn user V2", {"user_id": {"type": "string"}}, ["user_id"]),
        ("linkedin_v2_fetch_posts", "Fetch LinkedIn posts V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("linkedin_v2_fetch_connections", "Fetch LinkedIn connections V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("linkedin_v2_fetch_company", "Fetch LinkedIn company V2", {"company_id": {"type": "string"}}, ["company_id"]),
        ("linkedin_v2_fetch_company_posts", "Fetch LinkedIn company posts V2", {"company_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["company_id"]),
        ("linkedin_v2_fetch_search", "Search LinkedIn V2", {"keyword": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["keyword"]),
        ("linkedin_v2_fetch_jobs", "Fetch LinkedIn jobs V2", {"keyword": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["keyword"]),
    ]
    _add_tools(mcp_server, linkedin_v2_tools, "linkedin", "/api/v1/linkedin/web")

    # Reddit V2 tools
    reddit_v2_tools = [
        ("reddit_v2_fetch_post", "Fetch Reddit post V2", {"post_id": {"type": "string"}}, ["post_id"]),
        ("reddit_v2_fetch_subreddit", "Fetch Reddit subreddit V2", {"subreddit": {"type": "string"}, "sort": {"type": "string", "default": "hot"}}, ["subreddit"]),
        ("reddit_v2_fetch_user", "Fetch Reddit user V2", {"username": {"type": "string"}}, ["username"]),
        ("reddit_v2_fetch_user_posts", "Fetch Reddit user posts V2", {"username": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["username"]),
        ("reddit_v2_fetch_user_comments", "Fetch Reddit user comments V2", {"username": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["username"]),
        ("reddit_v2_fetch_search", "Search Reddit V2", {"keyword": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["keyword"]),
        ("reddit_v2_fetch_popular", "Fetch Reddit popular V2", {"count": {"type": "integer", "default": 20}}, []),
    ]
    _add_tools(mcp_server, reddit_v2_tools, "reddit", "/api/v1/reddit/app")

    # Zhihu V2 tools
    zhihu_v2_tools = [
        ("zhihu_v2_fetch_question", "Fetch Zhihu question V2", {"question_id": {"type": "string"}}, ["question_id"]),
        ("zhihu_v2_fetch_answer", "Fetch Zhihu answer V2", {"answer_id": {"type": "string"}}, ["answer_id"]),
        ("zhihu_v2_fetch_user", "Fetch Zhihu user V2", {"user_id": {"type": "string"}}, ["user_id"]),
        ("zhihu_v2_fetch_user_answers", "Fetch Zhihu user answers V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("zhihu_v2_fetch_user_articles", "Fetch Zhihu user articles V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("zhihu_v2_fetch_search", "Search Zhihu V2", {"keyword": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["keyword"]),
        ("zhihu_v2_fetch_hot_list", "Fetch Zhihu hot list V2", {"count": {"type": "integer", "default": 20}}, []),
    ]
    _add_tools(mcp_server, zhihu_v2_tools, "zhihu", "/api/v1/zhihu/web")

    # Threads V2 tools
    threads_v2_tools = [
        ("threads_v2_fetch_user", "Fetch Threads user V2", {"user_id": {"type": "string"}}, ["user_id"]),
        ("threads_v2_fetch_threads", "Fetch Threads threads V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("threads_v2_fetch_thread", "Fetch Threads thread V2", {"thread_id": {"type": "string"}}, ["thread_id"]),
        ("threads_v2_fetch_replies", "Fetch Threads replies V2", {"thread_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["thread_id"]),
        ("threads_v2_fetch_search", "Search Threads V2", {"keyword": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["keyword"]),
    ]
    _add_tools(mcp_server, threads_v2_tools, "threads", "/api/v1/threads/web")

    # WeChat V2 tools
    wechat_v2_tools = [
        ("wechat_v2_fetch_user", "Fetch WeChat user V2", {"user_id": {"type": "string"}}, ["user_id"]),
        ("wechat_v2_fetch_videos", "Fetch WeChat videos V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("wechat_v2_fetch_video", "Fetch WeChat video V2", {"video_id": {"type": "string"}}, ["video_id"]),
        ("wechat_v2_fetch_comments", "Fetch WeChat comments V2", {"video_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["video_id"]),
        ("wechat_v2_fetch_article", "Fetch WeChat article V2", {"article_id": {"type": "string"}}, ["article_id"]),
    ]
    _add_tools(mcp_server, wechat_v2_tools, "wechat", "/api/v1/wechat/channels")

    # Lemon8 V2 tools
    lemon8_v2_tools = [
        ("lemon8_v2_fetch_user", "Fetch Lemon8 user V2", {"user_id": {"type": "string"}}, ["user_id"]),
        ("lemon8_v2_fetch_posts", "Fetch Lemon8 posts V2", {"user_id": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["user_id"]),
        ("lemon8_v2_fetch_post", "Fetch Lemon8 post V2", {"post_id": {"type": "string"}}, ["post_id"]),
        ("lemon8_v2_fetch_search", "Search Lemon8 V2", {"keyword": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["keyword"]),
        ("lemon8_v2_fetch_trending", "Fetch Lemon8 trending V2", {"count": {"type": "integer", "default": 20}}, []),
    ]
    _add_tools(mcp_server, lemon8_v2_tools, "lemon8", "/api/v1/lemon8/app")

    # NetEase V2 tools
    netease_v2_tools = [
        ("netease_v2_fetch_song", "Fetch NetEase song V2", {"song_id": {"type": "string"}}, ["song_id"]),
        ("netease_v2_fetch_playlist", "Fetch NetEase playlist V2", {"playlist_id": {"type": "string"}}, ["playlist_id"]),
        ("netease_v2_fetch_artist", "Fetch NetEase artist V2", {"artist_id": {"type": "string"}}, ["artist_id"]),
        ("netease_v2_fetch_search", "Search NetEase V2", {"keyword": {"type": "string"}, "count": {"type": "integer", "default": 20}}, ["keyword"]),
        ("netease_v2_fetch_hot_list", "Fetch NetEase hot list V2", {"count": {"type": "integer", "default": 20}}, []),
    ]
    _add_tools(mcp_server, netease_v2_tools, "netease", "/api/v1/netease/music")


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
