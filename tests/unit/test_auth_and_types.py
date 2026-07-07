"""Tests for auth, types, and rate_limit modules."""

from __future__ import annotations

import os
from unittest.mock import patch

import pytest

from socialmedia_hub._auth import resolve_api_key
from socialmedia_hub._rate_limit import parse_retry_after
from socialmedia_hub._types import JSON, Headers, Params


class TestResolveApiKey:
    """Tests for resolve_api_key function."""

    def test_explicit_key_returned(self) -> None:
        assert resolve_api_key("my-key") == "my-key"

    def test_explicit_key_takes_precedence(self) -> None:
        with patch.dict(os.environ, {"SMH_API_KEY": "env-key"}):
            assert resolve_api_key("explicit") == "explicit"

    def test_smh_api_key_env(self) -> None:
        with patch.dict(os.environ, {"SMH_API_KEY": "smh-key"}, clear=False):
            os.environ.pop("SOCIALMEDIA_HUB_API_KEY", None)
            assert resolve_api_key() == "smh-key"

    def test_socialmedia_hub_api_key_env(self) -> None:
        with patch.dict(os.environ, {"SOCIALMEDIA_HUB_API_KEY": "smh-key2"}, clear=False):
            os.environ.pop("SMH_API_KEY", None)
            assert resolve_api_key() == "smh-key2"

    def test_no_key_raises(self) -> None:
        with patch.dict(os.environ, {}, clear=True):
            with pytest.raises(ValueError, match="No API key"):
                resolve_api_key()

    def test_smh_takes_precedence_over_socialmedia(self) -> None:
        with patch.dict(os.environ, {"SMH_API_KEY": "a", "SOCIALMEDIA_HUB_API_KEY": "b"}):
            assert resolve_api_key() == "a"


class TestParseRetryAfter:
    """Tests for parse_retry_after function."""

    def test_returns_none_when_missing(self) -> None:
        assert parse_retry_after({}) is None

    def test_returns_none_for_unknown_header(self) -> None:
        assert parse_retry_after({"X-Custom": "10"}) is None

    def test_parses_integer_seconds(self) -> None:
        assert parse_retry_after({"Retry-After": "30"}) == 30.0

    def test_parses_lowercase_header(self) -> None:
        assert parse_retry_after({"retry-after": "45"}) == 45.0

    def test_parses_float_seconds(self) -> None:
        assert parse_retry_after({"Retry-After": "1.5"}) == 1.5

    def test_returns_none_for_non_numeric(self) -> None:
        assert parse_retry_after({"Retry-After": "Wed, 21 Oct 2015 07:28:00 GMT"}) is None

    def test_retry_after_takes_precedence(self) -> None:
        assert parse_retry_after({"retry-after": "10", "Retry-After": "20"}) == 10.0


class TestTypeAliases:
    """Tests for type aliases."""

    def test_json_type(self) -> None:
        data: JSON = {"key": "value"}
        assert data["key"] == "value"

    def test_headers_type(self) -> None:
        headers: Headers = {"Content-Type": "application/json"}
        assert headers["Content-Type"] == "application/json"

    def test_params_type(self) -> None:
        params: Params = {"q": "test", "limit": 10, "offset": 0.5, "flag": True}
        assert params["q"] == "test"
        assert params["limit"] == 10
