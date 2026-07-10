# SocialMedia-Hub 使用指南

## 目录

- [快速开始](#快速开始)
- [安装](#安装)
- [配置](#配置)
- [SDK 使用](#sdk-使用)
- [API Server 使用](#api-server-使用)
- [CLI 使用](#cli-使用)
- [平台接口详解](#平台接口详解)
- [高级用法](#高级用法)
- [常见问题](#常见问题)
- [最佳实践](#最佳实践)

---

## 快速开始

### 5 分钟上手

```bash
# 1. 安装
pip install socialmedia-hub

# 2. 启动服务器
smh-server start

# 3. 创建 API Key
curl -X POST "http://localhost:8000/api/v1/auth/create_key?name=demo&tier=free"

# 4. 测试接口
curl -H "Authorization: Bearer <YOUR_API_KEY>" \
     "http://localhost:8000/api/v1/health/check"
```

---

## 安装

### pip 安装

```bash
# 基础安装
pip install socialmedia-hub

# 安装 CLI 工具
pip install "socialmedia-hub[cli]"

# 安装完整版（含服务器）
pip install "socialmedia-hub[server]"

# 开发模式安装
git clone https://github.com/SocialMedia-Hub/SocialMedia-Hub.git
cd SocialMedia-Hub
pip install -e ".[dev]"
```

### 环境要求

| 依赖 | 版本 |
|------|------|
| Python | >= 3.10 |
| httpx | >= 0.27 |
| pydantic | >= 2.6 |
| fastapi | >= 0.110 |
| uvicorn | >= 0.29 |

---

## 配置

### 环境变量

```bash
# API Key（必填）
export SMH_API_KEY="your_api_key_here"

# 或使用完整名称
export SOCIALMEDIA_HUB_API_KEY="your_api_key_here"
```

### 客户端配置

```python
from socialmedia_hub import SocialMediaHub

# 基础配置
client = SocialMediaHub(
    api_key="your_api_key",           # API Key
    base_url="http://127.0.0.1:8000",  # 服务器地址
)

# 高级配置
client = SocialMediaHub(
    api_key="your_api_key",
    base_url="http://127.0.0.1:8000",
    timeout=30,                        # 请求超时（秒）
    max_retries=3,                     # 最大重试次数
    proxy="http://proxy:8080",         # 代理服务器
    user_agent="MyApp/1.0",            # 自定义 User-Agent
)
```

### 服务器配置

```bash
# 启动服务器
smh-server start --host 0.0.0.0 --port 8000

# 或使用环境变量
export SMH_HOST=0.0.0.0
export SMH_PORT=8000
smh-server start
```

---

## SDK 使用

### 同步客户端

```python
from socialmedia_hub import SocialMediaHub

# 创建客户端
client = SocialMediaHub(api_key="YOUR_API_KEY")

try:
    # 抖音：获取单个视频
    video = client.douyin_web.fetch_one_video(aweme_id="7251234567890123456")
    print(f"视频标题: {video.get('data', {}).get('desc', 'N/A')}")

    # 抖音：获取用户信息
    user = client.douyin_web.fetch_user_profile_by_uid(uid="123456789")
    print(f"用户名: {user.get('data', {}).get('nickname', 'N/A')}")

    # 抖音：搜索视频
    results = client.douyin_search.fetch_general_search_result(
        keyword="Python",
        count=10
    )
    print(f"搜索结果: {len(results.get('data', {}).get('data', []))} 条")

finally:
    client.close()
```

### 异步客户端

```python
import asyncio
from socialmedia_hub import AsyncSocialMediaHub

async def main():
    async with AsyncSocialMediaHub(api_key="YOUR_API_KEY") as client:
        # 并发获取多个视频
        video1 = await client.douyin_web.fetch_one_video(aweme_id="111")
        video2 = await client.tiktok_web.fetch_post_detail(itemId="222")
        
        print(f"抖音视频: {video1.get('data', {}).get('desc')}")
        print(f"TikTok视频: {video2.get('data', {}).get('desc')}")

asyncio.run(main())
```

### 上下文管理器

```python
from socialmedia_hub import SocialMediaHub

# 推荐使用上下文管理器，自动关闭连接
with SocialMediaHub(api_key="YOUR_API_KEY") as client:
    # 使用客户端
    result = client.health_check.check()
    print(result)
# 自动调用 client.close()
```

### 错误处理

```python
from socialmedia_hub import SocialMediaHub
from socialmedia_hub._errors import (
    SMHError,
    SMHAuthError,
    SMHRateLimitError,
    SMHTimeoutError,
)

client = SocialMediaHub(api_key="YOUR_API_KEY")

try:
    result = client.douyin_web.fetch_one_video(aweme_id="...")
except SMHAuthError as e:
    print(f"认证失败: {e}")
except SMHRateLimitError as e:
    print(f"请求被限流，请在 {e.retry_after} 秒后重试")
except SMHTimeoutError as e:
    print(f"请求超时: {e}")
except SMHHTTPError as e:
    print(f"HTTP 错误 {e.status_code}: {e}")
except SMHError as e:
    print(f"SDK 错误: {e}")
finally:
    client.close()
```

### 分页处理

```python
from socialmedia_hub import SocialMediaHub

client = SocialMediaHub(api_key="YOUR_API_KEY")

# Cursor 分页
cursor = 0
while True:
    result = client.douyin_web.fetch_user_post_videos(
        sec_user_id="xxx",
        cursor=cursor,
        count=20
    )
    
    videos = result.get('data', {}).get('aweme_list', [])
    if not videos:
        break
    
    for video in videos:
        print(video.get('desc'))
    
    cursor = result.get('data', {}).get('max_cursor', 0)
    has_more = result.get('data', {}).get('has_more', False)
    if not has_more:
        break

client.close()
```

---

## API Server 使用

### 启动服务器

```bash
# 默认启动
smh-server start

# 自定义端口
smh-server start --port 9000

# 绑定所有接口
smh-server start --host 0.0.0.0 --port 8000
```

### API Key 管理

```bash
# 创建 API Key
curl -X POST "http://localhost:8000/api/v1/auth/create_key?name=myapp&tier=pro"

# 响应
{
  "api_key": "smh_xxxxxxxxxxxxxxxx",
  "name": "myapp",
  "tier": "pro"
}

# 验证 API Key
curl -H "Authorization: Bearer smh_xxxxxxxxxxxxxxxx" \
     "http://localhost:8000/api/v1/auth/verify"
```

### 健康检查

```bash
# 服务器健康检查
curl "http://localhost:8000/api/v1/health/check"

# 响应
{
  "status": "ok",
  "version": "0.1.0",
  "timestamp": "2026-07-06T01:00:00Z"
}

# 获取支持的平台列表
curl "http://localhost:8000/api/v1/health/platforms"
```

### 调用 API

```bash
# 抖音：获取视频
curl -H "Authorization: Bearer YOUR_API_KEY" \
     "http://localhost:8000/api/v1/douyin/web/fetch_one_video?aweme_id=123"

# TikTok：获取视频
curl -H "Authorization: Bearer YOUR_API_KEY" \
     "http://localhost:8000/api/v1/tiktok/web/fetch_post_detail?itemId=456"

# Instagram：获取用户
curl -H "Authorization: Bearer YOUR_API_KEY" \
     "http://localhost:8000/api/v1/instagram/v1/fetch_user_profile?username=instagram"

# 通用代理（任意平台）
curl -H "Authorization: Bearer YOUR_API_KEY" \
     "http://localhost:8000/api/v1/bilibili/web/fetch_video?bvid=BV1xx411c7mD"
```

### 使用 Python 调用

```python
import httpx

# 创建 HTTP 客户端
client = httpx.Client(base_url="http://localhost:8000")

# 设置 API Key
headers = {"Authorization": "Bearer YOUR_API_KEY"}

# 调用接口
response = client.get(
    "/api/v1/douyin/web/fetch_one_video",
    params={"aweme_id": "123"},
    headers=headers
)

print(response.json())
client.close()
```

---

## CLI 使用

### 基本命令

```bash
# 查看版本
smh version

# 健康检查
smh health

# 创建 API Key
smh create-key --name myapp --tier pro

# 解析 URL
smh fetch "https://v.douyin.com/abc/"
```

### 服务器管理

```bash
# 启动服务器
smh-server start

# 检查服务器状态
smh-server status
```

### 输出格式

CLI 默认输出 JSON 格式，可配合 `jq` 使用：

```bash
# 格式化输出
smh health | jq .

# 提取特定字段
smh health | jq -r '.status'
```

---

## 平台接口详解

### 抖音 (Douyin)

#### Web API

```python
# 获取单个视频
video = client.douyin_web.fetch_one_video(aweme_id="7251234567890123456")

# 获取用户信息
user = client.douyin_web.fetch_user_profile_by_uid(uid="123456789")

# 获取用户发布的视频
videos = client.douyin_web.fetch_user_post_videos(
    sec_user_id="xxx",
    max_cursor=0,
    count=20
)

# 搜索视频
results = client.douyin_search.fetch_general_search_result(
    keyword="Python",
    offset=0,
    count=20
)

# 获取视频评论
comments = client.douyin_web.fetch_video_comments(
    aweme_id="123",
    cursor=0,
    count=20
)

# 获取热搜榜
trending = client.douyin_web.fetch_hot_search_result()
```

#### App API

```python
# 获取视频（App端）
video = client.douyin_app_v3.fetch_one_video(aweme_id="123")

# 获取用户信息（App端）
user = client.douyin_app_v3.fetch_user_profile(sec_user_id="xxx")
```

### TikTok

```python
# 获取视频详情
video = client.tiktok_web.fetch_post_detail(itemId="7251234567890123456")

# 获取用户信息
user = client.tiktok_web.fetch_user_profile(uniqueId="username")

# 获取用户发布的视频
posts = client.tiktok_web.fetch_user_post(secUid="xxx", count=20)

# 搜索视频
results = client.tiktok_web.fetch_general_search(
    keyword="dance",
    count=20
)

# 获取趋势
trending = client.tiktok_web.fetch_trending_post()
```

### Instagram

```python
# 获取用户信息
user = client.instagram_v1.fetch_user_profile(username="instagram")

# 获取用户帖子
posts = client.instagram_v1.fetch_user_post_feed(user_id="123456")

# 获取帖子详情
post = client.instagram_v1.fetch_post_info(shortcode="ABC123")

# 获取帖子评论
comments = client.instagram_v1.fetch_post_comments(media_id="123")
```

### YouTube

```python
# 获取视频信息
video = client.youtube_web.get_video_info(video_id="dQw4w9WgXcQ")

# 获取频道信息
channel = client.youtube_web.get_channel_info(channel_id="UCxxxxxx")

# 获取频道视频
videos = client.youtube_web.get_channel_videos(channel_id="UCxxxxxx")

# 搜索视频
results = client.youtube_web.search_video(search_query="python tutorial")
```

### 小红书 (Xiaohongshu)

```python
# 获取笔记详情
note = client.xiaohongshu_web_v2.get_note_info_v2(note_id="xxx")

# 获取用户信息
user = client.xiaohongshu_web_v2.get_user_info(user_id="xxx")

# 搜索笔记
results = client.xiaohongshu_web_v2.search_notes_v3(
    keyword="穿搭",
    page=1
)

# 获取热榜
hot_list = client.xiaohongshu_web_v2.fetch_hot_list()
```

### B站 (Bilibili)

```python
# 获取视频信息
video = client.bilibili_web.fetch_one_video(bv_id="BV1xx411c7mD")

# 获取用户信息
user = client.bilibili_web.fetch_user_profile(uid="12345")

# 获取用户视频
videos = client.bilibili_web.fetch_user_post_videos(uid="12345", pn=1)

# 获取视频评论
comments = client.bilibili_web.fetch_video_comments(bv_id="BV1xx411c7mD")

# 获取弹幕
danmaku = client.bilibili_web.fetch_video_danmaku(cid="12345")
```

### 微博 (Weibo)

```python
# 获取用户信息
user = client.weibo_web.fetch_user_profile(uid="12345")

# 获取用户微博
posts = client.weibo_web.fetch_user_posts(uid="12345", page=1)

# 获取热搜
hot_list = client.weibo_web.fetch_hot_list()

# 搜索微博
results = client.weibo_web.fetch_search(keyword="Python", page=1)
```

---

## 高级用法

### 并发请求

```python
import asyncio
from socialmedia_hub import AsyncSocialMediaHub

async def fetch_multiple_videos(video_ids: list[str]):
    """并发获取多个视频"""
    async with AsyncSocialMediaHub(api_key="YOUR_API_KEY") as client:
        tasks = [
            client.douyin_web.fetch_one_video(aweme_id=vid)
            for vid in video_ids
        ]
        results = await asyncio.gather(*tasks, return_exceptions=True)
        return results

# 使用
video_ids = ["111", "222", "333", "444", "555"]
results = asyncio.run(fetch_multiple_videos(video_ids))
```

### 批量数据采集

```python
from socialmedia_hub import SocialMediaHub
import csv

def collect_user_videos(user_id: str, max_videos: int = 100):
    """采集用户所有视频"""
    client = SocialMediaHub(api_key="YOUR_API_KEY")
    all_videos = []
    cursor = 0
    
    while len(all_videos) < max_videos:
        result = client.douyin_web.fetch_user_post_videos(
            sec_user_id=user_id,
            cursor=cursor,
            count=20
        )
        
        videos = result.get('data', {}).get('aweme_list', [])
        if not videos:
            break
        
        all_videos.extend(videos)
        cursor = result.get('data', {}).get('max_cursor', 0)
    
    client.close()
    return all_videos[:max_videos]

# 保存到 CSV
videos = collect_user_videos("user_sec_id", max_videos=50)
with open('videos.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['aweme_id', 'desc', 'create_time'])
    writer.writeheader()
    for v in videos:
        writer.writerow({
            'aweme_id': v.get('aweme_id'),
            'desc': v.get('desc'),
            'create_time': v.get('create_time')
        })
```

### 数据分析

```python
from socialmedia_hub import SocialMediaHub
from collections import Counter
from datetime import datetime

def analyze_user_content(user_id: str):
    """分析用户内容特征"""
    client = SocialMediaHub(api_key="YOUR_API_KEY")
    
    # 获取用户视频
    result = client.douyin_web.fetch_user_post_videos(
        sec_user_id=user_id,
        count=50
    )
    videos = result.get('data', {}).get('aweme_list', [])
    
    # 分析统计
    stats = {
        'total_videos': len(videos),
        'total_likes': sum(v.get('statistics', {}).get('digg_count', 0) for v in videos),
        'total_comments': sum(v.get('statistics', {}).get('comment_count', 0) for v in videos),
        'avg_duration': sum(v.get('duration', 0) for v in videos) / len(videos) if videos else 0,
    }
    
    # 按发布时间分组
    date_groups = Counter()
    for v in videos:
        ts = v.get('create_time', 0)
        date = datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
        date_groups[date] += 1
    
    stats['posting_frequency'] = dict(date_groups)
    
    client.close()
    return stats
```

### 自定义中间件

```python
import logging
from socialmedia_hub import SocialMediaHub

# 配置日志
logging.basicConfig(level=logging.DEBUG)

# 启用详细日志
logger = logging.getLogger("socialmedia_hub")
logger.setLevel(logging.DEBUG)

client = SocialMediaHub(api_key="YOUR_API_KEY")
```

---

## 常见问题

### Q1: 如何获取 API Key？

A: 访问 [TikHub 官网](https://user.tikhub.io/login) 注册账号，在 Dashboard 中获取 API Key。

### Q2: 请求被限流怎么办？

A: API 有频率限制，被限流时会返回 429 错误。建议：
- 降低请求频率
- 使用缓存减少重复请求
- 升级到更高 tier 的套餐

```python
except SMHRateLimitError as e:
    print(f"被限流，等待 {e.retry_after} 秒后重试")
    time.sleep(e.retry_after)
```

### Q3: 如何处理网络超时？

A: 可以增加超时时间和重试次数：

```python
client = SocialMediaHub(
    api_key="YOUR_API_KEY",
    timeout=60,           # 60秒超时
    max_retries=5,        # 最多重试5次
)
```

### Q4: 支持哪些代理？

A: 支持 HTTP/HTTPS/SOCKS5 代理：

```python
client = SocialMediaHub(
    api_key="YOUR_API_KEY",
    proxy="http://proxy:8080",      # HTTP 代理
    # proxy="socks5://proxy:1080",  # SOCKS5 代理
)
```

### Q5: 如何查看请求日志？

A: 启用调试日志：

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

### Q6: 异步客户端如何使用？

A: 使用 `AsyncSocialMediaHub` 和 `async with`：

```python
import asyncio
from socialmedia_hub import AsyncSocialMediaHub

async def main():
    async with AsyncSocialMediaHub(api_key="YOUR_API_KEY") as client:
        result = await client.douyin_web.fetch_one_video(aweme_id="...")
        print(result)

asyncio.run(main())
```

---

## 最佳实践

### 1. 使用上下文管理器

```python
# ✅ 推荐
with SocialMediaHub(api_key="YOUR_API_KEY") as client:
    result = client.douyin_web.fetch_one_video(aweme_id="...")

# ❌ 避免
client = SocialMediaHub(api_key="YOUR_API_KEY")
result = client.douyin_web.fetch_one_video(aweme_id="...")
# 容易忘记关闭连接
```

### 2. 合理设置超时

```python
# 根据网络情况调整
client = SocialMediaHub(
    api_key="YOUR_API_KEY",
    timeout=30,  # 本地服务器
    # timeout=60,  # 跨国请求
)
```

### 3. 使用异步提高并发

```python
# 同步：串行执行，速度慢
for video_id in video_ids:
    result = client.fetch_video(video_id)

# 异步：并发执行，速度快
async with AsyncSocialMediaHub(api_key="...") as client:
    tasks = [client.fetch_video(vid) for vid in video_ids]
    results = await asyncio.gather(*tasks)
```

### 4. 处理错误和重试

```python
import time
from socialmedia_hub._errors import SMHRateLimitError

def fetch_with_retry(client, func, max_retries=3, **kwargs):
    """带重试的请求封装"""
    for attempt in range(max_retries):
        try:
            return func(**kwargs)
        except SMHRateLimitError as e:
            if attempt < max_retries - 1:
                time.sleep(e.retry_after or 1)
            else:
                raise
```

### 5. 缓存常用数据

```python
from functools import lru_cache

@lru_cache(maxsize=100)
def get_user_info(user_id: str):
    """缓存用户信息，避免重复请求"""
    with SocialMediaHub(api_key="...") as client:
        return client.douyin_web.fetch_user_profile_by_uid(uid=user_id)
```

### 6. 数据验证

```python
def safe_get(data: dict, *keys, default=None):
    """安全获取嵌套字典值"""
    for key in keys:
        if isinstance(data, dict):
            data = data.get(key, default)
        else:
            return default
    return data

# 使用
video = client.douyin_web.fetch_one_video(aweme_id="...")
title = safe_get(video, 'data', 'aweme_detail', 'desc', default='N/A')
likes = safe_get(video, 'data', 'aweme_detail', 'statistics', 'digg_count', default=0)
```

### 7. 监控和告警

```python
import logging
from socialmedia_hub._errors import SMHHTTPError

logger = logging.getLogger(__name__)

try:
    result = client.some_api()
except SMHHTTPError as e:
    logger.error(f"API 错误: {e.status_code} {e.url}")
    if e.status_code >= 500:
        # 服务端错误，触发告警
        send_alert(f"服务器错误: {e}")
    raise
```

---

## MCP 集成

### 创建 MCP 服务器

```python
from socialmedia_hub.mcp import create_mcp_server

# 创建 MCP 服务器
mcp = create_mcp_server(api_key="YOUR_API_KEY")

# 列出所有工具
tools = mcp.list_tools()
print(f"可用工具: {len(tools)}")

# 调用工具
result = mcp.call_tool("tiktok_fetch_video", {"video_id": "123"})
print(result)
```

### 可用工具 (1000 个)

| 平台 | 工具数 | 示例工具 |
|------|--------|----------|
| TikTok | 60 | tiktok_fetch_video, tiktok_fetch_user |
| 抖音 | 60 | douyin_fetch_video, douyin_fetch_user |
| Instagram | 60 | instagram_fetch_post, instagram_fetch_user |
| YouTube | 60 | youtube_fetch_video, youtube_fetch_channel |
| 其他平台 | 760 | 每个平台 27-60 个工具 |

---

## 反爬机制

### 自动反爬

SocialMedia-Hub 内置完整的反爬机制，自动处理：

1. **速率限制** — 每平台每分钟最多 10 个请求
2. **随机延迟** — 请求间 1-3 秒随机延迟
3. **Cookie 轮换** — 多账号 Cookie 自动轮换
4. **代理轮换** — 支持 4 种代理策略
5. **错误重试** — 429 自动等待重试

### 配置反爬参数

```python
from socialmedia_hub.proxy.real_proxy import RealProxyLayer

layer = RealProxyLayer(
    min_delay=1.0,  # 最小延迟（秒）
    max_delay=3.0,  # 最大延迟（秒）
)
```

### 配置代理池

```python
from socialmedia_hub.proxy.pool import ProxyPool

pool = ProxyPool()
pool.add_proxy(host="proxy1.com", port=8080)
pool.add_proxy(host="proxy2.com", port=8081)

# 使用不同策略
proxy = pool.get_proxy(strategy="round_robin")  # 轮询
proxy = pool.get_proxy(strategy="random")       # 随机
proxy = pool.get_proxy(strategy="least_used")   # 最少使用
proxy = pool.get_proxy(strategy="best_success") # 最高成功率
```

### 配置 Cookie 轮换

```python
from socialmedia_hub.proxy.cookies import CookieManager

manager = CookieManager(storage_path="cookies.json")

# 添加多个账号的 Cookie
manager.set_cookie("session1", "value1", "www.douyin.com")
manager.set_cookie("session2", "value2", "www.douyin.com")

# 自动轮换使用
cookie_header = manager.get_cookie_header("www.douyin.com")
```

---

## 附录

### 错误码参考

| 错误码 | 异常类 | 说明 |
|--------|--------|------|
| 400 | SMHBadRequestError | 请求参数错误 |
| 401 | SMHAuthError | 认证失败 |
| 403 | SMHPermissionError | 权限不足 |
| 404 | SMHNotFoundError | 资源不存在 |
| 429 | SMHRateLimitError | 请求频率超限 |
| 500 | SMHServerError | 服务器内部错误 |
| 502/503/504 | SMHUpstreamError | 上游服务不可用 |

### 平台端点速查

| 平台 | 获取视频 | 获取用户 | 搜索 |
|------|----------|----------|------|
| 抖音 | `douyin_web.fetch_one_video` | `douyin_web.fetch_user_profile_by_uid` | `douyin_search.fetch_general_search_result` |
| TikTok | `tiktok_web.fetch_post_detail` | `tiktok_web.fetch_user_profile` | `tiktok_web.fetch_general_search` |
| Instagram | `instagram_v1.fetch_post_info` | `instagram_v1.fetch_user_profile` | - |
| YouTube | `youtube_web.get_video_info` | `youtube_web.get_channel_info` | `youtube_web.search_video` |
| 小红书 | `xiaohongshu_web_v2.get_note_info_v2` | `xiaohongshu_web_v2.get_user_info` | `xiaohongshu_web_v2.search_notes_v3` |
| B站 | `bilibili_web.fetch_one_video` | `bilibili_web.fetch_user_profile` | `bilibili_web.fetch_general_search` |

### 联系方式

- **GitHub**: https://github.com/SocialMedia-Hub/SocialMedia-Hub
- **Issues**: https://github.com/SocialMedia-Hub/SocialMedia-Hub/issues
- **文档**: https://docs.socialmedia-hub.io
