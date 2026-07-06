"""NetEase Cloud Music App API routes — 10+ endpoints."""

from __future__ import annotations

from typing import Any

from fastapi import APIRouter, Depends

from socialmedia_hub.server._core import proxy_request, verify_api_key

router = APIRouter(prefix="/api/v1/netease", tags=["netease"])


# ===========================================================================
# Music API
# ===========================================================================


@router.get("/music/fetch_song_detail")
async def fetch_song_detail(song_id: str, token: str = Depends(verify_api_key)) -> dict[str, Any]:
    """获取歌曲详情 / Get song detail."""
    return await proxy_request("netease", "/api/v1/netease/music/song/detail", params={"id": song_id})


@router.get("/music/fetch_song_url")
async def fetch_song_url(song_id: str, token: str = Depends(verify_api_key)) -> dict[str, Any]:
    """获取歌曲播放链接 / Get song play URL."""
    return await proxy_request("netease", "/api/v1/netease/music/song/url", params={"id": song_id})


@router.get("/music/fetch_song_lyric")
async def fetch_song_lyric(song_id: str, token: str = Depends(verify_api_key)) -> dict[str, Any]:
    """获取歌曲歌词 / Get song lyrics."""
    return await proxy_request("netease", "/api/v1/netease/music/lyric", params={"id": song_id})


@router.get("/music/fetch_song_comment")
async def fetch_song_comment(
    song_id: str, limit: int = 20, token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取歌曲评论 / Get song comments."""
    return await proxy_request("netease", "/api/v1/netease/music/comment", params={"id": song_id, "limit": limit})


@router.get("/music/fetch_playlist_detail")
async def fetch_playlist_detail(playlist_id: str, token: str = Depends(verify_api_key)) -> dict[str, Any]:
    """获取歌单详情 / Get playlist detail."""
    return await proxy_request("netease", "/api/v1/netease/music/playlist/detail", params={"id": playlist_id})


@router.get("/music/fetch_playlist_tracks")
async def fetch_playlist_tracks(
    playlist_id: str, limit: int = 50, token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取歌单歌曲列表 / Get playlist tracks."""
    return await proxy_request(
        "netease", "/api/v1/netease/music/playlist/track",
        params={"id": playlist_id, "limit": limit}
    )


@router.get("/music/fetch_artist_songs")
async def fetch_artist_songs(
    artist_id: str, limit: int = 50, token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取歌手歌曲 / Get artist songs."""
    return await proxy_request(
        "netease", "/api/v1/netease/music/artist/songs",
        params={"id": artist_id, "limit": limit}
    )


@router.get("/music/fetch_artist_detail")
async def fetch_artist_detail(artist_id: str, token: str = Depends(verify_api_key)) -> dict[str, Any]:
    """获取歌手详情 / Get artist detail."""
    return await proxy_request("netease", "/api/v1/netease/music/artist/detail", params={"id": artist_id})


@router.get("/music/fetch_album_detail")
async def fetch_album_detail(album_id: str, token: str = Depends(verify_api_key)) -> dict[str, Any]:
    """获取专辑详情 / Get album detail."""
    return await proxy_request("netease", "/api/v1/netease/music/album/detail", params={"id": album_id})


@router.get("/music/fetch_search")
async def fetch_search(
    keyword: str, search_type: int = 1, limit: int = 30, token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """搜索音乐 / Search music."""
    return await proxy_request(
        "netease", "/api/v1/netease/music/search",
        params={"keywords": keyword, "type": search_type, "limit": limit}
    )


@router.get("/music/fetch_hot_search")
async def fetch_hot_search(token: str = Depends(verify_api_key)) -> dict[str, Any]:
    """获取热搜榜 / Get hot search."""
    return await proxy_request("netease", "/api/v1/netease/music/search/hot")


@router.get("/music/fetch_recommend_songs")
async def fetch_recommend_songs(token: str = Depends(verify_api_key)) -> dict[str, Any]:
    """获取每日推荐歌曲 / Get daily recommend songs."""
    return await proxy_request("netease", "/api/v1/netease/music/recommend/songs")


@router.get("/music/fetch_top_list")
async def fetch_top_list(token: str = Depends(verify_api_key)) -> dict[str, Any]:
    """获取排行榜 / Get top list."""
    return await proxy_request("netease", "/api/v1/netease/music/toplist")


@router.get("/music/fetch_mv_detail")
async def fetch_mv_detail(mv_id: str, token: str = Depends(verify_api_key)) -> dict[str, Any]:
    """获取MV详情 / Get MV detail."""
    return await proxy_request("netease", "/api/v1/netease/music/mv/detail", params={"mvid": mv_id})


@router.get("/music/fetch_mv_url")
async def fetch_mv_url(mv_id: str, token: str = Depends(verify_api_key)) -> dict[str, Any]:
    """获取MV播放链接 / Get MV play URL."""
    return await proxy_request("netease", "/api/v1/netease/music/mv/url", params={"id": mv_id})


# ===========================================================================
# User API
# ===========================================================================


@router.get("/user/fetch_user_detail")
async def fetch_user_detail(user_id: str, token: str = Depends(verify_api_key)) -> dict[str, Any]:
    """获取用户详情 / Get user detail."""
    return await proxy_request("netease", "/api/v1/netease/user/detail", params={"uid": user_id})


@router.get("/user/fetch_user_playlist")
async def fetch_user_playlist(
    user_id: str, limit: int = 30, token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户歌单 / Get user playlist."""
    return await proxy_request(
        "netease", "/api/v1/netease/user/playlist",
        params={"uid": user_id, "limit": limit}
    )


@router.get("/user/fetch_user_likedsongs")
async def fetch_user_likedsongs(
    user_id: str, limit: int = 50, token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户喜欢的歌曲 / Get user liked songs."""
    return await proxy_request(
        "netease", "/api/v1/netease/user/likedsongs",
        params={"uid": user_id, "limit": limit}
    )


@router.get("/user/fetch_user_followeds")
async def fetch_user_followeds(
    user_id: str, limit: int = 30, token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户粉丝 / Get user followers."""
    return await proxy_request(
        "netease", "/api/v1/netease/user/followeds",
        params={"uid": user_id, "limit": limit}
    )


@router.get("/user/fetch_user_follows")
async def fetch_user_follows(
    user_id: str, limit: int = 30, token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户关注 / Get user following."""
    return await proxy_request(
        "netease", "/api/v1/netease/user/follows",
        params={"uid": user_id, "limit": limit}
    )


@router.get("/user/fetch_user_event")
async def fetch_user_event(
    user_id: str, limit: int = 30, token: str = Depends(verify_api_key)
) -> dict[str, Any]:
    """获取用户动态 / Get user events."""
    return await proxy_request(
        "netease", "/api/v1/netease/user/event",
        params={"uid": user_id, "limit": limit}
    )
