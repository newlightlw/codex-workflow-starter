# 发布前验证记录

日期：2026-11-13。以下是本教学仓库的实际检查，独立于配套文章中的历史私有项目测试数。

## v0.2.3：组件总览与手机阅读

本次只修改文章与说明；Skill、业务实现、OpenSpec 和已有案例快照均未修改。表格根据仓库随附 Skills、说明和既有实践整理，不新增安装或真实项目验证结论。

本地隔离浏览器检查通过：12 行总览与 39 个表头/单元格完整复制、粘贴后文字一致且保留行内样式；10 个小节、2 个代码块和 116 个带样式段落保留。标题/摘要、备用复制、手动选中和封面下载通过。360px 与 390px 手机预览无横向溢出或单元格裁切，表格字号为 14px；已检查手机截图。纯行内样式版也通过窄屏检查，浏览器未发出外部网络请求。公众号后台粘贴、发布仍未验证。

Markdown 相对链接与最终 diff 已检查。文档改动未新增业务测试；本仓库完整回归由当前提交的 GitHub Actions 执行，见 [v0.2.3](https://github.com/newlightlw/codex-workflow-starter/releases/tag/v0.2.3) 与 [Actions](https://github.com/newlightlw/codex-workflow-starter/actions)。

## v0.2.2：连续两轮接续与分层验证

本次只修改文章与案例说明，Skill、Python 实现和 OpenSpec 未变。核对私有项目的 S2-05 阶段报告与最终日志（416 项）及 S2-06 回归日志（428 项）、真实演练记录和后续排查说明；没有为本次文章编辑执行私有项目的测试或付费任务。真实运行未形成准备证明，恢复未执行，详见[案例记录](case-deepagents-imp.md)。

本地 Skill 完整性检查通过（7 个 Skill、26 个锁定文件），70 个相对链接和最终 diff 已检查。新版公众号富文本复制保留两轮案例、10 个小节、2 个代码块和 111 个带样式段落；标题/摘要、备用复制、手动选中、封面下载和 390px 手机布局通过。隔离浏览器没有外部网络请求，公众号后台未发布。

本仓库的 22 项 Python 测试与 OpenSpec 校验由新提交的 GitHub Actions 执行，结果见 [v0.2.2](https://github.com/newlightlw/codex-workflow-starter/releases/tag/v0.2.2) 与 [Actions](https://github.com/newlightlw/codex-workflow-starter/actions)。私有项目的 416/428 项为两个阶段的回归快照，包含重叠用例；它们不是本仓库测试，也不是模型行为评测分数。

## v0.2.1：真实使用案例与文章更新（历史记录）

本次修改文章、案例和说明文档，Skill 包、Python 代码与 OpenSpec 均未改变。使用记录来自作者私有项目的会话及已有日志核对，见[案例快照](case-deepagents-imp.md)；没有为文章再次运行该项目或调用付费服务。

本地已检查 Skill 完整性（7 个 Skill、26 个锁定文件）、Markdown 相对链接和最终 diff。公众号富文本复制与本地粘贴保留 10 个小节、2 个代码块和 110 个带样式段落，新增真实案例完整；标题/摘要复制、备用复制、手动选中和封面下载通过，390px 手机预览无横向溢出。浏览器验证仅访问本地文件，没有外部网络请求。

文档修改没有额外增加代码测试；完整回归由当前提交的 GitHub Actions 执行。结果见 [Actions](https://github.com/newlightlw/codex-workflow-starter/actions) 与 [v0.2.1 发布记录](https://github.com/newlightlw/codex-workflow-starter/releases/tag/v0.2.1)。私有项目的 7/29 项定向检查与本仓库的 22 项测试是两组不同证据。

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
