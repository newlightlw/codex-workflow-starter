# 事实、教学适配与来源

整理日期：2026-11-13。

## 作者的真实实践

全局规则摘自本人开发偏好；`project-testing` 是本人定制的整体验收流程。个人项目使用开发主文档、OpenSpec 规格、分阶段测试报告及 `learns/` 学习说明。`grill-me/grilling`、`tdd` 与 `karpathy-guidelines` 是本机已安装能力。

2026-11-13，作者在一个实际项目的连续两轮接续开发中使用 `codex-workflow`。第一轮阶段报告和最终日志确认 416 项测试通过（新增 17 项），完成实现与隔离验证交付；第二轮首次真实演练前的回归日志确认 428 项通过，但首轮真实运行被引用校验拦截，未得到预期的恢复成功证据。已补充差异排查及后续复核安排，读取过程、真实运行及反馈边界见[连续使用案例](case-project-continuation.md)。这些数字不是本教学仓库结果。

文章中的状态冲突例子来自此前的实际开发记录，用于说明集成测试如何发现接口与数据库约束不一致。该例子没有在本次编辑中重跑，原私有项目代码、测试数据和报告全文未公开。

## 本仓库新增的教学材料

Taskbox、练习生成器、规格、教程和模板是为复现这套方法制作的小例子，不是将个人生产项目搬出来。它只用本地文件与标准库。根目录是参考答案；生成目录是未实现 `complete` 的练习起点。

使用固定版本第三方 Skills，并为当前 Codex 文件读取方式做了明确适配；不宣称与个人安装目录逐文件相同。详情见 `docs/skills.md` 和 `skills-lock.json`。本文的提示词是可复用整理版，不是历史对话逐字记录。

v0.2.0 参考用户提供的《Codex 高效使用技巧与工程实践指南》，重新组织任务定义、上下文分层、状态恢复、审查与可选协作方法，并新增独立工作流 Skill 和接入工具。未复制分发该教程全文。v0.2.1 首次补入工作流使用案例，v0.2.2 更新到两轮接续及分层验证结果；其他新增方法仍不能自动视为作者长期使用经历。实际新增项及边界见[补充说明](enhancement-notes.md)。

本地 CLI 0.154.0 的 `--help`、`exec --help`、`review --help`、`resume --help` 已核对；没有因此执行真实模型调用、并行 Agent 或 worktree 开发。命令及权限以当前客户端为准，详见[核对记录](codex-reference.md)。

## 可公开核对的来源

- [Codex AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md)
- [Codex Skills](https://learn.chatgpt.com/docs/build-skills)
- [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec)
- [Matt Pocock Skills 固定版本](https://github.com/mattpocock/skills/tree/5863806dd4e15c63174bee4e7515a4256792ecfa)
- [社区 Karpathy Guidelines 固定版本](https://github.com/multica-ai/andrej-karpathy-skills/tree/2c606141936f1eeef17fa3043a72095b4765b9c2)
- [Codex CLI 参考](https://learn.chatgpt.com/docs/cli/reference)
- [非交互模式](https://learn.chatgpt.com/docs/non-interactive-mode)
- [权限与沙箱](https://learn.chatgpt.com/docs/agent-approvals-security)
- [子 Agent](https://learn.chatgpt.com/docs/agent-configuration/subagents)
- [Codex worktree](https://learn.chatgpt.com/docs/environments/git-worktrees) 与 [Git worktree](https://git-scm.com/docs/git-worktree)

`karpathy-guidelines` 基于 Karpathy 的公开观察整理，Skill 的维护者是社区作者。本文不将它称作 Karpathy 官方提示词。
