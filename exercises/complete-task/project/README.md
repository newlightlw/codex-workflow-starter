# 练习：让任务可以标记为完成

你已获得新增/读取能力和一个故意失败的主流程测试。目标是依据 `docs/requirements.md` 完成 R3、R4，并保持原有行为。

## 先核对基线

```bash
python3 -m unittest discover -s tests -p test_baseline.py -v
python3 -m unittest discover -s tests -p test_complete.py -v
```

基线应通过；功能测试应有 1 个断言失败，错误包含 `complete is not implemented yet`。导入或环境错误不算目标红灯。Windows 可用 `py -3` 替代 `python3`。

## 第一轮：确认入口与范围

在 Codex 中打开此目录，启动新会话，发送：

```text
请使用本项目 .agents/skills/tdd/SKILL.md 的 tdd 流程。
先读 AGENTS.md、docs/requirements.md 和 openspec/changes/complete-task/。
本次只实现 R3、R4，保持新增和读取基线。
请先提出测试入口、能观察的结果与未覆盖部分，等我确认后再实施。
```

审阅它的提议。确认使用真实 CLI、临时存储、新进程读取后，发送下一轮。

## 第二轮：开始实现

```text
确认以真实 CLI 为测试入口；使用临时目录和合成数据。
请先运行预置的完成任务测试，确认它因目标行为缺失而失败，再做最小实现。
其余行为按一个新失败测试、一次最小实现的顺序补齐。
遵循本项目 karpathy-guidelines，不读取参考仓库中的答案。
完成后运行完整测试，更新验证记录、学习说明和 OpenSpec tasks。
最终报告实际命令、通过/失败/跳过/未执行，以及尚未验证的范围。
```

本目录没有参考答案。可以使用 `git init`、建立初始提交，再看最后 diff；Git 不是运行练习的前提。

## 验收

```bash
python3 -m unittest discover -s tests -v
python3 taskbox.py add "读规格"
python3 taskbox.py complete 1
python3 taskbox.py list
```

用新增命令实际返回的 ID。测试之外还要由你确认说明可理解、行为符合需求。若使用 `$project-testing` 做整体验收，先审阅其用例清单，再回复“可以开始测试”。

## 可选 OpenSpec

需要 Node.js 22.12+：`npm ci` 后运行 `npm run spec:check`。测试通过且你接受本次变更后，执行 `npx --no-install openspec archive complete-task --yes`，检查主规格和归档 diff，再运行规格检查。

## 交付物

保持 `AGENTS.md` 和 README 的命令真实可用；将结果写进 `docs/verification.md`，更新 `learns/01-taskbox.md`。这些文件目前明确标为未完成，只有实际做完才能改状态。
