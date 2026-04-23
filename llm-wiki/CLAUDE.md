# 综合知识库

> Schema document — read at the start of every session together with `wiki/index.md`.
> Update after every major compile, ingest batch, or structural change.

## Scope

本知识库覆盖三大领域，形成互相交织的知识网络：

**1. AI / 技术研究**
- 前沿论文、工具、框架的跟踪与消化
- 大模型、Agent、RAG、Prompt Engineering 等概念
- 代码实现、实验记录、性能对比

**2. 个人知识管理**
- 读书笔记、课程学习、技能习得
- 思维模型、方法论、决策框架
- 日常灵感、反思、长期关注的主题

**3. 工作项目**
- 业务文档、项目知识、流程规范
- 工具使用、环境配置、踩坑记录
- 跨团队协作、会议纪要、决策历史

### 排除范围
- 纯生活琐事（无知识沉淀价值的流水账）
- 与以上三大领域完全无关的临时文件
- 大型二进制文件（使用 raw/refs/ 指针文件管理）

## Operations

本知识库遵循 llm-wiki skill 的五种操作：`compile`, `ingest`, `query`, `lint`, `audit`。
每次操作后追加记录到 `log/YYYYMMDD.md`。

## Naming conventions

### 页面命名
- **概念页** (`wiki/concepts/`): Title Case 名词短语，中文优先。例如 `wiki/concepts/RAG.md` 或 `wiki/concepts/注意力机制.md`
- **分 folder 概念页** (`wiki/concepts/<topic>/`): 当主题超过 ~1200 词时使用。包含 `index.md` + 每个方面一个文件。
- **实体页** (`wiki/entities/`): 专有名词（人名、工具名、组织名、论文名）。例如 `wiki/entities/Claude.md`, `wiki/entities/Transformer论文.md`
- **摘要页** (`wiki/summaries/`): kebab-case 源文件 slug。例如 `wiki/summaries/attention-is-all-you-need.md`
- **查询产出页** (`outputs/queries/`): `<YYYY-MM-DD>-<question-slug>.md`，日期前缀 + kebab-case 问题短名。例如 `outputs/queries/2026-04-22-rag-vs-fine-tuning.md`。若内容具有长期价值，可提升（promote）至 `wiki/concepts/`。

### 分类标签
- `#ai-research` — AI/技术研究相关内容
- `#pkm` — 个人知识管理相关内容
- `#work` — 工作项目相关内容
- `#concept` — 概念页
- `#entity` — 实体页
- `#summary` — 摘要页
- `#output` — 查询产出

所有页面需要 YAML frontmatter: `title`, `type`, `created`, `updated`, `sources`, `tags`。

### 图表与公式
- 所有流程图、架构图、状态图必须使用 **mermaid**。禁止 ASCII 艺术。
- 所有公式必须使用 **KaTeX**: 行内 `$...$` 或块级 `$$...$$`。

### Raw 文件策略
- 小型文本源（md, txt, 小 pdf）→ 复制到 `raw/<subfolder>/`。
- 大型二进制文件（视频、模型权重、安装包、数据集、>10 MB 的 PDF）→ 创建指针文件于 `raw/refs/<slug>.md`，包含 `kind: ref` 和 `external_path` 字段。不要复制二进制文件。

## Current articles

### Concepts
- [[concepts/浏览器自动化]] — 浏览器自动化技术体系
- [[concepts/端到端测试]] — 端到端测试方法与最佳实践
- [[concepts/测试金字塔]] — Mike Cohn 推广的测试策略分层模型
- [[concepts/测试驱动开发]] — 先写测试再写实现的红绿重构循环
- [[concepts/可访问性测试]] — 验证应用对辅助技术用户的可用性
- [[concepts/AI辅助测试]] — 利用 AI 生成、执行和维护自动化测试
- [[concepts/Claude Code]] — Anthropic 的命令行 Agent
- [[concepts/LLM作为思考伙伴]] — 将 LLM 用作协同思考者
- [[concepts/Obsidian]] — 基于本地 markdown 和双向链接的笔记工具
- [[concepts/第二大脑]] — 外部化知识管理系统
- [[concepts/prompt提示工程]] — 提示工程方法论

### Entities
- [[entities/Playwright]] — Microsoft 开源的多浏览器自动化框架
- [[entities/Puppeteer]] — Google 推出的 Chromium 自动化库
- [[entities/Microsoft]] — 全球最大的软件公司之一
- [[entities/Testopic]] — 测试技术教育频道
- [[entities/freeCodeCamp]] — 全球最大的免费编程教育平台
- [[entities/TestMu]] — 软件测试领域公司，KaneAI 的开发者
- [[entities/KaneAI]] — AI 原生测试 Agent，支持自然语言生成测试
- [[entities/Vin]] — Obsidian + Claude Code 深度实践者
- [[entities/Varun Mayya]] — 提示工程世界构建理论提出者
- [[entities/Tech With Tim]] — 提示工程系统化教学创作者
- [[entities/Greg Isenberg]] — Startup Ideas 播客主持人
- [[entities/Obsidian]] — 笔记工具公司/产品

### Summaries
- [[summaries/software-testing-course-playwright-e2e-ai]] — freeCodeCamp 软件测试系统课程
- [[summaries/what-is-playwright]] — Testopic Playwright 入门教程
- [[summaries/how-i-use-obsidian-claude-code]] — Vin 的 Obsidian + Claude Code 实践
- [[summaries/obsidian-claude-codebook]] — 12 个自定义 slash 命令手册
- [[summaries/99-percent-prompt-ai-wrong]] — Varun Mayya 的提示工程技巧
- [[summaries/prompt-engineering-full-course]] — Tech With Tim 的提示工程系统教学

## Open research questions

- Q1: 如何设计一个高效的 RAG 系统，兼顾召回率与响应速度？
- Q2: 个人知识管理中，如何平衡「收集」与「消化」的比例？
- Q3: 工作项目中，哪些知识最适合用 wiki 沉淀，哪些适合用传统文档？

## Research gaps

待摄入的源：
- [ ] <URL 或论文标题> — 为什么相关

## Audit backlog

*(none — run `python3 scripts/audit_review.py llm-wiki --open` to refresh)*

## Notes for the LLM

- **Language**: 中文为主，技术术语保留英文原文并附中文解释
- **Tone**: 中性、清晰、结构化
- **Depth**: 概念页深入浅出（定义 + 原理 + 应用），实体页聚焦事实与关联
- **Handling contradictions**: 陈述双方观点，分别引用来源，加入 Open Research Questions
- **Cross-linking**: 积极使用 `[[...]]` 建立页面间关联，尤其要打通 AI 研究 ↔ 个人知识管理 ↔ 工作项目 三大领域的连接

---

## 工具选择

当需要查找笔记间的关系时，**优先使用 obsidian-cli skill**：

- Wiki links（双向链接）查询
- Tags 或带特定 tags 的笔记搜索
- Frontmatter 信息提取
- 笔记之间的相互关系梳理与分析

> [!note] 为什么用 obsidian-cli
> obsidian-cli 专门针对 Obsidian 的元数据和链接结构优化，比通用的文本搜索更精确高效
