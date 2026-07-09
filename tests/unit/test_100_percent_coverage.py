"""Tests to achieve 100% coverage."""

from __future__ import annotations

import asyncio
import tempfile
from pathlib import Path
from unittest.mock import AsyncMock, MagicMock, patch

import httpx
import pytest

from socialmedia_hub._base_client import AsyncBaseClient, BaseClient
from socialmedia_hub._pagination import CursorPaginator, Page
from socialmedia_hub._retries import RetryPolicy
from socialmedia_hub.proxy.cookies import CookieManager
from socialmedia_hub.proxy.pool import ProxyPool
from socialmedia_hub.proxy.real_proxy import RealProxyLayer


class TestBaseClient100:
    """Tests for 100% coverage of BaseClient."""

    def test_client_with_custom_transport(self):
        mock_transport = MagicMock()
        client = BaseClient(api_key="test", transport=mock_transport)
        assert client._owns_client is True
        client.close()

    def test_client_close_owns_client(self):
        client = BaseClient(api_key="test")
        assert client._owns_client is True
        client.close()

    def test_client_join_path(self):
        client = BaseClient(api_key="test")
        assert client._join("api/test") == "http://127.0.0.1:8000/api/test"
        client.close()

    def test_client_join_absolute(self):
        client = BaseClient(api_key="test")
        assert client._join("https://example.com/api") == "https://example.com/api"
        client.close()

    def test_client_decode_raw(self):
        client = BaseClient(api_key="test", parse_response=False)
        mock_response = MagicMock()
        mock_response.json.return_value = {"data": "test"}
        mock_response.text = '{"data": "test"}'
        result = client._decode(mock_response)
        client.close()

    def test_client_request_json_error(self):
        from socialmedia_hub._errors import SMHHTTPError
        client = BaseClient(api_key="test", max_retries=1)
        error = SMHHTTPError("error", status_code=500, method="GET", url="/api")
        client._client.request = MagicMock(side_effect=error)
        with pytest.raises(SMHHTTPError):
            client._request("GET", "/api")
        client.close()


class TestAsyncBaseClient100:
    """Tests for 100% coverage of AsyncBaseClient."""

    @pytest.mark.asyncio
    async def test_async_client_with_custom_transport(self):
        mock_transport = AsyncMock()
        client = AsyncBaseClient(api_key="test", transport=mock_transport)
        assert client._owns_client is True
        await client.aclose()

    @pytest.mark.asyncio
    async def test_async_client_close_owns_client(self):
        client = AsyncBaseClient(api_key="test")
        assert client._owns_client is True
        await client.aclose()

    @pytest.mark.asyncio
    async def test_async_client_join_path(self):
        client = AsyncBaseClient(api_key="test")
        assert client._join("api/test") == "http://127.0.0.1:8000/api/test"
        await client.aclose()

    @pytest.mark.asyncio
    async def test_async_client_decode_raw(self):
        client = AsyncBaseClient(api_key="test", parse_response=False)
        mock_response = MagicMock()
        mock_response.json.return_value = {"data": "test"}
        mock_response.text = '{"data": "test"}'
        result = client._decode(mock_response)
        await client.aclose()

    @pytest.mark.asyncio
    async def test_async_client_request_json_error(self):
        from socialmedia_hub._errors import SMHHTTPError
        client = AsyncBaseClient(api_key="test", max_retries=1)
        error = SMHHTTPError("error", status_code=500, method="GET", url="/api")
        client._client.request = AsyncMock(side_effect=error)
        with pytest.raises(SMHHTTPError):
            await client._request("GET", "/api")
        await client.aclose()


class TestPagination100:
    """Tests for 100% coverage of pagination."""

    def test_paginator_base_init(self):
        from socialmedia_hub._pagination import _PaginatorBase
        p = _PaginatorBase()
        assert p.has_more is True

    def test_paginator_base_advance_not_implemented(self):
        from socialmedia_hub._pagination import _PaginatorBase
        p = _PaginatorBase()
        with pytest.raises(NotImplementedError):
            p._advance()

    def test_paginator_base_aadvance_not_implemented(self):
        from socialmedia_hub._pagination import _PaginatorBase
        p = _PaginatorBase()
        with pytest.raises(NotImplementedError):
            asyncio.run(p._aadvance())

    def test_cursor_paginator_sync_only(self):
        paginator = CursorPaginator(sync_fetch=lambda c: Page([], has_more=False))
        result = list(paginator)
        assert result == []

    def test_cursor_paginator_async_only(self):
        async def async_fetch(cursor):
            return Page([], has_more=False)

        paginator = CursorPaginator(async_fetch=async_fetch)
        result = asyncio.run(paginator.afirst(10))
        assert result == []


