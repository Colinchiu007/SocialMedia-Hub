"""Pagination helpers for social media APIs."""

from __future__ import annotations

from collections.abc import AsyncIterator, Awaitable, Callable, Iterator
from typing import Any, Generic, TypeVar

T = TypeVar("T")


class _PaginatorBase(Generic[T]):
    """Common surface for sync + async paginators."""

    def __init__(self) -> None:
        self.has_more: bool = True

    def _advance(self) -> list[T]:
        raise NotImplementedError

    def __iter__(self) -> Iterator[T]:
        while self.has_more:
            yield from self._advance()

    def first(self, n: int) -> list[T]:
        """Eagerly collect at most n items."""
        out: list[T] = []
        for item in self:
            out.append(item)
            if len(out) >= n:
                break
        return out

    async def _aadvance(self) -> list[T]:
        raise NotImplementedError

    def __aiter__(self) -> AsyncIterator[T]:
        return self._aiter()

    async def _aiter(self) -> AsyncIterator[T]:
        while self.has_more:
            page = await self._aadvance()
            for item in page:
                yield item

    async def afirst(self, n: int) -> list[T]:
        """Async equivalent of first()."""
        out: list[T] = []
        async for item in self:
            out.append(item)
            if len(out) >= n:
                break
        return out


PageFn = Callable[[Any], "Page[T]"]
AsyncPageFn = Callable[[Any], Awaitable["Page[T]"]]


class Page(Generic[T]):
    """Result of one page fetch — items plus the cursor for the next call."""

    __slots__ = ("has_more", "items", "next_cursor")

    def __init__(
        self,
        items: list[T],
        *,
        next_cursor: Any = None,
        has_more: bool = False,
    ) -> None:
        self.items = items
        self.next_cursor = next_cursor
        self.has_more = has_more


class CursorPaginator(_PaginatorBase[T]):
    """Generic cursor pager."""

    def __init__(
        self,
        *,
        sync_fetch: PageFn[T] | None = None,
        async_fetch: AsyncPageFn[T] | None = None,
        initial_cursor: Any = 0,
    ) -> None:
        super().__init__()
        if sync_fetch is None and async_fetch is None:
            raise ValueError("CursorPaginator needs at least one of sync_fetch / async_fetch")
        self._sync_fetch = sync_fetch
        self._async_fetch = async_fetch
        self.cursor: Any = initial_cursor

    def _advance(self) -> list[T]:
        if self._sync_fetch is None:
            raise RuntimeError("This paginator is async-only.")
        page = self._sync_fetch(self.cursor)
        self.cursor = page.next_cursor
        self.has_more = page.has_more
        return page.items

    async def _aadvance(self) -> list[T]:
        if self._async_fetch is None:
            raise RuntimeError("This paginator is sync-only.")
        page = await self._async_fetch(self.cursor)
        self.cursor = page.next_cursor
        self.has_more = page.has_more
        return page.items


class PagePaginator(CursorPaginator[T]):
    """Page-number pager."""

    def __init__(
        self,
        *,
        sync_fetch: PageFn[T] | None = None,
        async_fetch: AsyncPageFn[T] | None = None,
        initial_page: int = 1,
    ) -> None:
        super().__init__(
            sync_fetch=sync_fetch, async_fetch=async_fetch, initial_cursor=initial_page
        )


class OffsetPaginator(CursorPaginator[T]):
    """Offset/limit pager."""

    def __init__(
        self,
        *,
        sync_fetch: PageFn[T] | None = None,
        async_fetch: AsyncPageFn[T] | None = None,
        initial_offset: int = 0,
    ) -> None:
        super().__init__(
            sync_fetch=sync_fetch, async_fetch=async_fetch, initial_cursor=initial_offset
        )
