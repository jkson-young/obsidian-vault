---
title: KaneAI
type: entity
created: 2026-04-23
updated: 2026-04-23
sources:
  - "[[summaries/software-testing-course-playwright-e2e-ai]]"
tags: [entity, tools, testing, ai, agents]
related:
  - "[[entities/TestMu]]"
  - "[[concepts/AI辅助测试]]"
  - "[[entities/Playwright]]"
---

KaneAI 是由 [[entities/TestMu|TestMu]] 开发的 AI 原生测试 Agent，允许用户用自然语言描述测试场景，自动生成并执行可复用的自动化测试。

## 核心能力

- **自然语言生成测试**：输入 "go to website, click search, type keyboard, verify one product card visible" 即可生成完整测试步骤
- **多平台支持**：桌面浏览器、移动浏览器、原生移动应用
- **Auto-healing**：当 UI 发生变化（如元素 ID 改变）时，AI 基于测试意图自动寻找替代元素，降低维护成本
- **代码导出**：可将生成的测试导出为 Python（Selenium）、JavaScript/Playwright 等多种语言和框架
- **API 测试**：支持在 UI 测试流程中嵌入 API 请求验证
- **CI/CD 集成**：提供 API 接口，可从 GitHub Actions、Jenkins 等流水线触发测试执行

## 使用场景

- 非技术人员（QA 分析师、产品经理）快速创建测试
- 原型阶段快速验证测试思路
- 减少因 UI 微调导致的测试崩溃
- 补充传统 coded 测试，形成「人工精确控制 + AI 快速覆盖」的组合策略

## 局限性

- 复杂边界 case 仍需人工审查和补充
- 不能完全替代对测试知识的理解（需判断测什么、为什么测）
- 部分高级功能（如多框架代码导出）可能仍在迭代中
