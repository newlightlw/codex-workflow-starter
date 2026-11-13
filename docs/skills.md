# Skills：内容、来源与使用边界

本仓库把流程放在项目 `.agents/skills/` 内。它们不是新的模型，也不会因为安装就自动完成工程保证。先检查你的 Codex 实际发现的路径；同名全局 Skill 可能同时出现。

| 名称 | 来源 | 当前包的处理 |
| --- | --- | --- |
| codex-workflow | 本仓库原创，v0.2.0 新增 | 独立的工程流程 Skill；附任务、状态、验证和项目入口模板；不依赖其余 Skills |
| karpathy-guidelines | multica-ai/andrej-karpathy-skills，固定 SHA 见清单 | SKILL.md 原样；社区维护，非 Karpathy 官方发布 |
| grill-me | mattpocock/skills | 显式入口；将专用 Skill 工具调用改为相对文件读取，使用 Codex 的显式调用策略 |
| grilling | mattpocock/skills | 保留分轮决策树；调查事实可由当前 Agent 直接完成，子 Agent 仅在可用且获授权时使用 |
| tdd | mattpocock/skills | 公开测试入口先确认；用文件引用连接 codebase-design；后续 review 不依赖未打包 Skill |
| codebase-design | mattpocock/skills | 原样保留及其两个参考文件；设计参考按需阅读 |
| project-testing | 作者定制 | SKILL.md 原样保留，整体验收先清单、确认后实施 |

适配另更新 tdd 的 UI 简介，使其准确说明该版本的红灯→绿灯循环；没有改成别的 TDD 流程。Matt 的固定版本为 `5863806dd4e15c63174bee4e7515a4256792ecfa`；Karpathy Guidelines 为 `2c606141936f1eeef17fa3043a72095b4765b9c2`。所有随附文件的摘要见 `skills-lock.json`，这是分发快照，不是自动更新器。

## 怎么调用

Codex CLI/IDE 可用 `$grill-me`、`$tdd`、`$project-testing` 或技能选择器。桌面端以实际技能选择入口为准；界面不支持相同语法时，明确写出本项目 `SKILL.md` 路径并让 Agent 读取。文件读取不等于已验证自动发现。

`codex-workflow` 可从项目中的完整目录独立安装，见[项目接入](adoption.md)。它按任务选择项目调查、恢复、审查或交付分支，不自动启用多 Agent，不把所有任务变成先写一套长文档再等批准。分层规则与已有授权仍然适用。

作者已在真实 `deepagents_imp` 项目中使用该工作流，详情见[案例记录](case-deepagents-imp.md)。这次有先前的显式使用约定，后续“继续开发”沿用约定；实际使用证据与无提示自动匹配、跨客户端效果分别看待。

`grill-me` 最终执行 `grilling`，两者不是两个追问阶段。需求已明确时可以直接实施。`tdd` 对首次测试入口确认后，小步循环；`project-testing` 面向整体验收，不覆盖每一次普通测试运行。

## 与完整个人工具箱的关系

我还安装了 `diagnosing-bugs`、`code-review`、`domain-modeling`、`writing-for-agents`、`to-spec` 等能力。这份 starter 只保留跑通本文方法所需的核心集合，避免把缺少 issue tracker、团队工具或平台专用工具的流程直接搬给读者。

若需要扩展，先读[Matt 的上游 README](https://github.com/mattpocock/skills)，检查对应 Skill 的支持文件、工具与触发方式，再安装；安装后重新核对来源和版本。不要假设上游当前版本与本包相同。
