"""Batch processing for social media data collection."""

from __future__ import annotations

import asyncio
import logging
from typing import Any, Callable

logger = logging.getLogger("socialmedia_hub.automation.batch")


class BatchProcessor:
    """Process multiple URLs or tasks in batch.

    Features:
    - Concurrent processing with rate limiting
    - Progress tracking
    - Error handling and retry
    - Result aggregation
    """

    def __init__(
        self,
        max_concurrent: int = 5,
        delay_between: float = 1.0,
        max_retries: int = 3,
    ) -> None:
        """Initialize batch processor.

        Args:
            max_concurrent: Maximum concurrent requests
            delay_between: Delay between requests (seconds)
            max_retries: Maximum retries per item
        """
        self.max_concurrent = max_concurrent
        self.delay_between = delay_between
        self.max_retries = max_retries
        self._results: list[dict[str, Any]] = []
        self._errors: list[dict[str, Any]] = []

    async def process_urls(
        self,
        urls: list[str],
        processor: Callable[[str], Any],
        progress_callback: Callable[[int, int, dict[str, Any]] | None] = None,
    ) -> dict[str, Any]:
        """Process a list of URLs concurrently.

        Args:
            urls: List of URLs to process
            processor: Async function to process each URL
            progress_callback: Optional callback for progress updates

        Returns:
            Dictionary with results and errors
        """
        self._results = []
        self._errors = []
        total = len(urls)

        # Create semaphore for concurrency control
        semaphore = asyncio.Semaphore(self.max_concurrent)

        async def process_one(url: str, index: int) -> None:
            async with semaphore:
                for attempt in range(self.max_retries):
                    try:
                        result = await processor(url)
                        self._results.append({
                            "url": url,
                            "index": index,
                            "result": result,
                            "attempt": attempt + 1,
                        })
                        if progress_callback:
                            progress_callback(index + 1, total, result)
                        break
                    except Exception as e:
                        if attempt == self.max_retries - 1:
                            self._errors.append({
                                "url": url,
                                "index": index,
                                "error": str(e),
                                "attempts": attempt + 1,
                            })
                            logger.error(f"Failed after {self.max_retries} attempts: {url}")

                # Delay between requests
                if self.delay_between > 0:
                    await asyncio.sleep(self.delay_between)

        # Process all URLs
        tasks = [process_one(url, i) for i, url in enumerate(urls)]
        await asyncio.gather(*tasks)

        return {
            "total": total,
            "success": len(self._results),
            "failed": len(self._errors),
            "results": self._results,
            "errors": self._errors,
        }

    def process_urls_sync(
        self,
        urls: list[str],
        processor: Callable[[str], Any],
        progress_callback: Callable[[int, int, dict[str, Any]] | None] = None,
    ) -> dict[str, Any]:
        """Process URLs synchronously.

        Args:
            urls: List of URLs to process
            processor: Function to process each URL
            progress_callback: Optional callback for progress updates

        Returns:
            Dictionary with results and errors
        """
        import time

        self._results = []
        self._errors = []
        total = len(urls)

        for index, url in enumerate(urls):
            for attempt in range(self.max_retries):
                try:
                    result = processor(url)
                    self._results.append({
                        "url": url,
                        "index": index,
                        "result": result,
                        "attempt": attempt + 1,
                    })
                    if progress_callback:
                        progress_callback(index + 1, total, result)
                    break
                except Exception as e:
                    if attempt == self.max_retries - 1:
                        self._errors.append({
                            "url": url,
                            "index": index,
                            "error": str(e),
                            "attempts": attempt + 1,
                        })

            if self.delay_between > 0:
                time.sleep(self.delay_between)

        return {
            "total": total,
            "success": len(self._results),
            "failed": len(self._errors),
            "results": self._results,
            "errors": self._errors,
        }

    def get_stats(self) -> dict[str, Any]:
        """Get processing statistics."""
        return {
            "total": len(self._results) + len(self._errors),
            "success": len(self._results),
            "failed": len(self._errors),
            "success_rate": len(self._results) / max(1, len(self._results) + len(self._errors)),
        }
