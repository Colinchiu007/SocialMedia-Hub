"""Data export for social media automation."""

from __future__ import annotations

import csv
import json
import logging
from pathlib import Path
from typing import Any

logger = logging.getLogger("socialmedia_hub.automation.exporter")


class DataExporter:
    """Export social media data to various formats.

    Supported formats:
    - JSON
    - CSV
    - JSON Lines (JSONL)
    """

    def __init__(self, output_dir: str | Path = "output") -> None:
        """Initialize exporter.

        Args:
            output_dir: Directory to save exported files
        """
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def export_json(
        self,
        data: list[dict[str, Any]],
        filename: str,
        indent: int = 2,
    ) -> Path:
        """Export data to JSON file.

        Args:
            data: List of dictionaries to export
            filename: Output filename (without extension)
            indent: JSON indentation

        Returns:
            Path to exported file
        """
        filepath = self.output_dir / f"{filename}.json"
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=indent, ensure_ascii=False)
        logger.info(f"Exported {len(data)} records to {filepath}")
        return filepath

    def export_csv(
        self,
        data: list[dict[str, Any]],
        filename: str,
    ) -> Path:
        """Export data to CSV file.

        Args:
            data: List of dictionaries to export
            filename: Output filename (without extension)

        Returns:
            Path to exported file
        """
        if not data:
            raise ValueError("No data to export")

        filepath = self.output_dir / f"{filename}.csv"
        fields = list(data[0].keys())

        with open(filepath, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fields)
            writer.writeheader()
            writer.writerows(data)

        logger.info(f"Exported {len(data)} records to {filepath}")
        return filepath

    def export_jsonl(
        self,
        data: list[dict[str, Any]],
        filename: str,
    ) -> Path:
        """Export data to JSON Lines file.

        Args:
            data: List of dictionaries to export
            filename: Output filename (without extension)

        Returns:
            Path to exported file
        """
        filepath = self.output_dir / f"{filename}.jsonl"
        with open(filepath, "w", encoding="utf-8") as f:
            for record in data:
                f.write(json.dumps(record, ensure_ascii=False) + "\n")

        logger.info(f"Exported {len(data)} records to {filepath}")
        return filepath

    def export_batch(
        self,
        results: dict[str, Any],
        filename: str,
        format: str = "json",
    ) -> Path:
        """Export batch processing results.

        Args:
            results: Batch processing results dictionary
            filename: Output filename (without extension)
            format: Export format ('json', 'csv', 'jsonl')

        Returns:
            Path to exported file
        """
        data = results.get("results", [])

        if format == "json":
            return self.export_json(data, filename)
        elif format == "csv":
            return self.export_csv(data, filename)
        elif format == "jsonl":
            return self.export_jsonl(data, filename)
        else:
            raise ValueError(f"Unsupported format: {format}")

    def get_stats(self) -> dict[str, Any]:
        """Get exporter statistics."""
        files = list(self.output_dir.glob("*"))
        total_size = sum(f.stat().st_size for f in files if f.is_file())
        return {
            "output_dir": str(self.output_dir),
            "files": len(files),
            "total_size_mb": total_size / (1024 * 1024),
        }
