# Codex Workflow Starter

**把需求问清楚，让文档约束开发，用测试留下可复核的结果。**

这是我的 Codex 开发工作流的可运行教学版：项目指令、7 个 Skills、规格、12 组提示词、测试与交接说明放在同一个仓库里。可以把仓库地址和接入要求交给自己的 Codex，让它按需复用这套方法，再从一个浏览器里看得见的小页面开始。

配套文章：[手把手教小白Codex从入门到进阶：如何用它完成高质量项目](article/wechat.md)。

v0.2.11 把第 12 章改为两个轻量实操：给 Codex 仓库地址与提示词，复用项目能力；再做一张个人介绍网页，打开查看并修改一次颜色。Taskbox 保留为进阶练习。标题与[当前封面](article/cover-beginners.png)采用作者定稿，12 项组件表、[5 张配图](article/images/README.md)和匿名案例保留。

## 新手实操一：让 Codex 帮你接入

在 Codex 中打开自己的项目；没有项目就新建一个空文件夹。复制下面整段，让它读取本仓库并完成轻量接入：

```text
参考仓库：https://github.com/newlightlw/codex-workflow-starter

请把这套 Codex 工作方法接入当前项目。
1. 先读取仓库 README、docs/adoption.md、docs/skills.md，再检查当前项目已有规则与 Skills。
2. 优先接入 codex-workflow 和 karpathy-guidelines；已有同名能力时先比较、复用，保留来源版本、许可与完整支持文件，不覆盖已有配置。其他 Skills 按需要再加。
3. 将按需使用约定合并进本项目 AGENTS.md：复杂任务按 codex-workflow 组织；编码时遵循 karpathy-guidelines；简单修改直接做，文档和验证按任务规模安排。
4. 本轮只接入工作方法，不复制 Taskbox 业务代码，不修改全局配置。能在本地完成的接入请直接做；无法访问仓库、无法写入或遇到规则冲突时，说明具体问题。
5. 完成后列出实际新增或修改的文件、已读取的 Skill 路径、未验证项，并告诉我接下来怎样提一个小需求。
```

具体接入范围、完整来源与检查方式见[轻量接入指南](docs/quick-start.md)。这条路线不要求你自己先学会终端命令，也不要求装齐全部 Skills；实际执行受你的 Codex 环境与权限影响。

## 新手实操二：做一张个人介绍网页

按[个人介绍页指南](docs/first-page.md)，给 Codex 一段需求，让它生成一个直接用浏览器打开的 `index.html`。检查昵称、介绍、三张兴趣卡片和窄屏排版，再提一次“主题色改成绿色”的小修改。练习只用 HTML/CSS，无需 Python、应用依赖或部署。

下面保留 Taskbox 的进阶路线，想进一步练习自动化测试、规格管理时再使用。

## 进阶：运行 Taskbox 参考实现

这一部分需要 Python 3.11+。首次上手可先完成上面的两个轻量实操。

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

## 进阶：让 Codex 完成一次测试驱动开发

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

## 已有项目：直接接入工作流

在本仓库根目录执行，替换目标路径：

```bash
python3 scripts/adopt_workflow.py /path/to/your-project
python3 scripts/adopt_workflow.py /path/to/your-project --apply
```

第一条只预览；第二条新增独立的 `codex-workflow` Skill。它不依赖其余 6 个 Skills，不覆盖已有文件、不改全局配置。随后在目标项目中让 Codex 读取 `.agents/skills/codex-workflow/SKILL.md`，核对实际规则、代码和测试，按当前目标使用。完整说明见 [项目接入](docs/adoption.md)。

这个 Skill 负责组织任务和工程状态；是否正确执行，仍需检查实际文件、diff 和验证证据。安装成功不等于模型行为已验收。

## 这套配置怎样分工

| 文件或能力 | 解决的问题 |
| --- | --- |
| [AGENTS.md](AGENTS.md) | 进入项目后先读哪里、怎样修改、怎样验证 |
| [全局规则模板](templates/AGENTS.global.md) | 跨项目沿用的工作偏好；按需合并 |
| [项目需求](docs/requirements.md)、[OpenSpec](openspec/) | 行为、范围、变更原因和验收条件 |
| `codex-workflow` | 项目接入、工程任务定义、状态恢复、审查与交付 |
| `grill-me` → `grilling` | 需求不清时分轮追问，有依赖的问题按顺序问 |
| `karpathy-guidelines` | 先澄清假设、简化实现、缩小改动、验证结果 |
| `tdd`、`codebase-design` | 从已确认的公开接口检查行为，小步推进 |
| `project-testing` | 先列整体验收用例，确认后实施和运行 |
| [测试映射](docs/testing.md)、[验证记录](docs/verification.md) | 哪些行为被检查，哪些结论尚不能下 |
| [学习说明](learns/01-taskbox.md)、[交接模板](templates/HANDOFF.md) | 理解实现，换会话时继续工作 |

Skills 已放在项目的 `.agents/skills/` 中，无需安装到全局。`grill-me` 是 `grilling` 的显式入口，所以 7 个目录不代表 7 套独立方法。详见 [来源与适配](docs/skills.md)。

## 按需深入

- [codex-workflow 匿名案例](docs/case-project-continuation.md)：实际项目的连续两轮开发、验证结果与失败记录；与本教学练习的成绩分别记录。
- [12 组可复制提示词](prompts/README.md)：覆盖澄清、开发、测试、接入、审查与复盘。
- [工程实践手册](docs/engineering-guide.md)：任务大小、文档分层、状态恢复、协作边界和证据。
- [Codex 命令与权限](docs/codex-reference.md)：本地 CLI help 已核对；命令示例与真实模型执行分开记录。
- [OpenSpec 进阶](docs/openspec.md)：固定 1.16.1；需要 Node.js 22.12+。基础练习无需安装它。
- [模板目录](templates/)：把工作流迁移到自己的项目。
- [事实与来源](docs/source-notes.md)：真实个人实践、教学适配、历史证据分别是什么。
- [本轮补充说明](docs/enhancement-notes.md)、[版本记录](CHANGELOG.md)：参考教程带来了哪些新增内容。

本例范围为单用户、单进程、本地 JSON 文件；没有登录、并发写入、云同步或生产部署。教学内容不等于生产系统验收。

## 许可与参与

原创代码、模板、文章和自定义 Skill 采用 [MIT](LICENSE)。第三方 Skills 保留其来源和许可，见 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) 与 [固定版本清单](skills-lock.json)。`karpathy-guidelines` 是社区整理，不代表 Karpathy 本人维护或背书。

反馈复现问题时，请提供系统、Python/Codex 版本、命令与脱敏后的错误；不要提交账号、私有项目文件或密钥。改动前阅读 [CONTRIBUTING.md](CONTRIBUTING.md)。
