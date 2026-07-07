"""Extended tests for WebSocket manager and endpoints."""

from __future__ import annotations

import json
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from fastapi import WebSocketDisconnect

from socialmedia_hub.websocket.manager import ConnectionManager


class TestConnectionManagerExtended:
    """Extended tests for ConnectionManager."""

    @pytest.fixture
    def manager(self) -> ConnectionManager:
        return ConnectionManager()

    @pytest.mark.asyncio
    async def test_connect(self, manager: ConnectionManager) -> None:
        ws = AsyncMock()
        await manager.connect(ws, "client1")
        assert "client1" in manager.active_connections
        ws.accept.assert_called_once()

    def test_disconnect(self, manager: ConnectionManager) -> None:
        manager.active_connections["client1"] = MagicMock()
        manager.disconnect("client1")
        assert "client1" not in manager.active_connections

    def test_disconnect_nonexistent(self, manager: ConnectionManager) -> None:
        manager.disconnect("nonexistent")
        assert len(manager.active_connections) == 0

    @pytest.mark.asyncio
    async def test_send_personal_message(self, manager: ConnectionManager) -> None:
        ws = AsyncMock()
        manager.active_connections["client1"] = ws
        await manager.send_personal_message({"type": "test"}, "client1")
        ws.send_json.assert_called_once_with({"type": "test"})

    @pytest.mark.asyncio
    async def test_send_personal_message_nonexistent(self, manager: ConnectionManager) -> None:
        await manager.send_personal_message({"type": "test"}, "nonexistent")

    @pytest.mark.asyncio
    async def test_send_personal_message_disconnect(self, manager: ConnectionManager) -> None:
        ws = AsyncMock()
        ws.send_json.side_effect = WebSocketDisconnect()
        manager.active_connections["client1"] = ws
        await manager.send_personal_message({"type": "test"}, "client1")
        assert "client1" not in manager.active_connections

    @pytest.mark.asyncio
    async def test_broadcast(self, manager: ConnectionManager) -> None:
        ws1 = AsyncMock()
        ws2 = AsyncMock()
        manager.active_connections["client1"] = ws1
        manager.active_connections["client2"] = ws2
        await manager.broadcast({"type": "broadcast"})
        ws1.send_json.assert_called_once()
        ws2.send_json.assert_called_once()

    @pytest.mark.asyncio
    async def test_broadcast_with_disconnect(self, manager: ConnectionManager) -> None:
        ws1 = AsyncMock()
        ws2 = AsyncMock()
        ws1.send_json.side_effect = WebSocketDisconnect()
        manager.active_connections["client1"] = ws1
        manager.active_connections["client2"] = ws2
        await manager.broadcast({"type": "broadcast"})
        assert "client1" not in manager.active_connections
        assert "client2" in manager.active_connections

    @pytest.mark.asyncio
    async def test_subscribe(self, manager: ConnectionManager) -> None:
        await manager.subscribe("client1", "channel1")
        assert "channel1" in manager.subscriptions
        assert "client1" in manager.subscriptions["channel1"]

    @pytest.mark.asyncio
    async def test_subscribe_multiple(self, manager: ConnectionManager) -> None:
        await manager.subscribe("client1", "channel1")
        await manager.subscribe("client2", "channel1")
        assert len(manager.subscriptions["channel1"]) == 2

    @pytest.mark.asyncio
    async def test_unsubscribe(self, manager: ConnectionManager) -> None:
        await manager.subscribe("client1", "channel1")
        await manager.unsubscribe("client1", "channel1")
        assert "client1" not in manager.subscriptions.get("channel1", set())

    @pytest.mark.asyncio
    async def test_unsubscribe_nonexistent_channel(self, manager: ConnectionManager) -> None:
        await manager.unsubscribe("client1", "nonexistent")

    @pytest.mark.asyncio
    async def test_broadcast_to_channel(self, manager: ConnectionManager) -> None:
        ws1 = AsyncMock()
        ws2 = AsyncMock()
        manager.active_connections["client1"] = ws1
        manager.active_connections["client2"] = ws2
        await manager.subscribe("client1", "channel1")
        await manager.subscribe("client2", "channel1")
        await manager.broadcast_to_channel("channel1", {"type": "channel_msg"})
        ws1.send_json.assert_called_once()
        ws2.send_json.assert_called_once()

    @pytest.mark.asyncio
    async def test_broadcast_to_channel_nonexistent(self, manager: ConnectionManager) -> None:
        await manager.broadcast_to_channel("nonexistent", {"type": "test"})

    @pytest.mark.asyncio
    async def test_broadcast_to_channel_with_disconnect(self, manager: ConnectionManager) -> None:
        ws1 = AsyncMock()
        ws2 = AsyncMock()
        ws1.send_json.side_effect = WebSocketDisconnect()
        manager.active_connections["client1"] = ws1
        manager.active_connections["client2"] = ws2
        await manager.subscribe("client1", "channel1")
        await manager.subscribe("client2", "channel1")
        await manager.broadcast_to_channel("channel1", {"type": "test"})
        assert "client1" not in manager.active_connections

    @pytest.mark.asyncio
    async def test_broadcast_to_channel_partial_connections(self, manager: ConnectionManager) -> None:
        ws2 = AsyncMock()
        manager.active_connections["client2"] = ws2
        await manager.subscribe("client1", "channel1")
        await manager.subscribe("client2", "channel1")
        await manager.broadcast_to_channel("channel1", {"type": "test"})
        ws2.send_json.assert_called_once()

    def test_get_connection_count(self, manager: ConnectionManager) -> None:
        assert manager.get_connection_count() == 0
        manager.active_connections["c1"] = MagicMock()
        manager.active_connections["c2"] = MagicMock()
        assert manager.get_connection_count() == 2

    def test_get_subscription_count(self, manager: ConnectionManager) -> None:
        manager.subscriptions["ch1"] = {"c1", "c2"}
        manager.subscriptions["ch2"] = {"c3"}
        counts = manager.get_subscription_count()
        assert counts == {"ch1": 2, "ch2": 1}

    def test_disconnect_removes_from_subscriptions(self, manager: ConnectionManager) -> None:
        manager.active_connections["client1"] = MagicMock()
        manager.subscriptions["ch1"] = {"client1", "client2"}
        manager.subscriptions["ch2"] = {"client1"}
        manager.disconnect("client1")
        assert "client1" not in manager.subscriptions["ch1"]
        assert "client1" not in manager.subscriptions["ch2"]
        assert "client2" in manager.subscriptions["ch1"]
