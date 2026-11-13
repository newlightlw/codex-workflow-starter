# 发布前验证记录

日期：2026-11-13。以下是本教学仓库的实际检查，独立于配套文章中的历史私有项目测试数。

## v0.2.0：工程工作流与项目接入

本地环境：macOS、Python 3.13.11。检查发生在 `8e66c4121ec5624e619d2a59364d9102312052d8` 基线加本次尚未提交改动的工作区，包含新增接入脚本、接入测试、独立 Skill 及更新后的锁文件；不是重测原提交。发布快照由 v0.2.0 tag 固定。

| 检查 | 实际结果 |
| --- | --- |
| `python3 -m unittest discover -s tests -v` | 22 项通过，0 失败、0 跳过；包含原有 15 项与新增接入 7 项 |
| `python3 scripts/verify_bundle.py` | 7 个 Skill、26 个锁定文件完整性通过 |
| 新 Skill 的格式校验 | skill-creator `quick_validate.py` 通过；不代表模型行为测试 |
| 公众号本地富文本复制与粘贴 | 10 个小节、2 个代码块、102 个带样式段落保留 |
| 标题/摘要复制、备用复制、手动选中、封面下载 | 通过；隔离 Chrome 只访问本地页面，未产生外部网络请求 |
| 390px 手机预览 | 无横向溢出、无超宽正文元素 |
| Codex CLI 入口 | 本机 0.154.0 帮助已核对；未调用模型执行教程命令 |

本轮没有修改 OpenSpec 规格和依赖版本。规格的本地安装、练习归档证据来自下面的 v0.1.0；远程 CI 会对新提交再次检查规格。完整跨平台结果请查看 [v0.2.0](https://github.com/newlightlw/codex-workflow-starter/releases/tag/v0.2.0) 对应提交的 [Actions](https://github.com/newlightlw/codex-workflow-starter/actions)，以实际作业结果及跳过项为准。

代码与文档进行了实施者自审；未运行独立 Agent 审查、多 Agent/worktree 实验或跨模型行为评测。接入工具未在用户真实业务项目上安装；自动测试采用临时的合成项目。

## v0.1.0：原有本地自动检查（历史记录）

环境：macOS，Python 3.12.14；独立练习还使用 Python 3.13.11；Node.js 24.12.0，npm 11.6.2，OpenSpec 1.16.1。

| 检查 | 命令或操作 | 结果 |
| --- | --- | --- |
| 参考实现与练习生成 | `python3 -m unittest discover -s tests -v` | 15 项通过，0 失败、0 跳过 |
| Skill 包完整性 | `python3 scripts/verify_bundle.py` | 6 个 Skill、15 个锁定文件通过 |
| OpenSpec 安装 | `npm ci --ignore-scripts` | 按锁文件安装 57 个包成功 |
| 规格严格检查 | `npm run spec:check` | 当前主规格 1 项、归档变更 1 项通过 |
| 全新练习初始状态 | 生成到独立目录并运行预置完成测试 | 1 个预期断言失败，原因为功能尚未实现 |
| 练习完整行为 | 放入参考实现和参考行为测试后运行 | 13 项行为测试通过 |
| 练习 OpenSpec 活动变更 | 独立 `npm ci --ignore-scripts` 后 `npm run spec:check` | 活动变更和基线规格通过 |
| 练习归档 | 完成清单后 `npx --no-install openspec archive complete-task --yes` | 主规格合并、归档成功，随后严格检查通过 |

“放入参考实现”用于验证教学材料之间是否一致，不代表真实读者或独立 Codex 会话已经完成练习。预置红灯是课程起点，根目录测试不留失败。

原版本提交为 `8e66c4121ec5624e619d2a59364d9102312052d8`，其 [5 项远程 CI 作业](https://github.com/newlightlw/codex-workflow-starter/actions/runs/43410441388) 已通过。下面的通用边界同样适用于新版本。

## 检查边界

- 测试使用临时文件和合成数据，主业务链通过真实 CLI 与新进程读取验证，无网络调用或模型 API。
- 没有把多个 Codex 模型或不同客户端的实际技能调用做自动评分；读者须按教程核对已读取的文件和交互行为。
- 文件错误与业务边界覆盖见 `testing.md`，不宣称生产部署、并发、断电恢复或所有 OS 错误已验证。
- GitHub Actions 配置包含 Linux（Python 3.11/3.13）、Windows、macOS（Python 3.13）及规格检查。远程实际状态以 [Actions](https://github.com/newlightlw/codex-workflow-starter/actions) 对应提交为准；配置存在本身不是通过证据。
- 公众号复制页的本地富文本检查与实际公众号后台发布分别记录；本任务没有登录公众号后台或发布文章。
