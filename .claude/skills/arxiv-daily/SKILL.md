~~~markdown
---
name: arxiv-daily
description: "获取 arXiv 最新 AI 论文并写入 Obsidian 今日日记"
argument-hint: "arXiv RSS URL（默认: https://export.arxiv.org/rss/cs.AI）"
allowed-tools: ["Bash", "Read", "Write"]
---

# arXiv Daily

获取 arXiv 最新 AI 论文并写入 Obsidian 今日日记。

## 输入

用户提供 RSS feed URL（可选，默认使用 AI 相关论文 RSS）。

## 执行步骤

1. **获取论文数据**
   从用户提供的 RSS feed URL 获取论文列表。

2. **解析 RSS 内容**
   - 提取：title, abstract, link, published date
   - 按发布时间排序，选取最新发布的论文（默认 10 篇）

3. **翻译处理**
   - 将 title 翻译为中文
   - 将 abstract 翻译为中文
   - 保留原始 link 和 published date

4. **生成 Markdown 表格**

   ```markdown
   | 标题（中文） | 摘要（中文） | 原文链接 | 发布日期 |
   | ------ | ------ | ---- | ---- |
   | ...    | ...    | ...  | ...  |
~~~

1. **写入 Obsidian 日记**

   必须使用`obsidian-cli` skill完成以下操作：

   - 打开或创建今天的日记
   - 在日记末尾追加以下内容：

   ```markdown
   ## 今日AI论文
   
   （插入生成的 Markdown 表格）
   ```

## 注意事项

- 必须使用 `obsidian daily` 相关命令，不要直接操作文件系统
- 表格中摘要不要截断
- 每篇论文一行