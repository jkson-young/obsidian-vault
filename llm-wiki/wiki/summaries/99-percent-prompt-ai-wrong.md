---
title: "99% of You Prompt AI Wrong"
type: summary
created: 2026-04-22
updated: 2026-04-22
sources:
  - "[[raw/articles/99% of You Prompt AI Wrong]]"
tags: [ai-research, prompt-engineering]
---

## 来源

YouTube 视频，[[entities/Varun Mayya]]，2025-12-02 发布。

## 核心论点

**提示工程的本质是世界构建（world building），而非打字。** 99% 的人之所以提示 AI 的方式是错的，是因为他们只给了 AI 一个空泛的指令，没有提供足够的「拼图碎片」让 AI 填充出一个符合你愿景的世界。

> "The more pieces of the puzzle you give, the more unique your world becomes."

## 关键洞察：世界构建

Varun 用《沙丘》的例子说明：如果你只说「有一个世界，里面住着巨人」，别人（和 AI）只会想到巨魔或独眼巨人。但如果你补充「这是一个干燥的世界，一切都是沙子构成的，人们穿防湿服，几个部落在争夺沙子中的特殊资源」——听者会自动联想到沙虫。

**AI 也是如此。** 你不给它足够的拼图碎片，它就会退回到最通用的世界，这就是为什么所有人的 AI 输出开始看起来一样。

## 十大提示技巧

### 1. 世界构建（World Building）
- 先想清楚你想要什么，再构建世界
- 给 AI 足够的上下文、参考和约束条件
- 最佳方式：用例子说话（example giving）

### 2. 深度研究（Deep Research）
向 AI 请求三个层次：
1. **摘要**：基础事实
2. **红药丸洞察（Red Pill Insights）**：书中相信但大多数人不相信的东西
3. **可行动的证据**：如何将这些洞察转化为行动

Varun 还强调**成本拆解**：让 AI 把任何数字拆分到最细粒度（如 3A 游戏的 1 亿美元预算拆解为开发成本 vs 营销成本，再拆解到具体岗位薪资）。

### 3. 元提示（Meta Prompting）
用 AI 来生成给另一个 AI 的提示词。例如：
- 先向 GPT 描述你的世界
- 然后让它「给我一个可以放进扩散模型的 prompt」
- GPT 知道 diffusion models 会不必要地「烘焙」哪些元素，因此会过滤掉

同样适用于代码：让 AI 先拆解 Stripe 页面的所有组件，再逐一修改生成。

### 4. 角色扮演（Personas）
让 AI 扮演不同角色来同一概念：
- 「像给 5 岁小孩解释」
- 「像给 10 岁有基础公式理解的小孩解释」
- 「像给 25 岁物理专业学生解释」

这比简单的「explain simply」有效得多，因为你可以在不同深度间跳跃。

### 5. 缺口发现（Gap Finder）
每周问 AI：
> "Based on what you know about me, what are the gaps in my knowledge?"

Varun 每周都用这个技巧，AI 曾指出他对免疫系统的理解过于简化。这是一种「安全空间」中的自我弱点暴露。

### 6. 防止幻觉（Preventing Hallucination）
- 要求 AI 只在有信心时回答
- 要求每个回答附带**置信度分数（confidence score）**
- AI（尤其是 GPT/Claude）倾向于「讨好你」，即使错了也表现得很自信

### 7. 语音笔记（Voice Notes）
好的提示通常需要 10-20 行，甚至几页。用语音输入（注意：是语音**笔记**转文字，不是实时语音对话）可以大幅降低输入成本，同时自然地进行大量世界构建。

### 8. 消除 AI 痕迹（Erase AI Stains）
避免典型 AI 句式结构：
- ❌ "X isn't just about Y"
- ❌ "X is more than just Y"
- ❌ "X goes beyond Y"

改用**直接的肯定句**。仅此一条就能消除 60-70% 的 AI 写作痕迹。

更进一步：混合多种写作风格（如「写得像 Paul Graham + Varun Mayya」），或让 AI 学习你 pre-AI 时代的内容语料。

### 9. 情感提示（Emotional Prompting）
AI 对情感语言有反应：
- "take a deep breath" 可以提升数学测试表现
- "think harder" 可以让 thinking models 消耗更多 token、给出更好答案
- 威胁式提示（如 "if you don't give me exact numbers, someone will pay for it"）可以提升数值准确性

原理：人类写作中，情感词汇会激活杏仁核和海马体的连接，LLM 在训练中学到了这些痕迹。

### 10. 下一步学什么（What's Next To Learn）
> "Based on what you know about me, what should I learn next?"

Varun 称这是他过去两年阅读量激增的主要原因——AI 不是帮他读内容，而是帮他**发现新路径**，然后他沿着路径去读 1950 年代或 1600 年代的书籍。

## 关键金句

> "We always thought AI is about getting the AI to do productive work, but actually it's about making you better. It's about figuring out where you should go, what you should learn, what your gaps are."

## 与 Vin 的对比

| 维度 | Varun Mayya | Vin |
|------|-------------|-----|
| 侧重点 | 单次提示的质量 | 系统化命令的设计 |
| 核心隐喻 | 世界构建 / 拼图碎片 | 上下文喂养 / markdown 是氧气 |
| 使用场景 | 日常任务、学习、创作 | 知识管理、思维追踪、自我检验 |
| 共同点 | **上下文质量决定输出质量** | **上下文质量决定输出质量** |
