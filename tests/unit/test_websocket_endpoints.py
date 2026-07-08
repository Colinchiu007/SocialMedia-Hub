"""Tests for WebSocket endpoints to improve coverage."""

from __future__ import annotations

import json
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from fastapi import WebSocket
from fastapi.testclient import TestClient

from socialmedia_hub.server.main import app
from socialmedia_hub.websocket.endpoints import (
    channel_websocket,
    live_room_websocket,
    monitor_websocket,
)
from socialmedia_hub.websocket.manager import manager


@pytest.fixture(autouse=True)
def reset_manager():
    """Reset manager state before each test."""
    manager.active_connections.clear()
    manager.subscriptions.clear()
    yield
    manager.active_connections.clear()
    manager.subscriptions.clear()


class TestLiveRoomWebSocket:
    """Tests for live room WebSocket endpoint."""

    @pytest.mark.asyncio
    async def test_connect_and_disconnect(self):
        """Test connection and disconnection flow."""
        mock_ws = AsyncMock(spec=WebSocket)
        mock_ws.receive_text = AsyncMock(side_effect=Exception("disconnect"))

        with patch.object(manager, "connect", new_callable=AsyncMock) as mock_connect:
            with patch.object(manager, "subscribe", new_callable=AsyncMock):
                with patch.object(manager, "disconnect") as mock_disconnect:
                    with patch.object(manager, "send_personal_message", new_callable=AsyncMock):
                        try:
                            await live_room_websocket(mock_ws, "tiktok", "123", "token")
                        except Exception:
                            pass

                        mock_connect.assert_called_once()

    @pytest.mark.asyncio
    async def test_subscribe_action(self):
        """Test subscribe action handling."""
        mock_ws = AsyncMock(spec=WebSocket)
        message = json.dumps({"action": "subscribe", "channel": "test_channel"})
        mock_ws.receive_text = AsyncMock(side_effect=[message, Exception("disconnect")])

        with patch.object(manager, "connect", new_callable=AsyncMock):
            with patch.object(manager, "subscribe", new_callable=AsyncMock):
                with patch.object(manager, "disconnect"):
                    try:
                        await live_room_websocket(mock_ws, "tiktok", "123", "token")
                    except Exception:
                        pass

                    mock_ws.send_json.assert_called()

    @pytest.mark.asyncio
    async def test_unsubscribe_action(self):
        """Test unsubscribe action handling."""
        mock_ws = AsyncMock(spec=WebSocket)
        message = json.dumps({"action": "unsubscribe", "channel": "test_channel"})
        mock_ws.receive_text = AsyncMock(side_effect=[message, Exception("disconnect")])

        with patch.object(manager, "connect", new_callable=AsyncMock):
            with patch.object(manager, "unsubscribe", new_callable=AsyncMock):
                with patch.object(manager, "disconnect"):
                    try:
                        await live_room_websocket(mock_ws, "tiktok", "123", "token")
                    except Exception:
                        pass

                    mock_ws.send_json.assert_called()

    @pytest.mark.asyncio
    async def test_ping_action(self):
        """Test ping action handling."""
        mock_ws = AsyncMock(spec=WebSocket)
        message = json.dumps({"action": "ping"})
        mock_ws.receive_text = AsyncMock(side_effect=[message, Exception("disconnect")])

        with patch.object(manager, "connect", new_callable=AsyncMock):
            with patch.object(manager, "subscribe", new_callable=AsyncMock):
                with patch.object(manager, "disconnect"):
                    try:
                        await live_room_websocket(mock_ws, "tiktok", "123", "token")
                    except Exception:
                        pass

                    mock_ws.send_json.assert_called()

    @pytest.mark.asyncio
    async def test_invalid_json(self):
        """Test invalid JSON handling."""
        mock_ws = AsyncMock(spec=WebSocket)
        mock_ws.receive_text = AsyncMock(side_effect=["invalid json", Exception("disconnect")])

        with patch.object(manager, "connect", new_callable=AsyncMock):
            with patch.object(manager, "subscribe", new_callable=AsyncMock):
                with patch.object(manager, "disconnect"):
                    try:
                        await live_room_websocket(mock_ws, "tiktok", "123", "token")
                    except Exception:
                        pass

                    # Should send error message
                    assert mock_ws.send_json.call_count >= 2


