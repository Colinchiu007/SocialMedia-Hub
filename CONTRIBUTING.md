# Contributing Guide

感谢你对 SocialMedia-Hub 的贡献！

## 开发环境设置

### 前置要求

- Python 3.10+
- Git
- pip

### 安装

```bash
# 克隆仓库
git clone https://github.com/SocialMedia-Hub/SocialMedia-Hub.git
cd SocialMedia-Hub

# 安装开发依赖
pip install -e ".[dev]"

# 验证安装
pytest -v
```

## 开发流程

### 1. 创建分支

```bash
git checkout -b feature/your-feature-name
```

### 2. 代码规范

#### 代码风格
- 使用 `ruff` 进行代码格式化
- 行长度限制：100 字符
- 遵循 PEP 8 规范

```bash
# 检查代码风格
ruff check src/ tests/

# 自动修复
ruff check src/ tests/ --fix
```

#### 类型标注
- 所有公共 API 必须有类型标注
- 使用 `mypy --strict` 进行类型检查

```bash
mypy --strict src/socialmedia_hub
```

#### 测试
- 新功能必须有对应的测试
- 测试文件放在 `tests/` 目录下
- 使用 `pytest` 运行测试

```bash
pytest -v
```

### 3. 提交规范

使用 [Conventional Commits](https://www.conventionalcommits.org/) 规范：

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

**类型**：
- `feat`: 新功能
- `fix`: 修复 bug
- `docs`: 文档更新
- `style`: 代码格式（不影响功能）
- `refactor`: 重构（不增加功能）
- `test`: 测试相关
- `chore`: 构建/工具相关

**示例**：
```
feat(douyin): 添加抖音创作者 API 端点

- 添加 16 个创作者相关端点
- 支持获取创作者数据、粉丝画像等

Closes #123
```

### 4. Pull Request 流程

1. 确保所有测试通过
2. 确保代码风格检查通过
3. 确保类型检查通过
4. 更新相关文档
5. 创建 Pull Request

## 项目结构

```
SocialMedia-Hub/
├── src/socialmedia_hub/
│   ├── __init__.py           # 包入口
│   ├── _base_client.py       # 核心客户端
│   ├── _errors.py            # 异常定义
│   ├── _retries.py           # 重试策略
│   ├── _pagination.py        # 分页器
│   ├── mcp/                  # MCP Server
│   │   └── server.py
│   ├── server/               # API Server
│   │   ├── main.py
│   │   ├── _core.py
│   │   └── routes/
│   └── cli/                  # CLI 工具
├── tests/
│   ├── unit/                 # 单元测试
│   └── integration/          # 集成测试
├── docs/                     # 文档
├── examples/                 # 示例
└── scripts/                  # 工具脚本
```

## 添加新平台

### 步骤

1. **更新 OpenAPI Spec**
   - 在 `spec/openapi.json` 中添加新平台的端点定义

2. **运行代码生成**
   ```bash
   python scripts/generate_resources.py
   ```

3. **添加平台配置**
   - 在 `src/socialmedia_hub/server/_core.py` 的 `PLATFORM_CONFIGS` 中添加配置

4. **添加 MCP 工具**（可选）
   - 在 `src/socialmedia_hub/mcp/server.py` 中添加工具注册

5. **添加测试**
   - 在 `tests/unit/` 中添加测试用例

6. **更新文档**
   - 更新 `docs/USER_GUIDE.md`
   - 更新 `docs/FEATURE_COMPARISON.md`

## 代码审查

提交 PR 前，请确保：

- [ ] 所有测试通过
- [ ] 代码风格检查通过
- [ ] 类型检查通过
- [ ] 新功能有对应测试
- [ ] 文档已更新
- [ ] CHANGELOG 已更新

## 问题反馈

- GitHub Issues: https://github.com/SocialMedia-Hub/SocialMedia-Hub/issues
- 邮件: support@socialmedia-hub.io
