# Architecture 文档

## 系统架构概览

```
┌─────────────────────────────────────────────────────────────────────────┐
│                          SocialMedia-Hub                               │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐     │
│  │   SDK Client    │    │   API Server    │    │   MCP Server    │     │
│  │                 │    │                 │    │                 │     │
│  │  SocialMedia    │    │    FastAPI      │    │  1000 Tools    │     │
│  │  Hub / Async    │───▶│    1068 路由    │───▶│  16 平台        │     │
│  │  SocialMedia    │    │    认证+限流     │    │  AI Agent 集成  │     │
│  │  Hub            │    │                 │    │                 │     │
│  └─────────────────┘    └─────────────────┘    └─────────────────┘     │
│         │                      │                      │                 │
│         ▼                      ▼                      ▼                 │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │                     HTTP Proxy Layer                            │   │
│  │  httpx (sync/async) + 自动重试 + 指数退避 + 限流感知           │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│         │                                                              │
│         ▼                                                              │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │                  16+ Social Media Platforms                     │   │
│  │  TikTok │ Douyin │ Instagram │ YouTube │ Twitter │ Xiaohongshu │   │
│  │  Bilibili │ Weibo │ Kuaishou │ LinkedIn │ Reddit │ Zhihu      │   │
│  │  Threads │ WeChat │ Lemon8 │ NetEase Music │ ...              │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

## 核心组件

### 1. SDK Client (`_base_client.py`)

| 组件 | 职责 |
|------|------|
| `BaseClient` | 同步 HTTP 客户端 |
| `AsyncBaseClient` | 异步 HTTP 客户端 |
| `_request()` | 统一请求方法（重试、限流、错误处理） |

**关键特性**：
- 自动重试（指数退避，最大 30s）
- 限流感知（`Retry-After` 头）
- 结构化异常（15 种类型）
- Cookie + Header 双认证

### 2. API Server (`server/`)

| 组件 | 职责 |
|------|------|
| `main.py` | FastAPI 应用入口 |
| `_core.py` | 共享核心（认证、代理、平台配置） |
| `routes/auto_*.py` | 自动生成的路由（1010 端点） |
| `routes/*.py` | 手写路由（Live Room、NetEase） |

**路由注册顺序**（重要）：
1. 自动生成的路由（按平台分组）
2. 手写路由（Live Room、NetEase）
3. 系统路由（Health、Auth、Monitor、MCP）
4. 通用代理路由（最后注册，避免拦截）

### 3. MCP Server (`mcp/server.py`)

| 组件 | 职责 |
|------|------|
| `MCPServer` | MCP 协议实现 |
| `_register_*_tools()` | 注册各平台工具 |
| `list_tools()` | 列出所有工具 |
| `call_tool()` | 调用指定工具 |

**工具分布**：1000 个工具覆盖 16 个平台

### 4. 代码生成管线 (`scripts/`)

```
spec/openapi.json
       │
       ▼
scripts/generate_resources.py
       │
       ├──▶ routes/auto_*.py (51 个文件)
       ├──▶ client.py
       └──▶ async_client.py
```

## 数据流

```
用户请求
    │
    ▼
SDK Client / HTTP Client
    │
    ▼
API Server (FastAPI)
    │
    ├──▶ 认证层 (API Key / Cookie)
    ├──▶ 限流层 (Rate Limit)
    ├──▶ 路由层 (Route Matching)
    │
    ▼
Proxy Layer (httpx)
    │
    ├──▶ 自动重试 (Exponential Backoff)
    ├──▶ 错误处理 (Structured Exceptions)
    │
    ▼
目标平台 API
    │
    ▼
响应标准化
    │
    ▼
返回用户
```

## 技术栈

| 层 | 技术 | 版本 |
|----|------|------|
| Web 框架 | FastAPI | >= 0.110 |
| HTTP 客户端 | httpx | >= 0.27 |
| 数据验证 | pydantic | >= 2.6 |
| 异步支持 | anyio | >= 4.0 |
| CLI | typer | >= 0.12 |
| 构建 | hatchling | - |
| 类型检查 | mypy | --strict |
| 代码规范 | ruff | - |
| 测试 | pytest | >= 8.0 |

## 安全设计

| 措施 | 实现 |
|------|------|
| API Key 认证 | Bearer Token + Cookie |
| 限流控制 | 基于时间窗口的滑动限流 |
| 密钥脱敏 | 异常信息中自动脱敏 Authorization |
| 输入验证 | 参数类型和范围验证 |
| CORS | 可配置的跨域策略 |

## 反爬机制

### RealProxyLayer

```
用户请求
    │
    ▼
① 速率检查（每分钟 10 个请求/平台）
    │
    ▼
② 随机延迟（1-3 秒）
    │
    ▼
③ Cookie 轮换（选择随机 Cookie）
    │
    ▼
④ 签名生成（X-Bogus, msToken）
    │
    ▼
⑤ 代理轮换（选择代理 IP）
    │
    ▼
⑥ 发送请求
    │
    ▼
⑦ 失败重试（429 自动等待）
```

### 配置参数

| 参数 | 默认值 | 说明 |
|------|--------|------|
| `min_delay` | 1.0s | 最小请求间隔 |
| `max_delay` | 3.0s | 最大请求间隔 |
| `max_requests_per_minute` | 10 | 每平台每分钟最大请求数 |
| `proxy_strategy` | round_robin | 代理轮换策略 |

## 扩展性

### 添加新平台

1. 在 `spec/openapi.json` 中添加端点定义
2. 运行 `python scripts/generate_resources.py`
3. 在 `PLATFORM_CONFIGS` 中添加平台配置
4. 在 MCP Server 中注册工具

### 添加新端点

1. 在对应平台的 OpenAPI tag 下添加端点
2. 运行代码生成脚本
3. 路由自动注册

## 性能考虑

| 指标 | 目标 | 实现 |
|------|------|------|
| 响应时间 | < 500ms (P95) | httpx 连接池 + 异步 |
| 并发 | 1000+ | FastAPI + uvicorn |
| 重试 | 指数退避 | 0.5s → 30s |
| 限流 | 滑动窗口 | 基于时间窗口 |
