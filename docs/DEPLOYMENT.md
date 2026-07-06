# Deployment Guide

本文档介绍如何部署 SocialMedia-Hub API Server。

## 部署方式

### 1. 本地开发

```bash
# 安装依赖
pip install -e ".[server]"

# 启动服务器
smh-server start --host 0.0.0.0 --port 8000
```

### 2. Docker 部署

#### Dockerfile

```dockerfile
FROM python:3.12-slim

WORKDIR /app

# 复制依赖文件
COPY pyproject.toml .
COPY src/ src/

# 安装依赖
RUN pip install --no-cache-dir -e ".[server]"

# 暴露端口
EXPOSE 8000

# 启动命令
CMD ["smh-server", "start", "--host", "0.0.0.0", "--port", "8000"]
```

#### docker-compose.yml

```yaml
version: '3.8'

services:
  socialmedia-hub:
    build: .
    ports:
      - "8000:8000"
    environment:
      - SMH_API_KEY=your_api_key_here
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/api/v1/health/check"]
      interval: 30s
      timeout: 10s
      retries: 3
```

#### 构建和运行

```bash
# 构建镜像
docker build -t socialmedia-hub .

# 运行容器
docker run -d -p 8000:8000 --name socialmedia-hub socialmedia-hub

# 或使用 docker-compose
docker-compose up -d
```

### 3. 云部署

#### Vercel (Serverless)

```bash
# 安装 Vercel CLI
npm i -g vercel

# 部署
vercel
```

#### AWS Lambda

```bash
# 安装 AWS CLI
pip install awscli

# 打包
zip -r function.zip .

# 部署
aws lambda create-function \
  --function-name socialmedia-hub \
  --runtime python3.12 \
  --handler index.handler \
  --zip-file fileb://function.zip
```

#### Google Cloud Run

```bash
# 构建镜像
gcloud builds submit --tag gcr.io/your-project/socialmedia-hub

# 部署
gcloud run deploy socialmedia-hub \
  --image gcr.io/your-project/socialmedia-hub \
  --platform managed \
  --region us-central1
```

## 配置

### 环境变量

| 变量 | 说明 | 默认值 |
|------|------|--------|
| `SMH_API_KEY` | API Key | - |
| `SMH_HOST` | 绑定地址 | 0.0.0.0 |
| `SMH_PORT` | 端口号 | 8000 |

### 配置文件

创建 `.env` 文件：

```env
SMH_API_KEY=your_api_key_here
SMH_HOST=0.0.0.0
SMH_PORT=8000
```

## 监控

### 健康检查

```bash
curl http://localhost:8000/api/v1/health/check
```

### 监控端点

```bash
# 服务器状态
curl http://localhost:8000/api/v1/monitor/status

# 性能指标
curl http://localhost:8000/api/v1/monitor/metrics

# 平台状态
curl http://localhost:8000/api/v1/monitor/platforms
```

### 日志

```bash
# 查看容器日志
docker logs -f socialmedia-hub

# 或使用 uvicorn 日志
smh-server start --log-level info
```

## 安全建议

1. **使用 HTTPS**：在生产环境中使用反向代理（Nginx/Caddy）启用 HTTPS
2. **限制访问**：配置防火墙或安全组规则
3. **定期轮换 API Key**：定期更换 API Key
4. **监控异常**：设置告警监控异常请求
5. **备份数据**：定期备份配置和日志

## 故障排除

### 端口被占用

```bash
# 查找占用端口的进程
lsof -i :8000

# 或使用 netstat
netstat -tulpn | grep 8000
```

### 无法启动

```bash
# 检查依赖
pip install -e ".[server]"

# 检查端口
smh-server start --port 8001
```

### 连接超时

```bash
# 增加超时时间
smh-server start --timeout 60

# 或在客户端设置
client = SocialMediaHub(api_key="...", timeout=60)
```

## 性能优化

### 1. 使用连接池

```python
# 创建持久化连接
client = SocialMediaHub(api_key="...")

# 复用连接进行多次请求
for url in urls:
    result = client.some_api(url)
```

### 2. 并发请求

```python
import asyncio
from socialmedia_hub import AsyncSocialMediaHub

async def main():
    async with AsyncSocialMediaHub(api_key="...") as client:
        tasks = [client.some_api(url) for url in urls]
        results = await asyncio.gather(*tasks)
```

### 3. 缓存结果

```python
from functools import lru_cache

@lru_cache(maxsize=100)
def get_cached_data(video_id: str):
    return client.some_api(video_id)
```

## 扩展

### 添加新平台

1. 在 `spec/openapi.json` 中添加端点
2. 运行 `python scripts/generate_resources.py`
3. 在 `_core.py` 中添加平台配置
4. 重启服务器

### 添加新端点

1. 在 OpenAPI spec 中添加端点定义
2. 运行代码生成脚本
3. 路由自动注册

## 参考

- [FastAPI 部署文档](https://fastapi.tiangolo.com/deployment/)
- [Docker 文档](https://docs.docker.com/)
- [Vercel 部署文档](https://vercel.com/docs)
