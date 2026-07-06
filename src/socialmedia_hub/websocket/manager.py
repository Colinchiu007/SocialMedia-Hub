"""WebSocket manager for real-time data push."""

from __future__ import annotations

import logging
from typing import Any

from fastapi import WebSocket, WebSocketDisconnect

logger = logging.getLogger("socialmedia_hub.websocket")


class ConnectionManager:
    """Manage WebSocket connections for real-time data push."""

    def __init__(self) -> None:
        self.active_connections: dict[str, WebSocket] = {}
        self.subscriptions: dict[str, set[str]] = {}  # channel -> connection_ids

    async def connect(self, websocket: WebSocket, client_id: str) -> None:
        """Accept a new WebSocket connection."""
        await websocket.accept()
        self.active_connections[client_id] = websocket
        logger.info(f"Client connected: {client_id}")

    def disconnect(self, client_id: str) -> None:
        """Remove a WebSocket connection."""
        if client_id in self.active_connections:
            del self.active_connections[client_id]
            # Remove from all subscriptions
            for channel in list(self.subscriptions.keys()):
                self.subscriptions[channel].discard(client_id)
            logger.info(f"Client disconnected: {client_id}")

    async def send_personal_message(self, message: dict[str, Any], client_id: str) -> None:
        """Send a message to a specific client."""
        if client_id in self.active_connections:
            websocket = self.active_connections[client_id]
            try:
                await websocket.send_json(message)
            except WebSocketDisconnect:
                self.disconnect(client_id)

    async def broadcast(self, message: dict[str, Any]) -> None:
        """Broadcast a message to all connected clients."""
        disconnected = []
        for client_id, websocket in self.active_connections.items():
            try:
                await websocket.send_json(message)
            except WebSocketDisconnect:
                disconnected.append(client_id)

        for client_id in disconnected:
            self.disconnect(client_id)

    async def subscribe(self, client_id: str, channel: str) -> None:
        """Subscribe a client to a channel."""
        if channel not in self.subscriptions:
            self.subscriptions[channel] = set()
        self.subscriptions[channel].add(client_id)
        logger.info(f"Client {client_id} subscribed to {channel}")

    async def unsubscribe(self, client_id: str, channel: str) -> None:
        """Unsubscribe a client from a channel."""
        if channel in self.subscriptions:
            self.subscriptions[channel].discard(client_id)
            logger.info(f"Client {client_id} unsubscribed from {channel}")

    async def broadcast_to_channel(self, channel: str, message: dict[str, Any]) -> None:
        """Broadcast a message to all clients subscribed to a channel."""
        if channel not in self.subscriptions:
            return

        disconnected = []
        for client_id in self.subscriptions[channel]:
            if client_id in self.active_connections:
                websocket = self.active_connections[client_id]
                try:
                    await websocket.send_json(message)
                except WebSocketDisconnect:
                    disconnected.append(client_id)

        for client_id in disconnected:
            self.disconnect(client_id)

    def get_connection_count(self) -> int:
        """Get the number of active connections."""
        return len(self.active_connections)

    def get_subscription_count(self) -> dict[str, int]:
        """Get the number of subscriptions per channel."""
        return {channel: len(clients) for channel, clients in self.subscriptions.items()}


# Global connection manager
manager = ConnectionManager()
