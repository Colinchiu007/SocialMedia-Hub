# 质量节拍 (Quality Beat)

> **开发质量不是靠检查清单堆出来的，是靠固定节奏的日常循环跑出来的。**
>
> **AI 编程不是自动写代码，而是辅助完整开发流程。**

---

## 核心理念：从文章出发

### 文章核心观点

> 代码生成只是第一层价值。AI 编程真正的价值，是辅助完整开发流程：
>
> **理解需求 → 拆解功能 → 设计接口 → 设计数据库 → 判断技术方案 → 编写代码 → 处理异常 → 补充测试 → 代码审查 → 写接口文档 → 上线前检查 → 复盘踩坑经验**

这 12 步就是质量节拍要覆盖的全流程。

### 文章的价值分层

```
第七层：经验沉淀 ← /retro, /learn, /ai-collaboration (Pillar 4)
第六层：文档整理 ← /document-release, documentation-and-adrs
第五层：代码审查 ← /review, code-review-and-quality, /cso
第四层：测试设计 ← TDD, /qa, testing-anti-patterns
第三层：报错排查 ← /investigate, systematic-debugging
第二层：代码理解 ← source-driven-dev, context-engineering, codex
第一层：代码生成 ← incremental-impl, source-driven-dev
```

**质量节拍让 AI 自动帮你往上爬** — 每次日常循环，价值层自动上移一层。

---

## 第一章：全流程覆盖总图

