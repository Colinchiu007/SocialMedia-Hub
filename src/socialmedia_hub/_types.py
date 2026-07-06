"""Common type aliases."""

from __future__ import annotations

from typing import Any

JSON = dict[str, Any]
Headers = dict[str, str]
Params = dict[str, str | int | float | bool | None]
