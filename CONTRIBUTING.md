# 参与改进

欢迎提交复现问题、文档勘误和小范围改进。请描述具体行为、期望、环境与复现命令；引用来源时尽量指向原始文档。

代码修改运行 `python3 -m unittest discover -s tests -v`。Skill 文件修改需注明来源及适配原因，更新 `skills-lock.json` 中对应文件的 SHA-256，再运行 `python3 scripts/verify_bundle.py`；同时人工复查说明与引用。规格修改运行 `npm run spec:check`。

参考实现应保持通过，练习初始失败必须仍对应目标行为缺失。不要将测试数当成质量分数；报告真实结果和缺口。提交不包含个人路径、私有项目内容、账号或凭证。
