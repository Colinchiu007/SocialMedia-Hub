"""Tests for automation module."""

from __future__ import annotations

import asyncio
import tempfile
from pathlib import Path

import pytest

from socialmedia_hub.automation.batch import BatchProcessor
from socialmedia_hub.automation.exporter import DataExporter
from socialmedia_hub.automation.scheduler import TaskScheduler, TaskStatus


class TestBatchProcessor:
    """Tests for BatchProcessor."""

    def test_init(self):
        processor = BatchProcessor(max_concurrent=5, delay_between=0.1)
        assert processor.max_concurrent == 5
        assert processor.delay_between == 0.1

    @pytest.mark.asyncio
    async def test_process_urls_sync(self):
        processor = BatchProcessor(delay_between=0)
        urls = ["url1", "url2", "url3"]

        def process(url):
            return {"url": url, "status": "ok"}

        result = processor.process_urls_sync(urls, process)
        assert result["total"] == 3
        assert result["success"] == 3
        assert result["failed"] == 0

    @pytest.mark.asyncio
    async def test_process_urls_async(self):
        processor = BatchProcessor(delay_between=0)
        urls = ["url1", "url2"]

        async def process(url):
            return {"url": url, "status": "ok"}

        result = await processor.process_urls(urls, process)
        assert result["total"] == 2
        assert result["success"] == 2

    def test_get_stats(self):
        processor = BatchProcessor()
        stats = processor.get_stats()
        assert stats["total"] == 0


class TestDataExporter:
    """Tests for DataExporter."""

    def test_init(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            exporter = DataExporter(output_dir=tmpdir)
            assert Path(tmpdir).exists()

    def test_export_json(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            exporter = DataExporter(output_dir=tmpdir)
            data = [{"id": 1, "name": "test"}]
            filepath = exporter.export_json(data, "test")
            assert filepath.exists()
            assert filepath.suffix == ".json"

    def test_export_csv(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            exporter = DataExporter(output_dir=tmpdir)
            data = [{"id": 1, "name": "test"}]
            filepath = exporter.export_csv(data, "test")
            assert filepath.exists()
            assert filepath.suffix == ".csv"

    def test_export_jsonl(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            exporter = DataExporter(output_dir=tmpdir)
            data = [{"id": 1, "name": "test"}]
            filepath = exporter.export_jsonl(data, "test")
            assert filepath.exists()
            assert filepath.suffix == ".jsonl"

    def test_get_stats(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            exporter = DataExporter(output_dir=tmpdir)
            stats = exporter.get_stats()
            assert stats["files"] == 0


class TestTaskScheduler:
    """Tests for TaskScheduler."""

    def test_init(self):
        scheduler = TaskScheduler()
        assert scheduler._tasks == {}

    def test_add_task(self):
        scheduler = TaskScheduler()
        task_id = scheduler.add_task("test_task", lambda: None, interval=60)
        assert task_id is not None
        assert len(scheduler._tasks) == 1

    def test_remove_task(self):
        scheduler = TaskScheduler()
        task_id = scheduler.add_task("test_task", lambda: None)
        result = scheduler.remove_task(task_id)
        assert result is True
        assert len(scheduler._tasks) == 0

    def test_get_task(self):
        scheduler = TaskScheduler()
        task_id = scheduler.add_task("test_task", lambda: None)
        task = scheduler.get_task(task_id)
        assert task is not None
        assert task.name == "test_task"

    def test_get_all_tasks(self):
        scheduler = TaskScheduler()
        scheduler.add_task("task1", lambda: None)
        scheduler.add_task("task2", lambda: None)
        tasks = scheduler.get_all_tasks()
        assert len(tasks) == 2

    @pytest.mark.asyncio
    async def test_run_task(self):
        scheduler = TaskScheduler()
        task_id = scheduler.add_task("test_task", lambda: "result")
        task = scheduler.get_task(task_id)
        result = await scheduler.run_task(task)
        assert result["status"] == "success"

    def test_get_stats(self):
        scheduler = TaskScheduler()
        scheduler.add_task("task1", lambda: None)
        stats = scheduler.get_stats()
        assert stats["total_tasks"] == 1
