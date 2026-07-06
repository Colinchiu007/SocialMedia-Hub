"""Tests for pagination helpers."""

from __future__ import annotations

from socialmedia_hub._pagination import (
    CursorPaginator,
    OffsetPaginator,
    Page,
    PagePaginator,
)


class TestCursorPaginator:
    """Test CursorPaginator."""

    def test_iter(self) -> None:
        pages = [
            Page(items=[1, 2], next_cursor=2, has_more=True),
            Page(items=[3, 4], next_cursor=4, has_more=False),
        ]
        call_count = 0

        def fetch(cursor: int) -> Page[int]:
            nonlocal call_count
            page = pages[call_count]
            call_count += 1
            return page

        paginator = CursorPaginator(sync_fetch=fetch)
        result = list(paginator)
        assert result == [1, 2, 3, 4]

    def test_first(self) -> None:
        pages = [
            Page(items=[1, 2, 3], next_cursor=3, has_more=True),
            Page(items=[4, 5, 6], next_cursor=6, has_more=False),
        ]
        call_count = 0

        def fetch(cursor: int) -> Page[int]:
            nonlocal call_count
            page = pages[call_count]
            call_count += 1
            return page

        paginator = CursorPaginator(sync_fetch=fetch)
        result = paginator.first(4)
        assert result == [1, 2, 3, 4]

    def test_initial_cursor(self) -> None:
        def fetch(cursor: int) -> Page[int]:
            assert cursor == 0
            return Page(items=[], has_more=False)

        paginator = CursorPaginator(sync_fetch=fetch, initial_cursor=0)
        list(paginator)


class TestPagePaginator:
    """Test PagePaginator."""

    def test_initial_page(self) -> None:
        def fetch(page: int) -> Page[str]:
            assert page == 1
            return Page(items=["a"], has_more=False)

        paginator = PagePaginator(sync_fetch=fetch, initial_page=1)
        result = list(paginator)
        assert result == ["a"]


class TestOffsetPaginator:
    """Test OffsetPaginator."""

    def test_initial_offset(self) -> None:
        def fetch(offset: int) -> Page[str]:
            assert offset == 0
            return Page(items=["a", "b"], has_more=False)

        paginator = OffsetPaginator(sync_fetch=fetch, initial_offset=0)
        result = list(paginator)
        assert result == ["a", "b"]
