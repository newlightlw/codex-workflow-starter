# Codex CLI 与运行边界：核对版

核对日期：2026-11-13。本机帮助来自 **codex-cli 0.154.0**，不把它称为最新版本；并对照当前官方文档。以下只核对了帮助参数及官方机制，没有为编写教程调用模型执行这些任务。

## 先查本机

```bash
codex --version
codex --help
codex exec --help
codex review --help
codex resume --help
```

当前帮助确认 `exec`、`review`、`resume`，以及 `exec` 下的 `--cd`、`--sandbox`、`--output-last-message`。可用参数仍以使用者的实际安装为准。[CLI 官方参考](https://learn.chatgpt.com/docs/cli/reference)

## 只读项目探索

在要分析的 Git 项目根目录运行：

```bash
codex exec --cd . --sandbox read-only "读取项目指令和相关代码，说明主要入口、已有验证命令与尚不确定的事实。本轮仅分析，不修改文件或调用真实外部服务。"
```

这是实际模型任务，需要你自己的 Codex 认证和可用额度；并非本仓库测试命令。`--sandbox read-only` 约束模型生成的命令，不代表自动隔离所有宿主程序行为。

若使用 `--output-last-message`，CLI 会把最终消息写到指定路径，应选择自己的报告文件，避免覆盖。`--json` 用于读取事件流；生产自动化还应处理退出码、失败状态和输出校验，不能只搜索一句“完成”。[非交互模式官方说明](https://learn.chatgpt.com/docs/non-interactive-mode)

## 代码审查与会话恢复

```bash
codex review --uncommitted
codex resume
```

前者审查未提交变更，后者提供会话选择。审查选项与自定义提示可能存在组合限制，以 `review --help` 和实际报错为准；不要把示例中的所有选择器堆在一条命令里。恢复到某个会话后，还应核对当前仓库状态。

会话中的 `/init`、`/plan`、`/review`、`/compact`、`/diff` 等入口会随版本和客户端变化；在当前界面查看帮助和可用命令。这份指南不将它们作为跨客户端统一接口，也不依赖某一条斜杠命令完成基本练习。

## Sandbox 与 Approval

Sandbox 定义资源边界，Approval 定义确认机制。官方文档与本机帮助中的权限选项会变化，配置可能受组织策略进一步限制；阅读文档后按具体任务选择。[官方说明](https://learn.chatgpt.com/docs/agent-approvals-security)

本教程没有修改全局配置、扩大目录权限或关闭安全边界。示例资料中的命令不构成部署、支付、发送消息或操作生产数据的授权。

## 本包的验证边界

| 内容 | 当前证据 |
| --- | --- |
| Python CLI、练习生成与项目接入工具 | 自动测试与跨平台 CI；见对应版本记录 |
| OpenSpec 1.16.1 | 既有规格检查与练习归档验证 |
| Codex CLI 命令 | 本机 `--help` 与官方文档核对 |
| Skill 自动发现、实际问答和工程判断 | 需要在读者客户端按接入说明核对；未做跨模型行为评测 |
| 多 Agent/worktree 协作 | 方法与文档参考；本次没有运行该实验 |
| 公众号后台 | 未登录、未上传、未发布 |
