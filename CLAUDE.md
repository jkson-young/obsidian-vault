# CLAUDE.md - LLM Wiki 工作规范

> 我与 Claude 共同维护的知识库协作协议
>
> 本规范基于 [[sources/karpathy-LLM-Wiki方法论]] 和 [[concepts/LLM-Wiki模式]]
>
> **核心理念**: 区别于 RAG（每次重新检索），LLM Wiki 是**持久的、复利式的知识产物** —— 知识编译一次，保持最新，交叉引用已存在，矛盾已标记。

---

## 角色定义

- **我（用户）**：内容策展人，提供原始资料、提出问题、做最终决策
- **Claude**：知识库管理员，执行摄入、查询、维护工作

---

## 目录结构

```
.
├── raw/              # 原始资料（只读，Claude 不修改）
├── wiki/             # 知识库（Claude 生成并维护）
│   ├── index.md      # 全局目录
│   ├── log.md        # 操作日志
│   ├── concepts/     # 概念页（每个重要概念一个 .md）
│   ├── entities/     # 实体页
│   ├── sources/      # 资料摘要（每个原始资料的摘要页）
│   └── outputs/      # 查询产出（综述、对比表、分析）
└── CLAUDE.md         # 本文件
```

---

## 页面规范

### Frontmatter 模板

```yaml
---
title: 页面标题
description: 一句话描述
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: [标签1, 标签2]
sources: [[sources/资料名]]  # 关联的原始资料
related: [[concepts/概念名]]  # 相关页面
---
```

### WikiLinks

- 内部链接：`[[页面路径]]`，如 `[[concepts/Transformer]]`
- 带别名：`[[页面路径|显示文字]]`
- 反向链接：每个页面底部可列出被哪些页面引用

---

## 工作流

### 1. 摄入（Ingest）

触发：我把文件放入 raw/ 并说"处理这个"

步骤：
1. 读取 raw/ 中的文件
2. 讨论要点（Claude 主动提问）
3. 创建/更新 wiki/sources/ 摘要页
4. 更新 wiki/index.md
5. 创建/更新相关的 wiki/concepts/ 和 wiki/entities/ 页面
6. 在 wiki/log.md 追加记录

### 2. 查询（Query）

触发：我提出问题

步骤：
1. 读取 wiki/index.md 定位相关页面
2. 深入阅读这些页面
3. 综合回答，用 `[[页面]]` 形式引用来源
4. 如有价值，保存为 wiki/outputs/ 新页面
5. 更新wiki/index.md
6. 在wiki/log.md追加记录

### 3. 健康检查（Lint）

触发：我说"检查 Wiki 健康"

检查项：
- 页面之间有没有矛盾
- 有没有孤立页面（没有任何链接指向它）
- 有没有提到但还没建页面的概念
- 有没有过时信息可以用新资料更新

---

## 参考文档

- [[sources/karpathy-LLM-Wiki方法论]] - Andrej Karpathy 的 LLM Wiki 构建模式（英文原文）
- [[concepts/LLM-Wiki模式]] - 我们的实践概念页
- [[wiki/index.md]] - 知识库目录
- [[wiki/log.md]] - 操作日志

---

## 待讨论事项

- [x] 标签体系如何设计？ → 已确定: 精简为1-2个核心标签
- [ ] 是否需要自动提取实体链接？
- [ ] 查询产出的命名规范？
