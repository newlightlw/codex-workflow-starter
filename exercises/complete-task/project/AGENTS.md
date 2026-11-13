# 练习项目约定

先读 README.md、docs/requirements.md 与 openspec/changes/complete-task/。本次只完成 R3/R4，不读取外部参考仓库的答案。新增/读取是已有基线。

- 遵循本项目 Skills；首次测试入口按 tdd 要求确认后实施。
- 先复现目标失败，再做最小完整修改；新行为小步补测试，预期以需求为依据。
- 所有自动测试使用临时数据，运行 `python3 -m unittest discover -s tests -v`。
- 基线需保持通过，完成后原预置失败测试也应通过。不要删除、跳过测试或降低断言。
- 同步受影响的规格与任务，更新 docs/verification.md 和 learns/01-taskbox.md。
- 收尾说明实际命令及通过/失败/跳过/未执行；区分自动测试与本人体验验收。
- 完成并接受变更后，才合并主规格与归档。project-testing 面向整体验收，清单确认前只读调查。
