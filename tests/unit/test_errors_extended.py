"""Extended tests for errors module."""

from __future__ import annotations

import httpx
import pytest

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
    _redact_headers,
    from_httpx_request_error,
    http_error_for_status,
)


class TestRedactHeaders:
    """Tests for _redact_headers function."""

    def test_none_headers(self):
        assert _redact_headers(None) == {}

    def test_empty_headers(self):
        assert _redact_headers({}) == {}

    def test_redact_authorization(self):
        headers = {"Authorization": "Bearer secret", "Content-Type": "application/json"}
        result = _redact_headers(headers)
        assert result["Authorization"] == "***"
        assert result["Content-Type"] == "application/json"

    def test_case_insensitive(self):
        headers = {"authorization": "Bearer secret"}
        result = _redact_headers(headers)
        assert result["authorization"] == "***"


class TestSMHErrorHierarchy:
    """Tests for error hierarchy."""

    def test_base_error(self):
        err = SMHError("test")
        assert str(err) == "test"
        assert isinstance(err, Exception)

    def test_config_error(self):
        err = SMHConfigError("config error")
        assert isinstance(err, SMHError)

    def test_connection_error(self):
        err = SMHConnectionError("connection error", cause=ValueError("original"))
        assert isinstance(err, SMHError)
        assert err.__cause__ is not None

    def test_timeout_error(self):
        err = SMHTimeoutError("timeout")
        assert isinstance(err, SMHConnectionError)

    def test_proxy_error(self):
        err = SMHProxyError("proxy error")
        assert isinstance(err, SMHConnectionError)


class TestSMHHTTPError:
    """Tests for SMHHTTPError."""

    def test_http_error_creation(self):
        err = SMHHTTPError(
            "bad request",
            status_code=400,
            method="GET",
            url="/api/test",
        )
        assert err.status_code == 400
        assert err.method == "GET"
        assert err.url == "/api/test"

    def test_http_error_str(self):
        err = SMHHTTPError(
            "not found",
            status_code=404,
            method="POST",
            url="/api/users",
            request_id="req-123",
        )
        s = str(err)
        assert "404" in s
        assert "POST" in s
        assert "req-123" in s

    def test_http_error_repr(self):
        err = SMHHTTPError(
            "error",
            status_code=500,
            method="GET",
            url="/api",
            params={"key": "value"},
            request_body={"data": 123},
            response_body={"error": "msg"},
            request_id="abc",
        )
        r = repr(err)
        assert "SMHHTTPError" in r
        assert "status_code=500" in r

    def test_http_error_with_headers(self):
        err = SMHHTTPError(
            "error",
            status_code=401,
            method="GET",
            url="/api",
            headers={"Authorization": "Bearer secret"},
        )
        assert err.headers["Authorization"] == "***"

    def test_http_error_with_params(self):
        err = SMHHTTPError(
            "error",
            status_code=400,
            method="GET",
            url="/api",
            params={"key": "value"},
        )
        assert err.params == {"key": "value"}


class TestSpecificErrors:
    """Tests for specific error types."""

    def test_bad_request_error(self):
        err = SMHBadRequestError("bad", status_code=400, method="GET", url="/")
        assert isinstance(err, SMHHTTPError)
        assert err.status_code == 400

    def test_auth_error(self):
        err = SMHAuthError("unauthorized", status_code=401, method="GET", url="/")
        assert isinstance(err, SMHHTTPError)
        assert err.status_code == 401

    def test_permission_error(self):
        err = SMHPermissionError("forbidden", status_code=403, method="GET", url="/")
        assert isinstance(err, SMHHTTPError)
        assert err.status_code == 403

    def test_not_found_error(self):
        err = SMHNotFoundError("not found", status_code=404, method="GET", url="/")
        assert isinstance(err, SMHHTTPError)
        assert err.status_code == 404

    def test_rate_limit_error(self):
        err = SMHRateLimitError(
            "rate limited",
            status_code=429,
            method="GET",
            url="/",
            retry_after=60.0,
        )
        assert isinstance(err, SMHHTTPError)
        assert err.retry_after == 60.0

    def test_server_error(self):
        err = SMHServerError("server error", status_code=500, method="GET", url="/")
        assert isinstance(err, SMHHTTPError)
        assert err.status_code == 500

    def test_upstream_error(self):
        err = SMHUpstreamError("upstream", status_code=502, method="GET", url="/")
        assert isinstance(err, SMHHTTPError)
        assert err.status_code == 502

    def test_validation_error(self):
        err = SMHValidationError("invalid", raw={"data": None})
        assert isinstance(err, SMHError)
        assert err.raw == {"data": None}

    def test_validation_error_with_cause(self):
        err = SMHValidationError("invalid", cause=ValueError("bad"))
        assert err.__cause__ is not None

    def test_feature_removed_error(self):
        err = SMHFeatureRemovedError("removed")
        assert isinstance(err, SMHError)


class TestHttpStatusMapping:
    """Tests for http_error_for_status function."""

    def test_400_bad_request(self):
        assert http_error_for_status(400) is SMHBadRequestError

    def test_401_auth(self):
        assert http_error_for_status(401) is SMHAuthError

    def test_403_permission(self):
        assert http_error_for_status(403) is SMHPermissionError

    def test_404_not_found(self):
        assert http_error_for_status(404) is SMHNotFoundError

    def test_422_bad_request(self):
        assert http_error_for_status(422) is SMHBadRequestError

    def test_429_rate_limit(self):
        assert http_error_for_status(429) is SMHRateLimitError

    def test_500_server(self):
        assert http_error_for_status(500) is SMHServerError

    def test_502_upstream(self):
        assert http_error_for_status(502) is SMHUpstreamError

    def test_503_upstream(self):
        assert http_error_for_status(503) is SMHUpstreamError

    def test_504_upstream(self):
        assert http_error_for_status(504) is SMHUpstreamError

    def test_unknown_status(self):
        assert http_error_for_status(418) is SMHHTTPError


class TestFromHttpxError:
    """Tests for from_httpx_request_error function."""

    def test_timeout_error(self):
        exc = httpx.TimeoutException("timeout")
        err = from_httpx_request_error(exc)
        assert isinstance(err, SMHTimeoutError)
        assert "timeout" in str(err)

    def test_proxy_error(self):
        exc = httpx.ProxyError("proxy error")
        err = from_httpx_request_error(exc)
        assert isinstance(err, SMHProxyError)
        assert "proxy error" in str(err)

    def test_connection_error(self):
        exc = httpx.ConnectError("connection refused")
        err = from_httpx_request_error(exc)
        assert isinstance(err, SMHConnectionError)
        assert not isinstance(err, SMHTimeoutError)
        assert not isinstance(err, SMHProxyError)

    def test_empty_message_timeout(self):
        exc = httpx.TimeoutException("")
        err = from_httpx_request_error(exc)
        assert "timed out" in str(err).lower()

    def test_empty_message_proxy(self):
        exc = httpx.ProxyError("")
        err = from_httpx_request_error(exc)
        assert "proxy" in str(err).lower()
