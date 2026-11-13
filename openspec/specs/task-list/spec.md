# Task List Specification

## Purpose

定义本地任务清单的新增、读取与输入错误行为。完整业务依据见 docs/requirements.md。

## Requirements

### Requirement: Add and list local tasks
The CLI SHALL 新增任务并以 JSON 输出结果，按新增顺序列出持久化任务。首个 ID 为 1，后续递增，初始状态为 pending。

#### Scenario: First list
- **WHEN** 存储文件不存在时执行 list
- **THEN** 返回空数组，退出码为 0，且不创建文件

#### Scenario: Add then reopen
- **WHEN** 新增标题为“读规格”的任务，再启动独立 list 进程
- **THEN** 两次结果均包含 ID 1、标题“读规格”及 pending 状态

### Requirement: Validate title before writing
The CLI SHALL 移除标题首尾空白，并只接受 1 至 80 个 Unicode code point 的标题。

#### Scenario: Invalid title
- **WHEN** 输入空白标题或 81 字符标题
- **THEN** 退出码为 2，stderr 有 JSON 错误，存储内容保持不变

### Requirement: Preserve invalid storage
The CLI SHALL 报告无效 JSON、非法任务结构与文件读写错误；不得将损坏文件当空列表覆盖。

#### Scenario: Corrupt store
- **WHEN** 在损坏的 JSON 文件上执行 add
- **THEN** 返回错误且原文件保持不变

#### Scenario: Missing parent directory
- **WHEN** 存储路径的父目录不存在时执行 add
- **THEN** 返回错误且不创建父目录


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
