# Stage 7 — Project State Reconciliation Audit

## Role

你现在接管一个长期建设中的 ResearchAI 项目。

你的任务不是继续执行已有 Stage，而是：

> 对当前项目进行一次完整的状态审计，确认“设计目标、历史执行计划、实际文件状态、Agent 系统状态”四者是否一致。

这是一次 **READ-ONLY Audit**。

禁止修改任何文件。

---

# Background

该项目最初目标：

构建一个面向科研人员的 AI-Augmented Research Operating System。

核心目标：

1. 建立长期维护的科研知识库
2. 将论文 → 方法 → 任务 → 数据集 → 实验 → Idea 形成知识图谱
3. 使用 Agent 自动化完成：

   * 文献收集
   * Paper Intake
   * Deep Reading
   * Knowledge Extraction
   * Knowledge Node Construction
   * Research Gap Discovery
   * Experiment Planning
4. 最终形成支持深度学习 + 地震 AI 研究的个人科研基础设施

历史 Stage：

```
Stage 0
Workspace Initialization

目标：
- ResearchAI workspace
- Git
- Agent workspace
- 基础目录


Stage 1
Knowledge Infrastructure Construction

目标：
- Obsidian KnowledgeVault
- Templates
- Meta Maps
- Paper Index
- Research Map


Stage 1.5
Agent Workflow System

目标：
- Skills
- Paper Intake
- Deep Read
- MinerU pipeline
- Zotero integration
- Encoding governance
- Workflow automation


Stage 2
Literature Intelligence

目标：
- 大规模论文处理
- Literature Card
- Paper Notes
- Knowledge Graph
- Research Gap


Stage 3
Research Direction Formation

目标：
- Seismic AI Research Map
- Method Nodes
- Dataset Nodes
- Task Nodes
- Idea Nodes


Stage 4
Experiment System

目标：
- Dataset management
- Baseline reproduction
- Model development
- Experiment tracking


Stage 5
Paper Production

目标：
- Writing pipeline
- Draft generation
- Revision
- Submission preparation


Stage 6.x
KnowledgeVault Refinement

已执行：
- Knowledge node extraction
- Schema repair
- Wikilink integrity
- Connectivity enhancement

包括：

Stage 6.5
Knowledge Node Extraction

Stage 6.5.2
新增：
- Method nodes
- Task nodes
- Dataset nodes

Stage 6.5.3
Audit

Stage 6.5.4
Vision Transformer completion

Stage 6.5.5
Quality improvement

Stage 6.6
Schema consistency audit

Stage 6.6.1
Schema repair

Stage 6.6.2
Wikilink integrity scan

Stage 6.7
Knowledge graph connectivity enhancement
```

---

# Current ResearchAI Focus

当前知识库主要围绕：

## Seismic AI + Deep Learning

包含：

### Methods

例如：

* CNN
* Transformer
* Vision Transformer
* SegFormer
* U-SegFormer-Hyper
* PhaseNet
* GENIE
* PLAN
* Multi-task Learning

### Tasks

例如：

* Seismic Phase Picking
* Phase Association
* Earthquake Location
* Earthquake Sequence Analysis
* Seismic Facies Segmentation

### Datasets

例如：

* NCEDC
* Japan Hi-net
* F3 Netherlands
* OpenFWI
* Marmousi
* SEAM
* SEG Salt
* Penobscot
* Thebe

---

# Important Historical Context

## Windows → Ubuntu Migration

项目曾从 Windows 迁移到 Ubuntu。

需要重点检查：

### Codex / Agent

检查：

* ~/.codex 是否完整迁移
* sessions 是否存在
* skills 是否存在
* plugins 是否一致
* config.toml 是否合理
* MCP 配置是否失效
* Windows path 是否残留

重点关注：

例如：

```
C:\ResearchAI
```

是否仍存在于：

* config
* session
* task
* prompt
* skill

检查：

Linux path：

```
/home/lco/ResearchAI
```

是否一致。

---

## Git

检查：

* 当前 git 状态
* branch
* remote
* commit 历史
* 是否存在大量未提交修改
* Windows 和 Ubuntu 是否产生冲突

---

## Encoding

历史出现：

* GBK → UTF-8
* BOM
* CRLF → LF

问题。