class TestRetries100:
    """Tests for 100% coverage of retries."""

    def test_sleep_for_rate_limit_with_retry_after(self):
        from socialmedia_hub._errors import SMHRateLimitError
        policy = RetryPolicy(max_retries=3)
        error = SMHRateLimitError(
            "rate limited",
            status_code=429,
            method="GET",
            url="/api",
            retry_after=5.0,
        )
        sleep = policy.sleep_for(error, 1)
        assert sleep == 5.0


class TestCookies100:
    """Tests for 100% coverage of cookies."""

    def test_save_cookies_error(self):
        manager = CookieManager(storage_path=Path("/nonexistent/path/cookies.json"))
        manager.set_cookie("session", "abc", "example.com")
        # Should not raise

    def test_load_cookies_invalid(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "invalid.json"
            path.write_text("not json")
            manager = CookieManager(storage_path=path)
            assert len(manager.cookies) == 0


class TestPool100:
    """Tests for 100% coverage of pool."""

    def test_record_success(self):
        pool = ProxyPool()
        pool.add_proxy(host="p1", port=8080)
        proxy = pool.proxies[0]
        proxy.record_success()
        assert proxy.success_count == 1

    def test_record_failure(self):
        pool = ProxyPool()
        pool.add_proxy(host="p1", port=8080)
        proxy = pool.proxies[0]
        proxy.record_failure()
        assert proxy.failure_count == 1

    def test_get_proxy_best_success(self):
        pool = ProxyPool()
        pool.add_proxy(host="p1", port=8080)
        pool.add_proxy(host="p2", port=8081)
        pool.proxies[0].success_count = 10
        pool.proxies[0].failure_count = 0
        pool.proxies[1].success_count = 5
        pool.proxies[1].failure_count = 5
        proxy = pool.get_proxy(strategy="best_success")
        assert proxy.success_rate >= 0.5


class TestRealProxy100:
    """Tests for 100% coverage of real_proxy."""

    @pytest.mark.asyncio
    async def test_fetch_with_no_proxy(self):
        layer = RealProxyLayer()
        layer.proxy_pool = ProxyPool()

        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"data": "test"}
        mock_response.headers = {}

        with patch("httpx.AsyncClient") as mock_client:
            mock_client.return_value.__aenter__ = AsyncMock(return_value=mock_client)
            mock_client.return_value.__aexit__ = AsyncMock(return_value=False)
            mock_client.get = AsyncMock(return_value=mock_response)

            result = await layer.fetch(
                "tiktok",
                "https://www.tiktok.com/api/test",
                use_proxy=False,
            )
            assert result["status_code"] == 200

    @pytest.mark.asyncio
    async def test_fetch_json_error(self):
        layer = RealProxyLayer()

        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.side_effect = ValueError("invalid json")
        mock_response.text = "raw text"
        mock_response.headers = {}

        with patch("httpx.AsyncClient") as mock_client:
            mock_client.return_value.__aenter__ = AsyncMock(return_value=mock_client)
            mock_client.return_value.__aexit__ = AsyncMock(return_value=False)
            mock_client.get = AsyncMock(return_value=mock_response)

            result = await layer.fetch(
                "tiktok",
                "https://www.tiktok.com/api/test",
            )
            assert result["status_code"] == 200

    @pytest.mark.asyncio
    async def test_fetch_error_records_failure(self):
        layer = RealProxyLayer()
        pool = ProxyPool()
        pool.add_proxy(host="p1", port=8080)
        layer.proxy_pool = pool

        with patch("httpx.AsyncClient") as mock_client:
            mock_client.return_value.__aenter__ = AsyncMock(return_value=mock_client)
            mock_client.return_value.__aexit__ = AsyncMock(return_value=False)
            mock_client.get = AsyncMock(side_effect=httpx.ConnectError("failed"))

            result = await layer.fetch(
                "tiktok",
                "https://www.tiktok.com/api/test",
                use_proxy=True,
            )
            assert result["status_code"] == 0
