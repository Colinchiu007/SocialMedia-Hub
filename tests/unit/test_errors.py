"""Tests for error hierarchy."""

from __future__ import annotations

import pytest

from socialmedia_hub._errors import (
    SMHAuthError,
    SMHBadRequestError,
    SMHConfigError,
    SMHConnectionError,
    SMHError,
    SMHHTTPError,
    SMHNotFoundError,
    SMHPermissionError,
    SMHRateLimitError,
    SMHServerError,
    SMHUpstreamError,
    http_error_for_status,
)


class TestStatusMapping:
    """Test HTTP status code to exception mapping."""

    @pytest.mark.parametrize(
        "status,expected",
        [
            (400, SMHBadRequestError),
            (401, SMHAuthError),
            (403, SMHPermissionError),
            (404, SMHNotFoundError),
            (422, SMHBadRequestError),
            (429, SMHRateLimitError),
            (500, SMHServerError),
            (502, SMHUpstreamError),
            (503, SMHUpstreamError),
            (504, SMHUpstreamError),
            (599, SMHServerError),
        ],
    )
    def test_status_maps_to_exception(self, status: int, expected: type) -> None:
        assert http_error_for_status(status) is expected


class TestExceptionProperties:
    """Test exception attributes."""

    def test_401_raises_auth_error(self) -> None:
        with pytest.raises(SMHAuthError) as exc_info:
            raise http_error_for_status(401)(
                "Unauthorized",
                status_code=401,
                method="GET",
                url="/api/test",
            )
        assert exc_info.value.status_code == 401
        assert exc_info.value.method == "GET"

    def test_429_carries_retry_after(self) -> None:
        exc = SMHRateLimitError(
            "Rate limited",
            status_code=429,
            method="GET",
            url="/api/test",
            retry_after=30.0,
        )
        assert exc.retry_after == 30.0

    def test_all_specific_errors_inherit_from_base(self) -> None:
        for exc_class in [
            SMHBadRequestError,
            SMHAuthError,
            SMHPermissionError,
            SMHNotFoundError,
            SMHRateLimitError,
            SMHServerError,
            SMHUpstreamError,
        ]:
            assert issubclass(exc_class, SMHHTTPError)
            assert issubclass(exc_class, SMHError)

    def test_connection_errors_inherit(self) -> None:
        assert issubclass(SMHConnectionError, SMHError)
        assert issubclass(SMHConfigError, SMHError)
