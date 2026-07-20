# Continue ResearchAI KnowledgeVault Project

你正在继续执行：

```

/home/lco/ResearchAI

```

项目中的 KnowledgeVault 稳定化工作。

---

# 当前项目状态（重要上下文）

已完成：

## Stage 6.5.2 — Knowledge Node Extraction

已创建：

### Methods

```

02_KnowledgeVault/03_Methods/

U-Segformer-Hyper.md
Segformer.md
GENIE.md
PLAN.md
Multi-task Learning.md

```

### Tasks

```

02_KnowledgeVault/04_Tasks/

Phase Association.md
Earthquake Location.md
Seismic Facies Segmentation.md
Earthquake Sequence Analysis.md

```

### Datasets

```

02_KnowledgeVault/05_Datasets/

Northern California Seismic Network.md
Japan Hi-net.md

```

并更新：

```

00_Meta/
Method_Map.md
Dataset_Map.md
Seismic_AI_Map.md
Deep_Learning_Map.md
Paper_Index.md

```

---

## Stage 6.5.4 — Foundational Method Completion

已完成：

```

03_Methods/Vision Transformer.md

```

从空文件补全。

---

## Stage 6.5.5 — Quality Improvement

已完成：

### 1. Method_Map 编码修复

```

00_Meta/Method_Map.md

````

- 修复 UTF-8 编码
- 删除 BOM
- 中文标题恢复


### 2. Dataset schema 修复

以下 dataset 添加：

```yaml
source_type: public_dataset
````

包括：

```
EGS Collab SURF.md
F3 Netherlands.md
Marmousi.md
OpenFWI.md
Parihaka.md
Penobscot.md
SEAM.md
SEG Salt.md
Thebe.md
```

### 3. Dataset → Task backlinks

添加：

```markdown
## Tasks Using This Dataset
```

到相关 Dataset nodes。

---

# 当前阶段

开始：

# Stage 6.6 — KnowledgeVault Schema Consistency Audit

## IMPORTANT

这是：

```
READ-ONLY AUDIT
```

阶段。

禁止：

* 修改任何文件
* 创建任何节点
* 删除任何节点
* 修改模板
* 修改 Paper Notes

先输出：

```
Stage 6.6 Audit Report
```

等待批准后才能执行修复。

---

# Audit Scope

## Phase A — YAML Schema Consistency

检查：

```
02_KnowledgeVault/03_Methods/*.md
```

确认是否包含：

```yaml
method_name:
category:
application:
related_tasks:
tags:
created:
```

并检查正文是否包含：

```markdown
## Definition

## Core Idea

## Architecture/Formulation

## Advantages

## Limitations

## Typical Applications

## Related Papers

## Related Methods
```

---

检查：

```
02_KnowledgeVault/04_Tasks/*.md
```

确认：

YAML:

```yaml
task_name:
category:
application:
related_methods:
related_datasets:
tags:
created:
```

正文：

```markdown
## Task Definition

## Problem Formulation

## Input Data

## Output

## Evaluation Metrics

## Common Methods

## Challenges

## Benchmark Datasets

## Open Problems
```

---

检查：

```
02_KnowledgeVault/05_Datasets/*.md
```

确认：

YAML:

```yaml
dataset_name:
source_type:
domain:
tasks:
papers:
tags:
created:
```

正文：

```markdown
## Dataset Overview

## Data Description

## Collection Method

## Application

## Related Papers

## Tasks Using This Dataset
```

---

# Phase B — Knowledge Graph Consistency Audit

检查：

## Method → Task

每个 Method 是否：

至少：

```
1 Task link
1 Paper link
```

例如：

```
PLAN
 ↓
Phase Association
 ↓
si2024_plan_allinone_note
```

---

## Task → Method

检查：

每个 Task 是否：

至少：

```
1 Method
```

例如：

```
Seismic Facies Segmentation

Methods:
- Segformer
- U-Segformer-Hyper
```

---

## Task → Dataset

检查：

每个 Task 是否：

至少：

```
1 Dataset
```

---

## Dataset → Task

检查：

Dataset 是否：

有：

```
Tasks Using This Dataset
```

并且 wikilink 有效。

---

# Phase C — Naming Consistency

检查重复节点风险：

例如：

```
SegFormer.md
Segformer.md
SEGFormer.md
```

检查：

* 大小写
* 空格
* 连字符
* 缩写

输出潜在 duplicate。

---

# Phase D — Orphan Node Detection

检查：

没有任何引用的节点：

包括：

```
03_Methods
04_Tasks
05_Datasets
```

分类：

1. 正常基础节点
2. 需要补链接节点
3. 废弃候选节点

不要删除。

---

# Phase E — Meta Map Consistency

检查：

```
00_Meta/
```

确认：

Method_Map
Dataset_Map
Seismic_AI_Map
Deep_Learning_Map
Paper_Index

是否包含所有新增节点。

检查：

* 缺失
* 重复
* 错误 wikilink

---

# Phase F — Generate Report

输出：

文件：

```
08_Agent_Config/Stage_6.6_Audit_Report.md
```

内容：

包括：

## Summary

## YAML Schema Findings

## Broken Wikilinks

## Missing Links

## Duplicate Names

## Orphan Nodes

## Meta Map Issues

## Recommended Fix Plan

---

# Constraints

不要：

* 修改任何文件
* 创建 validator script
* 修复问题
* 扩展知识节点

只生成 Audit Report。

完成后等待用户批准进入：

```
Stage 6.6.1 — Schema Repair
```

开始前先检查当前 filesystem 状态。

```

