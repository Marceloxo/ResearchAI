# ResearchAI 技能系统使用指南

> **版本**: 1.0
> **日期**: 2026-07-10
> **适用范围**: 所有 AI Agent（Codex、Claude Code、Gemini CLI 等）

---

## 1. 技能系统简介

### 为什么需要技能系统

ResearchAI 的论文处理流程已经经过严格的验证和冻结。技能系统的作用是将这些经过验证的工作流程标准化为可复用的 Agent 程序，确保每次处理都遵循相同的规则和质量标准。

### 技能与 Agent 的关系

技能是 Agent 执行的**标准化操作手册**。Agent 不是随意处理论文，而是按照技能定义的步骤执行。这确保了：

- 一致性：每次处理都遵循相同的流程
- 可追溯性：每个决策都有明确的依据
- 质量保证：关键检查点不会被跳过

### 技能与冻结架构的关系

技能系统是**基础设施扩展**，不是架构修改。它不改变：

- 目录结构（Zotero → MinerU → KnowledgeVault 三层不变）
- 模板格式（文献卡片、论文笔记、论文逻辑模板不变）
- 处理框架（三级处理策略不变）
- 命名规范（{author}{year}_{keyword}_{type}.md 不变）

技能只是在已有架构之上增加了一层**标准化操作流程**。

---

## 2. 技能调用方式

所有技能都通过 Agent 命令调用，格式如下：

```
/SKILL <技能名称> <参数>
```

### 2.1 新增论文

```
/SKILL Paper Intake 76SW77W3
```

用途：处理新导入 Zotero 的论文，生成文献卡片。

### 2.2 深度阅读

```
/SKILL Deep Read 6VTKJ8W2
```

用途：对已筛选为"Deep Read"的论文进行深度技术分析，生成论文笔记。

### 2.3 批量处理

```
/SKILL Batch Process 76SW77W3 6VTKJ8W2 NCKCP6BS
```

用途：批量处理多篇论文的文献卡片。

### 2.4 更新论文

```
/SKILL Paper Update 6VTKJ8W2 code_found https://github.com/example/snunet-cd
```

用途：更新已有论文的补充信息（如新发现的代码仓库）。

### 2.5 知识节点检查

```
/SKILL Knowledge Node Check ChangeFormer
```

用途：检查新概念是否需要创建新的知识节点，避免重复创建。

### 2.6 研究地图更新

```
/SKILL Research Map Update Seismic_AI_Map Add new section on transformer methods
```

用途：维护研究导航文件的组织结构。

### 2.7 文献综述生成

```
/SKILL Literature Synthesis Transformer in Seismic AI
```

用途：从知识库中生成写作素材和文献综述草稿。

### 2.8 架构审计

```
/SKILL Architecture Audit full
```

用途：对 ResearchAI 系统进行完整性审计，检查断链、命名规范、映射一致性等。

---

## 3. 工作流程图

```
研究资产（Zotero PDF）
    ↓
技能路由器（选择正确的技能）
    ↓
验证（Zotero → MinerU → 重复检查）
    ↓
执行计划（列出将要创建/修改的文件）
    ↓
人类确认（用户批准或拒绝）
    ↓
知识库更新（KnowledgeVault 文件创建/修改）
```

### 关键原则

1. **验证先行**：在任何文件创建之前，必须先完成 Zotero 验证和重复检查
2. **计划透明**：Agent 必须展示完整的执行计划，包括将要创建和修改的所有文件
3. **人类确认**：未经人类确认，不得修改任何文件
4. **只读审计**：架构审计技能永远不会修改文件，只生成报告

---

## 4. 技能列表

### 01_Literature（文献处理）

#### SKILL_Paper_Intake.md — 论文导入

- **用途**：处理新导入的论文，生成文献卡片
- **输入**：Zotero Item Key（8位字母数字）
- **输出**：02_KnowledgeVault/01_Papers/ 中的文献卡片文件
- **何时使用**：当新论文从 Zotero 导入并完成 MinerU 处理后

#### SKILL_Paper_Deep_Read.md — 深度阅读

- **用途**：生成技术论文笔记（Level 2 分析）
- **输入**：Zotero Item Key
- **输出**：02_KnowledgeVault/01_Papers/ 中的论文笔记文件
- **何时使用**：当文献卡片决定该论文需要"Deep Read"时

#### SKILL_Paper_Batch_Process.md — 批量处理

- **用途**：批量处理多篇论文的文献卡片
- **输入**：多个 Zotero Item Key
- **输出**：多篇文献卡片 + 映射表更新
- **何时使用**：当有大量论文需要快速筛选时

#### SKILL_Paper_Update.md — 论文更新

- **用途**：更新已有论文的补充信息
- **输入**：Zotero Item Key + 更新类型和详情
- **输出**：更新的论文文件
- **何时使用**：当发现新的代码仓库、引用信息或数据集时

### 02_Knowledge（知识管理）

#### SKILL_Knowledge_Node_Check.md — 知识节点检查

- **用途**：防止不必要的知识节点创建
- **输入**：新概念名称
- **输出**：建议（复用现有节点 / 创建新节点 / 等待更多证据）
- **何时使用**：在处理新论文时遇到可能的新概念

