# Index — 综合知识库

> 覆盖 AI 技术研究、个人知识管理、工作项目三大领域的交叉知识网络。

## 🔖 Navigation
- [[#AI 研究]] · [[#个人知识管理]] · [[#工作项目]] · [[#Entities]] · [[#Summaries]] · [[#Open Questions]]

---

## AI 研究

### 工具与 Agent
- [[concepts/Claude Code]] — Anthropic 的命令行 Agent，可读写文件、执行命令
- [[concepts/LLM作为思考伙伴]] — 将 LLM 用作协同思考者而非单纯执行者
- [[concepts/RAG]] — 检索增强生成：将外部知识检索与 LLM 生成结合的架构

### Prompt Engineering
- [[prompt提示工程]] — 通过世界构建和上下文碎片引导 LLM 输出高质量结果

## 个人知识管理

### 笔记与知识系统
- [[concepts/LLM Wiki]] — 利用 LLM 增量构建和维护持久化 wiki 的知识管理模式
- [[concepts/Obsidian]] — 基于本地 markdown 和双向链接的笔记工具
- [[concepts/第二大脑]] — 外部化知识管理系统（Personal OS），markdown 为核心

### 查询产出
- [[outputs/queries/2026-04-22-how-to-design-custom-slash-commands|如何设计自定义 slash 命令？]] — 基于 Vin 实践提炼的设计原则与元认知模型

## 工作项目

### 测试与质量保障
- [[concepts/浏览器自动化]] — 通过程序控制浏览器执行交互操作的技术体系
- [[concepts/端到端测试]] — 模拟真实用户完整流程的系统级测试方法
- [[concepts/测试金字塔]] — Mike Cohn 推广的测试策略分层模型
- [[concepts/测试驱动开发]] — 先写测试再写实现的红绿重构循环
- [[concepts/可访问性测试]] — 验证应用对辅助技术用户的可用性
- [[concepts/AI辅助测试]] — 利用 AI 生成、执行和维护自动化测试
- [[entities/Playwright]] — Microsoft 开源的多浏览器自动化框架
- [[entities/Puppeteer]] — Google 推出的 Chromium 自动化库，Playwright 的前身
- [[entities/KaneAI]] — TestMu 出品的 AI 原生测试 Agent
- [[entities/TestMu]] — 软件测试领域公司，KaneAI 的开发者

---

## Entities

### 人物
- [[entities/Andrej Karpathy]] — 深度学习研究者、AI 教育者，LLM Wiki 模式的提出者
- [[entities/Vannevar Bush]] — 工程师与科学管理者，Memex 概念的提出者（1945）
- [[entities/Vin]] — Internet Vin，Obsidian + Claude Code 深度实践者
- [[entities/Varun Mayya]] — 创业者、内容创作者，提示工程世界构建理论的提出者
- [[entities/Tech With Tim]] — 技术教育内容创作者，提示工程系统化教学的提出者
- [[entities/Greg Isenberg]] — Startup Ideas 播客主持人

### 工具与组织
- [[entities/Obsidian]] — 笔记工具公司/产品
- [[entities/Microsoft]] — 全球最大的软件公司之一，Playwright 的维护方
- [[entities/Testopic]] — 测试技术教育频道，专注 Playwright 内容输出
- [[entities/freeCodeCamp]] — 全球最大的免费编程教育平台
- [[entities/TestMu]] — 软件测试领域公司，KaneAI 的开发者
- [[entities/KaneAI]] — AI 原生测试 Agent，支持自然语言生成测试

## Summaries (chronological)

- 2026-04-23 — [[summaries/software-testing-course-playwright-e2e-ai]] — freeCodeCamp 软件测试系统课程：金字塔、Playwright 实战、AI 测试
- 2026-04-23 — [[summaries/what-is-playwright]] — Testopic 的 Playwright 入门教程：安装、Codegen、截图与录屏
- 2026-04-22 — [[summaries/how-i-use-obsidian-claude-code]] — Vin 展示如何用 Obsidian + Claude Code 构建个人操作系统
- 2026-04-22 — [[summaries/obsidian-claude-codebook]] — 12 个自定义 slash 命令的完整操作手册与 prompt 模板
- 2026-04-22 — [[summaries/99-percent-prompt-ai-wrong]] — Varun Mayya 拆解 10 个提示工程技巧与世界构建理论
- 2026-04-22 — [[summaries/prompt-engineering-full-course]] — Tech With Tim 系统化教学：从基础概念到高级参数调优的完整框架

---

## Open Questions

- Q1: 如何设计一个高效的 RAG 系统，兼顾召回率与响应速度？
- Q2: 个人知识管理中，如何平衡「收集」与「消化」的比例？
- Q3: 工作项目中，哪些知识最适合用 wiki 沉淀，哪些适合用传统文档？
