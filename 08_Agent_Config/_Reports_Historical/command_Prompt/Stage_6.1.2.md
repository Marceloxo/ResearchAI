你现在作为 ResearchAI 架构工程师。

基于以下已有状态：

- Stage 5.5 Paper Processing Registry 完成
- Stage 6.1 agent_state 完成
- Stage 6.1.1 Architecture Audit 完成

请不要修改任何文件。

请设计下一阶段 Stage 6.2-6.3 的实施方案。

重点分析：

1. research_config.yaml Linux迁移修复方案
   - 哪些文件应该修改
   - 哪些历史文件必须保留
   - 风险控制

2. KnowledgeVault Processing Pipeline设计

当前状态：

Zotero
 ↓
MinerU(full.md + images)
 ↓
Paper_Processing_State.yaml
 ↓
KnowledgeVault

已有：
- SKILL_Paper_Intake.md
- SKILL_Paper_Deep_Read.md
- scan_registry.py
- process_paper.py

请设计：

- literature_card自动生成流程
- deep_read触发条件
- registry状态更新机制
- Agent调用链

3. 不新增大量skill
请评估现有skill是否足够。

4. 输出：

08_Agent_Config/Migration/Stage_6.2_6.3_Architecture_Proposal.md

要求：

包含：

- 当前架构图
- 修改前后流程图
- 文件修改清单
- 数据流
- 状态机设计
- 风险分析
- rollback方案

约束：

- READ ONLY
- 不修改任何现有文件
- 不执行代码
- 只生成设计报告

