---
title: Claude Code
type: concept
created: 2026-04-22
updated: 2026-04-22
sources:
  - "[[summaries/how-i-use-obsidian-claude-code]]"
  - "[[summaries/obsidian-claude-codebook]]"
tags: [ai-research, tools, agents]
related:
  - "[[concepts/Obsidian]]"
  - "[[concepts/第二大脑]]"
---

Claude Code 是 Anthropic 推出的命令行 Agent，可通过自然语言控制计算机。与传统聊天界面不同，它直接操作文件系统、执行命令，并能读取和修改项目中的文件。

## 核心能力

- **文件操作**：创建、读取、编辑文件
- **命令执行**：运行 shell 命令
- **持久上下文**：通过引用文件传递项目描述，避免每次会话重复解释

## 与 Obsidian 的结合

当 Claude Code 通过 [[concepts/Obsidian CLI|Obsidian CLI]] 访问 Obsidian vault 时，它的能力被大幅增强：

1. **读取互连的 markdown 文件**：不仅获取内容，还获取 backlinks 关系
2. **发现隐性模式**：指出你在不同领域反复书写的同一主题
3. **作为思考伙伴**：通过自定义 slash 命令（如 /trace、/connect、/ideas）深度个性化

## 关键洞察

> "The whole game is feeding the beast good context."
>
> — [[entities/Vin]]

Agent 的输出质量完全取决于输入的上下文质量。一个结构良好的 Obsidian vault 就是最高质量的上下文来源。
