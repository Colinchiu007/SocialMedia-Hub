"""WebSocket endpoints for real-time data push."""

from __future__ import annotations

import json
import logging
from datetime import datetime, timezone

from fastapi import APIRouter, Query, WebSocket, WebSocketDisconnect

from socialmedia_hub.websocket.manager import manager

logger = logging.getLogger("socialmedia_hub.websocket")

router = APIRouter(prefix="/ws", tags=["websocket"])


@router.websocket("/live/{platform}/{room_id}")
async def live_room_websocket(
    websocket: WebSocket,
    platform: str,
    room_id: str,
    token: str = Query(...),
) -> None:
    """WebSocket endpoint for live room real-time data.

    Connect to receive real-time updates from a live room:
    - Danmaku (bullet comments)
    - Gift messages
    - User joins/leaves
    - Stream status changes
    """
    client_id = f"{platform}_{room_id}_{id(websocket)}"

    try:
        await manager.connect(websocket, client_id)
        await manager.subscribe(client_id, f"live:{platform}:{room_id}")

        # Send connection confirmation
        await websocket.send_json({
            "type": "connected",
            "platform": platform,
            "room_id": room_id,
            "timestamp": datetime.now(timezone.utc).isoformat(),
        })

        # Listen for messages
        while True:
            try:
                data = await websocket.receive_text()
                message = json.loads(data)

                # Handle subscription requests
                if message.get("action") == "subscribe":
                    channel = message.get("channel")
                    if channel:
                        await manager.subscribe(client_id, channel)
                        await websocket.send_json({
                            "type": "subscribed",
                            "channel": channel,
                        })

                # Handle unsubscription requests
                elif message.get("action") == "unsubscribe":
                    channel = message.get("channel")
                    if channel:
                        await manager.unsubscribe(client_id, channel)
                        await websocket.send_json({
                            "type": "unsubscribed",
                            "channel": channel,
                        })

                # Handle ping/pong
                elif message.get("action") == "ping":
                    await websocket.send_json({
                        "type": "pong",
                        "timestamp": datetime.now(timezone.utc).isoformat(),
                    })

            except WebSocketDisconnect:
                break
            except json.JSONDecodeError:
                await websocket.send_json({
                    "type": "error",
                    "message": "Invalid JSON",
                })

    except WebSocketDisconnect:
        pass
    finally:
        manager.disconnect(client_id)


@router.websocket("/subscribe/{channel}")
async def channel_websocket(
    websocket: WebSocket,
    channel: str,
    token: str = Query(...),
) -> None:
    """WebSocket endpoint for channel subscriptions.

    Subscribe to a channel to receive real-time updates:
    - Trending topics
    - Hot search changes
    - New content alerts
    """
    client_id = f"channel_{channel}_{id(websocket)}"

    try:
        await manager.connect(websocket, client_id)
        await manager.subscribe(client_id, channel)

        # Send connection confirmation
        await websocket.send_json({
            "type": "connected",
            "channel": channel,
            "timestamp": datetime.now(timezone.utc).isoformat(),
        })

        # Listen for messages
        while True:
            try:
                data = await websocket.receive_text()
                message = json.loads(data)

                # Handle subscription requests
                if message.get("action") == "subscribe":
                    new_channel = message.get("channel")
                    if new_channel:
                        await manager.subscribe(client_id, new_channel)
                        await websocket.send_json({
                            "type": "subscribed",
                            "channel": new_channel,
                        })

                # Handle unsubscription requests
                elif message.get("action") == "unsubscribe":
                    unsub_channel = message.get("channel")
                    if unsub_channel:
                        await manager.unsubscribe(client_id, unsub_channel)
                        await websocket.send_json({
                            "type": "unsubscribed",
                            "channel": unsub_channel,
                        })

                # Handle ping/pong
                elif message.get("action") == "ping":
                    await websocket.send_json({
                        "type": "pong",
                        "timestamp": datetime.now(timezone.utc).isoformat(),
                    })

            except WebSocketDisconnect:
                break
            except json.JSONDecodeError:
                await websocket.send_json({
                    "type": "error",
                    "message": "Invalid JSON",
                })

    except WebSocketDisconnect:
        pass
    finally:
        manager.disconnect(client_id)


@router.websocket("/monitor")
async def monitor_websocket(
    websocket: WebSocket,
    token: str = Query(...),
) -> None:
    """WebSocket endpoint for real-time monitoring.

    Receive real-time updates:
    - Connection count changes
    - Subscription changes
    - System status updates
    """
    client_id = f"monitor_{id(websocket)}"

    try:
        await manager.connect(websocket, client_id)
        await manager.subscribe(client_id, "monitor")

        # Send initial status
        await websocket.send_json({
            "type": "connected",
            "status": "monitoring",
            "connections": manager.get_connection_count(),
            "subscriptions": manager.get_subscription_count(),
            "timestamp": datetime.now(timezone.utc).isoformat(),
        })

        # Listen for messages
        while True:
            try:
                data = await websocket.receive_text()
                message = json.loads(data)

                # Handle ping/pong
                if message.get("action") == "ping":
                    await websocket.send_json({
                        "type": "pong",
                        "connections": manager.get_connection_count(),
                        "subscriptions": manager.get_subscription_count(),
                        "timestamp": datetime.now(timezone.utc).isoformat(),
                    })

                # Handle status request
                elif message.get("action") == "status":
                    await websocket.send_json({
                        "type": "status",
                        "connections": manager.get_connection_count(),
                        "subscriptions": manager.get_subscription_count(),
                        "timestamp": datetime.now(timezone.utc).isoformat(),
                    })

            except WebSocketDisconnect:
                break
            except json.JSONDecodeError:
                await websocket.send_json({
                    "type": "error",
                    "message": "Invalid JSON",
                })

    except WebSocketDisconnect:
        pass
    finally:
        manager.disconnect(client_id)
