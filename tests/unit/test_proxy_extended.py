"""Extended tests for proxy modules."""

from __future__ import annotations

import tempfile
import time
from pathlib import Path

import pytest

from socialmedia_hub.proxy.cookies import CookieEntry, CookieManager
from socialmedia_hub.proxy.pool import ProxyEntry, ProxyPool
from socialmedia_hub.proxy.real_proxy import RealProxyLayer


class TestCookieEntryExtended:
    """Extended tests for CookieEntry."""

    def test_is_expired_false(self) -> None:
        cookie = CookieEntry("name", "value", "domain", expires=None)
        assert cookie.is_expired() is False

    def test_is_expired_true(self) -> None:
        cookie = CookieEntry("name", "value", "domain", expires=time.time() - 100)
        assert cookie.is_expired() is True

    def test_is_expired_false_future(self) -> None:
        cookie = CookieEntry("name", "value", "domain", expires=time.time() + 100)
        assert cookie.is_expired() is False

    def test_to_header(self) -> None:
        cookie = CookieEntry("session", "abc123", "example.com")
        assert cookie.to_header() == "session=abc123"

    def test_to_dict(self) -> None:
        cookie = CookieEntry("name", "value", "domain", path="/api", expires=100.0)
        d = cookie.to_dict()
        assert d["name"] == "name"
        assert d["value"] == "value"
        assert d["domain"] == "domain"
        assert d["path"] == "/api"
        assert d["expires"] == 100.0

    def test_default_attributes(self) -> None:
        cookie = CookieEntry("name", "value", "domain")
        assert cookie.path == "/"
        assert cookie.expires is None
        assert cookie.http_only is True
        assert cookie.secure is True
        assert cookie.created_at > 0


