"""Tests for retry policy."""

from __future__ import annotations

from socialmedia_hub._errors import (
    SMHConnectionError,
    SMHRateLimitError,
    SMHServerError,
)
from socialmedia_hub._retries import RetryPolicy


class TestRetryPolicy:
    """Test RetryPolicy behavior."""

    def test_should_retry_5xx(self) -> None:
        policy = RetryPolicy(max_retries=3)
        assert policy.should_retry(SMHServerError("error", status_code=500, method="GET", url="/"), 1) is True
        assert policy.should_retry(SMHServerError("error", status_code=500, method="GET", url="/"), 2) is True
        assert policy.should_retry(SMHServerError("error", status_code=500, method="GET", url="/"), 3) is False

    def test_should_retry_connection_error(self) -> None:
        policy = RetryPolicy(max_retries=3)
        assert policy.should_retry(SMHConnectionError("timeout"), 1) is True

    def test_should_retry_rate_limit(self) -> None:
        policy = RetryPolicy(max_retries=3)
        assert policy.should_retry(
            SMHRateLimitError("rate limited", status_code=429, method="GET", url="/"), 1
        ) is True

    def test_should_not_retry_4xx(self) -> None:
        from socialmedia_hub._errors import SMHBadRequestError
        policy = RetryPolicy(max_retries=3)
        assert policy.should_retry(
            SMHBadRequestError("bad request", status_code=400, method="GET", url="/"), 1
        ) is False

    def test_uses_retry_after_when_present(self) -> None:
        policy = RetryPolicy(max_retries=3)
        exc = SMHRateLimitError("rate limited", status_code=429, method="GET", url="/", retry_after=10.0)
        assert policy.sleep_for(exc, 1) == 10.0

    def test_exponential_backoff(self) -> None:
        policy = RetryPolicy(max_retries=5, backoff_base=1.0, jitter=0.0)
        delay1 = policy.sleep_for(SMHServerError("error", status_code=500, method="GET", url="/"), 1)
        delay2 = policy.sleep_for(SMHServerError("error", status_code=500, method="GET", url="/"), 2)
        delay3 = policy.sleep_for(SMHServerError("error", status_code=500, method="GET", url="/"), 3)
        assert delay1 == 1.0
        assert delay2 == 2.0
        assert delay3 == 4.0

    def test_caps_at_backoff_max(self) -> None:
        policy = RetryPolicy(max_retries=10, backoff_base=1.0, backoff_max=5.0, jitter=0.0)
        delay = policy.sleep_for(SMHServerError("error", status_code=500, method="GET", url="/"), 10)
        assert delay == 5.0
