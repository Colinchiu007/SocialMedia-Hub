"""Comprehensive tests for proxy modules."""

from __future__ import annotations

import tempfile
import time
from pathlib import Path

import pytest

from socialmedia_hub.proxy.cookies import CookieEntry, CookieManager
from socialmedia_hub.proxy.pool import ProxyEntry, ProxyPool
from socialmedia_hub.proxy.real_proxy import RealProxyLayer
from socialmedia_hub.proxy.signatures import SignatureManager


class TestCookieEntryComprehensive:
    """Comprehensive tests for CookieEntry."""

    def test_creation_with_all_params(self):
        cookie = CookieEntry(
            name="session",
            value="abc123",
            domain="example.com",
            path="/api",
            expires=time.time() + 3600,
            http_only=False,
            secure=False,
        )
        assert cookie.name == "session"
        assert cookie.value == "abc123"
        assert cookie.domain == "example.com"
        assert cookie.path == "/api"
        assert cookie.http_only is False
        assert cookie.secure is False

    def test_is_expired_boundary(self):
        # Cookie that expires exactly now
        cookie = CookieEntry("name", "value", "domain", expires=time.time())
        # May or may not be expired depending on timing
        assert isinstance(cookie.is_expired(), bool)

    def test_to_dict_complete(self):
        cookie = CookieEntry("name", "value", "domain", expires=100.0)
        d = cookie.to_dict()
        assert len(d) == 8
        assert d["name"] == "name"
        assert d["expires"] == 100.0


class TestCookieManagerComprehensive:
    """Comprehensive tests for CookieManager."""

    def test_set_multiple_cookies(self):
        manager = CookieManager()
        manager.set_cookie("s1", "v1", "domain1.com")
        manager.set_cookie("s2", "v2", "domain1.com")
        manager.set_cookie("s3", "v3", "domain2.com")
        assert len(manager.cookies) == 2
        assert len(manager.cookies["domain1.com"]) == 2

    def test_get_expired_cookie_removes(self):
        manager = CookieManager()
        manager.set_cookie("expired", "value", "domain.com", expires=time.time() - 100)
        result = manager.get_cookie("domain.com", "expired")
        assert result is None
        assert "expired" not in manager.cookies.get("domain.com", {})

    def test_get_cookies_for_domain_with_expired(self):
        manager = CookieManager()
        manager.set_cookie("valid", "v1", "domain.com")
        manager.set_cookie("expired", "v2", "domain.com", expires=time.time() - 100)
        cookies = manager.get_cookies_for_domain("domain.com")
        assert cookies == {"valid": "v1"}

    def test_delete_nonexistent_domain(self):
        manager = CookieManager()
        assert manager.delete_cookie("nonexistent.com", "cookie") is False

    def test_get_stats_empty(self):
        manager = CookieManager()
        stats = manager.get_stats()
        assert stats["total"] == 0
        assert stats["expired"] == 0
        assert stats["domains"] == 0


class TestProxyEntryComprehensive:
    """Comprehensive tests for ProxyEntry."""

    def test_url_with_auth(self):
        entry = ProxyEntry(host="proxy.com", port=8080, username="user", password="pass")
        assert entry.url == "http://user:pass@proxy.com:8080"

    def test_url_without_auth(self):
        entry = ProxyEntry(host="proxy.com", port=8080)
        assert entry.url == "http://proxy.com:8080"

    def test_success_rate_empty(self):
        entry = ProxyEntry(host="proxy.com", port=8080)
        assert entry.success_rate == 1.0

    def test_success_rate_with_stats(self):
        entry = ProxyEntry(host="proxy.com", port=8080)
        entry.success_count = 8
        entry.failure_count = 2
        assert entry.success_rate == 0.8

    def test_record_success_updates_time(self):
        entry = ProxyEntry(host="proxy.com", port=8080)
        entry.record_success()
        assert entry.success_count == 1
        assert entry.last_used > 0

    def test_record_failure(self):
        entry = ProxyEntry(host="proxy.com", port=8080)
        entry.record_failure()
        assert entry.failure_count == 1

    def test_to_dict(self):
        entry = ProxyEntry(host="proxy.com", port=8080, country="US")
        d = entry.to_dict()
        assert d["host"] == "proxy.com"
        assert d["port"] == 8080
        assert d["country"] == "US"


class TestProxyPoolComprehensive:
    """Comprehensive tests for ProxyPool."""

    def test_empty_pool(self):
        pool = ProxyPool()
        assert pool.get_proxy() is None

    def test_add_and_get(self):
        pool = ProxyPool()
        pool.add_proxy(host="p1", port=8080)
        pool.add_proxy(host="p2", port=8081)
        proxy = pool.get_proxy()
        assert proxy is not None

    def test_round_robin(self):
        pool = ProxyPool()
        pool.add_proxy(host="p1", port=8080)
        pool.add_proxy(host="p2", port=8081)
        p1 = pool.get_proxy(strategy="round_robin")
        p2 = pool.get_proxy(strategy="round_robin")
        assert p1.host != p2.host or p1.port != p2.port

    def test_get_proxy_url(self):
        pool = ProxyPool()
        pool.add_proxy(host="p1", port=8080)
        url = pool.get_proxy_url()
        assert url == "http://p1:8080"

    def test_get_proxy_url_empty(self):
        pool = ProxyPool()
        assert pool.get_proxy_url() is None

    def test_record_success_failure(self):
        pool = ProxyPool()
        pool.add_proxy(host="p1", port=8080)
        proxy = pool.get_proxy()
        pool.record_success(proxy)
        pool.record_failure(proxy)
        assert proxy.success_count == 1
        assert proxy.failure_count == 1


class TestSignatureManagerComprehensive:
    """Comprehensive tests for SignatureManager."""

    def test_generate_douyin(self):
        mgr = SignatureManager()
        sig = mgr.generate_signature("douyin", url="https://www.douyin.com/test")
        assert isinstance(sig, dict)

    def test_generate_tiktok(self):
        mgr = SignatureManager()
        sig = mgr.generate_signature("tiktok", url="https://www.tiktok.com/test")
        assert isinstance(sig, dict)

    def test_generate_instagram(self):
        mgr = SignatureManager()
        sig = mgr.generate_signature("instagram", url="https://www.instagram.com/test")
        assert isinstance(sig, dict)

    def test_generate_unknown(self):
        mgr = SignatureManager()
        sig = mgr.generate_signature("unknown_platform")
        assert sig == {}


class TestRealProxyLayerComprehensive:
    """Comprehensive tests for RealProxyLayer."""

    def test_initialization_with_custom_managers(self):
        cookie_mgr = CookieManager()
        sig_mgr = SignatureManager()
        pool = ProxyPool()
        layer = RealProxyLayer(
            cookie_manager=cookie_mgr,
            signature_manager=sig_mgr,
            proxy_pool=pool,
        )
        assert layer.cookie_manager is cookie_mgr
        assert layer.signature_manager is sig_mgr
        assert layer.proxy_pool is pool

    def test_rate_control_initial(self):
        layer = RealProxyLayer()
        assert "test_platform" not in layer._request_times

    def test_get_stats(self):
        layer = RealProxyLayer()
        stats = layer.get_stats()
        assert "cookie_stats" in stats
        assert "proxy_stats" in stats
        assert "request_counts" in stats
