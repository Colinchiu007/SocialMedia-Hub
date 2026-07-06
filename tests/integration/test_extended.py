"""Extended WebSocket and proxy layer tests."""

from __future__ import annotations

import asyncio

from socialmedia_hub.proxy.cookies import CookieManager
from socialmedia_hub.proxy.pool import ProxyPool
from socialmedia_hub.proxy.signatures import SignatureManager
from socialmedia_hub.websocket.manager import ConnectionManager


class TestWebSocketManagerExtended:
    """Extended WebSocket manager tests."""

    def test_multiple_subscriptions(self):
        mgr = ConnectionManager()

        async def test():
            await mgr.subscribe("client1", "channel1")
            await mgr.subscribe("client1", "channel2")
            await mgr.subscribe("client2", "channel1")

            counts = mgr.get_subscription_count()
            assert counts["channel1"] == 2
            assert counts["channel2"] == 1

        asyncio.run(test())

    def test_unsubscribe_all(self):
        mgr = ConnectionManager()

        async def test():
            await mgr.subscribe("client1", "channel1")
            await mgr.subscribe("client1", "channel2")
            await mgr.unsubscribe("client1", "channel1")
            await mgr.unsubscribe("client1", "channel2")

            assert "client1" not in mgr.subscriptions.get("channel1", set())
            assert "client1" not in mgr.subscriptions.get("channel2", set())

        asyncio.run(test())


class TestCookieManagerExtended:
    """Extended cookie manager tests."""

    def test_multiple_domains(self):
        manager = CookieManager()
        manager.set_cookie("a", "1", ".douyin.com")
        manager.set_cookie("b", "2", ".tiktok.com")

        stats = manager.get_stats()
        assert stats["domains"] == 2
        assert stats["total"] == 2

    def test_cookie_expiry(self):
        manager = CookieManager()
        manager.set_cookie("a", "1", ".test.com", expires=0.001)
        import time
        time.sleep(0.01)

        cookie = manager.get_cookie(".test.com", "a")
        assert cookie is None


class TestProxyPoolExtended:
    """Extended proxy pool tests."""

    def test_multiple_proxies(self):
        pool = ProxyPool()
        pool.add_proxy("1.1.1.1", 8080)
        pool.add_proxy("2.2.2.2", 8080)
        pool.add_proxy("3.3.3.3", 8080)

        stats = pool.get_stats()
        assert stats["total"] == 3

    def test_proxy_success_rate(self):
        pool = ProxyPool()
        pool.add_proxy("1.1.1.1", 8080)
        proxy = pool.proxies[0]

        for _ in range(10):
            pool.record_success(proxy)
        for _ in range(2):
            pool.record_failure(proxy)

        assert proxy.success_rate == 10 / 12


class TestSignatureManagerExtended:
    """Extended signature manager tests."""

    def test_all_platforms(self):
        manager = SignatureManager()
        platforms = ["douyin", "tiktok", "instagram"]

        for platform in platforms:
            sig = manager.generate_signature(platform, data="test")
            assert isinstance(sig, dict)
