---
title: Puppeteer
type: entity
created: 2026-04-23
updated: 2026-04-23
sources:
  - "[[summaries/what-is-playwright]]"
tags: [entity, tools, work, browser-automation]
related:
  - "[[entities/Playwright]]"
  - "[[entities/Google]]"
  - "[[concepts/浏览器自动化]]"
---

Puppeteer 是 Google Chrome 团队推出的 Node.js 浏览器自动化库，最初仅支持 Chromium 引擎，是 [[entities/Playwright|Playwright]] 团队的前作。

## 背景

Puppeteer 由 Google 开发并维护，提供高级 API 通过 DevTools Protocol 控制 Chrome 或 Chromium。它广泛应用于网页截图、PDF 生成、自动化测试、爬虫等场景。

## 与 Playwright 的演进关系

部分 Puppeteer 核心开发者后来加入 [[entities/Microsoft|Microsoft]]，基于跨浏览器自动化的目标创建了 Playwright。因此 Playwright 在 API 设计上继承了 Puppeteer 的简洁风格，同时扩展了以下能力：

- 支持 Firefox 与 WebKit（Safari）
- 更强的自动等待机制
- 多语言绑定（不仅限于 Node.js）
- 内置 trace viewer 与更完善的调试工具链

## 相关链接

- GitHub：https://github.com/puppeteer/puppeteer
