"""Extended tests for dataset exporter."""

from __future__ import annotations

import tempfile
from pathlib import Path

import pytest

from socialmedia_hub.dataset.exporter import DatasetExporter


class TestDatasetExporterExtended:
    """Extended tests for DatasetExporter."""

    def test_export_to_csv(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            exporter = DatasetExporter(output_dir=tmpdir)
            data = [{"id": 1, "name": "test"}, {"id": 2, "name": "test2"}]
            filepath = exporter.export_csv(data, "test")
            assert filepath.exists()
            assert filepath.suffix == ".csv"

    def test_export_to_json(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            exporter = DatasetExporter(output_dir=tmpdir)
            data = [{"id": 1, "name": "test"}]
            filepath = exporter.export_json(data, "test")
            assert filepath.exists()
            assert filepath.suffix == ".json"

    def test_export_to_jsonl(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            exporter = DatasetExporter(output_dir=tmpdir)
            data = [{"id": 1, "name": "test"}]
            filepath = exporter.export_jsonl(data, "test")
            assert filepath.exists()
            assert filepath.suffix == ".jsonl"

    def test_export_to_buffer_json(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            exporter = DatasetExporter(output_dir=tmpdir)
            data = [{"id": 1, "name": "test"}]
            result = exporter.export_to_buffer(data, "json")
            assert isinstance(result, str)
            assert "test" in result

    def test_export_to_buffer_csv(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            exporter = DatasetExporter(output_dir=tmpdir)
            data = [{"id": 1, "name": "test"}]
            result = exporter.export_to_buffer(data, "csv")
            assert isinstance(result, str)

    def test_export_to_buffer_jsonl(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            exporter = DatasetExporter(output_dir=tmpdir)
            data = [{"id": 1, "name": "test"}]
            result = exporter.export_to_buffer(data, "jsonl")
            assert isinstance(result, str)

    def test_get_stats(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            exporter = DatasetExporter(output_dir=tmpdir)
            data = [{"id": 1, "name": "test"}, {"id": 2, "name": "test2"}]
            stats = exporter.get_stats(data)
            assert stats["count"] == 2
            assert "fields" in stats
