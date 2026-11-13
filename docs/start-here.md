# 从零复现一次开发

## 1. 准备与基线

准备 Python 3.11+、Git（也可下载 ZIP），以及已能正常工作的 Codex。先执行根目录 README 中的参考实现测试；若参考实现不通过，保存原始错误，先解决环境或仓库问题。

运行示例和测试不调用模型、不收费；与 Codex 对话遵循你所使用产品的账号与计费方式。本文不绑定模型名称、套餐或推理档位。

## 2. 建一个独立练习

在仓库根目录执行 `python3 scripts/new_exercise.py ../my-codex-practice`。目标必须不存在，父目录必须存在，且不能位于本参考仓库内。脚本只写这个新目录，不修改全局 Codex 配置，不联网，不初始化远程仓库。

进入生成目录，先运行基线，再运行 `test_complete.py`。基线应通过，完成任务测试应因为功能未实现而失败。若出现依赖导入、语法或路径错误，它们不是目标“红灯”。

## 3. 确认 Codex 看到正确材料

在 Codex 中将生成目录作为项目打开，并开启新会话。可先在该目录执行 `git init`，以便后续查看 diff；此命令只建立本地版本控制。

发给 Codex：

```text
先读取 AGENTS.md、README.md 和 docs/requirements.md。
请列出你实际读取的指令文件与 Skills 路径、需求范围、当前测试命令。
本轮只核对，不修改。
```

当前 Codex 官方支持项目 `.agents/skills/`。如果同名 Skill 同时存在全局与项目，不会自动合并；在提示词中给出本项目的实际路径，确认读取目标版本。没出现时刷新或重启会话，按[官方 Skills 文档](https://learn.chatgpt.com/docs/build-skills)核对客户端支持；也可以明确要求读取目标 `SKILL.md` 并依其流程执行，后者只能证明文件被读取，不能证明自动发现生效。

## 4. 让 Codex 做一个垂直切片

练习 README 提供分两轮的 `$tdd` 提示。第一轮先让它确认 CLI 是测试入口，列出能观察和不能观察的范围；你答复确认后，它才按 Skill 实施。

已有主流程失败测试用于启动第一个切片。先使该测试通过，再逐一补充重复完成、不存在 ID、其他任务不受影响等行为。每一条都应先失败再通过，避免写完全部代码后倒推测试。

观察：测试的期望是否来自需求；失败是否真的因为目标行为缺失；是否只修改当前范围；是否验证重新运行后的持久化状态。不要只看“绿了”。

## 5. 做一次项目验收

功能完成后，可以调用 `$project-testing`。第一轮只读调查和用例清单；你审阅清单后回复“可以开始测试”，才进入实施和运行。这是该定制 Skill 的明确流程。普通开发中运行已约定的测试，不必每次启动这套整体验收流程。

如果此时需求仍有歧义，使用 `$grill-me` 讨论范围后再继续。练习需求已明确时，无需为了走流程而重新访谈。

## 6. 留下可交接结果

让 Codex 更新 `docs/verification.md` 和 `learns/01-taskbox.md`，说明改了什么、命令及实际结果、未验证范围。验收后按 `docs/openspec.md` 将已接受变更合并到主规格并归档。

实际阅读 `git diff`；手动执行一次新增、完成、重新查看。自动测试通过和你看懂、确认体验，是不同的完成条件。

## 7. 迁移到自己的项目

只需要工程流程时，优先按[项目接入](adoption.md)使用预览与安装工具；它仅新增独立的 `codex-workflow`，保留现有项目规则。再按[工程实践手册](engineering-guide.md)补实际缺失的文档和验证入口。

选择性合并 `templates/AGENTS.global.md` 到你自己 Codex home 下的 AGENTS.md（默认 `~/.codex/AGENTS.md`）；保留已有规则，先解决冲突，不直接覆盖。

复制所需项目 Skills 时一并保留 `LICENSES/`、`THIRD_PARTY_NOTICES.md` 与来源清单。将项目 AGENTS 的文档路径、运行命令改成自己的真实入口。先用一个小功能检验这套规则，再增加确实需要的 Skill。

官方入口：[AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md) · [Skills](https://learn.chatgpt.com/docs/build-skills)。
