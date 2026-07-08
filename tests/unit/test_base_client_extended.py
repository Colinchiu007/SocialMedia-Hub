"""Extended tests for base client module."""

from __future__ import annotations

from unittest.mock import MagicMock, patch

import httpx
import pytest

from socialmedia_hub._base_client import (
    AsyncBaseClient,
    BaseClient,
    _build_user_agent,
    _format_error_message,
    _raise_for_status,
    _resolve_api_key,
    _resolve_base_url,
    _safe_json,
)
from socialmedia_hub._errors import (
    SMHConfigError,
    SMHHTTPError,
    SMHRateLimitError,
)


class TestResolveApiKey:
    """Tests for _resolve_api_key function."""

    def test_explicit_key(self):
        assert _resolve_api_key("my-key") == "my-key"

    def test_env_key(self):
        with patch.dict("os.environ", {"SMH_API_KEY": "env-key"}):
            assert _resolve_api_key(None) == "env-key"

    def test_missing_key(self):
        with patch.dict("os.environ", {}, clear=True):
            with pytest.raises(SMHConfigError):
                _resolve_api_key(None)


class TestResolveBaseUrl:
    """Tests for _resolve_base_url function."""

    def test_explicit_url(self):
        assert _resolve_base_url("http://custom:9000") == "http://custom:9000"

    def test_default_url(self):
        assert _resolve_base_url(None) == "http://127.0.0.1:8000"

    def test_strips_trailing_slash(self):
        assert _resolve_base_url("http://custom:9000/") == "http://custom:9000"


class TestBuildUserAgent:
    """Tests for _build_user_agent function."""

    def test_explicit_agent(self):
        assert _build_user_agent("Custom/1.0") == "Custom/1.0"

    def test_default_agent(self):
        from socialmedia_hub._version import __version__
        assert __version__ in _build_user_agent(None)


class TestSafeJson:
    """Tests for _safe_json function."""

    def test_valid_json(self):
        response = MagicMock(spec=httpx.Response)
        response.json.return_value = {"key": "value"}
        assert _safe_json(response) == {"key": "value"}

    def test_invalid_json(self):
        response = MagicMock(spec=httpx.Response)
        response.json.side_effect = ValueError("invalid")
        response.text = "raw text"
        assert _safe_json(response) == "raw text"


class TestFormatErrorMessage:
    """Tests for _format_error_message function."""

    def test_dict_with_message(self):
        response = MagicMock(spec=httpx.Response)
        response.status_code = 404
        assert _format_error_message(response, {"message": "Not found"}) == "Not found"

    def test_dict_with_error(self):
        response = MagicMock(spec=httpx.Response)
        response.status_code = 400
        assert _format_error_message(response, {"error": "Bad"}) == "Bad"

    def test_string_body(self):
        response = MagicMock(spec=httpx.Response)
        response.status_code = 500
        assert _format_error_message(response, "Server error") == "Server error"

    def test_empty_dict(self):
        response = MagicMock(spec=httpx.Response)
        response.status_code = 404
        assert "404" in _format_error_message(response, {})


class TestRaiseForStatus:
    """Tests for _raise_for_status function."""

    def test_success_status(self):
        response = MagicMock(spec=httpx.Response)
        response.status_code = 200
        _raise_for_status(response, method="GET", url="/api", params=None, request_body=None)

    def test_400_error(self):
        response = MagicMock(spec=httpx.Response)
        response.status_code = 400
        response.json.return_value = {"message": "bad request"}
        response.headers = {}
        with pytest.raises(SMHHTTPError):
            _raise_for_status(response, method="GET", url="/api", params=None, request_body=None)

    def test_401_error(self):
        response = MagicMock(spec=httpx.Response)
        response.status_code = 401
        response.json.return_value = {"message": "unauthorized"}
        response.headers = {}
        with pytest.raises(SMHHTTPError):
            _raise_for_status(response, method="GET", url="/api", params=None, request_body=None)

    def test_429_rate_limit(self):
        response = MagicMock(spec=httpx.Response)
        response.status_code = 429
        response.json.return_value = {"message": "rate limited"}
        response.headers = {"Retry-After": "60"}
        with pytest.raises(SMHRateLimitError):
            _raise_for_status(response, method="GET", url="/api", params=None, request_body=None)


class TestBaseClientExtended:
    """Extended tests for BaseClient."""

    def test_client_with_custom_timeout(self):
        client = BaseClient(api_key="test", timeout=60.0)
        assert client._client.timeout.connect == 60.0
        client.close()

    def test_client_with_proxy(self):
        client = BaseClient(api_key="test", proxy="http://proxy:8080")
        assert client is not None
        client.close()

    def test_client_close(self):
        client = BaseClient(api_key="test")
        client.close()
        assert client._client.is_closed

    def test_client_context_manager(self):
        with BaseClient(api_key="test") as client:
            assert not client._client.is_closed
        assert client._client.is_closed

    def test_client_join_absolute_url(self):
        client = BaseClient(api_key="test")
        assert client._join("http://example.com/api") == "http://example.com/api"
        client.close()

    def test_client_join_relative_url(self):
        client = BaseClient(api_key="test")
        assert client._join("/api/test") == "http://127.0.0.1:8000/api/test"
        client.close()

    def test_client_join_no_slash(self):
        client = BaseClient(api_key="test")
        assert client._join("api/test") == "http://127.0.0.1:8000/api/test"
        client.close()

    def test_client_http_client_and_transport_error(self):
        with pytest.raises(SMHConfigError):
            BaseClient(api_key="test", http_client=MagicMock(), transport=MagicMock())

    def test_client_with_custom_client(self):
        mock_client = MagicMock(spec=httpx.Client)
        client = BaseClient(api_key="test", http_client=mock_client)
        assert client._client is mock_client
        assert not client._owns_client


class TestAsyncBaseClientExtended:
    """Extended tests for AsyncBaseClient."""

    def test_async_client_with_custom_timeout(self):
        client = AsyncBaseClient(api_key="test", timeout=60.0)
        assert client._client.timeout.connect == 60.0

    def test_async_client_with_proxy(self):
        client = AsyncBaseClient(api_key="test", proxy="http://proxy:8080")
        assert client is not None

    def test_async_client_http_client_and_transport_error(self):
        with pytest.raises(SMHConfigError):
            AsyncBaseClient(api_key="test", http_client=MagicMock(), transport=MagicMock())

    def test_async_client_with_custom_client(self):
        mock_client = MagicMock(spec=httpx.AsyncClient)
        client = AsyncBaseClient(api_key="test", http_client=mock_client)
        assert client._client is mock_client
        assert not client._owns_client

    def test_async_client_context_manager(self):
        async def test():
            async with AsyncBaseClient(api_key="test") as client:
                assert not client._client.is_closed
            assert client._client.is_closed

        import asyncio
        asyncio.run(test())
