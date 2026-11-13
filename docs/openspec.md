# OpenSpec：管理规格与变更

基础 Python 练习不需要安装 OpenSpec。想复现我管理规格的方式，可以使用这个可选层。本仓库固定 `@fission-ai/openspec` 为 **1.16.1**；上游最新版本和命令可能已不同。

## 检查本仓库

需要 Node.js 22.12+（本地验证使用 24.12.0）、npm：

```bash
npm ci
npm run spec:check
```

`package-lock.json` 固定依赖；检查脚本关闭 OpenSpec 遥测，分别验证活动规格和归档变更。初次安装需要访问 npm registry。无需全局安装。

## 文件职责

- `openspec/specs/task-list/spec.md`：当前接受的完整行为。
- `openspec/changes/archive/2026-11-13-complete-task/`：已完成的教学变更；包含 proposal（为什么）、design（怎样）、specs（行为差异）、tasks（交付清单）。
- 生成的练习目录：主规格只包含新增/读取的基线；`openspec/changes/complete-task/` 是尚未完成的活动变更，任务未打勾。

根目录是参考答案，练习目录是学习起点；没有将已完成状态冒充练习进度。

## 在练习目录中使用 CLI

生成目录会带上 `package.json`、锁文件和检查脚本。先 `npm ci`，然后 `npm run spec:check`。在已完成测试、验收并确认接受变更后，可以执行：

```bash
npx --no-install openspec archive complete-task --yes
npm run spec:check
```

归档会修改主规格和变更目录，因此先确认变更已经完成；检查最终 diff。`--yes` 是在你已确认这次归档时跳过交互询问，不是跳过验收。

如果希望让 Codex 自动生成 OpenSpec 专项 Skills，可在自己项目运行 `npx --no-install openspec init --tools codex`，检查它新增的文件再使用；本仓库不依赖生成式 slash 命令，也不自动覆盖已有配置。不同版本生成的技能名称可能不同，以安装版本的 `--help` 和生成文件为准。

上游：[Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec)。
