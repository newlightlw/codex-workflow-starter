## Why

已有新增与读取的清单需要支持任务完成，并能在下一次运行中保留状态。用这一小功能练习从规格、测试到实现与交接。

## What Changes

- 增加 complete ID 的状态变化与持久化。
- 定义重复完成、缺失 ID 和其他任务不受影响的行为。
- 添加 CLI 测试及学习、验证记录。

## Capabilities

### New Capabilities

None.

### Modified Capabilities

- `task-list`: 新增完成任务与不存在 ID 的处理。

## Impact

只涉及本地 Python CLI、测试与文档；没有网络、账户或数据库迁移。
