"""Dataset export functionality for SocialMedia-Hub."""

from __future__ import annotations

import csv
import io
import json
import logging
from pathlib import Path
from typing import Any

logger = logging.getLogger("socialmedia_hub.dataset")


class DatasetExporter:
    """Export social media data to various formats."""

    def __init__(self, output_dir: str | Path = "exports") -> None:
        """Initialize exporter.

        Args:
            output_dir: Directory to save exported files
        """
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def export_csv(
        self,
        data: list[dict[str, Any]],
        filename: str,
        fields: list[str] | None = None,
    ) -> Path:
        """Export data to CSV format.

        Args:
            data: List of dictionaries to export
            filename: Output filename (without extension)
            fields: Specific fields to export (None for all)

        Returns:
            Path to the exported file
        """
        filepath = self.output_dir / f"{filename}.csv"

        if not data:
            logger.warning("No data to export")
            return filepath

        # Determine fields
        if not fields:
            fields = list(data[0].keys())

        with open(filepath, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
            writer.writeheader()
            writer.writerows(data)

        logger.info(f"Exported {len(data)} records to {filepath}")
        return filepath

    def export_json(
        self,
        data: list[dict[str, Any]],
        filename: str,
        indent: int = 2,
    ) -> Path:
        """Export data to JSON format.

        Args:
            data: List of dictionaries to export
            filename: Output filename (without extension)
            indent: JSON indentation

        Returns:
            Path to the exported file
        """
        filepath = self.output_dir / f"{filename}.json"

        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=indent, ensure_ascii=False)

        logger.info(f"Exported {len(data)} records to {filepath}")
        return filepath

    def export_jsonl(
        self,
        data: list[dict[str, Any]],
        filename: str,
    ) -> Path:
        """Export data to JSONL (JSON Lines) format.

        Args:
            data: List of dictionaries to export
            filename: Output filename (without extension)

        Returns:
            Path to the exported file
        """
        filepath = self.output_dir / f"{filename}.jsonl"

        with open(filepath, "w", encoding="utf-8") as f:
            for record in data:
                f.write(json.dumps(record, ensure_ascii=False) + "\n")

        logger.info(f"Exported {len(data)} records to {filepath}")
        return filepath

    def export_parquet(
        self,
        data: list[dict[str, Any]],
        filename: str,
    ) -> Path:
        """Export data to Parquet format.

        Args:
            data: List of dictionaries to export
            filename: Output filename (without extension)

        Returns:
            Path to the exported file
        """
        try:
            import pandas as pd

            filepath = self.output_dir / f"{filename}.parquet"
            df = pd.DataFrame(data)
            df.to_parquet(filepath, index=False)

            logger.info(f"Exported {len(data)} records to {filepath}")
            return filepath
        except ImportError:
            logger.error("pandas is required for Parquet export")
            raise

    def export_to_buffer(
        self,
        data: list[dict[str, Any]],
        format: str = "json",
    ) -> str:
        """Export data to a string buffer.

        Args:
            data: List of dictionaries to export
            format: Export format ('json', 'csv', 'jsonl')

        Returns:
            Exported data as string
        """
        if format == "json":
            return json.dumps(data, indent=2, ensure_ascii=False)
        elif format == "csv":
            if not data:
                return ""
            fields = list(data[0].keys())
            output = io.StringIO()
            writer = csv.DictWriter(output, fieldnames=fields, extrasaction="ignore")
            writer.writeheader()
            writer.writerows(data)
            return output.getvalue()
        elif format == "jsonl":
            return "\n".join(json.dumps(record, ensure_ascii=False) for record in data)
        else:
            raise ValueError(f"Unsupported format: {format}")

    def get_stats(self, data: list[dict[str, Any]]) -> dict[str, Any]:
        """Get statistics about the data.

        Args:
            data: List of dictionaries

        Returns:
            Statistics dictionary
        """
        if not data:
            return {"count": 0, "fields": []}

        fields: set[str] = set()
        for record in data:
            fields.update(record.keys())

        return {
            "count": len(data),
            "fields": sorted(fields),
            "sample_size": min(10, len(data)),
        }
