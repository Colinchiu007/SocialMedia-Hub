"""Proxy layer for social media platform authentication."""

from socialmedia_hub.proxy.cookies import CookieManager, cookie_manager
from socialmedia_hub.proxy.pool import ProxyPool, proxy_pool
from socialmedia_hub.proxy.providers import (
    BrightDataProvider,
    FreeProxyProvider,
    KuaiDaiLiProvider,
    ProxyProvider,
    ZhiMaProvider,
    create_provider,
)
from socialmedia_hub.proxy.real_proxy import RealProxyLayer, real_proxy
from socialmedia_hub.proxy.signatures import SignatureManager, signature_manager

__all__ = [
    "BrightDataProvider",
    "CookieManager",
    "FreeProxyProvider",
    "KuaiDaiLiProvider",
    "ProxyPool",
    "ProxyProvider",
    "RealProxyLayer",
    "SignatureManager",
    "ZhiMaProvider",
    "cookie_manager",
    "create_provider",
    "proxy_pool",
    "real_proxy",
    "signature_manager",
]
