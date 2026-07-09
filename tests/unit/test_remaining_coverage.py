"""Tests to improve coverage for remaining uncovered code."""

from __future__ import annotations

import asyncio
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from socialmedia_hub._base_client import AsyncBaseClient, BaseClient
from socialmedia_hub._retries import RetryPolicy
from socialmedia_hub.proxy.cookies import CookieManager
from socialmedia_hub.proxy.pool import ProxyPool
from socialmedia_hub.proxy.real_proxy import RealProxyLayer


class TestBaseClientRemaining:
    """Tests for remaining uncovered code in BaseClient."""

    def test_client_with_custom_http_client(self):
        mock_client = MagicMock()
        mock_client.is_closed = False
        client = BaseClient(api_key="test", http_client=mock_client)
        assert client._owns_client is False
        client.close()

    def test_client_close_when_not_owned(self):
        mock_client = MagicMock()
        mock_client.is_closed = False
        client = BaseClient(api_key="test", http_client=mock_client)
        client.close()
        mock_client.close.assert_not_called()

    def test_client_close_when_already_closed(self):
        mock_client = MagicMock()
        mock_client.is_closed = True
        client = BaseClient(api_key="test", http_client=mock_client)
        client.close()
        mock_client.close.assert_not_called()

    def test_client_join_full_url(self):
        client = BaseClient(api_key="test")
        assert client._join("https://example.com/api") == "https://example.com/api"
        client.close()

    def test_client_decode(self):
        client = BaseClient(api_key="test")
        mock_response = MagicMock()
        mock_response.json.return_value = {"data": "test"}
        result = client._decode(mock_response)
        assert result == {"data": "test"}
        client.close()


class TestAsyncBaseClientRemaining:
    """Tests for remaining uncovered code in AsyncBaseClient."""

    def test_async_client_with_custom_client(self):
        mock_client = MagicMock()
        mock_client.is_closed = False
        client = AsyncBaseClient(api_key="test", http_client=mock_client)
        assert client._owns_client is False

    def test_async_client_close(self):
        async def test():
            client = AsyncBaseClient(api_key="test")
            await client.aclose()
            assert client._client.is_closed

        asyncio.run(test())

    def test_async_client_context_manager(self):
        async def test():
            client = AsyncBaseClient(api_key="test")
            async with client:
                assert not client._client.is_closed
            assert client._client.is_closed

        asyncio.run(test())


class TestRetryPolicyRemaining:
    """Tests for remaining uncovered code in RetryPolicy."""

    def test_should_retry_on_connection_error(self):
        from socialmedia_hub._errors import SMHConnectionError
        policy = RetryPolicy(max_retries=3)
        error = SMHConnectionError("connection error")
        assert policy.should_retry(error, 1) is True

    def test_should_retry_on_server_error(self):
        from socialmedia_hub._errors import SMHServerError
        policy = RetryPolicy(max_retries=3)
        error = SMHServerError("server error", status_code=500, method="GET", url="/")
        assert policy.should_retry(error, 1) is True

    def test_sleep_for_connection_error(self):
        from socialmedia_hub._errors import SMHConnectionError
        policy = RetryPolicy(max_retries=3, backoff_base=1.0, jitter=0.0)
        error = SMHConnectionError("connection error")
        assert policy.sleep_for(error, 1) == 1.0
        assert policy.sleep_for(error, 2) == 2.0


class TestCookieManagerRemaining:
    """Tests for remaining uncovered code in CookieManager."""

    def test_load_cookies_from_file(self):
        import json
        import tempfile
        from pathlib import Path

        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "cookies.json"
            data = {
                "example.com": {
                    "session": {
                        "name": "session",
                        "value": "abc123",
                        "domain": "example.com",
                        "path": "/",
                        "expires": None,
                        "http_only": True,
                        "secure": True,
                        "created_at": 1234567890.0,
                    }
                }
            }
            path.write_text(json.dumps(data))

            manager = CookieManager(storage_path=path)
            assert "example.com" in manager.cookies

    def test_load_cookies_error(self):
        import tempfile
        from pathlib import Path

        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "cookies.json"
            path.write_text("invalid json")

            manager = CookieManager(storage_path=path)
            assert len(manager.cookies) == 0


class TestProxyPoolRemaining:
    """Tests for remaining uncovered code in ProxyPool."""

    def test_add_proxies_bulk(self):
        pool = ProxyPool()
        pool.add_proxies([
            {"host": "p1", "port": 8080},
            {"host": "p2", "port": 8081},
        ])
        assert len(pool.proxies) == 2

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


class TestRealProxyLayerRemaining:
    """Tests for remaining uncovered code in RealProxyLayer."""

    def test_rate_control_first_request(self):
        async def test():
            layer = RealProxyLayer()
            await layer._rate_control("platform1")
            assert "platform1" in layer._request_times
            assert len(layer._request_times["platform1"]) == 1

        asyncio.run(test())

    def test_rate_control_multiple_requests(self):
        async def test():
            layer = RealProxyLayer()
            for _ in range(5):
                await layer._rate_control("platform1")
            assert len(layer._request_times["platform1"]) == 5

        asyncio.run(test())

    def test_rate_control_cleans_old_timestamps(self):
        async def test():
            layer = RealProxyLayer()
            layer._request_times["platform1"] = [1.0, 2.0, 3.0]
            await layer._rate_control("platform1")
            # Old timestamps should be cleaned

        asyncio.run(test())
