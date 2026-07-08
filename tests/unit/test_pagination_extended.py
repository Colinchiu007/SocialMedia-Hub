"""Extended tests for pagination module."""

from __future__ import annotations

import pytest

from socialmedia_hub._pagination import (
    CursorPaginator,
    OffsetPaginator,
    Page,
    PagePaginator,
)


class TestPage:
    """Tests for Page class."""

    def test_page_creation(self):
        page = Page(items=[1, 2, 3])
        assert page.items == [1, 2, 3]
        assert page.has_more is False
        assert page.next_cursor is None

    def test_page_with_cursor(self):
        page = Page(items=[1, 2], next_cursor=10, has_more=True)
        assert page.next_cursor == 10
        assert page.has_more is True


class TestCursorPaginatorExtended:
    """Extended tests for CursorPaginator."""

    def test_requires_fetch_function(self):
        with pytest.raises(ValueError):
            CursorPaginator()

    def test_sync_iteration(self):
        pages = [
            Page(items=[1, 2], next_cursor=2, has_more=True),
            Page(items=[3, 4], next_cursor=4, has_more=False),
        ]
        call_count = 0

        def fetch(cursor):
            nonlocal call_count
            page = pages[call_count]
            call_count += 1
            return page

        paginator = CursorPaginator(sync_fetch=fetch)
        result = list(paginator)
        assert result == [1, 2, 3, 4]

    def test_first_n_items(self):
        pages = [
            Page(items=[1, 2, 3], next_cursor=3, has_more=True),
            Page(items=[4, 5, 6], next_cursor=6, has_more=False),
        ]
        call_count = 0

        def fetch(cursor):
            nonlocal call_count
            page = pages[call_count]
            call_count += 1
            return page

        paginator = CursorPaginator(sync_fetch=fetch)
        result = paginator.first(4)
        assert result == [1, 2, 3, 4]

    def test_sync_only_error(self):
        paginator = CursorPaginator(sync_fetch=lambda c: Page([], has_more=False))
        assert paginator._sync_fetch is not None

    def test_async_only_paginator(self):
        async def async_fetch(cursor):
            return Page([], has_more=False)

        paginator = CursorPaginator(async_fetch=async_fetch)
        assert paginator._async_fetch is not None
        assert paginator._sync_fetch is None


class TestPagePaginator:
    """Tests for PagePaginator."""

    def test_page_number_iteration(self):
        pages = [
            Page(items=[1, 2], next_cursor=2, has_more=True),
            Page(items=[3, 4], next_cursor=4, has_more=False),
        ]
        call_count = 0

        def fetch(page_num):
            nonlocal call_count
            page = pages[call_count]
            call_count += 1
            return page

        paginator = PagePaginator(sync_fetch=fetch)
        result = list(paginator)
        assert result == [1, 2, 3, 4]

    def test_initial_page(self):
        pages = [Page(items=[1], has_more=False)]

        def fetch(page_num):
            assert page_num == 5
            return pages[0]

        paginator = PagePaginator(sync_fetch=fetch, initial_page=5)
        result = list(paginator)
        assert result == [1]


class TestOffsetPaginator:
    """Tests for OffsetPaginator."""

    def test_offset_iteration(self):
        pages = [
            Page(items=[1, 2], next_cursor=2, has_more=True),
            Page(items=[3, 4], next_cursor=4, has_more=False),
        ]
        call_count = 0

        def fetch(offset):
            nonlocal call_count
            page = pages[call_count]
            call_count += 1
            return page

        paginator = OffsetPaginator(sync_fetch=fetch)
        result = list(paginator)
        assert result == [1, 2, 3, 4]

    def test_initial_offset(self):
        pages = [Page(items=[1], has_more=False)]

        def fetch(offset):
            assert offset == 10
            return pages[0]

        paginator = OffsetPaginator(sync_fetch=fetch, initial_offset=10)
        result = list(paginator)
        assert result == [1]


class TestAsyncPaginator:
    """Tests for async pagination."""

    @pytest.mark.asyncio
    async def test_async_iteration(self):
        pages = [
            Page(items=[1, 2], next_cursor=2, has_more=True),
            Page(items=[3, 4], next_cursor=4, has_more=False),
        ]
        call_count = 0

        async def async_fetch(cursor):
            nonlocal call_count
            page = pages[call_count]
            call_count += 1
            return page

        paginator = CursorPaginator(async_fetch=async_fetch)
        result = []
        async for item in paginator:
            result.append(item)
        assert result == [1, 2, 3, 4]

    @pytest.mark.asyncio
    async def test_async_first(self):
        pages = [
            Page(items=[1, 2, 3], next_cursor=3, has_more=True),
            Page(items=[4, 5, 6], next_cursor=6, has_more=False),
        ]
        call_count = 0

        async def async_fetch(cursor):
            nonlocal call_count
            page = pages[call_count]
            call_count += 1
            return page

        paginator = CursorPaginator(async_fetch=async_fetch)
        result = await paginator.afirst(4)
        assert result == [1, 2, 3, 4]