```
┌─────────────────────────────────────────────────────────────────────────┐
│                        质量节拍 全流程                                │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  Phase 0: 探索期 (Explore)                                              │
│  ├── 0.0 目标定义 ──→ /define-goal                                       │
│  ├── 0.1 市场调研 ──→ /office-hours, /interview-me, idea-refine          │
│  ├── 0.2 创意构想 ──→ /pm, /plan-ceo-review, design-consultation         │
│  ├── 0.3 需求确认 ──→ /pm (PRD), /office-hours Phase 2.8, spec-driven-dev│
│  └── 0→1 方案输出 ──→ /create-plan, Feature List                         │
│                                                                         │
│  Phase 1: 规划期 (Plan)                                                 │
│  ├── 1.1 技术架构 ──→ /plan-eng-review, api-and-interface-design         │
│  ├── 1.2 设计评审 ──→ /plan-design-review, /design-review               │
│  ├── 1.3 开发计划 ──→ planning-and-task-breakdown, writing-plans        │
│  └── 1.4 DX 审查  ──→ /plan-devex-review, /plan-tune                    │
│  ├── 1→2 测试计划 ──→ Test Plan                                          │
│                                                                         │
│  Phase 2: 开发期 (Build) — 进入日常循环                                  │
│  ├── 2.1 编码     ──→ 日常循环 ⓪→①→②→③→④→⑤                           │
│  ├── 2.2 集成测试 ──→ /qa, verification-before-completion               │
│  └── 2.3 安全审查 ──→ /cso, /guard, /freeze                             │
│                                                                         │
│  Phase 3: 交付期 (Ship)                                                 │
│  ├── 3.1 发布审查 ──→ /review (完整), /ship                             │
│  ├── 3.2 灰度验证 ──→ /canary, /browse, pair-agent                     │
│  ├── 3.3 发布上线 ──→ /land-and-deploy, ci-cd-and-automation            │
│  ├── 3.4 文档同步 ──→ /document-release                                  │
│  ├── 3.5 用户说明 ──→ User Manual                                        │
│  ├── 3.6 决策归档 ──→ Decision Log                                       │
│  └── 3.7 用户反馈 ──→ User Feedback                                      │
│                                                                         │
│  Phase 4: 复盘期 (Retro)                                                │
│  ├── 4.1 质量体检 ──→ /health                                            │
│  ├── 4.2 技术复盘 ──→ /retro                                             │
│  └── 4.3 经验沉淀 ──→ /learn, /ai-collaboration (Pillar 4)              │
│                                                                         │
│  Phase 5: 运营期 (Operate)                                              │
│  ├── 5.1 问题排查 ──→ /investigate                                      │
│  ├── 5.2 性能优化 ──→ /benchmark, performance-optimization              │
│  ├── 5.3 可观测性 ──→ observability-and-instrumentation                 │
│  ├── 5.4 安全运营 ──→ /cso (daily mode)                                 │
│  ├── 5.5 运维手册 ──→ Operations Manual                                 │
│  └── 5.6 安全审计 ──→ Security Audit Report                             │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

### 总计集成的 57 个 Skills

| 类别 | Skills |
|------|--------|
| **gstack 核心 (33)** | /office-hours, /plan-ceo-review, /plan-eng-review, /plan-design-review, /plan-devex-review, /plan-tune, /autoplan, /review, /investigate, /retro, /learn, /ai-collaboration, /ship, /land-and-deploy, /canary, /cso, /guard, /freeze, /unfreeze, /qa, /qa-only, /design-review, /design-consultation, /design-html, /design-shotgun, /document-release, /health, /benchmark, /browse, /pair-agent, /codex, /careful, /pm, /define-goal, /create-plan, /interview-me, /auto-exec |
| **Superpowers (11)** | subagent-driven-development, executing-plans, writing-plans, requesting-code-review, receiving-code-review, dispatching-parallel-agents, finishing-a-development-branch, systematic-debugging, root-cause-tracing, verification-before-completion, test-driven-development, testing-anti-patterns, condition-based-waiting, remembering-conversations, using-git-worktrees, brainstorming, defense-in-depth |
| **Addy-Agent (15)** | planning-and-task-breakdown, spec-driven-development, incremental-implementation, code-review-and-quality, idea-refine, shipping-and-launch, ci-cd-and-automation, documentation-and-adrs, source-driven-development, doubt-driven-development, code-simplification, context-engineering, api-and-interface-design, frontend-ui-engineering, performance-optimization, observability-and-instrumentation, security-and-hardening, git-workflow-and-versioning, deprecation-and-migration, interview-me |

---

## 第二章：三种触发机制

### 触发方式 A：全流程自动路由

```
当前 Phase       AI 自动调用的 Skill 序列
──────────────────────────────────────────────────
Phase 0.0 (目标) → /define-goal
Phase 0.1 (调研) → /office-hours → /interview-me → idea-refine
Phase 0.2 (构想) → /pm → /plan-ceo-review → design-consultation
Phase 0.3 (需求) → /pm (PRD) → /office-hours Phase 2.8 → spec-driven-dev
Phase 0→1 (方案) → /create-plan
Phase 1.1 (架构) → /plan-eng-review → api-and-interface-design
Phase 1.2 (设计) → /plan-design-review
Phase 1.3 (计划) → /autoplan → planning-and-task-breakdown
Phase 1.4 (DX)   → /plan-devex-review
Phase 2.x (开发) → 日常循环 ⓪→①→②→③→④→⑤
Phase 3.1 (发布) → /review → /ship
Phase 3.2 (灰度) → /canary → /browse → pair-agent
Phase 3.3 (上线) → /land-and-deploy → ci-cd-and-automation
Phase 3.4 (文档) → /document-release → documentation-and-adrs
Phase 4.x (复盘) → /health → /retro → /learn
Phase 5.x (运营) → /investigate → /benchmark → /cso
```

### 触发方式 B：AI 主动提示

```
信号                        AI 提示
──────────────────────────────────────────────────
你说了"有个想法"            → "需要跑一轮 /office-hours 吗？"
任务描述模糊不清             → "需要先出 PRD 吗？"
代码变更涉及数据库           → "检查了事务一致性吗？"
引入了新依赖                → "安全检查跑了吗？"
子任务完成                  → "要跑 /verification-before-completion 吗？"
PHASE 结束                  → "要跑 /health + /retro 全身体检吗？"
同类型问题出现 3 次以上     → "这个模式反复出现，试试 /learn skillify？"
```

### 触发方式 C：一句话触发（52+ 场景）

```
你说                        AI 映射
──────────────────────────────────────────────────
"我有一个想法"              /office-hours → /plan-ceo-review
"帮我分析一下需求"          /office-hours Phase 2.8 → spec-driven-dev
"出个技术方案"              /plan-eng-review → api-and-interface-design
"这个设计怎么样"            /plan-design-review
"规划一下"                 /autoplan → planning-and-task-breakdown
"开始开发"                 → 日常循环 ⓪→①→②→③→④→⑤→⑥
"出 bug 了"                /investigate + systematic-debugging
"帮我看一下代码"            /review + code-review-and-quality
"安全审计"                 /cso comprehensive + /guard
"跑测试"                   /qa + TDD
"上线"                     /ship → /land-and-deploy
"复盘一下"                 /retro → /learn → /learn skillify
"检查质量"                 /health + verification-before-completion
"优化性能"                 /benchmark → performance-optimization
"写文档"                   /document-release + documentation-and-adrs
"AI 怎么用"                /ai-collaboration (Pillar 1-4)
```

---

## 第三章：日常循环（6 步）

```
你开始一个新子任务
    │
    ▼
⓪ pre-flight（自动检查）
    ├── 子任务有明确的验收标准吗？
    ├── 依赖的上下游功能已经就绪吗？
    ├── 需要先写 PRD 或架构文档吗？
    ├── 需求边界清楚吗？
    │
    ▼
① 上下文检查 + source-driven-dev
    ├── 错误信息/堆栈完整？
    ├── 相关代码已读取？
    └── 技术栈/版本已确认？
    │
    ▼
