---
title: "如何设计自定义 slash 命令？"
type: output
created: 2026-04-22
updated: 2026-04-22
sources:
  - "[[summaries/how-i-use-obsidian-claude-code]]"
  - "[[concepts/LLM作为思考伙伴]]"
  - "[[concepts/Claude Code]]"
tags: [query, ai-research, pkm, claude-code]
---

## 回答

基于当前 wiki 中 [[summaries/how-i-use-obsidian-claude-code|Vin 的访谈]] 和 [[concepts/LLM作为思考伙伴|LLM 作为思考伙伴]] 的资料，自定义 slash 命令的设计可以从以下层面理解：

### 一、Vin 的实践：两类命令

Vin 的 slash 命令分为**日常运营**和**思考工具**两大类：

**日常运营命令**
| 命令 | 功能 | 设计意图 |
|------|------|---------|
| /context | 加载完整生活与工作上下文 | 消除每次会话重复解释 |
| /today | 拉取日历、任务、笔记生成优先计划 | 将外部数据与内部反思结合 |
| /close-day | 日终处理，提取行动项、发现 vault 关联 | 闭环每日信息流 |

**思考工具命令**
| 命令 | 功能 | 认知目标 |
|------|------|---------|
| /ghost | 以你的声音回答问题 | 检验自我认知的一致性 |
| /challenge | 用 vault 历史压力测试当前信念 | 发现偏见与盲点 |
| /emerge | 提炼隐含但未明确表达的想法 | 命名未命名之物 |
| /drift | 对比 stated intentions vs 实际行为 | 发现逃避与偏差 |
| /trace | 追踪想法的演变历史 | 理解认知发展轨迹 |
| /connect | 桥接两个不同领域 | 激发跨界创新 |
| /ideas | 基于全库生成跨域可行想法 | 从反思转向行动 |
| /graduate | 将日常笔记中的想法提升为独立概念页 | 想法的"毕业"机制 |

### 二、可提炼的设计原则

1. **从问题出发，而非从功能出发**
   Vin 的命令命名都是动词（trace, connect, challenge, emerge），每个对应一个具体的认知困境："我是否在某件事上一直在自欺欺人？" → /drift

2. **利用 vault 的链接图谱**
   最有价值的命令（/connect, /trace）都依赖 Obsidian CLI 提供的**关系数据**，而非单纯的文本内容。设计命令时应思考：哪些洞察只能从"文件间的关联"中诞生？

3. **输出格式决定思考深度**
   /trace 输出的是按时间线组织的历史演变报告；/ideas 输出的是分类明确的行动清单。命令的设计应包含明确的输出模板。

4. **元认知层级递进**
   - 第一层（/context, /today）：获取信息
   - 第二层（/ghost, /challenge）：检验认知
   - 第三层（/emerge, /connect）：发现新模式
   - 第四层（/graduate）：将洞察转化为持久知识

### 三、当前 wiki 的缺失

本 wiki 目前**缺少设计方法论层面的内容**：
- Vin 是如何从"我想解决什么问题"推导出具体命令的？
- 命令的 prompt 工程细节（系统提示词、上下文窗口策略）
- 如何评估一个命令是否"有效"？
- 命令之间的组合工作流

### 四、建议摄入的资料

如需补全这一主题，建议摄入：
- Vin 公开的 skills/commands 代码（访谈中提到会在 show notes 中分享）
- Claude Code 官方文档中关于自定义命令的部分
- 其他 Obsidian + LLM 实践者的命令设计案例

---

*本回答基于 wiki 现有资料综合。如需深入 prompt 工程或具体实现细节，建议摄入上述缺失资料。*
