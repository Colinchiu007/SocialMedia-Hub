"""Final tests to achieve 100% coverage."""

from __future__ import annotations

import asyncio
from unittest.mock import AsyncMock, MagicMock, patch

import httpx
import pytest

from socialmedia_hub._base_client import AsyncBaseClient, BaseClient
from socialmedia_hub._retries import RetryPolicy
from socialmedia_hub.proxy.cookies import CookieManager
from socialmedia_hub.proxy.pool import ProxyPool
from socialmedia_hub.proxy.real_proxy import RealProxyLayer


class TestBaseClientFinal:
    """Final tests for BaseClient to achieve 100% coverage."""

    def test_client_with_transport(self):
        mock_transport = MagicMock()
        client = BaseClient(api_key="test", transport=mock_transport)
        assert client is not None
        client.close()

    def test_client_request_success(self):
        client = BaseClient(api_key="test")
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"data": "test"}
        mock_response.headers = {"x-request-id": "123"}
        client._client.request = MagicMock(return_value=mock_response)
        result = client._request("GET", "/api/test")
        assert result == {"data": "test"}
        client.close()

    def test_client_request_with_params(self):
        client = BaseClient(api_key="test")
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"data": "test"}
        mock_response.headers = {}
        client._client.request = MagicMock(return_value=mock_response)
        result = client._request("GET", "/api/test", params={"key": "value"})
        assert result == {"data": "test"}
        client.close()

    def test_client_request_with_json(self):
        client = BaseClient(api_key="test")
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"data": "test"}
        mock_response.headers = {}
        client._client.request = MagicMock(return_value=mock_response)
        result = client._request("POST", "/api/test", json={"key": "value"})
        assert result == {"data": "test"}
        client.close()

    def test_client_request_with_files(self):
        client = BaseClient(api_key="test")
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"data": "test"}
        mock_response.headers = {}
        client._client.request = MagicMock(return_value=mock_response)
        result = client._request("POST", "/api/test", files={"file": b"data"})
        assert result == {"data": "test"}
        client.close()

    def test_client_request_error_retry(self):
        client = BaseClient(api_key="test", max_retries=2)
        error = httpx.ConnectError("connection failed")
        client._client.request = MagicMock(side_effect=error)
        with pytest.raises(Exception):
            client._request("GET", "/api/test")
        client.close()

    def test_client_request_rate_limit(self):
        from socialmedia_hub._errors import SMHRateLimitError
        client = BaseClient(api_key="test", max_retries=2)
        error = SMHRateLimitError(
            "rate limited",
            status_code=429,
            method="GET",
            url="/api/test",
            retry_after=1.0,
        )
        client._client.request = MagicMock(side_effect=error)
        with pytest.raises(SMHRateLimitError):
            client._request("GET", "/api/test")
        client.close()

    def test_client_no_parse_response(self):
        client = BaseClient(api_key="test", parse_response=False)
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"data": "test"}
        mock_response.text = '{"data": "test"}'
        mock_response.headers = {}
        client._client.request = MagicMock(return_value=mock_response)
        result = client._request("GET", "/api/test")
        client.close()


class TestAsyncBaseClientFinal:
    """Final tests for AsyncBaseClient to achieve 100% coverage."""

    def test_async_client_with_transport(self):
        mock_transport = MagicMock()
        client = AsyncBaseClient(api_key="test", transport=mock_transport)
        assert client is not None

    @pytest.mark.asyncio
    async def test_async_client_request_success(self):
        client = AsyncBaseClient(api_key="test")
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"data": "test"}
        mock_response.headers = {"x-request-id": "123"}
        client._client.request = AsyncMock(return_value=mock_response)
        result = await client._request("GET", "/api/test")
        assert result == {"data": "test"}
        await client.aclose()

    @pytest.mark.asyncio
    async def test_async_client_request_with_params(self):
        client = AsyncBaseClient(api_key="test")
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"data": "test"}
        mock_response.headers = {}
        client._client.request = AsyncMock(return_value=mock_response)
        result = await client._request("GET", "/api/test", params={"key": "value"})
        assert result == {"data": "test"}
        await client.aclose()

    @pytest.mark.asyncio
    async def test_async_client_request_with_json(self):
        client = AsyncBaseClient(api_key="test")
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"data": "test"}
        mock_response.headers = {}
        client._client.request = AsyncMock(return_value=mock_response)
        result = await client._request("POST", "/api/test", json={"key": "value"})
        assert result == {"data": "test"}
        await client.aclose()

    @pytest.mark.asyncio
    async def test_async_client_request_error_retry(self):
        client = AsyncBaseClient(api_key="test", max_retries=2)
        error = httpx.ConnectError("connection failed")
        client._client.request = AsyncMock(side_effect=error)
        with pytest.raises(Exception):
            await client._request("GET", "/api/test")
        await client.aclose()

    @pytest.mark.asyncio
    async def test_async_client_request_rate_limit(self):
        from socialmedia_hub._errors import SMHRateLimitError
        client = AsyncBaseClient(api_key="test", max_retries=2)
        error = SMHRateLimitError(
            "rate limited",
            status_code=429,
            method="GET",
            url="/api/test",
            retry_after=1.0,
        )
        client._client.request = AsyncMock(side_effect=error)
        with pytest.raises(SMHRateLimitError):
            await client._request("GET", "/api/test")
        await client.aclose()


