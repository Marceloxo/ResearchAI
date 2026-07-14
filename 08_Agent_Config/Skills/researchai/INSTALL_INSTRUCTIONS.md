# ResearchAI Skill 安装说明

## 问题

Skill 已创建在 `C:\ResearchAI\08_Agent_Config\Skills\researchai\`，但 Codex 不会自动从这里发现它。

## 解决方法

你需要手动将 skill 复制到 Codex 的技能目录。

### 方法 1：手动复制（推荐）

在 PowerShell 中执行：

```powershell
Copy-Item -Path "C:\ResearchAI\08_Agent_Config\Skills\researchai" -Destination "$env:USERPROFILE\.codex\skills\" -Recurse -Force
```

然后重启 Codex 桌面应用。

### 方法 2：设置环境变量

如果你希望 Codex 从 workspace 中发现 skills，可以设置环境变量：

```powershell
$env:CODEX_HOME = "C:\ResearchAI\08_Agent_Config\Skills"
```

但这需要 Codex 配置支持。

### 验证安装

安装后，在 Codex 中你应该能看到 "ResearchAI" skill，并且可以使用：

```
/SKILL Paper Intake 76SW77W3
/SKILL Deep Read 6VTKJ8W2
/SKILL Batch Process 76SW77W3 6VTKJ8W2
```

## 权限问题

如果遇到 "拒绝访问" 错误，说明你的账户对 `~/.codex/skills/` 目录没有写入权限。请以管理员身份运行 PowerShell，或手动复制文件。
