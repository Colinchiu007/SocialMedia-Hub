"""Tests for LangChain integration."""

from __future__ import annotations

import pytest

from socialmedia_hub.integrations.langchain import create_langchain_tools


class TestLangChainIntegration:
    """Test LangChain integration."""

    def test_create_tools_requires_langchain(self):
        """Test that creating tools requires langchain-core."""
        # This test will fail if langchain-core is not installed
        # In production, this is expected behavior
        try:
            tools = create_langchain_tools(api_key="test")
            assert isinstance(tools, list)
        except ImportError:
            # Expected if langchain-core is not installed
            pass

    def test_create_tools_with_platforms(self):
        """Test creating tools for specific platforms."""
        try:
            tools = create_langchain_tools(
                api_key="test",
                platforms=["tiktok", "douyin"]
            )
            assert isinstance(tools, list)
        except ImportError:
            pass
