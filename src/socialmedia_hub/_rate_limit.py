"""Rate-limit header parsing."""

from __future__ import annotations

from collections.abc import Mapping


def parse_retry_after(headers: Mapping[str, str]) -> float | None:
    """Extract Retry-After value from response headers.

    Supports both integer seconds and HTTP-date formats.
    """
    val = headers.get("retry-after") or headers.get("Retry-After")
    if val is None:
        return None
    try:
        return float(val)
    except ValueError:
        return None
