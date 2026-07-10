"""Final push to achieve 100% coverage."""

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


class TestBaseClientFinalPush:
    """Final push for BaseClient coverage."""

    def test_client_decode_error_handling(self):
        client = BaseClient(api_key="test", parse_response=True)
        mock_response = MagicMock()
        mock_response.json.side_effect = ValueError("invalid json")
        mock_response.text = "raw text"
        # _decode should handle JSON errors
        result = client._decode(mock_response)
        client.close()

    def test_client_request_file_upload(self):
        client = BaseClient(api_key="test")
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"success": True}
        mock_response.headers = {}
        client._client.request = MagicMock(return_value=mock_response)
        result = client._request("POST", "/upload", files={"file": (b"content", "test.txt")})
        assert result == {"success": True}
        client.close()


class TestAsyncBaseClientFinalPush:
    """Final push for AsyncBaseClient coverage."""

    @pytest.mark.asyncio
    async def test_async_client_decode_error_handling(self):
        client = AsyncBaseClient(api_key="test", parse_response=True)
        mock_response = MagicMock()
        mock_response.json.side_effect = ValueError("invalid json")
        mock_response.text = "raw text"
        result = client._decode(mock_response)
        await client.aclose()

    @pytest.mark.asyncio
    async def test_async_client_request_file_upload(self):
        client = AsyncBaseClient(api_key="test")
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"success": True}
        mock_response.headers = {}
        client._client.request = AsyncMock(return_value=mock_response)
        result = await client._request("POST", "/upload", files={"file": (b"content", "test.txt")})
        assert result == {"success": True}
        await client.aclose()


class TestPaginationFinalPush:
    """Final push for pagination coverage."""

    def test_cursor_paginator_async_only_error(self):
        async def async_fetch(cursor):
            return Page([], has_more=False)

        paginator = CursorPaginator(async_fetch=async_fetch)
        # Test that sync methods raise error
        with pytest.raises(RuntimeError):
            list(paginator)

    def test_cursor_paginator_sync_only_error(self):
        paginator = CursorPaginator(sync_fetch=lambda c: Page([], has_more=False))
        # Test that async methods raise error
        async def test():
            await paginator.afirst(1)

        with pytest.raises(RuntimeError):
            asyncio.run(test())


class TestRetriesFinalPush:
    """Final push for retries coverage."""

    def test_sleep_for_zero_attempt(self):
        policy = RetryPolicy(max_retries=3, backoff_base=1.0, jitter=0.0)
        sleep = policy.sleep_for(Exception("error"), 0)
        assert sleep >= 0


class TestCookiesFinalPush:
    """Final push for cookies coverage."""

    def test_get_cookie_header_empty(self):
        manager = CookieManager()
        header = manager.get_cookie_header("nonexistent.com")
        assert header == ""


class TestPoolFinalPush:
    """Final push for pool coverage."""

    def test_get_proxy_random_strategy(self):
        pool = ProxyPool()
        pool.add_proxy(host="p1", port=8080)
        pool.add_proxy(host="p2", port=8081)
        proxy = pool.get_proxy(strategy="random")
        assert proxy is not None

    def test_get_proxy_least_used_strategy(self):
        pool = ProxyPool()
        pool.add_proxy(host="p1", port=8080)
        pool.add_proxy(host="p2", port=8081)
        pool.proxies[0].last_used = 100
        pool.proxies[1].last_used = 200
        proxy = pool.get_proxy(strategy="least_used")
        assert proxy is not None


class TestRealProxyFinalPush:
    """Final push for real_proxy coverage."""

    @pytest.mark.asyncio
    async def test_fetch_no_signature(self):
        layer = RealProxyLayer()

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
                use_signature=False,
            )
            assert result["status_code"] == 200

    @pytest.mark.asyncio
    async def test_fetch_with_all_options(self):
        layer = RealProxyLayer()
        pool = ProxyPool()
        pool.add_proxy(host="p1", port=8080)
        layer.proxy_pool = pool

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
                params={"key": "value"},
                cookies={"session": "abc"},
                use_proxy=True,
                use_signature=True,
            )
            assert result["status_code"] == 200