② AI 辅助测试场景脑暴
    ├── 列出正常路径、异常路径、业务规则
    ├── 先写测试（normal + error + edge）
    └── 检查测试质量
    │
    ▼
③ 增量实现
    ├── 一次只实现一个模块
    ├── 依赖审查
    └── 代码简化检查
    │
    ▼
④ 上下文完整性审查
    ├── 异常处理
    ├── 权限边界
    ├── 事务一致性
    ├── 边界值
    ├── 代码风格
    └── Demo 代码
    │
    ▼
⑤ 文档更新
    ├── 更新 CHANGELOG
    ├── 更新接口文档
    └── 技术债务记录
    │
    ▼
⑥ AI 协作质量检查
    ├── 用 /ai-collaboration Pillar 3 checklist 自检
    └── 记录本次协作经验
    │
    ▼
回到 ①，进入下一个子任务
```

---

## 第四章：阶段检查

### Phase 0 门禁
- [ ] 需求边界清楚
- [ ] 至少 2 个技术方案对比
- [ ] 明确"不做什么"清单

### Phase 1 门禁
- [ ] 架构审查通过
- [ ] 任务粒度符合小步规则
- [ ] 每个任务有测试/文档/审查阶段

### Phase 2 门禁
- [ ] 日常循环 6 步完整执行
- [ ] 代码审查无 CRITICAL 问题
- [ ] 测试覆盖 >= 3 场景/模块
- [ ] API Key 无硬编码

### Phase 3 门禁
- [ ] /review 全量审查通过
- [ ] /qa 端到端测试通过
- [ ] 文档同步完成
- [ ] CHANGELOG 更新

### Phase 4 门禁
- [ ] /health 评分 >= 7
- [ ] /retro 产出了 learnings
- [ ] learnings 已 review

### Phase 5 门禁
- [ ] /investigate 无未解决的告警
- [ ] /cso daily 安全扫描通过
- [ ] 性能指标在基线内

---

## 第五章：57 个技能的集成与映射

### gstack 核心技能（33 个）

| Skill | 在全流程中的位置 |
|-------|-----------------|
| /office-hours | Phase 0.1-0.3 |
| /plan-ceo-review | Phase 0.2 |
| /plan-eng-review | Phase 1.1 |
| /plan-design-review | Phase 1.2 |
| /plan-devex-review | Phase 1.4 |
| /autoplan | Phase 1.3 |
| /review | Phase 2→④ / Phase 3.1 |
| /investigate | Phase 5.1 |
| /retro | Phase 4.2 |
| /learn | Phase 4.3 |
| /ai-collaboration | 所有 Phase |
| /ship | Phase 3.1 |
| /land-and-deploy | Phase 3.3 |
| /canary | Phase 3.2 |
| /cso | Phase 2.3 / 3.1 / 5.4 |
| /guard | Phase 2.3 |
| /freeze/unfreeze | Phase 2→③ |
| /qa / qa-only | Phase 2.2 / 3.1 |
| /design-review | Phase 1.2 |
| /design-consultation | Phase 0.2 |
| /design-html | Phase 2.1 |
| /design-shotgun | Phase 0.2 |
| /document-release | Phase 3.4 |
| /health | Phase 4.1 |
| /benchmark | Phase 5.2 |
| /browse | Phase 3.2 / 0.1 |
| /pair-agent | Phase 3.2 |
| /codex | Phase 2→④ |
| /careful | Phase 2.3 |
| /pm | Phase 0.2 |
| /define-goal | Phase 0.0 |
| /create-plan | Phase 0→1 |
| /interview-me | Phase 0.1 |
| /auto-exec | Phase 2.x |

### Superpowers Skills（11 个）

| Skill | 在全流程中的位置 |
|-------|-----------------|
| subagent-driven-dev | Phase 2.x |
| executing-plans | Phase 1.3→2.x |
| writing-plans | Phase 1.3 |
| requesting-code-review | Phase 2→④ |
| receiving-code-review | Phase 2→④ |
| dispatching-parallel-agents | Phase 2.x |
| finishing-a-development-branch | Phase 2→3 |
| systematic-debugging | Phase 5.1 |
| root-cause-tracing | Phase 5.1 |
| verification-before-completion | Phase 2.2 |
| test-driven-development | Phase 2→② |
| testing-anti-patterns | Phase 2→② |
| condition-based-waiting | Phase 2→② |
| remembering-conversations | 所有 Phase |
| using-git-worktrees | Phase 2.x |
| brainstorming | Phase 0.1 |
| defense-in-depth | Phase 2→④ |

### Addy-Agent Skills（15 个）

| Skill | 在全流程中的位置 |
|-------|-----------------|
| planning-and-task-breakdown | Phase 1.3 |
| spec-driven-development | Phase 0.3→1.1 |
| incremental-implementation | Phase 2→③ |
| code-review-and-quality | Phase 2→④ |
| idea-refine | Phase 0.1 |
| shipping-and-launch | Phase 3.1-3.3 |
| ci-cd-and-automation | Phase 3.3 |
| documentation-and-adrs | Phase 3.4 / Phase 4 |
| source-driven-development | Phase 2→① |
| doubt-driven-development | Phase 2→④ |
| code-simplification | Phase 2→③ |
| context-engineering | Phase 2→① |
| api-and-interface-design | Phase 1.1 |
| frontend-ui-engineering | Phase 2.x |
| performance-optimization | Phase 5.2 |
| observability-and-instrumentation | Phase 5.3 |
| security-and-hardening | Phase 2.3 |
| git-workflow-and-versioning | Phase 2→3 |
| deprecation-and-migration | Phase 4.2 |

---

## 第六章：特殊场景映射表

```
你说                                    AI 映射
────────────────────────────────────────────────────────────────
"我有一个想法"                          /office-hours → /plan-ceo-review
"帮我分析一下需求"                      /office-hours Phase 2.8 → spec-driven-dev
"出个技术方案"                          /plan-eng-review → api-and-interface-design
"审查一下架构"                          /plan-eng-review
"这个设计怎么样"                        /plan-design-review
"规划一下"                             /autoplan → planning-and-task-breakdown
"开始开发"                             → 日常循环 ⓪→①→②→③→④→⑤→⑥
"出 bug 了"                            /investigate + systematic-debugging
"帮我看一下代码"                        /review + code-review-and-quality
"安全审计"                             /cso + /guard
"跑测试"                               /qa + TDD
"上线"                                 /ship → /land-and-deploy
"复盘一下"                             /retro → /learn
"检查质量"                             /health
"优化性能"                             /benchmark → performance-optimization
"写文档"                               /document-release
"AI 怎么用"                            /ai-collaboration
```

---

## 第七章：文章核心方法论

### 7.1 "代码理解比代码生成更实用"

质量节拍的日常循环以代码理解（Step ①）开头：

```
⓪ pre-flight
    │
    ▼
