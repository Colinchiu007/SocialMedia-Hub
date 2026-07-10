"""Final tests for exporter to achieve 100% coverage."""

from __future__ import annotations

import tempfile
from pathlib import Path

import pytest

from socialmedia_hub.dataset.exporter import DatasetExporter


class TestExporterFinal:
    """Final tests for DatasetExporter."""

    def test_export_csv_empty_data(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            exporter = DatasetExporter(output_dir=tmpdir)
            filepath = exporter.export_csv([], "empty")
            # Empty data logs warning but still returns filepath
            assert filepath is not None

    def test_export_csv_with_fields(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            exporter = DatasetExporter(output_dir=tmpdir)
            data = [{"id": 1, "name": "test"}]
            filepath = exporter.export_csv(data, "test", fields=["id", "name"])
            assert filepath.exists()

    def test_export_json_empty_data(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            exporter = DatasetExporter(output_dir=tmpdir)
            filepath = exporter.export_json([], "empty")
            assert filepath.exists()

    def test_export_jsonl_empty_data(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            exporter = DatasetExporter(output_dir=tmpdir)
            filepath = exporter.export_jsonl([], "empty")
            assert filepath.exists()

    def test_export_parquet_no_pandas(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            exporter = DatasetExporter(output_dir=tmpdir)
            data = [{"id": 1, "name": "test"}]
            # This should raise ImportError if pandas is not installed
            try:
                filepath = exporter.export_parquet(data, "test")
                assert filepath.exists()
            except ImportError:
                pass  # pandas not installed

    def test_export_to_buffer_json(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            exporter = DatasetExporter(output_dir=tmpdir)
            data = [{"id": 1, "name": "test"}]
            result = exporter.export_to_buffer(data, "json")
            assert isinstance(result, str)

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
