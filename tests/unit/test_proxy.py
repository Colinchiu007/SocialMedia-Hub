"""Tests for proxy layer components."""

from __future__ import annotations

import time

from socialmedia_hub.proxy.cookies import CookieEntry, CookieManager
from socialmedia_hub.proxy.pool import ProxyEntry, ProxyPool
from socialmedia_hub.proxy.signatures import (
    SignatureManager,
)


class TestCookieEntry:
    """Test CookieEntry."""

    def test_creation(self):
        cookie = CookieEntry(
            name="session_id",
            value="abc123",
            domain=".douyin.com",
        )
        assert cookie.name == "session_id"
        assert cookie.value == "abc123"
        assert cookie.domain == ".douyin.com"

    def test_is_expired(self):
        cookie = CookieEntry(
            name="test",
            value="value",
            domain=".test.com",
            expires=time.time() - 10,  # Expired
        )
        assert cookie.is_expired() is True

    def test_not_expired(self):
        cookie = CookieEntry(
            name="test",
            value="value",
            domain=".test.com",
            expires=time.time() + 3600,  # Not expired
        )
        assert cookie.is_expired() is False

    def test_to_header(self):
        cookie = CookieEntry(name="session", value="abc123", domain=".test.com")
        assert cookie.to_header() == "session=abc123"

    def test_to_dict(self):
        cookie = CookieEntry(name="test", value="value", domain=".test.com")
        d = cookie.to_dict()
        assert d["name"] == "test"
        assert d["value"] == "value"


class TestCookieManager:
    """Test CookieManager."""

    def test_set_and_get_cookie(self):
        manager = CookieManager()
        manager.set_cookie("session", "abc123", ".douyin.com")
        cookie = manager.get_cookie(".douyin.com", "session")
        assert cookie is not None
        assert cookie.value == "abc123"

    def test_get_expired_cookie(self):
        manager = CookieManager()
        manager.set_cookie("session", "abc123", ".test.com", expires=time.time() - 10)
        cookie = manager.get_cookie(".test.com", "session")
        assert cookie is None

    def test_get_cookie_header(self):
        manager = CookieManager()
        manager.set_cookie("session", "abc123", ".douyin.com")
        header = manager.get_cookie_header(".douyin.com")
        assert "session=abc123" in header

    def test_delete_cookie(self):
        manager = CookieManager()
        manager.set_cookie("session", "abc123", ".douyin.com")
        assert manager.delete_cookie(".douyin.com", "session") is True
        assert manager.get_cookie(".douyin.com", "session") is None

    def test_clear_domain(self):
        manager = CookieManager()
        manager.set_cookie("a", "1", ".test.com")
        manager.set_cookie("b", "2", ".test.com")
        count = manager.clear_domain(".test.com")
        assert count == 2

    def test_get_stats(self):
        manager = CookieManager()
        manager.set_cookie("a", "1", ".test.com")
        stats = manager.get_stats()
        assert stats["total"] == 1
        assert stats["domains"] == 1


class TestProxyEntry:
    """Test ProxyEntry."""

    def test_creation(self):
        proxy = ProxyEntry(host="1.2.3.4", port=8080)
        assert proxy.host == "1.2.3.4"
        assert proxy.port == 8080

    def test_url(self):
        proxy = ProxyEntry(host="1.2.3.4", port=8080)
        assert proxy.url == "http://1.2.3.4:8080"

    def test_url_with_auth(self):
        proxy = ProxyEntry(host="1.2.3.4", port=8080, username="user", password="pass")
        assert proxy.url == "http://user:pass@1.2.3.4:8080"

    def test_success_rate(self):
        proxy = ProxyEntry(host="1.2.3.4", port=8080)
        proxy.record_success()
        proxy.record_success()
        proxy.record_failure()
        assert proxy.success_rate == 2 / 3


class TestProxyPool:
    """Test ProxyPool."""

    def test_add_proxy(self):
        pool = ProxyPool()
        pool.add_proxy("1.2.3.4", 8080)
        assert len(pool.proxies) == 1

    def test_get_proxy_round_robin(self):
        pool = ProxyPool()
        pool.add_proxy("1.1.1.1", 8080)
        pool.add_proxy("2.2.2.2", 8080)
        p1 = pool.get_proxy("round_robin")
        p2 = pool.get_proxy("round_robin")
        assert p1.host != p2.host

    def test_get_proxy_random(self):
        pool = ProxyPool()
        pool.add_proxy("1.1.1.1", 8080)
        pool.add_proxy("2.2.2.2", 8080)
        proxy = pool.get_proxy("random")
        assert proxy is not None

    def test_get_proxy_empty_pool(self):
        pool = ProxyPool()
        assert pool.get_proxy() is None

    def test_record_success_failure(self):
        pool = ProxyPool()
        pool.add_proxy("1.2.3.4", 8080)
        proxy = pool.proxies[0]
        pool.record_success(proxy)
        pool.record_success(proxy)
        pool.record_failure(proxy)
        assert proxy.success_count == 2
        assert proxy.failure_count == 1

    def test_get_stats(self):
        pool = ProxyPool()
        pool.add_proxy("1.2.3.4", 8080)
        stats = pool.get_stats()
        assert stats["total"] == 1


class TestSignatureManager:
    """Test SignatureManager."""

    def test_generate_douyin_signature(self):
        manager = SignatureManager()
        sig = manager.generate_signature("douyin", data="test")
        assert "X-Bogus" in sig
        assert "msToken" in sig

    def test_generate_tiktok_signature(self):
        manager = SignatureManager()
        sig = manager.generate_signature("tiktok", data="test")
        assert "X-Bogus" in sig

    def test_generate_instagram_signature(self):
        manager = SignatureManager()
        sig = manager.generate_signature("instagram")
        assert "X-IG-App-ID" in sig

    def test_unknown_platform(self):
        manager = SignatureManager()
        sig = manager.generate_signature("unknown")
        assert sig == {}
