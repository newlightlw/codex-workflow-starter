# 事实、教学适配与来源

整理日期：2026-11-13。

## 作者的真实实践

全局规则摘自本人开发偏好；`project-testing` 是本人定制的整体验收流程。个人项目使用开发主文档、OpenSpec 规格、分阶段测试报告及 `learns/` 学习说明。`grill-me/grilling`、`tdd` 与 `karpathy-guidelines` 是本机已安装能力。

2026-11-13，作者又在 `deepagents_imp` 的 S2-05 接续开发中实际使用了 `codex-workflow`。已核对 Skill 与参考文件的读取记录，以及 7 项定向合同测试、29 项相关集成测试的通过日志。取材快照截至当日 19:45（Asia/Shanghai），该轮仍在进行；具体过程、尚未通过的检查与反馈边界见[真实使用案例](case-deepagents-imp.md)。这些数字不是本教学仓库结果。

配套文章引用的受控网页抓取阶段是历史例子：2026-11-12 的阶段记录为 80 项单元、107 项断网合同、149 项隔离 PostgreSQL 集成检查通过，共 336 项；另有公开文档抓取实测。该数字不是本教学仓库结果，也不是本次重跑。原报告包含尚未验收的后续能力。没有公开原私有项目代码、测试数据或报告全文。

## 本仓库新增的教学材料

Taskbox、练习生成器、规格、教程和模板是为复现这套方法制作的小例子，不是将个人生产项目搬出来。它只用本地文件与标准库。根目录是参考答案；生成目录是未实现 `complete` 的练习起点。

使用固定版本第三方 Skills，并为当前 Codex 文件读取方式做了明确适配；不宣称与个人安装目录逐文件相同。详情见 `docs/skills.md` 和 `skills-lock.json`。本文的提示词是可复用整理版，不是历史对话逐字记录。

v0.2.0 参考用户提供的《Codex 高效使用技巧与工程实践指南》，重新组织任务定义、上下文分层、状态恢复、审查与可选协作方法，并新增独立工作流 Skill 和接入工具。未复制分发该教程全文。v0.2.1 将已核对的工作流使用案例补入真实实践；其他新增方法仍不能自动视为作者长期使用经历。实际新增项及边界见[补充说明](enhancement-notes.md)。

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
