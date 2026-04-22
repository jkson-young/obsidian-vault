---
title: "Obsidian + Claude Codebook"
type: summary
created: 2026-04-22
updated: 2026-04-22
sources:
  - "[[raw/articles/Obsidian + Claude Codebook (doc)]]"
tags: [pkm, ai-research, obsidian, claude-code]
---

## 来源

[[entities/Vin|Internet Vin]] 撰写的配套操作手册，详细拆解其 Obsidian + Claude Code 系统中的 **12 个自定义 slash 命令**。

与 [[summaries/how-i-use-obsidian-claude-code|视频访谈]] 互为补充：访谈讲理念与动机，Codebook 讲具体命令的实现与使用场景。

## 核心论点

> "The quality of information that the agent has entirely determines what it can do for you."

你的 vault 就是 Agent 的上下文。你写得越多，Agent 能为你做的事情就越多。

## 12 个 Slash 命令

| 命令 | 功能 | 使用时机 |
|------|------|----------|
| `/context` | 加载完整生活与工作上下文（项目、偏好、优先级、当前焦点） | 每次新会话开始时 |
| `/today` | 拉取日历、任务和近期笔记，生成当日优先计划 | 晨间规划；感到 overwhelmed 时 |
| `/trace` | 追踪某个想法在 vault 中的演变历史 | 理解认知弧线；某个想法反复出现时 |
| `/connect` | 用链接图谱桥接两个不同领域，发现意外关联 | 卡壳时；怀疑两个想法有关但看不清关联时 |
| `/ghost` | 基于你的写作和 stated beliefs，以你的声音回答问题 | 外化自身思维；需要「像自己写的」草稿时 |
| `/challenge` | 压力测试当前信念，发现矛盾或薄弱点 | 重大决策前；想 stress-test 一个想法时 |
| `/ideas` | 扫描全库生成完整的想法报告（工具、人脉、主题、写作） | 需要 grounded in 真实兴趣的新鲜想法时 |
| `/graduate` | 从日常笔记中提取未成熟的想法，提升为独立文件 | 周回顾；daily notes 充满半成品想法时 |
| `/closeday` | 捕获今日所做和所学，/today 的日终对应 | 日终；记录进展、清空大脑 |
| `/drift` | 发现跨笔记反复出现但缺乏清晰线索的松散关联主题 | 感觉有东西在浮现但无法命名时 |
| `/emerge` | 识别开始凝聚成更大事物的模式集群 | 零散想法开始聚集，想看哪些能变成项目/文章/产品时 |
| `/schedule` | 读取优先事项和日历，建议时间分配方案 | 周规划；需要将 stated priorities 映射到实际时间块时 |

## 关键设计原则

1. **无需编码**：向 Claude Code 描述需求，它自动生成命令并保存
2. **渐进构建**：从一个命令开始，测试、精炼 prompt，再建下一个
3. **日常写作是前提**：命令只在 vault 有丰富上下文时才有效
4. **质量决定一切**：Agent 的输出质量完全取决于你喂给它的上下文质量

## 实现方式示例

以 `/trace` 为例，向 Claude Code 描述：

> Create a slash command called `/trace` that tracks how a specific idea has evolved over time across my Obsidian vault. It should:
> 1. Take a topic as input
> 2. Search the vault for all mentions of that topic
> 3. Use Obsidian CLI to follow backlinks and find related notes
> 4. Output a timeline showing when the idea first appeared, how it evolved, and what it's connected to now

Claude Code 生成命令后，直接输入 `/trace` 即可运行。

## 与访谈的对比

| 维度 | 访谈 (How I Use...) | Codebook |
|------|---------------------|----------|
| 形式 | 口语化对话 | 结构化文档 |
| 命令数量 | 约 10 个 | 明确 12 个 |
| 新增命令 | — | `/emerge`, `/schedule` |
| 重点 | 理念、动机、个人故事 | 实操、prompt 模板、使用场景 |
| 关键金句 | "Markdown 是 LLM 的氧气" | "The quality of information..." |
