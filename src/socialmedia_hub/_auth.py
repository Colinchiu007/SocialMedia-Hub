"""API Key authentication helpers."""

from __future__ import annotations

import os


def resolve_api_key(explicit: str | None = None) -> str:
    """Resolve API key from explicit value or environment variable."""
    if explicit:
        return explicit
    env = os.environ.get("SMH_API_KEY") or os.environ.get("SOCIALMEDIA_HUB_API_KEY")
    if env:
        return env
    raise ValueError(
        "No API key provided. Pass api_key= to the client or set $SMH_API_KEY."
    )
