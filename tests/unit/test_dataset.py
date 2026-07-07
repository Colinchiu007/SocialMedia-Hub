"""Tests for dataset export functionality."""

from __future__ import annotations

import json
import tempfile
from pathlib import Path

import pytest

from socialmedia_hub.dataset.exporter import DatasetExporter


@pytest.fixture
def sample_data():
    return [
        {"id": 1, "title": "Video 1", "views": 1000, "likes": 100},
        {"id": 2, "title": "Video 2", "views": 2000, "likes": 200},
        {"id": 3, "title": "Video 3", "views": 3000, "likes": 300},
    ]


@pytest.fixture
def exporter():
    with tempfile.TemporaryDirectory() as tmpdir:
        yield DatasetExporter(output_dir=tmpdir)


class TestDatasetExporter:
    """Test DatasetExporter."""

    def test_export_csv(self, exporter, sample_data):
        filepath = exporter.export_csv(sample_data, "test_data")
        assert filepath.exists()
        assert filepath.suffix == ".csv"

    def test_export_csv_with_fields(self, exporter, sample_data):
        filepath = exporter.export_csv(sample_data, "test_data", fields=["id", "title"])
        assert filepath.exists()

    def test_export_json(self, exporter, sample_data):
        filepath = exporter.export_json(sample_data, "test_data")
        assert filepath.exists()
        assert filepath.suffix == ".json"

    def test_export_jsonl(self, exporter, sample_data):
        filepath = exporter.export_jsonl(sample_data, "test_data")
        assert filepath.exists()
        assert filepath.suffix == ".jsonl"

    def test_export_to_buffer_json(self, exporter, sample_data):
        result = exporter.export_to_buffer(sample_data, format="json")
        assert isinstance(result, str)
        data = json.loads(result)
        assert len(data) == 3

    def test_export_to_buffer_csv(self, exporter, sample_data):
        result = exporter.export_to_buffer(sample_data, format="csv")
        assert isinstance(result, str)
        assert "id" in result
        assert "title" in result

    def test_export_to_buffer_jsonl(self, exporter, sample_data):
        result = exporter.export_to_buffer(sample_data, format="jsonl")
        assert isinstance(result, str)
        lines = result.strip().split("\n")
        assert len(lines) == 3

    def test_get_stats(self, exporter, sample_data):
        stats = exporter.get_stats(sample_data)
        assert stats["count"] == 3
        assert "id" in stats["fields"]
        assert "title" in stats["fields"]

    def test_empty_data(self, exporter):
        stats = exporter.get_stats([])
        assert stats["count"] == 0
        assert stats["fields"] == []