① 代码理解 ← 第一步不是写，是读！
    ├── 读取相关源码
    ├── 理解现有逻辑
    ├── 找到改动点
    └── 确认"要改什么"之后 → 才进入 Step ②
```

### 7.2 "小步开发 — 一次只改一个模块"

```
✅ 正确：实现一个独立模块，提交，测试
❌ 错误：同时改 3 个文件，一次性提交
❌ 错误：改代码时"顺手"修了另一个不相关的 bug
```

---

## 第八章：开始使用

### 首次会话

```
使用质量节拍，当前焦点：[Phase 编号] —— [子任务名称]
```

### 后续会话

```
遵循质量节拍。当前焦点：[Phase 编号] —— [新子任务]
```

### 快速切换 Phase

```
"Phase 0 — 调研视频转推文功能"
"Phase 1 — 出技术方案"
"Phase 2 — 实现核心模块"
"Phase 3 — 准备发布"
"Phase 4 — 复盘这个 Sprint"
"Phase 5 — 排查线上问题"
```

---

## 第九章：质量门禁系统

```
Phase 0 门禁：
  [ ] 需求边界清楚
  [ ] 至少 2 个技术方案对比
  [ ] 明确"不做什么"清单

Phase 1 门禁：
  [ ] 架构审查通过
  [ ] 任务粒度符合小步规则
  [ ] 每个任务有测试/文档/审查阶段

Phase 2 门禁：
  [ ] 日常循环 6 步完整执行
  [ ] 代码审查无 CRITICAL 问题
  [ ] 测试覆盖 >= 3 场景/模块
  [ ] API Key 无硬编码

Phase 3 门禁：
  [ ] /review 全量审查通过
  [ ] /qa 端到端测试通过
  [ ] 文档同步完成
  [ ] CHANGELOG 更新

Phase 4 门禁：
  [ ] /health 评分 >= 7
  [ ] /retro 产出了 learnings
  [ ] learnings 已 review

Phase 5 门禁：
  [ ] /investigate 无未解决的告警
  [ ] /cso daily 安全扫描通过
  [ ] 性能指标在基线内
```

**门禁失败处理：**
- ❌ 一个门禁失败 → 在当前 Phase 修复再重跑
- ❌❌ 三个门禁失败 → 降级到上一 Phase 重新执行

---

## 附录：版本

### 2026-07 更新（基于 quality-rhythm v2）
- 57 个技能集成（新增 /define-goal, /pm, /create-plan, /interview-me, /auto-exec）
- 新增 Phase 0.0 目标定义、Phase 3.5/3.6/3.7、Phase 5.5/5.6
- 四层团队架构
- Design Note 流程
- LLM 分级策略
- 环形审查机制
- Bug 反思循环
- Research 阶段
- Page-Level TDD
- 质量门禁系统