#### SKILL_Research_Map_Update.md — 研究地图更新

- **用途**：维护研究导航文件
- **输入**：地图名称 + 更新描述
- **输出**：更新后的导航文件
- **何时使用**：当知识库增长到需要更新组织结构时

### 03_Writing（写作辅助）

#### SKILL_Literature_Synthesis.md — 文献综述生成

- **用途**：生成写作素材和文献综述草稿
- **输入**：研究主题
- **输出**：02_Writing/ 中的综述文件
- **何时使用**：当需要撰写论文引言或相关工作部分时

### 04_System（系统维护）

#### SKILL_Architecture_Audit.md — 架构审计

- **用途**：定期系统完整性审计
- **输入**：审计范围（full/papers/mapping/links）
- **输出**：审计报告（只读，不修改任何文件）
- **何时使用**：定期或在批量处理前后

---

## 5. 使用示例

### 示例 1：添加新论文

```
用户: /SKILL Paper Intake 76SW77W3

Agent:
执行计划:
  输入:
    Zotero Item Key: 76SW77W3
    PDF: Abdallah 等 - 2024 - Automated deformation...pdf
  
  检测到:
    MinerU: Abdallah 等 - 2024 - ...pdf-bd0d85e1.../full.md
    论文类型: 研究文章
    处理级别: Level 1 (文献卡片)
  
  将创建:
    02_KnowledgeVault/01_Papers/abdallah2024_inasar_vit_card.md
  
  将修改:
    MinerU_Zotero_Mapping.md (追加行)
    Paper_Index.md (添加条目)
  
  等待确认。

用户: 确认

Agent: （执行创建和修改）
```

### 示例 2：深度阅读重要论文

```
用户: /SKILL Deep Read 6VTKJ8W2

Agent:
执行计划:
  输入:
    Zotero Item Key: 6VTKJ8W2
    来源: MinerU/full.md
  
  将创建:
    02_KnowledgeVault/01_Papers/fang2022_snunet_cd_note.md
  
  将分析:
    - 问题、动机、贡献
    - 架构和方法细节
    - 结果和消融实验
    - 局限性和可迁移性
    - 复现性评估
  
  等待确认。

用户: 确认

Agent: （生成完整的论文笔记）
```

### 示例 3：更新旧论文

```
用户: /SKILL Paper Update 6VTKJ8W2 code_found https://github.com/example/snunet-cd

Agent:
现有文件: 02_KnowledgeVault/01_Papers/fang2022_snunet_cd_card.md
修改:
  章节: Reproducibility Status / Code Availability
  当前: Status: [ ] Not Found Yet
  新: Status: [x] Available, URL: https://github.com/example/snunet-cd
原因: 发现了新的代码仓库

等待确认。
```

### 示例 4：生成文献综述

```
用户: /SKILL Literature Synthesis Transformer in Seismic AI

Agent:
文献综述大纲:
  主题: Transformer in Seismic AI
  
  结构:
  1. 历史演进
     - 早期方法（2020年前）
     - 过渡期（2020-2023）
     - 近期进展（2023+）
  
  2. 当前方法
     - Vision Transformer: <摘要>
     - Swin Transformer: <摘要>
     - Transformer-CNN 混合: <摘要>
  
  3. 比较
     - 准确率对比表
     - 效率对比表
     - 数据集覆盖
  
  4. 研究空白
     - 空白 1: <描述>
     - 空白 2: <描述>
  
  5. 未来方向
     - 方向 1: <描述>
     - 方向 2: <描述>
  
  6. 参考文献
     - <N> 篇知识库论文
     - <N> 篇外部参考
  
  来源论文: [[chen2022_rs_transformer_cd_survey]], [[bandara2022_changeformer_card]], ...
  
  等待确认。
```

### 示例 5：运行架构审计

```
用户: /SKILL Architecture Audit full

Agent:
架构审计报告

日期: 2026-07-10
范围: full

## 摘要
总检查项: 6
通过: 5
警告: 1
错误: 0

## 发现

### 严重错误
无

### 警告
- 3 篇调查/基准论文缺少 Zotero 区块（chen2022, liu2025, ghorman2022）

### 通过的检查
- 断链检查: 无断链
- 命名规范: 全部合规
- Zotero 映射: 一致
- 重复论文: 无
- 模板合规: 大部分合规
- 目录完整性: 正常

## 建议
1. 为调查/基准论文模板添加 Zotero 区块
```

---

## 6. 权限模型

所有技能都遵循**半自动模式（Mode B）**：

1. Agent 分析请求
2. Agent 生成执行计划
3. Agent 展示计划供人类确认
4. 人类确认后，Agent 执行修改
5. 没有任何技能可以在未经确认的情况下静默修改知识库

**唯一例外**：架构审计技能（SKILL_Architecture_Audit）是只读的，不会修改任何文件。

---

## 7. 注意事项

- 技能系统是基础设施扩展，不是架构修改
- 不改变任何现有模板、目录结构或处理框架
- 不自动处理任何论文
- 不创建文献卡片、论文笔记或知识节点（除非人类确认）
- 所有操作都遵循冻结的 ResearchAI 架构原则
