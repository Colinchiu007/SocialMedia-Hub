"""Shared server utilities."""

from __future__ import annotations

import logging
import time
import uuid
from datetime import datetime, timezone
from typing import Any

from fastapi import Header, HTTPException

logger = logging.getLogger("socialmedia_hub.server.core")

# ---------------------------------------------------------------------------
# API Key management
# ---------------------------------------------------------------------------

API_KEYS: dict[str, dict[str, Any]] = {}
_rate_limits: dict[str, list[float]] = {}


def generate_api_key(name: str, tier: str = "free") -> str:
    """Generate a new API key."""
    key = f"smh_{uuid.uuid4().hex}"
    API_KEYS[key] = {
        "name": name,
        "tier": tier,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "rate_limit": {"free": 60, "pro": 600, "enterprise": 6000}[tier],
    }
    return key


def verify_api_key(authorization: str | None = Header(None), request: Any = None) -> str:
    """Verify API key from Authorization header or Cookie.

    Supports two authentication methods:
    - Method 1 (Recommended): Authorization header with Bearer token
    - Method 2: Cookie named 'Authorization' with Bearer token
    """
    token = None

    # Method 1: Check Authorization header
    if authorization:
        token = authorization.replace("Bearer ", "").strip()

    # Method 2: Check Cookie (fallback)
    if not token and request:
        cookie_auth = request.cookies.get("Authorization")
        if cookie_auth:
            token = cookie_auth.replace("Bearer ", "").strip()

    if not token:
        raise HTTPException(status_code=401, detail="Missing Authorization header or Cookie")

    if token not in API_KEYS:
        raise HTTPException(status_code=401, detail="Invalid API key")

    key_info = API_KEYS[token]
    now = time.time()
    window_key = f"{token}:{int(now // 60)}"

    if window_key not in _rate_limits:
        _rate_limits[window_key] = []
    _rate_limits[window_key] = [t for t in _rate_limits[window_key] if t > now - 60]

    if len(_rate_limits[window_key]) >= key_info["rate_limit"]:
        raise HTTPException(
            status_code=429,
            detail="Rate limit exceeded",
            headers={"Retry-After": str(60 - int(now % 60))},
        )

    _rate_limits[window_key].append(now)
    return token


# ---------------------------------------------------------------------------
# Platform configs
# ---------------------------------------------------------------------------

PLATFORM_CONFIGS: dict[str, dict[str, Any]] = {
    "douyin": {
        "base_url": "https://www.douyin.com",
        "app_base_url": "https://api.amemv.com",
        "headers": {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Referer": "https://www.douyin.com/",
        },
    },
    "tiktok": {
        "base_url": "https://www.tiktok.com",
        "headers": {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Referer": "https://www.tiktok.com/",
        },
    },
    "instagram": {
        "base_url": "https://www.instagram.com",
        "api_base_url": "https://i.instagram.com/api/v1",
        "headers": {
            "User-Agent": "Instagram 275.0.0.27.98 Android (33/13; 420dpi; 1080x2400; samsung; SM-G991B; o1s; exynos2100; en_US; 458229258)",
        },
    },
    "youtube": {
        "base_url": "https://www.youtube.com",
        "headers": {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        },
    },
    "twitter": {
        "base_url": "https://api.twitter.com",
        "headers": {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        },
    },
    "xiaohongshu": {
        "base_url": "https://www.xiaohongshu.com",
        "headers": {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        },
    },
    "bilibili": {
        "base_url": "https://api.bilibili.com",
        "headers": {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Referer": "https://www.bilibili.com/",
        },
    },
    "weibo": {
        "base_url": "https://m.weibo.cn",
        "headers": {
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1",
        },
    },
    "kuaishou": {
        "base_url": "https://www.kuaishou.com",
        "headers": {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        },
    },
    "reddit": {
        "base_url": "https://www.reddit.com",
        "headers": {
            "User-Agent": "SocialMedia-Hub/0.1.0",
        },
    },
    "threads": {
        "base_url": "https://www.threads.net",
        "headers": {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        },
    },
    "linkedin": {
        "base_url": "https://www.linkedin.com",
        "headers": {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        },
    },
    "wechat": {
        "base_url": "https://channels.weixin.qq.com",
        "headers": {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        },
    },
    "zhihu": {
        "base_url": "https://www.zhihu.com",
        "headers": {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        },
    },
    "lemon8": {
        "base_url": "https://www.lemon8-app.com",
        "headers": {
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15",
        },
    },
    "netease": {
        "base_url": "https://music.163.com",
        "headers": {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Referer": "https://music.163.com/",
        },
    },
}


async def proxy_request(
    platform: str,
    path: str,
    method: str = "GET",
    params: dict[str, Any] | None = None,
    json_body: Any = None,
    cookies: dict[str, str] | None = None,
) -> dict[str, Any]:
    """Proxy a request to the target platform using RealProxyLayer."""
    from socialmedia_hub.proxy import real_proxy

    config = PLATFORM_CONFIGS.get(platform)
    if not config:
        raise HTTPException(status_code=400, detail=f"Unsupported platform: {platform}")

    base_url = config["base_url"]
    url = f"{base_url}/{path.lstrip('/')}"

    request_id = str(uuid.uuid4())

    try:
        # Use RealProxyLayer for authenticated requests
        result = await real_proxy.fetch(
            platform=platform,
            url=url,
            method=method,
            params=params,
            json_body=json_body,
            cookies=cookies,
            use_proxy=True,
            use_signature=True,
        )

        return {
            "code": result.get("status_code", 200),
            "request_id": request_id,
            "router": f"/api/v1/{platform}/{path}",
            "params": params,
            "data": result.get("data", {}),
            "time": datetime.now(timezone.utc).isoformat(),
            "time_zone": "UTC",
            "proxy_info": {
                "used_proxy": result.get("proxy_url") is not None,
                "signature_used": True,
            },
        }

    except Exception as e:
        logger.error(f"Proxy request failed: {e}")
        return {
            "code": 500,
            "request_id": request_id,
            "router": f"/api/v1/{platform}/{path}",
            "error": str(e),
            "time": datetime.now(timezone.utc).isoformat(),
        }
