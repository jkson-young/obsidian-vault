---
title: "如何设计自定义 slash 命令？"
type: output
created: 2026-04-22
updated: 2026-04-22
sources:
  - "[[summaries/how-i-use-obsidian-claude-code]]"
  - "[[summaries/obsidian-claude-codebook]]"
  - "[[concepts/LLM作为思考伙伴]]"
  - "[[concepts/Claude Code]]"
tags: [query, ai-research, pkm, claude-code]
---

## 核心框架

基于 [[entities/Vin|Internet Vin]] 的 12 命令实践体系，自定义 slash 命令的设计遵循 **"问题识别 → 命令定义 → 输出规范 → 迭代精炼"** 四阶段流程。

## 一、12 个命令的完整分类

### 会话与规划（建立上下文，消除重复）

| 命令 | 核心问题 | 输出形式 | 使用时机 |
|------|---------|---------|---------|
| `/context` | "我现在在忙什么？" | 完整生活/工作上下文摘要 | 每次新会话开始时 |
| `/today` | "今天最重要的是什么？" | 优先级日程计划 | 晨间；感到 overwhelmed 时 |
| `/closeday` | "今天我做了什么、学到了什么？" | 日终总结 + 未完成延续项 | 日终；清空大脑 |
| `/schedule` | "我的时间分配是否反映了我的优先级？" | 周时间分配建议 + 冲突标记 | 周规划 |

### 洞察与发现（从 vault 中提取无法靠记忆获得的模式）

| 命令 | 核心问题 | 输出形式 | 使用时机 |
|------|---------|---------|---------|
| `/trace` | "这个想法是怎么走到今天的？" | 时间线演变报告 | 理解认知弧线；想法反复出现时 |
| `/connect` | "这两个看似无关的领域有什么联系？" | 关联路径图 + 桥接洞察 | 卡壳时；怀疑两个想法有关联 |
| `/drift` | "我的潜意识在反复盘旋什么？" | 跨笔记松散主题聚类 | 感觉有东西浮现但无法命名 |
| `/emerge` | "哪些零散想法快要变成更大的东西了？" | 潜在项目/文章/产品识别 | 零散想法开始聚集时 |

### 压力测试与外化（检验认知一致性，将洞察转化为行动）

| 命令 | 核心问题 | 输出形式 | 使用时机 |
|------|---------|---------|---------|
| `/ghost` | "如果是我在回答这个问题，我会怎么说？" | 用你的声音撰写的回答 | 外化思维；需要"像自己写的"草稿 |
| `/challenge` | "我现在的信念有没有漏洞？" | 矛盾点 + 薄弱假设 + 替代视角 | 重大决策前；stress-test 想法 |
| `/ideas` | "基于我的真实兴趣，有什么值得做的？" | 分类行动建议（工具/人脉/主题/写作）| 需要 grounded in 真实兴趣的创新 |
| `/graduate` | "哪些日常想法值得变成独立概念？" | 新生成的概念页草稿 | 周回顾；daily notes 充满半成品 |

## 二、四条设计原则

### 1. 从认知困境出发，而非从功能出发

Vin 的命令命名全是**动词**，每个对应一个具体的思维困境：

- "我是否在某件事上一直在自欺欺人？" → `/drift`
- "我感觉有两个想法有关联，但看不清" → `/connect`
- "我零散写了很多东西，但不知道哪些能变成项目" → `/emerge`
- "如果是我来回答这个问题，我会怎么说？" → `/ghost`

### 2. 利用关系数据，而非仅文本内容

最有价值的命令（`/trace`、`/connect`、`/emerge`）依赖的是 **Obsidian CLI 提供的 backlinks 关系**，而非单纯的文本搜索。

> 设计命令时应问：**哪些洞察只能从"文件间的关联"中诞生？**

### 3. 输出格式决定思考深度

命令的设计必须包含明确的输出模板：

- `/trace` → 按时间线组织的历史演变报告（首次出现 → 关键演变 → 当前连接）
- `/ideas` → 分类明确的行动清单（工具 / 人脉 / 主题 / 写作）
- `/challenge` → 矛盾点 + 薄弱假设 + 替代视角

### 4. 元认知层级递进

| 层级 | 命令 | 目标 |
|------|------|------|
| 获取信息 | `/context`, `/today`, `/schedule` | 建立上下文，消除每次重复解释 |
| 检验认知 | `/ghost`, `/challenge` | 发现偏见、盲点、自我矛盾 |
| 发现模式 | `/emerge`, `/connect`, `/drift` | 命名未命名之物，发现隐性关联 |
| 转化为知识 | `/graduate`, `/ideas` | 将洞察持久化为可行动的知识 |

## 三、实现方式：无需编码

向 Claude Code 用自然语言描述需求即可。以下是两个典型示例。

### 示例 1：/trace

> Create a slash command called `/trace` that tracks how a specific idea has evolved over time across my Obsidian vault. It should:
> 1. Take a topic as input
> 2. Search the vault for all mentions of that topic
> 3. Use Obsidian CLI to follow backlinks and find related notes
> 4. Output a timeline showing when the idea first appeared, how it evolved, and what it's connected to now

### 示例 2：/challenge

> Create a slash command called `/challenge` that pressure-tests my current beliefs. It should:
> 1. Take a topic or recent note as input
> 2. Scan my vault for related notes and past statements on this topic
> 3. Identify contradictions between what I believe now and what I've written before
> 4. Surface assumptions I might be making without evidence
> 5. Output a structured critique with specific note references

Claude Code 生成并保存命令后，直接输入 `/trace` 或 `/challenge` 即可运行。

## 四、迭代策略

1. **从一个命令开始**：选一个你最频繁遇到的认知困境
2. **测试并记录**：运行后记录输出是否解决了你的问题
3. **精炼 prompt**：
   - 输出太泛 → 增加输出格式约束
   - 搜索范围太窄 → 放宽时间窗口或放宽关联条件
4. **建立组合工作流**：
   - `/today` → 工作 → `/closeday` → `/graduate`（将当日灵感提升为概念页）
   - `/drift` → `/emerge` → `/ideas`（从潜意识盘旋到潜在项目到行动建议）

## 五、当前知识库的缺口

如需深化这一主题，wiki 还缺少：

- **Prompt 工程细节**：系统提示词、上下文窗口策略、token 优化
- **评估方法论**：如何判断一个命令是否"有效"？是否有量化指标？
- **代码实现**：Vin 的 skills/commands 实际代码结构（访谈中提到会在 show notes 分享）
- **更多实践者的案例**：除 Vin 之外的命令设计模式
- **命令之间的依赖与冲突**：多个命令组合使用时如何避免重复扫描 vault

## 六、可操作的下一步

如需设计一个**具体的 slash 命令**，可以按以下模板描述给 Claude Code：

```
Create a slash command called /[命令名] that [解决什么问题].
It should:
1. [输入方式：主题/时间段/笔记范围]
2. [搜索策略：文本搜索 / backlinks / tags / frontmatter]
3. [处理逻辑：排序方式、关联深度、过滤条件]
4. [输出格式：时间线/列表/对比表/图表]
```

---

*本回答综合了 [[summaries/how-i-use-obsidian-claude-code|Vin 的访谈]] 与 [[summaries/obsidian-claude-codebook|Codebook 文档]]。两者互为补充：访谈讲理念与动机，Codebook 讲具体命令与 prompt 模板。*