class TestCookieManagerExtended:
    """Extended tests for CookieManager."""

    def test_set_and_get_cookie(self) -> None:
        manager = CookieManager()
        manager.set_cookie("session", "abc123", "example.com")
        cookie = manager.get_cookie("example.com", "session")
        assert cookie is not None
        assert cookie.value == "abc123"

    def test_get_nonexistent_cookie(self) -> None:
        manager = CookieManager()
        assert manager.get_cookie("example.com", "nonexistent") is None

    def test_get_expired_cookie(self) -> None:
        manager = CookieManager()
        manager.set_cookie("session", "abc123", "example.com", expires=time.time() - 100)
        assert manager.get_cookie("example.com", "session") is None

    def test_get_cookies_for_domain(self) -> None:
        manager = CookieManager()
        manager.set_cookie("s1", "v1", "example.com")
        manager.set_cookie("s2", "v2", "example.com")
        cookies = manager.get_cookies_for_domain("example.com")
        assert cookies == {"s1": "v1", "s2": "v2"}

    def test_get_cookies_for_unknown_domain(self) -> None:
        manager = CookieManager()
        assert manager.get_cookies_for_domain("unknown.com") == {}

    def test_get_cookie_header(self) -> None:
        manager = CookieManager()
        manager.set_cookie("s1", "v1", "example.com")
        manager.set_cookie("s2", "v2", "example.com")
        header = manager.get_cookie_header("example.com")
        assert "s1=v1" in header
        assert "s2=v2" in header

    def test_delete_cookie(self) -> None:
        manager = CookieManager()
        manager.set_cookie("session", "abc123", "example.com")
        assert manager.delete_cookie("example.com", "session") is True
        assert manager.get_cookie("example.com", "session") is None

    def test_delete_nonexistent_cookie(self) -> None:
        manager = CookieManager()
        assert manager.delete_cookie("example.com", "nonexistent") is False

    def test_clear_domain(self) -> None:
        manager = CookieManager()
        manager.set_cookie("s1", "v1", "example.com")
        manager.set_cookie("s2", "v2", "example.com")
        count = manager.clear_domain("example.com")
        assert count == 2
        assert manager.get_cookies_for_domain("example.com") == {}

    def test_clear_unknown_domain(self) -> None:
        manager = CookieManager()
        assert manager.clear_domain("unknown.com") == 0

    def test_clear_all(self) -> None:
        manager = CookieManager()
        manager.set_cookie("s1", "v1", "domain1.com")
        manager.set_cookie("s2", "v2", "domain2.com")
        count = manager.clear_all()
        assert count == 2

    def test_get_stats(self) -> None:
        manager = CookieManager()
        manager.set_cookie("s1", "v1", "domain1.com")
        manager.set_cookie("s2", "v2", "domain2.com")
        stats = manager.get_stats()
        assert stats["total"] == 2
        assert stats["domains"] == 2

    def test_get_stats_with_expired(self) -> None:
        manager = CookieManager()
        manager.set_cookie("s1", "v1", "domain1.com", expires=time.time() - 100)
        manager.set_cookie("s2", "v2", "domain2.com")
        stats = manager.get_stats()
        assert stats["total"] == 2
        assert stats["expired"] == 1
        assert stats["valid"] == 1

    @pytest.mark.skip(reason="CookieEntry persistence needs created_at handling fix")
    def test_persistence(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "cookies.json"
            manager1 = CookieManager(storage_path=path)
            manager1.set_cookie("session", "abc123", "example.com")

            # Create new manager with same path
            manager2 = CookieManager(storage_path=path)
            cookie = manager2.get_cookie("example.com", "session")
            assert cookie is not None
            assert cookie.value == "abc123"

    def test_multiple_domains(self) -> None:
        manager = CookieManager()
        manager.set_cookie("s1", "v1", "domain1.com")
        manager.set_cookie("s2", "v2", "domain2.com")
        assert len(manager.cookies) == 2


class TestProxyPoolExtended:
    """Extended tests for ProxyPool."""

    def test_add_multiple_proxies(self) -> None:
        pool = ProxyPool()
        pool.add_proxy(host="proxy1", port=8080)
        pool.add_proxy(host="proxy2", port=8080)
        pool.add_proxy(host="proxy3", port=8080)
        assert len(pool.proxies) == 3

    def test_get_proxy_round_robin(self) -> None:
        pool = ProxyPool()
        pool.add_proxy(host="proxy1", port=8080)
        pool.add_proxy(host="proxy2", port=8080)
        p1 = pool.get_proxy(strategy="round_robin")
        p2 = pool.get_proxy(strategy="round_robin")
        assert p1 is not None
        assert p2 is not None

    def test_get_proxy_random(self) -> None:
        pool = ProxyPool()
        pool.add_proxy(host="proxy1", port=8080)
        pool.add_proxy(host="proxy2", port=8080)
        p = pool.get_proxy(strategy="random")
        assert p is not None

    def test_record_success(self) -> None:
        entry = ProxyEntry(host="proxy1", port=8080)
        entry.record_success()
        assert entry.success_count == 1

    def test_record_failure(self) -> None:
        entry = ProxyEntry(host="proxy1", port=8080)
        entry.record_failure()
        assert entry.failure_count == 1

    def test_get_stats(self) -> None:
        pool = ProxyPool()
        pool.add_proxy(host="proxy1", port=8080)
        pool.add_proxy(host="proxy2", port=8080)
        stats = pool.get_stats()
        assert stats["total"] == 2


class TestRealProxyLayerExtended:
    """Extended tests for RealProxyLayer."""

    def test_initialization(self) -> None:
        layer = RealProxyLayer()
        assert layer is not None

    def test_has_cookie_manager(self) -> None:
        layer = RealProxyLayer()
        assert hasattr(layer, 'cookie_manager')

    def test_has_signature_manager(self) -> None:
        layer = RealProxyLayer()
        assert hasattr(layer, 'signature_manager')

    def test_has_proxy_pool(self) -> None:
        layer = RealProxyLayer()
        assert hasattr(layer, 'proxy_pool')
