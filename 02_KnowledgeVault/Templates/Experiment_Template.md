---
experiment_id: "{{experiment_id}}"
project: "{{project}}"
task: "{{task}}"
dataset: "{{dataset}}"
method: "{{method}}"
date: {{date}}
status: {{status}}
priority: P2  # P0(Active) | P1(Planned) | P2(Designing) | P3(Secondary) | P4(Deferred) | Completed
tags: []
created: {{date}}
---

# Experiment Objective / 实验目标

<!-- 为什么做这个实验？要回答什么问题？ -->


# Hypothesis / 假设

<!-- 希望验证什么？预期的结果是什么？ -->


# Configuration / 实验配置

- **Model / 模型**: [[Method - {{method}}]]
- **Dataset / 数据集**: [[Dataset - {{dataset}}]]
- **Task / 任务**: [[Task - {{task}}]]
- **Hyperparameters / 超参数**:
  - Learning rate:
  - Batch size:
  - Epochs:
  - Optimizer:
  - Loss function:
- **Hardware / 硬件**:
- **Code Location / 代码位置**: `/home/lco/ResearchAI/03_Projects/{{project}}/`


# Results / 实验结果

## Quantitative Results / 定量结果

| Metric | Value |
|---|---|
| | |

## Qualitative Results / 定性结果

<!-- 可视化观察、典型案例分析 -->


# Comparison / 对比分析

<!-- 与已有方法的对比 -->

| Method | Metric 1 | Metric 2 | Notes |
|---|---|---|---|
| Ours | | | |
| [[Method - ]] | | | |


# Ablation / 消融实验

| Variant | Metric 1 | Metric 2 | Conclusion |
|---|---|---|---|
| Full model | | | — |
| w/o Module A | | | |
| w/o Module B | | | |


# Analysis / 分析

<!-- 为什么结果是这样？成功/失败的原因是什么？ -->


# Conclusion / 结论

<!-- 这个实验告诉了我们什么？假设是否得到验证？ -->


# Related / 相关链接

- Method: [[Method - {{method}}]]
- Dataset: [[Dataset - {{dataset}}]]
- Task: [[Task - {{task}}]]
- Idea: [[Idea - ]]
