# Troubleshooting Guide

本文档帮助你解决使用 SocialMedia-Hub 时遇到的常见问题。

## 常见问题

### 1. 安装问题

#### 问题：pip install 失败

```bash
ERROR: Could not find a version that satisfies the requirement
```

**解决方案**：

```bash
# 确保 Python 版本 >= 3.10
python --version

# 升级 pip
pip install --upgrade pip

# 重试安装
pip install socialmedia-hub
```

#### 问题：依赖冲突

```bash
ERROR: pip's dependency resolver does not take into account all the packages installed
```

**解决方案**：

```bash
# 使用虚拟环境
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或
venv\Scripts\activate  # Windows

# 重新安装
pip install socialmedia-hub
```

### 2. 认证问题

#### 问题：401 Unauthorized

```bash
{"detail": "Missing Authorization header"}
```

**解决方案**：

```python
# 确保正确设置 API Key
client = SocialMediaHub(api_key="your_api_key_here")

# 或使用环境变量
export SMH_API_KEY="your_api_key_here"
client = SocialMediaHub()
```

#### 问题：API Key 无效

```bash
{"detail": "Invalid API key"}
```

**解决方案**：

```bash
# 创建新的 API Key
smh create-key --name myapp --tier free

# 验证 API Key
smh health
```

### 3. 连接问题

#### 问题：连接超时

```bash
httpx.ConnectTimeout: Connection timed out
```

**解决方案**：

```python
# 增加超时时间
client = SocialMediaHub(api_key="...", timeout=60)

# 或使用代理
client = SocialMediaHub(api_key="...", proxy="http://proxy:8080")
```

#### 问题：连接被拒绝

```bash
httpx.ConnectError: Connection refused
```

**解决方案**：

```bash
# 检查服务器是否运行
smh-server status

# 启动服务器
smh-server start --port 8000

# 检查端口
netstat -tulpn | grep 8000
```

### 4. API 问题

#### 问题：429 Too Many Requests

```bash
{"detail": "Rate limit exceeded"}
```

**解决方案**：

```python
# 等待后重试
import time
time.sleep(30)

# 或降低请求频率
for url in urls:
    result = client.some_api(url)
    time.sleep(1)  # 每次请求间隔 1 秒
```

#### 问题：500 Internal Server Error

```bash
{"detail": "Internal server error"}
```

**解决方案**：

```bash
# 检查服务器日志
docker logs -f socialmedia-hub

# 重启服务器
smh-server start
```

### 5. MCP 问题

#### 问题：MCP 工具调用失败

```python
{"error": "[WinError 10061] 由于目标计算机积极拒绝，无法连接。"}
```

**解决方案**：

```python
# 确保服务器正在运行
smh-server start

# 或检查 MCP 配置
smh mcp config
```

#### 问题：Claude Desktop 无法连接

**解决方案**：

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

### 6. 性能问题

#### 问题：响应慢

**解决方案**：

```python
# 使用异步客户端
import asyncio
from socialmedia_hub import AsyncSocialMediaHub

async def main():
    async with AsyncSocialMediaHub(api_key="...") as client:
        # 并发请求
        tasks = [client.some_api(url) for url in urls]
        results = await asyncio.gather(*tasks)
```

#### 问题：内存占用高

**解决方案**：

```python
# 使用上下文管理器确保资源释放
with SocialMediaHub(api_key="...") as client:
    result = client.some_api(url)
# 自动关闭连接
```

### 7. 开发问题

#### 问题：导入错误

```bash
ImportError: cannot import name 'SocialMediaHub' from 'socialmedia_hub'
```

**解决方案**：

```bash
# 重新安装
pip install -e ".[dev]"

# 检查版本
python -c "import socialmedia_hub; print(socialmedia_hub.__version__)"
```

#### 问题：类型检查失败

```bash
mypy: error: Missing type arguments for generic type
```

**解决方案**：

```bash
# 更新类型标注
mypy --strict src/socialmedia_hub

# 或忽略特定错误
mypy --ignore-missing-imports src/socialmedia_hub
```

## 调试技巧

### 1. 启用详细日志

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

### 2. 检查请求/响应

```python
# 使用 httpx 的事件钩子
def log_request(request):
    print(f"Request: {request.method} {request.url}")

def log_response(response):
    print(f"Response: {response.status_code}")

client = SocialMediaHub(api_key="...")
client._client.event_hooks["request"].append(log_request)
client._client.event_hooks["response"].append(log_response)
```

### 3. 使用测试客户端

```python
from fastapi.testclient import TestClient
from socialmedia_hub.server.main import app

client = TestClient(app)
response = client.get("/api/v1/health/check")
print(response.json())
```

### 4. 检查 MCP 工具

```python
from socialmedia_hub.mcp.server import create_mcp_server

mcp = create_mcp_server(api_key="...")
tools = mcp.list_tools()
print(f"Available tools: {len(tools)}")
```

## 获取帮助

- **GitHub Issues**: https://github.com/SocialMedia-Hub/SocialMedia-Hub/issues
- **文档**: https://docs.socialmedia-hub.io
- **Discord**: https://discord.gg/socialmedia-hub
