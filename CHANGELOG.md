# Changelog

All notable changes to `socialmedia-hub` will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.2.0] - 2026-07-07

### Added

#### 测试覆盖率持续提升
- 新增 62 个测试 (260 → 322)
- WebSocket manager 覆盖率: 48% → 100%
- 新增 auto routes 集成测试覆盖 16+ 平台
- 新增 server 核心端点测试

### Changed
- 版本号更新至 1.2.0

## [1.1.0] - 2026-07-07

### Added

#### 测试覆盖率提升
- 新增 37 个测试 (223 → 260)
- `_auth.py` 覆盖率: 0% → 100%
- `_types.py` 覆盖率: 0% → 100%
- `_rate_limit.py` 覆盖率: 30% → 100%
- `_base_client.py` 覆盖率: 44% → 50%
- `cli/main.py` 覆盖率: 0% → 34%

### Changed
- 版本号更新至 1.1.0

## [1.0.0] - 2026-07-07

### Added

#### 类型安全
- 修复 mypy 类型错误 (49 → 0)
- 添加 ToolDef 类型别名
- 完善 signatures.py 和 exporter.py 类型注解

### Changed
- 版本号更新至 1.0.0 (正式发布)

## [0.9.0] - 2026-07-07

### Added

#### MCP 工具扩展至 1000+
- 新增 7 个次要平台 V3 工具 (LinkedIn/Reddit/Zhihu/Threads/WeChat/Lemon8/NetEase)
- 新增 29 个实用工具 (analytics/scheduler/batch/export/compare/trend/sentiment/tag/translate/summarize/hashtag/optimize/schedule/competitor)
- MCP 工具总数达到 1000 个

#### 工具分布
- 主要平台 (TikTok/Douyin/Instagram/YouTube/Twitter/Xiaohongshu/Bilibili/Weibo/Kuaishou): 各 60 个工具 (V1/V2/V3)
- 次要平台 (LinkedIn/Reddit/Zhihu/Threads/WeChat/Lemon8/NetEase): 各 27-30 个工具 (V1/V2/V3)
- 实用工具: 29 个

### Changed
- 版本号更新至 0.9.0

## [0.2.0] - 2026-07-06

### Added

#### RealProxyLayer (真实代理层)
- `CookieManager` - Cookie 存储/管理/过期处理
- `SignatureGenerator` - 抖音/TikTok/Instagram 签名生成
- `ProxyPool` - IP 轮换（round_robin/random/least_used/best_success）
- `RealProxyLayer` - 统一代理层（认证+签名+代理+限流）

#### WebSocket 支持
- WebSocket 管理器（连接管理、频道订阅、广播）
- 3 个 WebSocket 端点（live/subscribe/monitor）
- 实时数据推送支持

#### MCP 扩展
- MCP 工具从 150 扩展到 314
- 覆盖 16 个平台的完整工具集

#### 测试
- 新增 25 个代理层测试
- 总测试数达到 166

#### 文档
- 新增 Security Audit Report
- 更新 Quality Rhythm 至 v2

### Changed
- `proxy_request` 函数更新为使用 RealProxyLayer
- 集成 Cookie 管理、签名生成、代理轮换

## [0.1.0] - 2026-07-06

### Added

#### Core SDK
- `SocialMediaHub` (sync) and `AsyncSocialMediaHub` (async) clients
- Bearer-token authentication via constructor or `$SMH_API_KEY`
- Cookie-based authentication (Method 2)
- Automatic retry with exponential backoff
- Rate-limit-aware sleeping based on `Retry-After` headers
- Structured exception hierarchy (15 exception types)
- Context manager support (`with` / `async with`)
- Proper SDK exports in `__init__.py`

#### API Server
- FastAPI-based REST API server
- 1068 endpoints across 20 platforms
- Swagger UI at `/docs`
- ReDoc at `/redoc`
- OpenAPI spec at `/openapi.json`
- CORS support
- Generic platform proxy routes
- API Key management (create, verify)
- Rate limiting per API key

#### Platform APIs (20 platforms)
- **TikTok**: 150+ endpoints (Web, App V3, Creator, Analytics, Shop, Ads)
- **Douyin**: 234 endpoints (Web, App V3, Search, Billboard, Xingtu, Creator)
- **Instagram**: 88 endpoints (V1, V2, V3)
- **YouTube**: 40 endpoints (Web, Web V2)
- **Twitter/X**: 13 endpoints
- **Xiaohongshu**: 79 endpoints (Web, Web V2, Web V3, App, App V2)
- **Bilibili**: 41 endpoints (Web, App)
- **Weibo**: 64 endpoints (Web, Web V2, App)
- **Kuaishou**: 33 endpoints (Web, App)
- **LinkedIn**: 25 endpoints
- **Reddit**: 26 endpoints (App)
- **Zhihu**: 34 endpoints
- **Threads**: 11 endpoints
- **WeChat**: 20 endpoints (Channels, Media Platform)
- **Lemon8**: 16 endpoints
- **PiPiXia**: 17 endpoints
- **Sora2**: 17 endpoints
- **Xigua**: 7 endpoints
- **Toutiao**: 7 endpoints
- **NetEase Cloud Music**: 24 endpoints

#### MCP (Model Context Protocol)
- 150 MCP tools across 16 platforms
- MCP server implementation
- Claude Desktop integration support
- Tool listing and calling endpoints

#### Live Room API
- Real-time live streaming data endpoints
- Support for Douyin, TikTok, Bilibili, Kuaishou, Weibo
- Room info, danmaku, gift ranking, products

#### Monitoring & Health
- API status monitoring endpoints
- Platform health checks
- Metrics collection

#### CLI
- `smh` command-line tool
- `smh-server` for starting the API server
- Health check, URL parsing, API key management

#### Documentation
- PRD (Product Requirements Document)
- User Guide
- Feature Comparison with TikHub
- Quality Rhythm workflow integration

#### Testing
- 93 unit + integration tests
- API endpoint tests
- SDK client tests
- MCP server tests
- Integration tests (SDK + Server)

### Changed

- Migrated from hand-written routes to auto-generated routes from OpenAPI spec
- Improved MCP server with 150 tools (up from 36)
- Enhanced Cookie authentication support
- Added Swagger UI and ReDoc
- Fixed SDK exports (SocialMediaHub, AsyncSocialMediaHub)

### Fixed

- MCP route conflict with generic proxy route
- Import ordering issues
- Unused import warnings
- SDK client exports

## [Unreleased]

### Planned
- Chrome Extension for browser-based analytics
- Datasets marketplace
- WebSocket support for real-time data push
- Performance optimization
- Security hardening
