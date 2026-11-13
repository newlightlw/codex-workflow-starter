# 项目工作约定

维护参考实现前读 `docs/requirements.md`；修改练习生成流程时，再读 `docs/start-here.md` 和 `exercises/complete-task/project/README.md`。需求中的 R1–R6 是行为依据，`openspec/` 记录其规格与变更。

修改项目接入工具前读 `docs/adoption.md`，其中 A1–A4 是接入行为依据。需要组织复杂任务、接续工作或阶段交付时，按需读取 `.agents/skills/codex-workflow/SKILL.md`；已有规格与记录优先复用，不新建重复事实源。仅讨论并行方法不构成启用子 Agent 的授权。

- 先核对目标、现有代码、测试和工作区改动。做最小完整修改，保护已有工作。
- 正常开发持续完成实现、相关验证和文档更新；重大范围选择、无法推断的关键条件或外部副作用需先明确。
- Bug 先复现，再按根因修复；测试断言以已确认需求为准。
- 修改代码后运行 `python3 -m unittest discover -s tests -v`；修改 Skill 包或其来源时运行 `python3 scripts/verify_bundle.py`。如不能执行，如实报告未验证范围。
- 修改 OpenSpec 时，按 `docs/openspec.md` 运行规格检查；基础 Python 变更不要求安装 Node.js。
- `project-testing` 只在整体验收或建立测试体系时触发，其阶段确认见该 Skill；日常开发的相关测试按已有授权执行。
- 练习保留未实现行为；参考实现保持通过。修改一侧后检查生成出的练习仍能正确经历失败与通过。
- 最终报告实际命令、通过/失败/跳过/未执行，区分实现、自动验证和真人体验。同步受影响的需求、测试映射和学习说明。
