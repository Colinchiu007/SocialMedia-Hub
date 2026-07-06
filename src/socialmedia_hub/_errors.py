"""Exception hierarchy for the SocialMedia-Hub SDK."""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any

import httpx

__all__ = [
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
]

_REDACT = "***"


def _redact_headers(headers: Mapping[str, str] | None) -> dict[str, str]:
    if not headers:
        return {}
    return {
        k: (_REDACT if k.lower() == "authorization" else v) for k, v in headers.items()
    }


class SMHError(Exception):
    """Base class for every error raised by the SDK."""


class SMHConfigError(SMHError):
    """Configuration is invalid (missing API key, bad base URL, etc.)."""


class SMHConnectionError(SMHError):
    """Network failure before any HTTP response was received."""

    def __init__(self, message: str, *, cause: BaseException | None = None) -> None:
        super().__init__(message)
        self.__cause__ = cause


class SMHTimeoutError(SMHConnectionError):
    """Timed out waiting for a response."""


class SMHProxyError(SMHConnectionError):
    """Proxy could not be contacted or rejected the request."""


class SMHHTTPError(SMHError):
    """The server returned a non-2xx response."""

    def __init__(
        self,
        message: str,
        *,
        status_code: int,
        method: str,
        url: str,
        params: Mapping[str, Any] | None = None,
        request_body: Any = None,
        response_body: Any = None,
        request_id: str | None = None,
        headers: Mapping[str, str] | None = None,
    ) -> None:
        super().__init__(message)
        self.status_code = status_code
        self.method = method
        self.url = url
        self.params: dict[str, Any] = dict(params) if params else {}
        self.request_body = request_body
        self.response_body = response_body
        self.request_id = request_id
        self.headers: dict[str, str] = _redact_headers(headers)

    def __str__(self) -> str:
        rid = f" request_id={self.request_id}" if self.request_id else ""
        return f"{self.status_code} {self.method} {self.url}{rid}: {self.args[0]}"

    def __repr__(self) -> str:
        return (
            f"{type(self).__name__}("
            f"status_code={self.status_code}, "
            f"method={self.method!r}, "
            f"url={self.url!r}, "
            f"params={self.params!r}, "
            f"request_body={self.request_body!r}, "
            f"response_body={self.response_body!r}, "
            f"request_id={self.request_id!r}, "
            f"headers={self.headers!r}"
            ")"
        )


class SMHBadRequestError(SMHHTTPError):
    """400 / 422 — caller sent something the API rejected."""


class SMHAuthError(SMHHTTPError):
    """401 — missing, malformed, or invalid API key."""


class SMHPermissionError(SMHHTTPError):
    """403 — authenticated but not allowed."""


class SMHNotFoundError(SMHHTTPError):
    """404 — endpoint or resource doesn't exist."""


class SMHRateLimitError(SMHHTTPError):
    """429 — rate limited."""

    def __init__(self, *args: Any, retry_after: float | None = None, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.retry_after = retry_after


class SMHServerError(SMHHTTPError):
    """5xx — server internal failure."""


class SMHUpstreamError(SMHHTTPError):
    """502 / 503 / 504 indicating upstream platform unreachable."""


class SMHValidationError(SMHError):
    """Response payload could not be parsed."""

    def __init__(self, message: str, *, raw: Any = None, cause: BaseException | None = None) -> None:
        super().__init__(message)
        self.raw = raw
        if cause is not None:
            self.__cause__ = cause


class SMHFeatureRemovedError(SMHError):
    """Endpoint has been removed from the spec."""


_STATUS_MAP: dict[int, type[SMHHTTPError]] = {
    400: SMHBadRequestError,
    401: SMHAuthError,
    403: SMHPermissionError,
    404: SMHNotFoundError,
    422: SMHBadRequestError,
    429: SMHRateLimitError,
}


def http_error_for_status(status: int) -> type[SMHHTTPError]:
    """Return the exception subclass best matching ``status``."""
    if status in _STATUS_MAP:
        return _STATUS_MAP[status]
    if status in (502, 503, 504):
        return SMHUpstreamError
    if 500 <= status < 600:
        return SMHServerError
    return SMHHTTPError


def from_httpx_request_error(exc: httpx.RequestError) -> SMHConnectionError:
    """Translate an httpx low-level error into an SDK exception."""
    if isinstance(exc, httpx.TimeoutException):
        return SMHTimeoutError(str(exc) or "Request timed out", cause=exc)
    if isinstance(exc, httpx.ProxyError):
        return SMHProxyError(str(exc) or "Proxy error", cause=exc)
    return SMHConnectionError(str(exc) or "Connection error", cause=exc)
