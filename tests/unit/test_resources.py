"""Tests for resource base classes."""

from __future__ import annotations

from unittest.mock import MagicMock

from socialmedia_hub.resources._base import AsyncResource, SyncResource


class TestSyncResource:
    """Test SyncResource."""

    def test_stores_client(self) -> None:
        client = MagicMock()
        resource = SyncResource(client)
        assert resource._client is client


class TestAsyncResource:
    """Test AsyncResource."""

    def test_stores_client(self) -> None:
        client = MagicMock()
        resource = AsyncResource(client)
        assert resource._client is client
