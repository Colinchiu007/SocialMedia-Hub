"""Tests for WebSocket functionality."""

from __future__ import annotations

import pytest
from fastapi.testclient import TestClient

from socialmedia_hub.server.main import app
from socialmedia_hub.websocket.manager import ConnectionManager, manager


@pytest.fixture(autouse=True)
def reset_global_manager():
    """Reset global manager state before each test."""
    manager.active_connections.clear()
    manager.subscriptions.clear()
    yield
    manager.active_connections.clear()
    manager.subscriptions.clear()


@pytest.fixture
def client():
    """Create test client."""
    return TestClient(app)


class TestWebSocketManager:
    """Test WebSocket connection manager."""

    def test_manager_initialization(self):
        """Test manager initialization."""
        mgr = ConnectionManager()
        assert mgr.get_connection_count() == 0
        assert mgr.get_subscription_count() == {}

    def test_manager_subscribe(self):
        """Test channel subscription."""
        mgr = ConnectionManager()
        import asyncio

        async def test():
            await mgr.subscribe("client1", "channel1")
            assert "channel1" in mgr.subscriptions
            assert "client1" in mgr.subscriptions["channel1"]

        asyncio.run(test())

    def test_manager_unsubscribe(self):
        """Test channel unsubscription."""
        mgr = ConnectionManager()
        import asyncio

        async def test():
            await mgr.subscribe("client1", "channel1")
            await mgr.unsubscribe("client1", "channel1")
            assert "channel1" in mgr.subscriptions
            assert "client1" not in mgr.subscriptions["channel1"]

        asyncio.run(test())

    def test_manager_connection_count(self):
        """Test connection count."""
        mgr = ConnectionManager()
        assert mgr.get_connection_count() == 0


class TestWebSocketEndpoints:
    """Test WebSocket endpoints."""

    def test_websocket_route_exists(self, client):
        """Test that WebSocket routes are registered."""
        # Check that the WebSocket routes exist in the app
        routes = [route.path for route in app.routes if hasattr(route, "path")]
        assert "/ws/live/{platform}/{room_id}" in routes or any("/ws/" in r for r in routes)

    def test_websocket_manager_global(self):
        """Test that global manager exists."""
        from socialmedia_hub.websocket import manager
        assert manager is not None
        assert isinstance(manager, ConnectionManager)


class TestWebSocketIntegration:
    """Test WebSocket integration."""

    def test_manager_broadcast(self):
        """Test broadcast functionality."""
        mgr = ConnectionManager()
        # Test broadcast to empty channel - should not raise
        import asyncio
        asyncio.run(mgr.broadcast_to_channel("empty_channel", {"type": "test"}))

    def test_manager_subscription_count(self):
        """Test subscription count."""
        mgr = ConnectionManager()
        import asyncio

        async def setup():
            await mgr.subscribe("client1", "channel1")
            await mgr.subscribe("client2", "channel1")
            await mgr.subscribe("client1", "channel2")

        asyncio.run(setup())

        counts = mgr.get_subscription_count()
        assert counts["channel1"] == 2
        assert counts["channel2"] == 1
