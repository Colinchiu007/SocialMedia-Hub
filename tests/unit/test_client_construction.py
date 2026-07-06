"""Tests for client construction."""

from __future__ import annotations

import os
from unittest.mock import patch

import pytest

from socialmedia_hub._base_client import AsyncBaseClient, BaseClient
from socialmedia_hub._errors import SMHConfigError


class TestBaseClientConstruction:
    """Test BaseClient initialization."""

    def test_explicit_api_key(self) -> None:
        client = BaseClient(api_key="test-key-123")
        assert client._api_key == "test-key-123"
        client.close()

    def test_api_key_from_env(self) -> None:
        with patch.dict(os.environ, {"SMH_API_KEY": "env-key-456"}):
            client = BaseClient()
            assert client._api_key == "env-key-456"
            client.close()

    def test_missing_api_key_raises(self) -> None:
        with patch.dict(os.environ, {}, clear=True):
            with pytest.raises(SMHConfigError, match="No API key"):
                BaseClient()

    def test_explicit_overrides_env(self) -> None:
        with patch.dict(os.environ, {"SMH_API_KEY": "env-key"}):
            client = BaseClient(api_key="explicit-key")
            assert client._api_key == "explicit-key"
            client.close()

    def test_base_url_default(self) -> None:
        client = BaseClient(api_key="test")
        assert client._base_url == "http://127.0.0.1:8000"
        client.close()

    def test_base_url_override_strips_trailing_slash(self) -> None:
        client = BaseClient(api_key="test", base_url="http://example.com/")
        assert client._base_url == "http://example.com"
        client.close()

    def test_context_manager_closes_client(self) -> None:
        with BaseClient(api_key="test") as client:
            assert not client._client.is_closed
        assert client._client.is_closed

    def test_repr_does_not_leak_key(self) -> None:
        client = BaseClient(api_key="secret-key-123")
        assert "secret-key" not in repr(client)
        client.close()


class TestAsyncBaseClientConstruction:
    """Test AsyncBaseClient initialization."""

    def test_explicit_api_key(self) -> None:
        client = AsyncBaseClient(api_key="test-key-123")
        assert client._api_key == "test-key-123"

    def test_async_repr_does_not_leak_key(self) -> None:
        client = AsyncBaseClient(api_key="secret-key-123")
        assert "secret-key" not in repr(client)
