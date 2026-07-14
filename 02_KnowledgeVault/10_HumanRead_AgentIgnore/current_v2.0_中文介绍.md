# ResearchAI 框架结构总览与设计评估（v2.0）

## 1. 总体设计目标

ResearchAI 当前架构采用**三层分离设计**：

```
                人工阅读 / AI Agent工作区
                         │
                         ▼
        C:\ResearchAI  (Knowledge Workspace)
        知识管理 + Agent规则 + Obsidian知识库
                         │
                         │ 通过映射关系关联
                         ▼
        D:\ResearchAI_Data (External Data Layer)
        原始数据 + Zotero + MinerU + 实验数据
                         │
                         ▼
        Zotero / MinerU / Dataset / Model Checkpoint
        外部工具与大型文件存储
```

核心设计原则：

1. **知识与数据分离**
    
    - Markdown知识文件放在 C 盘 Workspace。
        
    - PDF、MinerU解析结果、大型实验数据放在 D 盘 Data Layer。
        
2. **Zotero-first 文献入口**
    
    - 所有论文必须首先进入 Zotero。
        
    - Zotero 是论文身份唯一来源。
        
    - MinerU 只负责 PDF → Markdown 转换。
        
3. **Obsidian KnowledgeVault作为知识层**
    
    - 不直接保存论文PDF。
        
    - 保存结构化后的 Card、Note、Method、Dataset、Task 等知识节点。
        
4. **Agent可恢复设计**
    
    - Agent通过 AGENT_BOOTSTRAP.md 恢复上下文。
        
    - 通过配置文件理解工作流。
        
    - 避免每次重新设计架构。
        

---

# 一、C:\ResearchAI 工作区

## 定位

> AI Agent 工作空间 + 人类研究管理空间

主要保存：

- Agent规则
    
- 项目状态
    
- 文献处理规范
    
- Obsidian知识库
    
- 写作系统
    

---

# 根目录文件

## AGENT_BOOTSTRAP.md

作用：

Agent启动入口。

包含：

- Agent启动流程
    
- 核心规则
    
- Quick Reference
    
- 文件读取顺序
    

目前包含的重要规则：

- Zotero-first
    
- KnowledgeVault重复检测
    
- 文献处理等级判断
    
- Context Recovery
    

---

## PROJECT_STATUS.md

作用：

项目状态数据库。

记录：

- 当前Stage
    
- 已完成阶段
    
- 下一步任务
    

相当于：

> Agent的项目进度记忆。

---

## README.md

作用：

整个ResearchAI系统说明。

---

## research_config.yaml

作用：

机器读取配置。

用于：

- 数据路径
    
- 环境配置
    
- 自动化脚本
    

---

## current_v1.0.md

作用：

旧版本设计记录。

建议：

长期保留作为历史版本。

---

# 00_Inbox

作用：

临时入口。

目前：

```
00_Inbox/
└── README.md
```

用途：

未来：

- 新论文
    
- 新想法
    
- 未分类资料
    

进入系统前暂存。

---

# 01_Literature

## 定位

旧版文献管理目录。

当前状态：

> 已废弃，但保留历史兼容。

包含：

- 文献模板
    
- Bib管理
    
- 老版目录结构
    

例如：

```
01_PDFs
02_MinerU_Output
03_Processed_Markdown
```

这些目录：

- 不再使用
    
- 仅保留README说明
    

当前真实流程已经迁移到：

```
Zotero
 ↓
MinerU
 ↓
KnowledgeVault
```

---

# 02_KnowledgeVault

## 定位

整个系统核心。

这是：

> Obsidian知识数据库

结构：

```
KnowledgeVault
│
├── Meta
├── Papers
├── Methods
├── Tasks
├── Datasets
├── Experiments
├── Ideas
├── Writing
└── Templates
```

---

# 00_Meta

## 定位

知识导航层。

包含：

- Home
    
- Research Map
    
- Deep Learning Map
    
- Method Map
    
- Dataset Map
    
- Paper Index
    

作用：

建立知识网络入口。

例如：

```
Deep Learning Map
        |
        |
     Transformer
        |
        |
   EQTransformer
        |
        |
    Paper Note
```

---

# 01_Papers

## 定位

论文级知识节点。

当前：

13个Markdown文件。

采用：

```
作者+年份+关键词+类型
```

格式：

例如：

```
mousavi2020_eqtransformer_note.md
```

避免：

同作者同年份论文冲突。

论文文件类型：

## Card

轻量筛选：

记录：

- 基本信息
    
- 贡献
    
- 是否值得深入
    

## Note

深度分析：

记录：

- 方法
    
- 实验
    
- 优缺点
    
- 可迁移思想
    

## Survey

综述论文专用。

## Logic

论文论证结构分析。

---

# 03_Methods

## 定位

方法知识库。

当前：

- CNN
    
- U-Net
    
- Transformer
    
- Attention
    
- PhaseNet
    
- Transfer Learning
    
- Vision Transformer
    

作用：

跨论文共享。

例如：

多个论文：

```
EQTransformer
PhaseNet
SegFormer
```

都会连接：

```
Transformer
Attention
CNN
```

避免重复记录。

---

# 04_Tasks

## 定位

任务知识库。

当前：

- Fault Segmentation
    
- Seismic Image Segmentation
    
- Seismic Phase Picking
    

作用：

描述：

“研究问题是什么”。

---

# 05_Datasets

## 定位

数据集知识库。

当前：

9个数据集。

例如：

