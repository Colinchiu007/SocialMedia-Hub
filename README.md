# SocialMedia-Hub

High-performance Python SDK and API server for multi-platform social media data.

**Version: v3.4.0**

## Features

- **20 platforms**: Douyin, TikTok, Instagram, YouTube, Twitter/X, Xiaohongshu, Bilibili, Weibo, Kuaishou, Threads, LinkedIn, Reddit, WeChat, Zhihu, Lemon8, NetEase Cloud Music, and more
- **1068+ endpoints**: Complete API coverage across all platforms
- **1000 MCP tools**: Model Context Protocol integration for AI agents
- **RealProxyLayer**: Cookie management, signature generation, proxy rotation
- **WebSocket support**: Real-time data push for live rooms
- **Chrome Extension**: Browser sidebar for social media analytics
- **LangChain integration**: 45 LangChain tools for AI workflows
- **Sync + async clients**: `SocialMediaHub` and `AsyncSocialMediaHub`
- **FastAPI server**: Production-ready API server with authentication and rate limiting
- **Type-safe**: `mypy --strict` clean, built on `httpx` + `pydantic v2`
- **CLI tool**: Command-line interface for quick access
- **Swagger UI**: Interactive API documentation at `/docs`
- **Live Room API**: Real-time live streaming data support

## Install

```bash
pip install socialmedia-hub
```

Requires Python 3.10+.

## Quick Start

### As SDK Client

```python
from socialmedia_hub import SocialMediaHub

# Connect to your local server
client = SocialMediaHub(api_key="YOUR_API_KEY", base_url="http://127.0.0.1:8000")

# Fetch a Douyin video
video = client.douyin.fetch_video(video_id="7251234567890123456")
print(video)

client.close()
```

### As API Server

```bash
# Start the server
smh-server start --port 8000

# Create an API key
smh create-key --name myapp --tier pro

# Use the CLI
smh health
smh fetch "https://v.douyin.com/abc/"
```

### As MCP Server

```python
from socialmedia_hub.mcp import create_mcp_server

# Create MCP server
mcp = create_mcp_server(api_key="YOUR_API_KEY")

# List available tools
tools = mcp.list_tools()
print(f"Available tools: {len(tools)}")

# Call a tool
result = mcp.call_tool("tiktok_fetch_video", {"video_id": "123"})
print(result)
```

## Supported Platforms

| Platform | Endpoints | Features |
|----------|-----------|----------|
| TikTok | 150+ | Video, User, Search, Live, Ads, Shop, Analytics |
| Douyin | 234 | Video, User, Search, Billboard, Xingtu, Creator |
| Instagram | 88 | User, Posts, Reels, Stories, Hashtags |
| YouTube | 40 | Video, Channel, Search, Trending |
| Twitter/X | 13 | Tweets, Users, Search, Trending |
| Xiaohongshu | 79 | Notes, Users, Comments, Search |
| Bilibili | 41 | Video, User, Danmaku, Live |
| Weibo | 64 | Posts, Users, Topics, Search |
| Kuaishou | 33 | Video, User, Live |
| LinkedIn | 25 | Profiles, Posts, Jobs |
| Reddit | 26 | Posts, Comments, Subreddits |
| Zhihu | 34 | Questions, Answers, Articles |
| Threads | 11 | Users, Posts, Comments |
| WeChat | 20 | Channels, Media Platform |
| Lemon8 | 16 | Posts, Users, Trending |
| NetEase Music | 24 | Songs, Playlists, Artists |

## Architecture

```
Client SDK                    API Server
─────────                    ──────────
SocialMediaHub ──HTTP──→ FastAPI Server
                              │
                              ├── Auth layer (API key + rate limiting)
                              ├── Router (platform detection)
                              ├── Proxy layer (httpx → platform APIs)
                              └── Response normalization
```

## Documentation

- [PRD](docs/PRD.md) - Product Requirements Document
- [User Guide](docs/USER_GUIDE.md) - Complete usage guide
- [Feature Comparison](docs/FEATURE_COMPARISON.md) - vs TikHub comparison
- [Quality Rhythm](docs/QUALITY_RHYTHM.md) - Development workflow

## Development

```bash
git clone https://github.com/SocialMedia-Hub/SocialMedia-Hub.git
cd SocialMedia-Hub
pip install -e ".[dev]"

# Run tests
pytest -v

# Run linter
ruff check src/ tests/

# Run type checker
mypy --strict src/socialmedia_hub
```

## License

MIT
