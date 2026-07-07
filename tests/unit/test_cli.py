"""Tests for CLI module."""

from __future__ import annotations

from unittest.mock import MagicMock, patch

from typer.testing import CliRunner

from socialmedia_hub.cli.main import app

runner = CliRunner()


class TestCLI:
    """Tests for CLI commands."""

    def test_version(self) -> None:
        result = runner.invoke(app, ["version"])
        assert result.exit_code == 0
        assert "socialmedia-hub" in result.output

    def test_help(self) -> None:
        result = runner.invoke(app, ["--help"])
        assert result.exit_code == 0
        assert "SocialMedia-Hub CLI" in result.output

    def test_health_success(self) -> None:
        mock_response = MagicMock()
        mock_response.json.return_value = {"status": "ok"}
        mock_client = MagicMock()
        mock_client.__enter__ = MagicMock(return_value=mock_client)
        mock_client.__exit__ = MagicMock(return_value=False)
        mock_client.get.return_value = mock_response

        with patch("socialmedia_hub.cli.main.httpx.Client", return_value=mock_client):
            result = runner.invoke(app, ["health"])
            assert result.exit_code == 0
            assert "ok" in result.output

    def test_health_error(self) -> None:
        mock_client = MagicMock()
        mock_client.__enter__ = MagicMock(return_value=mock_client)
        mock_client.__exit__ = MagicMock(return_value=False)
        mock_client.get.side_effect = Exception("Connection refused")

        with patch("socialmedia_hub.cli.main.httpx.Client", return_value=mock_client):
            result = runner.invoke(app, ["health"])
            assert result.exit_code == 1
            assert "Error" in result.output

    def test_platforms_requires_api_key(self) -> None:
        result = runner.invoke(app, ["platforms"], catch_exceptions=False)
        assert result.exit_code != 0

    def test_server_help(self) -> None:
        result = runner.invoke(app, ["server", "--help"])
        assert result.exit_code == 0
        assert "Server management" in result.output
