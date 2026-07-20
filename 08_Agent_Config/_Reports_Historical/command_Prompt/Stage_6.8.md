# Stage 6.8 — ResearchAI Reality Audit

## Objective

对当前 ResearchAI 项目进行一次全面只读审计。

目的：

1. 建立当前项目真实状态（Reality State）
2. 检查过去所有 Stage 执行报告是否与 filesystem 实际状态一致
3. 检查 Windows → Ubuntu 迁移造成的隐性问题
4. 检查项目架构是否仍符合最初建设目标
5. 输出完整审计报告

IMPORTANT:

- READ ONLY
- 不修改任何文件
- 不修复任何问题
- 不创建新节点
- 不调整目录结构

最终只输出：

08_Agent_Config/Stage_6.8_Reality_Audit_Report.md


---

# Part 1 — Project Architecture Reality Check

检查当前目录：

ResearchAI/

重点检查：

- Stage 0~6 当前实际完成情况
- README、设计文档、Agent配置是否匹配当前目录
- 是否存在历史设计已经废弃但文档仍保留的问题

重点关注：

- 目标架构是否仍然是：

Raw Data
 ↓
Processed Literature
 ↓
KnowledgeVault
 ↓
Research Map
 ↓
Experiment System
 ↓
Paper Production


判断：

- 当前实现是否偏离最初设计
- 哪些模块已经完成
- 哪些模块只是文档存在但实际未实现


---

# Part 2 — Documentation vs Filesystem Verification

检查所有 Stage 报告：

范围：

08_Agent_Config/

包括：

- Stage_6.5.x
- Stage_6.6.x
- Stage_6.7
- Stage_1.5-7D.x
- 其他重要完成报告


建立表格：

| Stage | Report Claim | Actual Filesystem | Status |
|---|---|---|---|
| | | | Verified / Partial / Incorrect |


重点检查：

- 文件是否真的存在
- 文件内容是否符合报告
- 数量是否一致
- 是否存在报告遗漏修改
- 是否存在报告声称修改但实际未修改


---

# Part 3 — Windows → Ubuntu Migration Audit

重点检查迁移残留问题。


检查：

## Path Problems

搜索：

D:/
C:/
\\ResearchAI
Windows absolute path


检查：

- README
- Agent prompt
- skill
- config
- template
- workflow


特别检查：

01_Literature README

Zotero路径：

旧：

D:\ResearchAI_Data\

新：

/home/lco/ResearchAI_Data/


输出：

| File | Old Path | Current Reality | Severity |


---

## Encoding Audit

重新检查：

所有 md 文件：

检查：

- UTF-8 BOM
- CRLF
- GBK乱码
- Windows newline
- 中文乱码


不要只检查部分文件。


输出：

统计：

- BOM数量
- CRLF数量
- suspected corrupted files


特别检查：

- Templates
- README
- Meta files
- Agent prompts


---

# Part 4 — KnowledgeVault Schema Reality Audit

检查：

02_KnowledgeVault/


包括：

03_Methods
04_Tasks
05_Datasets
00_Meta


检查 YAML frontmatter：

## Methods

确认：

method_name
category
application
related_tasks
tags


## Tasks

确认：

task_name
domain
related_methods
related_datasets


## Datasets

确认：

dataset_name
source_type
related_tasks
related_papers


不要假设模板正确。

以：

实际文件

为准。


输出：

| Node Type | Expected Field | Missing Count | Files |


---

# Part 5 — Knowledge Graph Integrity

扫描全部 wikilinks。


检查：

## Broken Links

分类：

A. 真正错误

例如：

[[XXX]]

但是不存在。


B. Intentional placeholders

例如：

Meta Map navigation stubs


C. Historical leftovers


输出：

数量和列表。


---

检查：

## Bidirectional Connectivity

分析：

Method ↔ Task

Task ↔ Dataset

Dataset ↔ Paper


不要强制全部双向。

判断：

- 哪些缺失合理
- 哪些影响发现能力


---

# Part 6 — Agent Workflow System Audit

检查：

08_Agent_Config/


重点：

## Skills

检查：

- skill目录
- prompt
- workflow


确认：

文档中的skill是否真实存在。


## MCP / Tool references

检查：

是否存在：

旧server名称

旧路径

Windows路径


例如：

skill:researchai

是否仍有效。


## Codex Migration

检查：

.codex/

包括：

- config.toml
- skills
- plugins
- memories
- sessions


检查：

Windows backup迁移是否完整。


---

# Part 7 — Git Repository Audit

检查：

git status

git log


分析：

- 当前branch
- 未提交修改
- 是否存在大文件
- 是否包含临时文件


检查：

.gitignore


特别关注：

Windows迁移产生：

- backup
- cache
- tar
- temp
- generated files


---

# Part 8 — Original Goal Alignment

回顾最初目标：

ResearchAI 是为了：

1. 文献智能管理
2. 深度阅读自动化
3. 知识图谱构建
4. 研究方向发现
5. 实验管理
6. 论文生产


请评价：

当前系统：

## 已实现

## 部分实现

## 尚未实现


并判断：

当前最大风险是什么。


---

# Part 9 — Final Report

生成：

Stage_6.8_Reality_Audit_Report.md


结构：

# Executive Summary

# Current Architecture Status

# Documentation vs Reality

# Migration Issues

# Encoding Status

# Schema Status

# Knowledge Graph Status

# Agent System Status

# Git Status

# Risks

# Recommended Next Steps


不要执行任何修复。


等待用户审核。
