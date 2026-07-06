"""Tests for SDK client functionality."""

from __future__ import annotations

import pytest

from socialmedia_hub._base_client import AsyncBaseClient, BaseClient
from socialmedia_hub._errors import (
    SMHRateLimitError,
)


class TestBaseClient:
    """Test BaseClient functionality."""

    def test_client_initialization(self):
        client = BaseClient(api_key="test-key")
        assert client._api_key == "test-key"
        assert client._base_url == "http://127.0.0.1:8000"
        client.close()

    def test_client_custom_base_url(self):
        client = BaseClient(api_key="test-key", base_url="http://custom:9000")
        assert client._base_url == "http://custom:9000"
        client.close()

    def test_client_context_manager(self):
        with BaseClient(api_key="test-key") as client:
            assert not client._client.is_closed
        assert client._client.is_closed

    def test_client_custom_timeout(self):
        client = BaseClient(api_key="test-key", timeout=60)
        assert client._client.timeout.connect == 60.0
        client.close()

    def test_client_custom_max_retries(self):
        client = BaseClient(api_key="test-key", max_retries=5)
        assert client._retry_policy.max_retries == 5
        client.close()

    def test_client_user_agent(self):
        client = BaseClient(api_key="test-key", user_agent="TestAgent/1.0")
        assert "TestAgent/1.0" in str(client._client.headers)
        client.close()


class TestAsyncBaseClient:
    """Test AsyncBaseClient functionality."""

    def test_async_client_initialization(self):
        client = AsyncBaseClient(api_key="test-key")
        assert client._api_key == "test-key"
        assert client._base_url == "http://127.0.0.1:8000"

    @pytest.mark.asyncio
    async def test_async_client_context_manager(self):
        async with AsyncBaseClient(api_key="test-key") as client:
            assert not client._client.is_closed
        assert client._client.is_closed


class TestRetryPolicy:
    """Test retry policy."""

    def test_should_retry_on_5xx(self):
        from socialmedia_hub._retries import RetryPolicy
        policy = RetryPolicy(max_retries=3)
        error = SMHRateLimitError(
            "rate limited",
            status_code=429,
            method="GET",
            url="/test",
        )
        assert policy.should_retry(error, 1) is True
        assert policy.should_retry(error, 2) is True
        assert policy.should_retry(error, 3) is False

    def test_should_not_retry_on_4xx(self):
        from socialmedia_hub._errors import SMHBadRequestError
        from socialmedia_hub._retries import RetryPolicy
        policy = RetryPolicy(max_retries=3)
        error = SMHBadRequestError(
            "bad request",
            status_code=400,
            method="GET",
            url="/test",
        )
        assert policy.should_retry(error, 1) is False

    def test_exponential_backoff(self):
        from socialmedia_hub._retries import RetryPolicy
        policy = RetryPolicy(max_retries=5, backoff_base=1.0, jitter=0.0)
        error = SMHRateLimitError(
            "rate limited",
            status_code=429,
            method="GET",
            url="/test",
        )
        assert policy.sleep_for(error, 1) == 1.0
        assert policy.sleep_for(error, 2) == 2.0
        assert policy.sleep_for(error, 3) == 4.0

    def test_uses_retry_after(self):
        from socialmedia_hub._retries import RetryPolicy
        policy = RetryPolicy(max_retries=3)
        error = SMHRateLimitError(
            "rate limited",
            status_code=429,
            method="GET",
            url="/test",
            retry_after=10.0,
        )
        assert policy.sleep_for(error, 1) == 10.0


class TestPagination:
    """Test pagination helpers."""

    def test_cursor_paginator(self):
        from socialmedia_hub._pagination import CursorPaginator, Page

        pages = [
            Page(items=[1, 2], next_cursor=2, has_more=True),
            Page(items=[3, 4], next_cursor=4, has_more=False),
        ]
        call_count = 0

        def fetch(cursor):
            nonlocal call_count
            page = pages[call_count]
            call_count += 1
            return page

        paginator = CursorPaginator(sync_fetch=fetch)
        result = list(paginator)
        assert result == [1, 2, 3, 4]

    def test_cursor_paginator_first(self):
        from socialmedia_hub._pagination import CursorPaginator, Page

        pages = [
            Page(items=[1, 2, 3], next_cursor=3, has_more=True),
            Page(items=[4, 5, 6], next_cursor=6, has_more=False),
        ]
        call_count = 0

        def fetch(cursor):
            nonlocal call_count
            page = pages[call_count]
            call_count += 1
            return page

        paginator = CursorPaginator(sync_fetch=fetch)
        result = paginator.first(4)
        assert result == [1, 2, 3, 4]
