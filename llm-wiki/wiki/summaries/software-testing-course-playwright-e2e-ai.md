---
title: "Software Testing Course – Playwright, E2E, and AI Agents"
type: summary
created: 2026-04-23
updated: 2026-04-23
sources:
  - "[[raw/articles/Software Testing Course – Playwright, E2E, and AI Agents|Software Testing Course]]"
tags: [summary, work, testing, ai-research]
---

> 来源：freeCodeCamp.org（Bo KS）2026-03-19 发布于 YouTube。一部时长约 1 小时的软件测试系统课程，涵盖测试理论基础、Playwright 实战、以及 AI 驱动的测试工具 KaneAI。

## 核心要点

1. **测试的价值**：通过 Knight Capital（45 分钟损失 4.4 亿美元）、Therac-25（辐射过量致死）、Boeing 737 Max（软件导致坠机）等案例，说明生产环境修复 bug 的成本是开发阶段的 10–100 倍。
2. **测试金字塔**：由 Mike Cohn 推广的三层模型——底层大量快速的单元测试，中层适量的集成测试，顶层少量但关键的端到端测试。越往上层，测试越慢、维护成本越高、越容易脆弱（brittle）。
3. **Playwright 实战**：以 TechMart 电商应用为例，演示了：
   - 测试结构：`test.describe` 分组、`beforeEach` 前置、`test()` 用例、`expect` 断言
   - 定位器策略：ID、class、text content、role/accessibility、CSS 组合选择器
   - 动作-验证模式：执行操作 → 验证即时反馈 → 验证状态变更
   - API 测试：`request.get`/`post` 直接测试后端接口
   - 调试手段：headed 模式、UI interactive 模式、trace viewer、失败截图与录屏
4. **进阶测试技术**：
   - **边缘 case 测试**：空输入、特殊字符、XSS 注入、重复点击、空购物车结算
   - **Mocking**：`page.route` 拦截网络请求，模拟 500 错误、慢网络（3s 延迟）、缺货数据、POST 失败
   - **可访问性测试**：alt text、form labels、heading 层级、键盘导航（tab 可达性）
5. **传统测试的挑战**：学习曲线陡峭、UI 变动导致维护负担重、flaky test（时间/网络/动态内容导致的间歇性失败）、编写成本高。
6. **AI 辅助测试**：以 [[entities/KaneAI|KaneAI]]（[[entities/TestMu|TestMu]] 出品）为例，展示用自然语言描述即可生成可执行测试，支持 auto-healing（UI 变化时自动修复选择器）、导出为多语言/多框架代码、API 测试、CI/CD 集成。
7. **最佳实践**：测试命名要自描述、保持测试独立（不相互依赖）、Page Object Pattern 降低维护成本、集成 CI/CD 自动执行、人工探索性测试与自动化测试互补。
