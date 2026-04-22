---
title: "How I Use Obsidian + Claude Code to Run My Life"
type: summary
created: 2026-04-22
updated: 2026-04-22
sources:
  - "[[raw/articles/How I Use Obsidian + Claude Code to Run My Life]]"
tags: [pkm, ai-research, obsidian, claude-code]
---

## 来源

YouTube 访谈，[[entities/Greg Isenberg]] 采访 [[entities/Vin|Internet Vin]]，2026-02-24 发布。

## 核心论点

Vin 展示了一套将 [[concepts/Obsidian|Obsidian]] 与 [[concepts/Claude Code|Claude Code]] 结合的个人操作系统（Personal OS）。核心洞察：**markdown 互连文件是 LLM 的氧气** —— 你写得越多，Agent 能为你做的事情就越多。

## 关键要点

1. **上下文即一切**：Claude Code 的能力取决于你喂给它的上下文质量。通过文件传递持久化上下文，避免每次会话重复解释项目。
2. **Obsidian CLI 是桥接器**：它让 Claude Code 不仅能读取 vault 中的文件，还能理解文件间的 backlinks 关系，从而发现跨域模式。
3. **自定义 Slash 命令作为思考工具**：Vin 构建了 /context、/today、/trace、/connect、/ideas、/ghost、/challenge、/drift 等命令，将 Claude Code 从通用助手转化为深度个性化的思考伙伴。
4. **写作是引擎**：日常反思和笔记是生成想法、内化知识的主要方式，也是委托 Agent 的前提条件。
5. **严格分离人类 vs Agent 内容**：Vin 坚持只让人类在 vault 中写作，Agent 只在侧边输出，确保模式发现的源头是人类思想而非 Agent 生成内容。
6. **OpenClaw 与自主 Agent**：未来 Agent 可自主读取 vault、发现关联并代做决策，vault 成为人与 Agent 之间的「源文件」。
7. **Alpha 效应**：99.99% 的人不会花时间去建立这套系统，而这正是竞争优势所在。

## 可操作的命令

| 命令 | 功能 |
|------|------|
| /context | 加载完整生活与工作上下文 |
| /today | 拉取日历、任务、近期笔记并生成优先计划 |
| /close-day | 日终处理，提取行动项、发现 vault 关联 |
| /trace | 追踪某个想法在 vault 中的演变历史 |
| /connect | 用链接图谱桥接两个不同领域 |
| /ideas | 基于全库生成跨域可行想法 |
| /ghost | 以你的声音回答问题 |
| /challenge | 用 vault 历史压力测试当前信念 |
| /drift | 对比 stated intentions vs 实际行为（30-60天）|
| /graduate | 将日常笔记中的想法提升为独立概念页 |
