---
title: "Prompt Engineering Full Course"
type: summary
created: 2026-04-22
updated: 2026-04-22
sources:
  - "[[raw/articles/Prompt Engineering Full Course]]"
tags: [ai-research, prompt-engineering]
---

## 来源

YouTube 视频，[[entities/Tech With Tim]]，2026-03-11 发布。

## 核心论点

**提示工程是用自然语言编程。** 与 Python、JavaScript 不同，你用的是日常语言来指导模型完成任务。同一个模型在不同提示下可以表现得「聪明」或「无用」——差异不在模型，而在你提供的清晰度、上下文和结构。

## 什么是提示工程

- **本质**：自然语言编程，而非打字
- **模型没有内置任务清单**：你必须在提示中定义任务、角色、格式和约束
- **Agent 时代的增强**：现代模型不仅能生成文本，还能调用工具、搜索网页、执行操作，提示工程的价值因此进一步放大

## LLM 如何「思考」

### 核心机制：文本预测
- LLM 本质上是**文本预测模型**（text prediction model）
- 给定输入 tokens，预测下一个最可能出现的 tokens
- 推理模型（reasoning models）的「思考」其实是后台 orchestration 在自动注入 chain-of-thought 指令

### 关键认知：上下文注入
- **模型本身没有记忆**
- ChatGPT、Claude 等工具在后台自动注入：对话历史、系统提示、工具描述等
- 99% 的情况下，你写的 prompt 不是模型看到的全部内容

## Steering vs Commanding

| 方式 | 示例 | 结果 |
|------|------|------|
| **Commanding** | "Summarize this" | 模型自行选择长度、风格、焦点 |
| **Steering** | "You are an executive assistant. Summarize the meeting transcript in 4 bullet points, focus on decisions and action items. No filler." | 精确控制输出方向 |

**Steering 的核心要素**：长度、焦点、格式、约束条件

## 核心技巧

### 1. 设定场景（Set the Scene）
四要素框架：
- **Role**（角色）："You are a senior B2B copywriter"
- **Audience**（受众）："The audience is ops managers at mid-sized companies"
- **Tone**（语气）："Confident but not salesy"
- **Format**（格式）："Two sentence LinkedIn ad, end with a clear CTA"

### 2. Few-Shot Prompting
- 提供输入-输出对示例，让模型推断模式
- 特别适用于：分类任务、特定格式输出、edge cases
- 与 fine-tuning 的本质相同：通过示例让模型学习特定模式

### 3. Chain of Thought
- 要求模型在给出最终答案前**逐步推理**
- 减少逻辑、数学、规划类任务的错误
- 现代推理模型（如 o1/o3、Claude 3.7 Sonnet thinking）已内置此机制，但在 API 调用或非推理模型中仍需要显式要求

### 4. Structured Output
- 要求模型以 JSON、XML、Markdown 表格等结构化格式输出
- 提供**精确的 schema 示例**，便于下游解析和使用
- 与 few-shot 结合：给格式示例 + 给数据示例

### 5. Constraints & Negatives
- **有时最有效的提示是告诉模型「不要做什么」**
- 示例约束：
  - 长度："Keep under 150 words"
  - 语气："No slang or humor. Do not apologize."
  - 格式："Do not use bullet points. Use one short paragraph."
  - 内容："Do not suggest paid tools. Do not include code."

### 6. Iterative Refinement
- 第一个 prompt 很少给出完美结果
- **将提示视为对话而非一次性尝试**
- 迭代流程：给出初稿 → "Shorter" → "More formal" → "Add another example" → "Focus only on X"

### 7. Interview Style Prompting
- **让模型 Interview 你**，而非你猜测模型需要什么上下文
- 流程：陈述目标 → 模型提出澄清问题 → 你逐一回答 → 模型基于完整上下文执行
- 价值：人类往往会遗漏细节、做出假设，而模型知道它自己需要什么信息

## 高级技巧

### System vs User Prompts
- **System Prompt**：设定模型身份、规则、风格，通常对用户不可见，持久生效
- **User Prompt**：单次任务指令
- 应用：ChatGPT 的 Custom Instructions、Cursor 的 agent 配置、API 的 system message

### Prompt Chaining
- 将复杂任务拆分为多个步骤，用前一步的输出作为下一步的输入
- 优势：可以在每一步验证结果质量，避免一次性提示中的信息丢失或混乱
- 示例：生成大纲 → 基于大纲扩写段落 → 生成 SEO meta 信息

### Self Evaluation
- 让模型对自己的输出进行 critique 或评分
- **关键技巧**：在**新会话**中进行评估，并谎称 "I wrote this"（而非 "AI wrote this"），以获得更客观的反馈
- 示例："Here's a summary I generated. Rate it 1-5 for clarity and completeness. In one sentence, suggest the single most important improvement."

### Temperature & Parameters
- **Temperature** 控制模型的确定性/创造性：
  - **低 temperature（~0-0.3）**：更可重复、确定性高，适合事实、代码、结构化输出、分类
  - **高 temperature（~0.7-1.0）**：更创意、更多样，适合头脑风暴、文案变体、创意写作
- 默认 temperature 通常偏保守（~0.7）

## 常见错误

| 错误 | 症状 | 修复 |
|------|------|------|
| 过于模糊 | 通用或不相关输出 | 添加 role, audience, tone, format, length |
| 一次塞入太多任务 | 遗漏、混淆、未完成 | 拆分为步骤或独立 prompt（chaining） |
| 缺少上下文/示例 | 格式或风格错误 | 添加 few-shot 示例，或用 interview 技巧补充 |
| 模型忽略格式 | 难以解析或复用 | 显式请求特定结构，加上 "only output..." |
| 假设模型有记忆 | 遗忘之前的上下文 | 重复或总结关键事实；新会话不要假设记忆 |

## 效率工具：语音输入

Tech With Tim 强烈推荐用**语音 dictation** 代替打字写 prompt：
- 好的 prompt 通常需要 10-20+ 行
- 语音输入速度快 3-5 倍，自然包含更多细节
- 推荐使用 Wispr Flow 等工具（自动标点、去 filler words、支持格式化指令如 "bullet point"）

## 与 Varun Mayya 的互补

| 维度 | Tech With Tim | Varun Mayya |
|------|---------------|-------------|
| 风格 | 系统化、结构化、教学导向 | 启发式、哲学化、案例驱动 |
| 侧重点 | 技巧分类与具体实现 | 世界构建理论与认知洞察 |
| 适用场景 | 学习框架、API 开发、工作流设计 | 创意写作、深度研究、个人成长 |
| 共同基础 | **上下文、 specificity、structure 决定输出质量** | **上下文、specificity、structure 决定输出质量** |
