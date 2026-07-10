"""Tests for proxy providers."""

from __future__ import annotations

import pytest

from socialmedia_hub.proxy.providers import (
    FreeProxyProvider,
    KuaiDaiLiProvider,
    create_provider,
)


class TestFreeProxyProvider:
    """Tests for FreeProxyProvider."""

    def test_init(self):
        provider = FreeProxyProvider()
        assert provider._proxy_cache == []

    def test_get_proxies_empty(self):
        provider = FreeProxyProvider()
        # May return empty list if no proxies available
        proxies = provider.get_proxies(count=5)
        assert isinstance(proxies, list)

    def test_report_proxy_failure(self):
        provider = FreeProxyProvider()
        provider._working_proxies = [{"host": "test.com", "port": 8080}]
        provider.report_proxy({"host": "test.com", "port": 8080}, success=False)
        assert len(provider._working_proxies) == 0

    def test_report_proxy_success(self):
        provider = FreeProxyProvider()
        provider._working_proxies = [{"host": "test.com", "port": 8080}]
        provider.report_proxy({"host": "test.com", "port": 8080}, success=True)
        assert len(provider._working_proxies) == 1


class TestKuaiDaiLiProvider:
    """Tests for KuaiDaiLiProvider."""

    def test_init(self):
        provider = KuaiDaiLiProvider(api_key="test_key")
        assert provider.api_key == "test_key"


class TestCreateProvider:
    """Tests for create_provider function."""

    def test_create_free(self):
        provider = create_provider("free")
        assert isinstance(provider, FreeProxyProvider)

    def test_create_kuaidaili(self):
        provider = create_provider("kuaidaili", api_key="test")
        assert isinstance(provider, KuaiDaiLiProvider)

    def test_create_unknown(self):
        with pytest.raises(ValueError):
            create_provider("unknown")
