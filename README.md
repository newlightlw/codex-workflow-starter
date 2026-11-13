# Codex Workflow Starter

**把需求问清楚，让文档约束开发，用测试留下可复核的结果。**

这是我的 Codex 开发工作流的可运行教学版：项目指令、6 个 Skills、规格、提示词、测试与交接说明放在同一个仓库里。你可以先运行参考实现，再让 Codex 在独立目录中完成一个小功能。

配套文章：[我用 Codex 做项目的工作流，整理成了一个开源仓库](article/wechat.md)。

## 先跑通：只需 Python 3.11+

```bash
git clone https://github.com/newlightlw/codex-workflow-starter.git
cd codex-workflow-starter
python3 -m unittest discover -s tests -v
python3 scripts/verify_bundle.py
```

Windows 可将 `python3` 换成 `py -3`；先用 `py -3 --version` 确认版本。Python 示例没有第三方依赖，不访问网络，也不需要模型密钥。通过 GitHub 下载 ZIP 也可以运行。

体验参考实现：

```bash
python3 taskbox.py add "读完项目规格"
python3 taskbox.py list
python3 taskbox.py complete 1
python3 taskbox.py list
```

默认只在当前目录保存 `.taskbox.json`。第一次新增返回 `pending`，完成后重新读取应返回 `completed`。已有本地数据时请使用输出中的真实 ID，或通过 `--store` 指定新文件。

## 再让 Codex 完成一次开发

```bash
python3 scripts/new_exercise.py ../my-codex-practice
cd ../my-codex-practice
python3 -m unittest discover -s tests -p test_baseline.py -v
python3 -m unittest discover -s tests -p test_complete.py -v
```

前一条测试命令应通过，后一条应有 **1 个断言失败**，错误中包含 `complete is not implemented yet`。这是练习故意保留的功能缺口。根目录参考实现的全部测试应通过。

在 Codex 中打开 `my-codex-practice`，开启新会话，先发：

```text
请先读 AGENTS.md、README.md 和 docs/requirements.md。
列出你实际读取到的项目指令、Skills 路径，以及当前需求和测试状态。
本轮只核对，不修改代码。
```

确认加载的是本练习目录里的配置后，再按练习 README 的提示使用 `$tdd`：确认 CLI 测试入口，复现失败，实现功能，补足其他行为的测试并同步文档。**预置的一个失败测试是起点；其余测试由你与 Codex 根据规格补齐。**

Codex 的使用需要你自己的可用客户端和账号/认证配置。模型版本、权限和上下文会影响执行过程，本仓库不承诺逐字一致的模型回复。完整步骤见 [从零复现](docs/start-here.md)。

## 这套配置怎样分工

| 文件或能力 | 解决的问题 |
| --- | --- |
| [AGENTS.md](AGENTS.md) | 进入项目后先读哪里、怎样修改、怎样验证 |
| [全局规则模板](templates/AGENTS.global.md) | 跨项目沿用的工作偏好；按需合并 |
| [项目需求](docs/requirements.md)、[OpenSpec](openspec/) | 行为、范围、变更原因和验收条件 |
| `grill-me` → `grilling` | 需求不清时分轮追问，有依赖的问题按顺序问 |
| `karpathy-guidelines` | 先澄清假设、简化实现、缩小改动、验证结果 |
| `tdd`、`codebase-design` | 从已确认的公开接口检查行为，小步推进 |
| `project-testing` | 先列整体验收用例，确认后实施和运行 |
| [测试映射](docs/testing.md)、[验证记录](docs/verification.md) | 哪些行为被检查，哪些结论尚不能下 |
| [学习说明](learns/01-taskbox.md)、[交接模板](templates/HANDOFF.md) | 理解实现，换会话时继续工作 |

Skills 已放在项目的 `.agents/skills/` 中，无需安装到全局。`grill-me` 是 `grilling` 的显式入口，所以 6 个目录不代表 6 套独立方法。详见 [来源与适配](docs/skills.md)。

## 按需深入

- [7 组可复制提示词](prompts/README.md)：澄清、写文档、执行阶段、TDD、验收、修 Bug、接续。
- [OpenSpec 进阶](docs/openspec.md)：固定 1.16.1；需要 Node.js 22.12+。基础练习无需安装它。
- [模板目录](templates/)：把工作流迁移到自己的项目。
- [事实与来源](docs/source-notes.md)：真实个人实践、教学适配、历史证据分别是什么。

本例范围为单用户、单进程、本地 JSON 文件；没有登录、并发写入、云同步或生产部署。教学内容不等于生产系统验收。

## 许可与参与

原创代码、模板、文章和自定义 Skill 采用 [MIT](LICENSE)。第三方 Skills 保留其来源和许可，见 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) 与 [固定版本清单](skills-lock.json)。`karpathy-guidelines` 是社区整理，不代表 Karpathy 本人维护或背书。

反馈复现问题时，请提供系统、Python/Codex 版本、命令与脱敏后的错误；不要提交账号、私有项目文件或密钥。改动前阅读 [CONTRIBUTING.md](CONTRIBUTING.md)。