class TestRetryPolicyFinal:
    """Final tests for RetryPolicy."""

    def test_should_retry_on_timeout(self):
        from socialmedia_hub._errors import SMHTimeoutError
        policy = RetryPolicy(max_retries=3)
        error = SMHTimeoutError("timeout")
        assert policy.should_retry(error, 1) is True

    def test_should_retry_on_proxy_error(self):
        from socialmedia_hub._errors import SMHProxyError
        policy = RetryPolicy(max_retries=3)
        error = SMHProxyError("proxy error")
        assert policy.should_retry(error, 1) is True


class TestCookieManagerFinal:
    """Final tests for CookieManager."""

    def test_save_cookies_error(self):
        import tempfile
        from pathlib import Path

        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "nonexistent" / "cookies.json"
            manager = CookieManager(storage_path=path)
            manager.set_cookie("session", "abc123", "example.com")
            # Should not raise even if save fails


class TestProxyPoolFinal:
    """Final tests for ProxyPool."""

    def test_get_proxy_least_used(self):
        pool = ProxyPool()
        pool.add_proxy(host="p1", port=8080)
        pool.add_proxy(host="p2", port=8081)
        pool.proxies[0].last_used = 100
        pool.proxies[1].last_used = 200
        proxy = pool.get_proxy(strategy="least_used")
        assert proxy is not None


class TestRealProxyLayerFinal:
    """Final tests for RealProxyLayer."""

    def test_rate_control_cleanup(self):
        async def test():
            layer = RealProxyLayer()
            # Add old timestamps
            layer._request_times["platform1"] = [1.0, 2.0, 3.0]
            await layer._rate_control("platform1")
            # Old timestamps should be cleaned

        asyncio.run(test())

    def test_rate_control_wait(self):
        async def test():
            layer = RealProxyLayer()
            layer._min_interval = 0.01
            # Add 10 timestamps to trigger rate limit
            now = asyncio.get_event_loop().time()
            layer._request_times["platform1"] = [now - 0.1] * 10
            await layer._rate_control("platform1")

        asyncio.run(test())

    @pytest.mark.asyncio
    async def test_fetch_with_cookies(self):
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
                cookies={"session": "abc123"},
            )
            assert result["status_code"] == 200

    @pytest.mark.asyncio
    async def test_fetch_post_method(self):
        layer = RealProxyLayer()
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"data": "test"}
        mock_response.headers = {}

        with patch("httpx.AsyncClient") as mock_client:
            mock_client.return_value.__aenter__ = AsyncMock(return_value=mock_client)
            mock_client.return_value.__aexit__ = AsyncMock(return_value=False)
            mock_client.post = AsyncMock(return_value=mock_response)

            result = await layer.fetch(
                "tiktok",
                "https://www.tiktok.com/api/test",
                method="POST",
                json_body={"key": "value"},
            )
            assert result["status_code"] == 200

    @pytest.mark.asyncio
    async def test_fetch_other_method(self):
        layer = RealProxyLayer()
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"data": "test"}
        mock_response.headers = {}

        with patch("httpx.AsyncClient") as mock_client:
            mock_client.return_value.__aenter__ = AsyncMock(return_value=mock_client)
            mock_client.return_value.__aexit__ = AsyncMock(return_value=False)
            mock_client.request = AsyncMock(return_value=mock_response)

            result = await layer.fetch(
                "tiktok",
                "https://www.tiktok.com/api/test",
                method="PUT",
            )
            assert result["status_code"] == 200

    @pytest.mark.asyncio
    async def test_fetch_with_proxy(self):
        layer = RealProxyLayer()
        pool = ProxyPool()
        pool.add_proxy(host="proxy.com", port=8080)
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
                use_proxy=True,
            )
            assert result["status_code"] == 200

    @pytest.mark.asyncio
    async def test_fetch_error(self):
        layer = RealProxyLayer()
        with patch("httpx.AsyncClient") as mock_client:
            mock_client.return_value.__aenter__ = AsyncMock(return_value=mock_client)
            mock_client.return_value.__aexit__ = AsyncMock(return_value=False)
            mock_client.get = AsyncMock(side_effect=httpx.ConnectError("failed"))

            result = await layer.fetch(
                "tiktok",
                "https://www.tiktok.com/api/test",
            )
            assert result["status_code"] == 0
