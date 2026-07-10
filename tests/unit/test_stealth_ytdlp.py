"""Tests for stealth and ytdlp modules."""

from __future__ import annotations

import pytest

from socialmedia_hub.proxy.stealth import StealthFetcher, USER_AGENTS
from socialmedia_hub.proxy.ytdlp_extractor import YTDLExtractor


class TestStealthFetcher:
    """Tests for StealthFetcher."""

    def test_init(self):
        fetcher = StealthFetcher()
        assert fetcher.impersonate == "edge"

    def test_init_custom(self):
        fetcher = StealthFetcher(impersonate="chrome")
        assert fetcher.impersonate == "chrome"

    def test_get_random_user_agent(self):
        fetcher = StealthFetcher()
        ua = fetcher._get_random_user_agent()
        assert ua in USER_AGENTS

    def test_get_smart_delay_normal(self):
        fetcher = StealthFetcher(min_delay=2.0, max_delay=5.0)
        delays = [fetcher._get_smart_delay() for _ in range(100)]
        normal_count = sum(1 for d in delays if d < 5)
        assert normal_count >= 80  # At least 80% should be normal

    def test_user_agents_count(self):
        assert len(USER_AGENTS) >= 8


class TestYTDLExtractor:
    """Tests for YTDLExtractor."""

    def test_init(self):
        extractor = YTDLExtractor()
        assert extractor.timeout == 30

    def test_init_custom(self):
        extractor = YTDLExtractor(timeout=60)
        assert extractor.timeout == 60
