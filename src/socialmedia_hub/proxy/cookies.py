"""Cookie manager for social media platform authentication."""

from __future__ import annotations

import json
import logging
import time
from pathlib import Path
from typing import Any

logger = logging.getLogger("socialmedia_hub.proxy.cookie")


class CookieEntry:
    """A single cookie entry."""

    def __init__(
        self,
        name: str,
        value: str,
        domain: str,
        path: str = "/",
        expires: float | None = None,
        http_only: bool = True,
        secure: bool = True,
    ) -> None:
        self.name = name
        self.value = value
        self.domain = domain
        self.path = path
        self.expires = expires
        self.http_only = http_only
        self.secure = secure
        self.created_at = time.time()

    def is_expired(self) -> bool:
        """Check if cookie is expired."""
        if self.expires is None:
            return False
        return time.time() > self.expires

    def to_header(self) -> str:
        """Convert to Cookie header string."""
        return f"{self.name}={self.value}"

    def to_dict(self) -> dict[str, Any]:
        """Convert to dictionary."""
        return {
            "name": self.name,
            "value": self.value,
            "domain": self.domain,
            "path": self.path,
            "expires": self.expires,
            "http_only": self.http_only,
            "secure": self.secure,
            "created_at": self.created_at,
        }


class CookieManager:
    """Manage cookies for social media platform authentication."""

    def __init__(self, storage_path: str | Path | None = None) -> None:
        """Initialize cookie manager.

        Args:
            storage_path: Path to store cookies persistently
        """
        self.storage_path = Path(storage_path) if storage_path else None
        self.cookies: dict[str, dict[str, CookieEntry]] = {}  # domain -> name -> cookie
        self._load_cookies()

    def _load_cookies(self) -> None:
        """Load cookies from storage."""
        if self.storage_path and self.storage_path.exists():
            try:
                data = json.loads(self.storage_path.read_text(encoding="utf-8"))
                for domain, cookies_data in data.items():
                    self.cookies[domain] = {}
                    for name, cookie_data in cookies_data.items():
                        self.cookies[domain][name] = CookieEntry(**cookie_data)
                logger.info(f"Loaded cookies from {self.storage_path}")
            except Exception as e:
                logger.warning(f"Failed to load cookies: {e}")

    def _save_cookies(self) -> None:
        """Save cookies to storage."""
        if self.storage_path:
            try:
                data = {}
                for domain, cookies in self.cookies.items():
                    data[domain] = {name: cookie.to_dict() for name, cookie in cookies.items()}
                self.storage_path.parent.mkdir(parents=True, exist_ok=True)
                self.storage_path.write_text(json.dumps(data, indent=2), encoding="utf-8")
                logger.info(f"Saved cookies to {self.storage_path}")
            except Exception as e:
                logger.warning(f"Failed to save cookies: {e}")

    def set_cookie(
        self,
        name: str,
        value: str,
        domain: str,
        path: str = "/",
        expires: float | None = None,
    ) -> None:
        """Set a cookie."""
        if domain not in self.cookies:
            self.cookies[domain] = {}

        self.cookies[domain][name] = CookieEntry(
            name=name,
            value=value,
            domain=domain,
            path=path,
            expires=expires,
        )
        self._save_cookies()
        logger.debug(f"Set cookie: {name} for {domain}")

    def get_cookie(self, domain: str, name: str) -> CookieEntry | None:
        """Get a cookie by domain and name."""
        if domain in self.cookies and name in self.cookies[domain]:
            cookie = self.cookies[domain][name]
            if not cookie.is_expired():
                return cookie
            else:
                # Remove expired cookie
                del self.cookies[domain][name]
                self._save_cookies()
        return None

    def get_cookies_for_domain(self, domain: str) -> dict[str, str]:
        """Get all valid cookies for a domain."""
        if domain not in self.cookies:
            return {}

        result = {}
        expired = []
        for name, cookie in self.cookies[domain].items():
            if not cookie.is_expired():
                result[name] = cookie.value
            else:
                expired.append(name)

        # Remove expired cookies
        for name in expired:
            del self.cookies[domain][name]

        if expired:
            self._save_cookies()

        return result

    def get_cookie_header(self, domain: str) -> str:
        """Get Cookie header string for a domain."""
        cookies = self.get_cookies_for_domain(domain)
        return "; ".join(f"{k}={v}" for k, v in cookies.items())

    def delete_cookie(self, domain: str, name: str) -> bool:
        """Delete a cookie."""
        if domain in self.cookies and name in self.cookies[domain]:
            del self.cookies[domain][name]
            self._save_cookies()
            return True
        return False

    def clear_domain(self, domain: str) -> int:
        """Clear all cookies for a domain."""
        if domain in self.cookies:
            count = len(self.cookies[domain])
            del self.cookies[domain]
            self._save_cookies()
            return count
        return 0

    def clear_all(self) -> int:
        """Clear all cookies."""
        count = sum(len(cookies) for cookies in self.cookies.values())
        self.cookies.clear()
        self._save_cookies()
        return count

    def get_stats(self) -> dict[str, Any]:
        """Get cookie statistics."""
        total = sum(len(cookies) for cookies in self.cookies.values())
        expired = sum(
            1
            for cookies in self.cookies.values()
            for cookie in cookies.values()
            if cookie.is_expired()
        )
        return {
            "total": total,
            "expired": expired,
            "valid": total - expired,
            "domains": len(self.cookies),
        }


# Global cookie manager
cookie_manager = CookieManager()
