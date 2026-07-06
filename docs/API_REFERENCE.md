# API Reference

> 本文档自动生成，覆盖 SocialMedia-Hub 的所有 API 端点。

## 认证

所有 API 请求需要在 Header 中携带 API Key：

```
Authorization: Bearer YOUR_API_KEY
```

或在 Cookie 中：

```
Authorization=Bearer YOUR_API_KEY
```

## 基础端点

### 健康检查

```
GET /api/v1/health/check
```

**响应**：
```json
{
  "status": "ok",
  "version": "0.1.0",
  "timestamp": "2026-07-06T00:00:00Z"
}
```

### 平台列表

```
GET /api/v1/health/platforms
```

**响应**：
```json
{
  "platforms": ["douyin", "tiktok", "instagram", ...],
  "count": 20
}
```

### API 统计

```
GET /api/v1/health/stats
```

**响应**：
```json
{
  "total_endpoints": 1068,
  "platforms": 20,
  "active_keys": 5,
  "version": "0.1.0",
  "mcp_tools": 150
}
```

## 认证管理

### 创建 API Key

```
POST /api/v1/auth/create_key?name=myapp&tier=free
```

**参数**：
- `name` (string): 应用名称
- `tier` (string): 套餐类型 (free/pro/enterprise)

**响应**：
```json
{
  "api_key": "smh_xxxxxxxxxxxxxxxx",
  "name": "myapp",
  "tier": "free"
}
```

### 验证 API Key

```
GET /api/v1/auth/verify
```

**响应**：
```json
{
  "valid": true,
  "name": "myapp",
  "tier": "free"
}
```

## 监控端点

### 服务器状态

```
GET /api/v1/monitor/status
```

**响应**：
```json
{
  "status": "operational",
  "version": "0.1.0",
  "uptime": "running",
  "platforms_supported": 20,
  "endpoints_total": 1068,
  "mcp_enabled": true,
  "swagger_enabled": true
}
```

### 性能指标

```
GET /api/v1/monitor/metrics
```

**响应**：
```json
{
  "requests_total": 1000,
  "requests_per_minute": 50,
  "error_rate": 0.01,
  "avg_response_time_ms": 150,
  "active_connections": 10,
  "rate_limit_hits": 2
}
```

### 平台状态

```
GET /api/v1/monitor/platforms
```

**响应**：
```json
{
  "platforms": {
    "douyin": {
      "name": "douyin",
      "base_url": "https://www.douyin.com",
      "status": "available",
      "endpoints": "dynamic"
    },
    ...
  },
  "count": 20
}
```

## MCP 端点

### 列出工具

```
GET /api/v1/mcp/tools
```

**响应**：
```json
{
  "tools": [
    {
      "name": "tiktok_fetch_video",
      "description": "Fetch TikTok video details",
      "inputSchema": {
        "type": "object",
        "properties": {
          "video_id": {"type": "string"}
        }
      }
    },
    ...
  ],
  "count": 150
}
```

### 调用工具

```
POST /api/v1/mcp/call
Content-Type: application/json

{
  "tool": "tiktok_fetch_video",
  "arguments": {
    "video_id": "123456"
  }
}
```

**响应**：
```json
{
  "result": {
    "data": {
      "id": "123456",
      "desc": "Video description",
      ...
    }
  }
}
```

### MCP 配置

```
GET /api/v1/mcp/config
```

**响应**：
```json
{
  "mcpServers": {
    "socialmedia-hub": {
      "command": "npx",
      "args": [
        "mcp-remote",
        "http://127.0.0.1:8000/api/v1/mcp/sse",
        "--header",
        "Authorization: Bearer YOUR_API_KEY"
      ]
    }
  }
}
```

## 平台端点

### 通用代理

```
GET /api/v1/{platform}/{path}
POST /api/v1/{platform}/{path}
```

**参数**：
- `platform`: 平台名称 (douyin, tiktok, instagram, etc.)
- `path`: API 路径

**示例**：
```bash
# 获取抖音视频
curl -H "Authorization: Bearer YOUR_API_KEY" \
     "http://localhost:8000/api/v1/douyin/web/fetch_one_video?aweme_id=123"

# 获取 TikTok 用户
curl -H "Authorization: Bearer YOUR_API_KEY" \
     "http://localhost:8000/api/v1/tiktok/web/fetch_user_profile?unique_id=username"
```

### Live Room 端点

```
GET /api/v1/live/{platform}/fetch_room_info
GET /api/v1/live/{platform}/fetch_room_danmaku
GET /api/v1/live/{platform}/fetch_gift_ranking
```

### NetEase Cloud Music 端点

```
GET /api/v1/netease/music/fetch_song_detail
GET /api/v1/netease/music/fetch_search
GET /api/v1/netease/music/fetch_playlist_detail
```

## 错误码

| 错误码 | 说明 |
|--------|------|
| 400 | 请求参数错误 |
| 401 | 认证失败 |
| 403 | 权限不足 |
| 404 | 资源不存在 |
| 429 | 请求频率超限 |
| 500 | 服务器内部错误 |
| 502/503/504 | 上游服务不可用 |

## SDK 使用

### 同步客户端

```python
from socialmedia_hub import SocialMediaHub

client = SocialMediaHub(api_key="YOUR_API_KEY")
result = client.some_api()
client.close()
```

### 异步客户端

```python
from socialmedia_hub import AsyncSocialMediaHub

async with AsyncSocialMediaHub(api_key="YOUR_API_KEY") as client:
    result = await client.some_api()
```

### MCP 客户端

```python
from socialmedia_hub.mcp import create_mcp_server

mcp = create_mcp_server(api_key="YOUR_API_KEY")
tools = mcp.list_tools()
result = mcp.call_tool("tool_name", {"arg": "value"})
```

## 更多信息

- [用户指南](USER_GUIDE.md)
- [架构文档](ARCHITECTURE.md)
- [部署指南](DEPLOYMENT.md)
- [故障排除](TROUBLESHOOTING.md)