- EGS Collab SURF
    
- Marmousi
    
- OpenFWI
    
- SEAM
    

---

# 06_Experiments

实验记录。

当前：

```
exp_chai2020_phase_picking
```

未来用于：

- 训练实验
    
- 参数记录
    
- 结果分析
    

---

# 07_Ideas

研究想法池。

当前为空。

未来：

保存：

- 新模型想法
    
- 改进方向
    
- Paper idea
    

---

# 08_Writing

论文写作系统。

未来：

用于：

- Introduction
    
- Related Work
    
- Method
    
- Experiment
    

---

# 09_Paper_Logic

论文逻辑分析。

用途：

分析：

- 作者如何提出问题
    
- 如何证明贡献
    
- 实验如何支撑结论
    

当前：

Chai 2020已有：

- v1旧格式
    
- v2 Argument Mining格式
    

---

# Templates

模板库。

包含：

- Literature Card
    
- Paper Note
    
- Survey
    
- Method
    
- Dataset
    
- Experiment
    
- Idea
    
- Writing
    
- Paper Logic
    

作用：

保证Agent输出统一格式。

---

# 03_Projects

未来项目管理目录。

当前：

仅README。

---

# 04_Tools

工具配置。

包含：

## Zotero配置

包括：

- 部署记录
    
- Storage策略
    
- 工作流配置
    
- Metadata映射
    

---

# 05_Experiments

旧实验目录。

目前为空。

注意：

与KnowledgeVault/06_Experiments存在功能重复。

建议：

未来统一。

---

# 06_Writing

旧写作目录。

目前为空。

与：

```
KnowledgeVault/08_Writing
```

存在重复。

建议：

未来冻结或删除。

---

# 07_Research_Ideas

旧想法目录。

目前为空。

与：

```
KnowledgeVault/07_Ideas
```

重复。

建议：

未来冻结或删除。

---

# 二、D:\ResearchAI_Data 数据层

## 定位

大型文件存储层。

保存：

- Zotero数据库
    
- PDF
    
- MinerU结果
    
- 数据集
    
- 模型
    

---

# Zotero

## 定位

论文唯一身份数据库。

包含：

## zotero.sqlite

核心数据库：

保存：

- 标题
    
- 作者
    
- DOI
    
- 标签
    
- 引用信息
    

---

## storage

论文PDF真实位置。

结构：

```
storage
 |
 └── ItemKey
        |
        └── paper.pdf
```

例如：

```
QKMKLG2N
|
└── EQTransformer.pdf
```

Item Key 是论文唯一ID。

---

# Paper/MinerU_md

## 定位

PDF解析缓存。

流程：

```
Zotero PDF
      |
      ↓
MinerU
      |
      ↓
full.md
```

保存：

- Markdown正文
    
- 图片
    
- layout
    
- json
    

注意：

这里不是知识库。

只是：

> PDF机器解析结果。

---

# Datasets

当前：

空。

未来：

保存：

- Seismic dataset
    
- MRI dataset
    
- benchmark
    

---

# Experiment_Results

当前：

空。

未来：

保存：

- loss
    
- metrics
    
- checkpoints
    

---

# Model_Checkpoints

当前：

空。

未来：

保存：

- pretrained model
    
- experiment checkpoint
    

---

# 三、当前数据流

完整流程：

```
论文发现
   |
   ↓
Zotero导入
   |
   ↓
PDF storage
   |
   ↓
MinerU解析
   |
   ↓
MinerU_md
   |
   ↓
Agent读取full.md
   |
   ↓
生成KnowledgeVault
   |
   ↓
Card / Note / Logic
   |
   ↓
连接Method / Task / Dataset
```

---

# 四、当前架构检查结果

## 已满足设计目标

|目标|状态|
|---|---|
|知识与数据分离|✅|
|Zotero作为唯一论文入口|✅|
|MinerU作为解析层|✅|
|Obsidian作为知识层|✅|
|Agent可恢复上下文|✅|
|避免重复知识节点|✅|
|论文命名规范|✅|
|批量处理能力|✅|

---

# 五、发现的问题

## 1. 空目录重复（低风险）

存在：

```
C:\ResearchAI\05_Experiments
C:\ResearchAI\06_Writing
C:\ResearchAI\07_Research_Ideas
```

同时：

```
KnowledgeVault
├──06_Experiments
├──08_Writing
└──07_Ideas
```

问题：

功能重复。

建议：

不要立即删除。

原因：

当前没有实际内容。

未来冻结即可。

---

## 2. 01_Literature旧结构

存在：

```
PDFs
MinerU_Output
Processed_Markdown
```

这些已经被：

```
D:\ResearchAI_Data
```

替代。

建议：

保持README占位。

不要删除。

原因：

帮助Agent理解历史。

---

## 3. MinerU origin PDF重复

MinerU输出包含：

```
_origin.pdf
```

这是MinerU行为。

不建议删除。

原因：

属于解析缓存。

---

# 六、总体评价

当前ResearchAI已经从：

> 文件管理系统

升级为：

> AI Agent驱动的科研知识操作系统。

核心架构：

```
Zotero
(论文身份层)

↓

MinerU
(文本解析层)

↓

KnowledgeVault
(知识推理层)

↓

Agent
(自动化科研助手)
```

目前结构稳定。

不建议继续重构。

下一阶段重点应该从：

**架构建设**

转向：

**批量文献处理 + 知识积累 + 科研任务执行**。

当前Stage 1.5-7A后的冻结条件基本满足。