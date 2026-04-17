---
title: 操作日志
date: 2026-04-09
description: 所有操作的完整记录
---

# 操作日志

记录格式：`## [YYYY-MM-DD] 操作类型 | 标题`

---

## [2026-04-13] ingest | karpathy LLM Wiki 方法论

- 读取 raw/karpathy wiki方法论.md
- 创建 sources/karpathy-LLM-Wiki方法论.md（核心方法论文档）
- 创建 concepts/LLM-Wiki模式.md（我们的实践概念页）
- 更新 index.md

## [2026-04-13] restructure | Product/Project 结构调整 + 标签精简

- 重命名 `entities/project/活动助手.md` → `entities/project/活动助手测试.md`
- 简化 `entities/product/活动助手.md`，只保留产品定义
- 创建 `entities/project/途邦SCRM测试.md`，简化 `entities/product/途邦SCRM.md`
- 调整分工：product/ 是产品档案，project/ 是测试工作区
- **标签精简**：
  - product/*: `[产品]`
  - project/*: `[测试项目]`
  - sources/*: 只保留最核心1个标签（部署/运维/数据查询/集成测试）
  - 移除 `内部文档` `网吧管理` 等冗余标签
- 更新 index.md 中的链接

操作类型：ingest（摄入）/ query（查询）/ lint（健康检查）/ init（初始化）

---

## [2026-04-13] ingest | 活动助手：线上环境切换 + 游戏数据查询

- 读取 raw/活动助手切换线上环境.md、raw/活动助手游戏对局数据查询.md
- 创建 sources/活动助手切换线上环境.md（已脱敏）
- 创建 sources/活动助手游戏对局数据查询.md（已脱敏）
- 创建 concepts/无畏契约赛事数据.md（新概念页）
- 更新 entities/project/活动助手.md：添加环境切换对照表、数据查询章节
- 更新 index.md

## [2026-04-09] ingest | 活动助手切换登录门店

- 读取 raw/活动助手切换登录门店.md
- 创建 sources/活动助手切换登录门店.md（已脱敏）
- 建立专题聚合页：entities/project/活动助手.md
- 更新 entities/product/活动助手.md 添加反向链接
- 更新 index.md

## [2026-04-09] ingest | 活动助手测试环境安装

- 读取 raw/活动助手测试环境安装.md
- 创建 sources/活动助手测试环境安装.md（已脱敏）
- 创建 entities/product/活动助手.md（产品实体页）
- 更新 index.md
- 讨论要点：确认活动助手为公司产品、DSSP 无需单独页面、敏感信息脱敏、摘要页仅用文字

## [2026-04-09] init | 初始化 LLM Wiki 系统

- 创建目录结构
- 创建 index.md 和 log.md
- 准备就绪，等待第一次资料摄入
