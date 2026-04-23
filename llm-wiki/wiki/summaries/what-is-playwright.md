---
title: What is Playwright? (Playwright introduction tutorial, features & demo)
type: summary
created: 2026-04-23
updated: 2026-04-23
sources:
  - "[[raw/articles/What is Playwright (🎭 Playwright introduction tutorial, features & demo)|What is Playwright?]]"
tags: [summary, work, tools]
---

> 来源：Testopic 频道（Victor）2021-06-02 发布于 YouTube。一部面向初学者的 15 分钟 Playwright 入门教程，涵盖安装、代码生成器、脚本结构、截图与录屏。

## 核心要点

1. **Playwright 定位**：由 Microsoft  backing 的开源 Node.js 浏览器自动化库。核心团队成员来自原 Google [[entities/Puppeteer|Puppeteer]] 团队，bug 响应速度极快（平均 48 小时内）。
2. **多引擎、多语言**：支持 Chromium、Firefox、WebKit 三大引擎，覆盖 Chrome、Edge、Safari 等主流浏览器；提供 TypeScript/JavaScript、Python、C#、Java 绑定。
3. **核心特性**：内置代码生成器（Codegen / Inspector）、自动截图与录屏、网络请求拦截与修改、设备/地理位置/时区模拟、默认 headless 运行。
4. **脚本三层结构**：所有 Playwright 脚本均遵循 **Browser → Context → Page** 的层级：
   - **Browser**：类似真实浏览器进程；
   - **Context**：相互隔离的浏览会话（可理解为无痕窗口）；
   - **Page**：具体标签页。
5. **零代码起步**：通过 `npx playwright codegen <url>` 启动 Inspector，在浏览器中手动操作即可实时生成对应语言的自动化脚本，大幅降低入门门槛。
6. ** headless 与 headed**：Playwright 默认以 headless（无界面）模式运行；Inspector 自动生成的代码会显式设置 `headless: false`，方便初学者观察执行过程。

## 教程演示流程

- 安装 Node.js + VS Code + Playwright（`npm i -D playwright`）
- 使用 `codegen` 访问 Wikipedia 并记录点击、导航操作
- 将生成的 JS 代码粘贴到本地文件并运行（`node hello-playwright.js`）
- 扩展脚本：添加 `page.screenshot()` 实现截图
- 扩展脚本：在 `browser.newContext({ recordVideo: { dir: 'videos/' } })` 中开启录屏
