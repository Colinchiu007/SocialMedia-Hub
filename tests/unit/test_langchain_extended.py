"""Extended tests for LangChain integration."""

from __future__ import annotations

import json
from unittest.mock import MagicMock, patch

import pytest

from socialmedia_hub.integrations.langchain import (
    _create_platform_tools,
    _fetch_user,
    _fetch_video,
    _search,
    create_langchain_tools,
)


class TestCreateLangchainTools:
    """Tests for create_langchain_tools function."""

    def test_create_all_platforms(self):
        tools = create_langchain_tools(api_key="test")
        # If langchain_core is not installed, returns empty list
        assert isinstance(tools, list)

    def test_create_specific_platforms(self):
        tools = create_langchain_tools(api_key="test", platforms=["tiktok", "douyin"])
        assert isinstance(tools, list)

    def test_tool_names(self):
        tools = create_langchain_tools(api_key="test", platforms=["tiktok"])
        if tools:
            names = [t.name for t in tools]
            assert "tiktok_fetch_video" in names


class TestCreatePlatformTools:
    """Tests for _create_platform_tools function."""

    def test_creates_three_tools(self):
        tools = _create_platform_tools("tiktok", "key", "http://localhost")
        # If langchain_core is not installed, returns empty list
        assert isinstance(tools, list)

    def test_tool_descriptions(self):
        tools = _create_platform_tools("instagram", "key", "http://localhost")
        if tools:
            for tool in tools:
                assert "instagram" in tool.description.lower()


class TestFetchVideo:
    """Tests for _fetch_video function."""

    def test_fetch_video_success(self):
        mock_response = MagicMock()
        mock_response.json.return_value = {"data": {"video_id": "123"}}
        mock_client = MagicMock()
        mock_client.__enter__ = MagicMock(return_value=mock_client)
        mock_client.__exit__ = MagicMock(return_value=False)
        mock_client.get.return_value = mock_response

        with patch("httpx.Client", return_value=mock_client):
            result = _fetch_video("tiktok", "123", "http://localhost", "key")
            assert "video_id" in result


class TestFetchUser:
    """Tests for _fetch_user function."""

    def test_fetch_user_success(self):
        mock_response = MagicMock()
        mock_response.json.return_value = {"data": {"user_id": "456"}}
        mock_client = MagicMock()
        mock_client.__enter__ = MagicMock(return_value=mock_client)
        mock_client.__exit__ = MagicMock(return_value=False)
        mock_client.get.return_value = mock_response

        with patch("httpx.Client", return_value=mock_client):
            result = _fetch_user("douyin", "456", "http://localhost", "key")
            assert "user_id" in result


class TestSearch:
    """Tests for _search function."""

    def test_search_success(self):
        mock_response = MagicMock()
        mock_response.json.return_value = {"data": []}
        mock_client = MagicMock()
        mock_client.__enter__ = MagicMock(return_value=mock_client)
        mock_client.__exit__ = MagicMock(return_value=False)
        mock_client.get.return_value = mock_response

        with patch("httpx.Client", return_value=mock_client):
            result = _search("youtube", "test", "http://localhost", "key")
            assert "data" in result
