"""Proxy pool for IP rotation."""

from __future__ import annotations

import logging
import random
import time
from dataclasses import dataclass
from typing import Any

logger = logging.getLogger("socialmedia_hub.proxy.pool")


@dataclass
class ProxyEntry:
    """A single proxy entry."""

    host: str
    port: int
    protocol: str = "http"
    username: str | None = None
    password: str | None = None
    country: str | None = None
    last_used: float = 0
    success_count: int = 0
    failure_count: int = 0

    @property
    def url(self) -> str:
        """Get proxy URL."""
        if self.username and self.password:
            return f"{self.protocol}://{self.username}:{self.password}@{self.host}:{self.port}"
        return f"{self.protocol}://{self.host}:{self.port}"

    @property
    def success_rate(self) -> float:
        """Get success rate."""
        total = self.success_count + self.failure_count
        if total == 0:
            return 1.0
        return self.success_count / total

    def record_success(self) -> None:
        """Record a successful request."""
        self.success_count += 1
        self.last_used = time.time()

    def record_failure(self) -> None:
        """Record a failed request."""
        self.failure_count += 1

    def to_dict(self) -> dict[str, Any]:
        """Convert to dictionary."""
        return {
            "host": self.host,
            "port": self.port,
            "protocol": self.protocol,
            "country": self.country,
            "success_rate": self.success_rate,
        }


class ProxyPool:
    """Manage a pool of proxies for IP rotation."""

    def __init__(self) -> None:
        self.proxies: list[ProxyEntry] = []
        self._index = 0

    def add_proxy(
        self,
        host: str,
        port: int,
        protocol: str = "http",
        username: str | None = None,
        password: str | None = None,
        country: str | None = None,
    ) -> None:
        """Add a proxy to the pool."""
        proxy = ProxyEntry(
            host=host,
            port=port,
            protocol=protocol,
            username=username,
            password=password,
            country=country,
        )
        self.proxies.append(proxy)
        logger.info(f"Added proxy: {host}:{port}")

    def add_proxies(self, proxies: list[dict[str, Any]]) -> None:
        """Add multiple proxies to the pool."""
        for proxy_data in proxies:
            self.add_proxy(
                host=proxy_data["host"],
                port=proxy_data["port"],
                protocol=proxy_data.get("protocol", "http"),
                username=proxy_data.get("username"),
                password=proxy_data.get("password"),
                country=proxy_data.get("country"),
            )

    def get_proxy(self, strategy: str = "round_robin") -> ProxyEntry | None:
        """Get a proxy from the pool.

        Args:
            strategy: Rotation strategy ('round_robin', 'random', 'least_used', 'best_success')

        Returns:
            ProxyEntry or None if pool is empty
        """
        if not self.proxies:
            return None

        if strategy == "round_robin":
            proxy = self.proxies[self._index % len(self.proxies)]
            self._index += 1
            return proxy

        elif strategy == "random":
            return random.choice(self.proxies)

        elif strategy == "least_used":
            return min(self.proxies, key=lambda p: p.last_used)

        elif strategy == "best_success":
            return max(self.proxies, key=lambda p: p.success_rate)

        else:
            return self.proxies[0]

    def get_proxy_url(self, strategy: str = "round_robin") -> str | None:
        """Get a proxy URL string."""
        proxy = self.get_proxy(strategy)
        if proxy:
            return proxy.url
        return None

    def record_success(self, proxy: ProxyEntry) -> None:
        """Record a successful request for a proxy."""
        proxy.record_success()

    def record_failure(self, proxy: ProxyEntry) -> None:
        """Record a failed request for a proxy."""
        proxy.record_failure()

    def remove_proxy(self, host: str, port: int) -> bool:
        """Remove a proxy from the pool."""
        for i, proxy in enumerate(self.proxies):
            if proxy.host == host and proxy.port == port:
                self.proxies.pop(i)
                return True
        return False

    def get_stats(self) -> dict[str, Any]:
        """Get pool statistics."""
        if not self.proxies:
            return {"total": 0}

        success_rates = [p.success_rate for p in self.proxies]
        return {
            "total": len(self.proxies),
            "avg_success_rate": sum(success_rates) / len(success_rates),
            "best_proxy": max(self.proxies, key=lambda p: p.success_rate).to_dict(),
        }

    def load_from_config(self, config: list[dict[str, Any]]) -> None:
        """Load proxies from configuration."""
        self.proxies.clear()
        for proxy_data in config:
            self.add_proxy(
                host=proxy_data["host"],
                port=proxy_data["port"],
                protocol=proxy_data.get("protocol", "http"),
                username=proxy_data.get("username"),
                password=proxy_data.get("password"),
                country=proxy_data.get("country"),
            )


# Global proxy pool
proxy_pool = ProxyPool()
