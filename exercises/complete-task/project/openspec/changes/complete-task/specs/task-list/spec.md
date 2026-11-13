## ADDED Requirements


### Requirement: Complete a task
The CLI SHALL 通过 complete ID 将存在的任务设为 completed，持久化后返回该任务，并保留其他任务及列表顺序。

#### Scenario: Complete and reopen
- **WHEN** 新增一个 pending 任务，执行 complete 1，再启动独立 list 进程
- **THEN** 完成命令与后续列表均显示该任务状态为 completed，退出码均为 0

#### Scenario: Repeat completion
- **WHEN** 再次完成同一已完成任务
- **THEN** 成功返回同一任务，存储文件内容不变

#### Scenario: Keep other tasks
- **WHEN** 完成多个任务中的其中一个
- **THEN** 其他任务的 ID、标题、状态及顺序不变

### Requirement: Reject unknown task ids
The CLI SHALL 对不存在的整数 ID 返回 task not found，退出码为 2，且保持存储不变。

#### Scenario: Unknown id
- **WHEN** 对现有清单执行 complete 99，且 ID 99 不存在
- **THEN** stderr 返回 JSON 错误且现有文件不变

#### Scenario: No store yet
- **WHEN** 在存储文件不存在时执行 complete 1
- **THEN** 返回 task not found 且不创建文件