检查：

所有核心文件：

```
00_Meta
03_Methods
04_Tasks
05_Datasets
08_Agent_Config
```

是否：

* UTF-8
* 无 BOM
* LF

---

# Audit Scope

请检查：

---

# 1. Project Structure Audit

检查：

```
ResearchAI/
```

目录是否符合设计。

输出：

* 当前目录结构
* 与设计目标差异
* 异常文件
* 空目录
* 废弃文件

---

# 2. Stage Completion Audit

建立：

```
Stage
|
Expected State
|
Actual State
|
Status
```

例如：

| Stage  | Expected             | Actual  | Status  |
| ------ | -------------------- | ------- | ------- |
| Stage1 | Vault infrastructure | exists  | done    |
| Stage2 | Paper pipeline       | partial | warning |

判断：

* 已完成
* 部分完成
* 未开始
* 被后续修改破坏

---

# 3. KnowledgeVault Graph Audit

检查：

## Nodes

统计：

```
Methods
Tasks
Datasets
Papers
Meta
Ideas
```

数量。

检查：

* orphan nodes
* duplicate nodes
* naming inconsistency
* case sensitivity

例如：

```
Segformer
SegFormer
```

这种问题。

---

# 4. Schema Consistency Audit

检查：

所有 YAML frontmatter。

确认：

Method:

```
method_name
category
application
related_tasks
tags
created
```

Task:

```
task_name
category/domain
related_methods
datasets
tags
```

Dataset:

```
dataset_name
source_type
domain
related_tasks
```

是否统一。

---

# 5. Wikilink Integrity

全面扫描：

检查：

* broken links
* fake links
* intentional placeholders
* unresolved references

分类：

P0:
严重错误

P1:
影响知识图谱

P2:
格式问题

P3:
可以接受

---

# 6. Agent System Audit

重点检查：

```
08_Agent_Config
```

包括：

* prompt 文件
* stage 文件
* templates
* skill 文件

检查：

是否存在：

* 旧 Stage 编号
* 已废弃流程
* 与当前结构冲突的 prompt

特别检查：

Windows迁移后：

```
~/.codex
```

以及：

```
ResearchAI/08_Agent_Config
```

是否一致。

---

# 7. Obsidian Compatibility Audit

检查：

* Markdown syntax
* YAML
* wikilink
* folder naming
* spaces in filenames

确认：

Obsidian Linux 下是否正常。

---

# 8. Research Workflow Audit

评估：

当前系统是否真的支持：

```
Paper
 ↓
Paper Note
 ↓
Method / Task / Dataset
 ↓
Knowledge Graph
 ↓
Research Idea
 ↓
Experiment
 ↓
Paper Writing
```

指出：

目前断点在哪里。

---

# 9. Hidden Technical Debt

主动寻找：

例如：

* 重复节点
* 无意义文件
* 历史遗留
* Agent生成质量问题
* 不一致命名
* 未来扩展风险

---

# 10. Future Roadmap Recommendation

不要执行。

只输出建议：

重新规划：

```
Stage 7+
Stage 8
Stage 9
```

应该是什么。

判断：

下一步应该：

* 修复
* 扩展
* 开始实验系统
* 开始论文生产

---

# Output Requirement

生成：

```
08_Agent_Config/Stage_7_Project_Audit_Report.md
```

格式：

```markdown
# Stage 7 Project State Audit Report

## Executive Summary

## Current Project Status

## Stage Completion Matrix

## Directory Audit

## KnowledgeVault Audit

## Agent System Audit

## Migration Audit

## Git Audit

## Encoding Audit

## Technical Debt

## Critical Issues

## Recommended Next Actions

## Proposed Future Stage Roadmap
```

---

# Strict Rules

1. READ ONLY
2. 不修改任何文件
3. 不创建节点
4. 不修复问题
5. 不假设不存在的信息
6. 所有结论必须基于实际文件检查

最终目标：

> 让一个新的 Agent 完全理解 ResearchAI 当前真实状态，并找出历史规划与实际执行之间的不一致，为下一阶段开发提供可靠基础。

---

执行前请先确认：

```
1. 已读取上述背景
2. 已理解这是 Audit，不是 Implementation
3. 不会修改任何文件
```

然后开始审计。

