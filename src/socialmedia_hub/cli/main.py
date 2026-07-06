"""CLI entry point for SocialMedia-Hub."""

from __future__ import annotations

import json

import httpx
import typer

app = typer.Typer(
    name="smh",
    help="SocialMedia-Hub CLI — multi-platform social media data tool.",
    no_args_is_help=True,
)

server_app = typer.Typer(help="Server management commands.")
app.add_typer(server_app, name="server")


def _print_json(data: object) -> None:
    print(json.dumps(data, indent=2, ensure_ascii=False, default=str))


@app.command()
def version():
    """Print the SDK version."""
    from socialmedia_hub._version import __version__
    print(f"socialmedia-hub {__version__}")


@app.command()
def health(
    base_url: str = typer.Option("http://127.0.0.1:8000", help="API server URL"),
):
    """Ping the API server health check."""
    try:
        with httpx.Client(timeout=10) as client:
            resp = client.get(f"{base_url}/api/v1/health/check")
            _print_json(resp.json())
    except Exception as e:
        typer.echo(f"Error: {e}", err=True)
        raise typer.Exit(1) from None


@app.command()
def platforms(
    base_url: str = typer.Option("http://127.0.0.1:8000", help="API server URL"),
    api_key: str = typer.Option(..., envvar="SMH_API_KEY", help="API key"),
):
    """List supported platforms."""
    try:
        with httpx.Client(timeout=10) as client:
            resp = client.get(
                f"{base_url}/api/v1/health/platforms",
                headers={"Authorization": f"Bearer {api_key}"},
            )
            _print_json(resp.json())
    except Exception as e:
        typer.echo(f"Error: {e}", err=True)
        raise typer.Exit(1) from None


@app.command()
def create_key(
    name: str = typer.Option("default", help="Key name"),
    tier: str = typer.Option("free", help="Key tier (free/pro/enterprise)"),
    base_url: str = typer.Option("http://127.0.0.1:8000", help="API server URL"),
):
    """Create a new API key."""
    try:
        with httpx.Client(timeout=10) as client:
            resp = client.post(
                f"{base_url}/api/v1/auth/create_key",
                params={"name": name, "tier": tier},
            )
            _print_json(resp.json())
    except Exception as e:
        typer.echo(f"Error: {e}", err=True)
        raise typer.Exit(1) from None


@app.command()
def fetch(
    url: str = typer.Argument(..., help="Social media URL to parse"),
    api_key: str = typer.Option(..., envvar="SMH_API_KEY", help="API key"),
    base_url: str = typer.Option("http://127.0.0.1:8000", help="API server URL"),
):
    """Universal social media URL parser."""
    # Auto-detect platform from URL
    platform = _detect_platform(url)
    if not platform:
        typer.echo("Could not detect platform from URL.", err=True)
        raise typer.Exit(1)

    try:
        with httpx.Client(timeout=30) as client:
            resp = client.get(
                f"{base_url}/api/v1/{platform}/fetch",
                params={"url": url},
                headers={"Authorization": f"Bearer {api_key}"},
            )
            _print_json(resp.json())
    except Exception as e:
        typer.echo(f"Error: {e}", err=True)
        raise typer.Exit(1) from None


def _detect_platform(url: str) -> str | None:
    """Detect social media platform from URL."""
    url_lower = url.lower()
    if "douyin.com" in url_lower or "v.douyin.com" in url_lower:
        return "douyin"
    if "tiktok.com" in url_lower:
        return "tiktok"
    if "instagram.com" in url_lower:
        return "instagram"
    if "youtube.com" in url_lower or "youtu.be" in url_lower:
        return "youtube"
    if "twitter.com" in url_lower or "x.com" in url_lower:
        return "twitter"
    if "xiaohongshu.com" in url_lower or "xhslink.com" in url_lower:
        return "xiaohongshu"
    if "bilibili.com" in url_lower:
        return "bilibili"
    if "weibo.com" in url_lower or "m.weibo.cn" in url_lower:
        return "weibo"
    if "kuaishou.com" in url_lower:
        return "kuaishou"
    if "reddit.com" in url_lower:
        return "reddit"
    if "threads.net" in url_lower:
        return "threads"
    if "linkedin.com" in url_lower:
        return "linkedin"
    if "zhihu.com" in url_lower:
        return "zhihu"
    return None


# ---------------------------------------------------------------------------
# Server subcommands
# ---------------------------------------------------------------------------


@server_app.command()
def start(
    host: str = typer.Option("0.0.0.0", help="Bind host"),
    port: int = typer.Option(8000, help="Bind port"),
):
    """Start the API server."""
    from socialmedia_hub.server.main import run_server
    run_server(host=host, port=port)


@server_app.command()
def status(
    base_url: str = typer.Option("http://127.0.0.1:8000", help="Server URL"),
):
    """Check server status."""
    try:
        with httpx.Client(timeout=5) as client:
            resp = client.get(f"{base_url}/api/v1/health/check")
            if resp.status_code == 200:
                data = resp.json()
                typer.echo(f"Server: OK (v{data.get('version', '?')})")
            else:
                typer.echo(f"Server: Error {resp.status_code}")
    except Exception:
        typer.echo("Server: Offline")
        raise typer.Exit(1) from None


def main():
    app()


if __name__ == "__main__":
    main()
