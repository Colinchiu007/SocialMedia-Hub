"""SocialMedia-Hub: Multi-platform social media data SDK and API server.

Quick start::

    from socialmedia_hub import SocialMediaHub

    with SocialMediaHub(api_key="YOUR_API_KEY") as client:
        video = client.douyin.fetch_video(video_id="...")
        print(video)

"""

from __future__ import annotations

from socialmedia_hub._base_client import AsyncBaseClient, BaseClient
from socialmedia_hub._errors import (
    SMHAuthError,
    SMHBadRequestError,
    SMHConfigError,
    SMHConnectionError,
    SMHError,
    SMHFeatureRemovedError,
    SMHHTTPError,
    SMHNotFoundError,
    SMHPermissionError,
    SMHProxyError,
    SMHRateLimitError,
    SMHServerError,
    SMHTimeoutError,
    SMHUpstreamError,
    SMHValidationError,
)
from socialmedia_hub._pagination import (
    CursorPaginator,
    OffsetPaginator,
    Page,
    PagePaginator,
)
from socialmedia_hub._version import __version__

# Aliases for convenience
SocialMediaHub = BaseClient
AsyncSocialMediaHub = AsyncBaseClient

__all__ = [
    "AsyncBaseClient",
    "AsyncSocialMediaHub",
    "BaseClient",
    "CursorPaginator",
    "OffsetPaginator",
    "Page",
    "PagePaginator",
    "SMHAuthError",
    "SMHBadRequestError",
    "SMHConfigError",
    "SMHConnectionError",
    "SMHError",
    "SMHFeatureRemovedError",
    "SMHHTTPError",
    "SMHNotFoundError",
    "SMHPermissionError",
    "SMHProxyError",
    "SMHRateLimitError",
    "SMHServerError",
    "SMHTimeoutError",
    "SMHUpstreamError",
    "SMHValidationError",
    "SocialMediaHub",
    "__version__",
]
