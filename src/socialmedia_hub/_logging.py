"""Logging setup for the SDK."""

from __future__ import annotations

import logging

_prefix = "socialmedia_hub"


def _make(name: str) -> logging.Logger:
    return logging.getLogger(f"{_prefix}.{name}")


requests_logger = _make("requests")
retries_logger = _make("retries")
rate_limit_logger = _make("rate_limit")
server_logger = _make("server")
