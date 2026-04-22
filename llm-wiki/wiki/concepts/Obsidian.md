---
title: Obsidian
type: concept
created: 2026-04-22
updated: 2026-04-22
sources:
  - "[[summaries/how-i-use-obsidian-claude-code]]"
tags: [pkm, tools, ai-research]
related:
  - "[[concepts/第二大脑]]"
  - "[[concepts/Claude Code]]"
  - "[[entities/Vin]]"
---

Obsidian 是一个基于本地 [[markdown]] 文件的笔记工具，其核心价值在于**双向链接（backlinks）**机制：笔记之间可以互相引用，形成一张反映思维关联的知识图谱。

## 为什么它与众不同

与基于文件夹的传统文件管理不同，Obsidian 的 backlinks 模拟了大脑形成联想的方式。打开一个文件时，你能看到所有引用它的其他文件，从而在不同想法之间跳跃。

## 与 AI 的协同

Obsidian 的新 [[concepts/Obsidian CLI|Obsidian CLI]] 让 [[concepts/Claude Code|Claude Code]] 等 Agent 不仅能读取文件内容，还能理解文件间的链接关系。这意味着 Agent 可以：

- 发现跨域的隐性模式
- 追踪某个想法的历史演变
- 桥接两个看似无关的领域

正如 [[entities/Vin]] 所说，**markdown 文件是 LLM 的氧气**。

## 核心实践

- **每日笔记**：持续写作，为 Agent 积累上下文
- **实体笔记**：为每个重要的人、项目、概念创建独立页面
- ** backlinks 优先**：链接到具体的模式、理论或项目，而非泛泛的标签
- **人类撰写优先**：保持 vault 中内容的人类原创性，Agent 输出放在侧边
