# 发布前验证记录

日期：2026-11-13。以下是本教学仓库的实际检查，独立于配套文章中的历史私有项目测试数。

## 本地自动检查

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

## 检查边界

- 测试使用临时文件和合成数据，主业务链通过真实 CLI 与新进程读取验证，无网络调用或模型 API。
- 没有把多个 Codex 模型或不同客户端的实际技能调用做自动评分；读者须按教程核对已读取的文件和交互行为。
- 文件错误与业务边界覆盖见 `testing.md`，不宣称生产部署、并发、断电恢复或所有 OS 错误已验证。
- GitHub Actions 配置包含 Linux（Python 3.11/3.13）、Windows、macOS（Python 3.13）及规格检查。远程实际状态以 [Actions](https://github.com/newlightlw/codex-workflow-starter/actions) 对应提交为准；配置存在本身不是通过证据。
- 公众号复制页的本地富文本检查与实际公众号后台发布分别记录；本任务没有登录公众号后台或发布文章。