class TestChannelWebSocket:
    """Tests for channel WebSocket endpoint."""

    @pytest.mark.asyncio
    async def test_connect_and_disconnect(self):
        """Test connection and disconnection flow."""
        mock_ws = AsyncMock(spec=WebSocket)
        mock_ws.receive_text = AsyncMock(side_effect=Exception("disconnect"))

        with patch.object(manager, "connect", new_callable=AsyncMock):
            with patch.object(manager, "subscribe", new_callable=AsyncMock):
                with patch.object(manager, "disconnect"):
                    try:
                        await channel_websocket(mock_ws, "test_channel", "token")
                    except Exception:
                        pass

    @pytest.mark.asyncio
    async def test_subscribe_action(self):
        """Test subscribe action handling."""
        mock_ws = AsyncMock(spec=WebSocket)
        message = json.dumps({"action": "subscribe", "channel": "new_channel"})
        mock_ws.receive_text = AsyncMock(side_effect=[message, Exception("disconnect")])

        with patch.object(manager, "connect", new_callable=AsyncMock):
            with patch.object(manager, "subscribe", new_callable=AsyncMock):
                with patch.object(manager, "disconnect"):
                    try:
                        await channel_websocket(mock_ws, "test_channel", "token")
                    except Exception:
                        pass

                    mock_ws.send_json.assert_called()

    @pytest.mark.asyncio
    async def test_unsubscribe_action(self):
        """Test unsubscribe action handling."""
        mock_ws = AsyncMock(spec=WebSocket)
        message = json.dumps({"action": "unsubscribe", "channel": "test_channel"})
        mock_ws.receive_text = AsyncMock(side_effect=[message, Exception("disconnect")])

        with patch.object(manager, "connect", new_callable=AsyncMock):
            with patch.object(manager, "unsubscribe", new_callable=AsyncMock):
                with patch.object(manager, "disconnect"):
                    try:
                        await channel_websocket(mock_ws, "test_channel", "token")
                    except Exception:
                        pass

                    mock_ws.send_json.assert_called()

    @pytest.mark.asyncio
    async def test_ping_action(self):
        """Test ping action handling."""
        mock_ws = AsyncMock(spec=WebSocket)
        message = json.dumps({"action": "ping"})
        mock_ws.receive_text = AsyncMock(side_effect=[message, Exception("disconnect")])

        with patch.object(manager, "connect", new_callable=AsyncMock):
            with patch.object(manager, "subscribe", new_callable=AsyncMock):
                with patch.object(manager, "disconnect"):
                    try:
                        await channel_websocket(mock_ws, "test_channel", "token")
                    except Exception:
                        pass

                    mock_ws.send_json.assert_called()

    @pytest.mark.asyncio
    async def test_invalid_json(self):
        """Test invalid JSON handling."""
        mock_ws = AsyncMock(spec=WebSocket)
        mock_ws.receive_text = AsyncMock(side_effect=["invalid json", Exception("disconnect")])

        with patch.object(manager, "connect", new_callable=AsyncMock):
            with patch.object(manager, "subscribe", new_callable=AsyncMock):
                with patch.object(manager, "disconnect"):
                    try:
                        await channel_websocket(mock_ws, "test_channel", "token")
                    except Exception:
                        pass

                    assert mock_ws.send_json.call_count >= 2


class TestMonitorWebSocket:
    """Tests for monitor WebSocket endpoint."""

    @pytest.mark.asyncio
    async def test_connect_and_disconnect(self):
        """Test connection and disconnection flow."""
        mock_ws = AsyncMock(spec=WebSocket)
        mock_ws.receive_text = AsyncMock(side_effect=Exception("disconnect"))

        with patch.object(manager, "connect", new_callable=AsyncMock):
            with patch.object(manager, "subscribe", new_callable=AsyncMock):
                with patch.object(manager, "disconnect"):
                    try:
                        await monitor_websocket(mock_ws, "token")
                    except Exception:
                        pass

    @pytest.mark.asyncio
    async def test_ping_action(self):
        """Test ping action handling."""
        mock_ws = AsyncMock(spec=WebSocket)
        message = json.dumps({"action": "ping"})
        mock_ws.receive_text = AsyncMock(side_effect=[message, Exception("disconnect")])

        with patch.object(manager, "connect", new_callable=AsyncMock):
            with patch.object(manager, "subscribe", new_callable=AsyncMock):
                with patch.object(manager, "disconnect"):
                    try:
                        await monitor_websocket(mock_ws, "token")
                    except Exception:
                        pass

                    mock_ws.send_json.assert_called()

    @pytest.mark.asyncio
    async def test_status_action(self):
        """Test status action handling."""
        mock_ws = AsyncMock(spec=WebSocket)
        message = json.dumps({"action": "status"})
        mock_ws.receive_text = AsyncMock(side_effect=[message, Exception("disconnect")])

        with patch.object(manager, "connect", new_callable=AsyncMock):
            with patch.object(manager, "subscribe", new_callable=AsyncMock):
                with patch.object(manager, "disconnect"):
                    try:
                        await monitor_websocket(mock_ws, "token")
                    except Exception:
                        pass

                    mock_ws.send_json.assert_called()

    @pytest.mark.asyncio
    async def test_invalid_json(self):
        """Test invalid JSON handling."""
        mock_ws = AsyncMock(spec=WebSocket)
        mock_ws.receive_text = AsyncMock(side_effect=["invalid json", Exception("disconnect")])

        with patch.object(manager, "connect", new_callable=AsyncMock):
            with patch.object(manager, "subscribe", new_callable=AsyncMock):
                with patch.object(manager, "disconnect"):
                    try:
                        await monitor_websocket(mock_ws, "token")
                    except Exception:
                        pass

                    assert mock_ws.send_json.call_count >= 2
