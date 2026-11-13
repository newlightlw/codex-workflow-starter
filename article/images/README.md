# 正文配图与生成说明

这 5 张配图使用 Codex 内置 imagegen 生成，作为解释本文工作流的编辑插画；它们不是产品截图或新增实测证据。现有封面继续保留。

配色与封面一致：米白纸张、深蓝、橙色；用少量文字帮助手机阅读。所有原始 PNG 保存在本目录，不依赖作者机器上的路径。

| 图片 | 放置位置 | 说明 |
| --- | --- | --- |
| [图 1](01-workflow.png) | 引言后、组件表前 | 整体开发闭环 |
| [图 2](02-context-layers.png) | 第 3 节结尾 | 规则、规格与记录的分工 |
| [图 3](03-testing.png) | 第 4 节 | 开发反馈与整体验收 |
| [图 4](04-continuation.png) | 第 5 节 | 两轮接续与验证边界 |
| [图 5](05-start-small.png) | 第 8 节开头 | 读者最小入门路线 |

## 复现与使用

生成使用内置 imagegen，每张独立生成；模型具有随机性，相同提示词不保证同一像素结果。下面保留最终完整提示词。公众号复制版嵌入图片，可离线预览；若公众号编辑器粘贴时未保留图片，请按图号单独上传 PNG。公众号后台尚未验证。

## 图 1：01-workflow

```text
Use case: illustration-story with sparse educational labels. Asset type: inline editorial illustration for a Chinese WeChat article about the author's Codex software development workflow. Generate a polished landscape image, approximately 1536 x 1024, aspect ratio 3:2. Consistent series art direction: warm ivory lightly textured paper background, deep navy #112b46, restrained burnt orange #e95a24 accents, small muted green accents only for passed checks, tactile layered paper-cut objects with soft shadows, crisp modern editorial composition, lots of breathing room, no photorealistic people, no robots, no neon, no gradients, no watermark, no brand logos. All text must be large, extremely legible on a phone, exact Chinese characters or exact specified English; no additional tiny text or fake code. Use broad visual objects instead of dense tables.
Primary request: Visualize a complete development loop that leaves evidence for the next session. Title exact: “从想法到可接续的项目”. Four substantial objects in a spacious 2 by 2 clockwise loop connected with simple navy arrows: upper left a specification page labeled “明确需求”; upper right an editor window labeled “实现代码”; lower right a checklist labeled “验证结果”; lower left an orderly folder with a bookmark labeled “留下交接”. Use a small orange human decision marker near the specification, no claims of automatic success. Only those five text strings. Narrative should feel practical and calm.
```

## 图 2：02-context-layers

```text
Use case: illustration-story with sparse educational labels. Asset type: inline editorial illustration for a Chinese WeChat article about the author's Codex software development workflow. Generate a polished landscape image, approximately 1536 x 1024, aspect ratio 3:2. Consistent series art direction: warm ivory lightly textured paper background, deep navy #112b46, restrained burnt orange #e95a24 accents, small muted green accents only for passed checks, tactile layered paper-cut objects with soft shadows, crisp modern editorial composition, lots of breathing room, no photorealistic people, no robots, no neon, no gradients, no watermark, no brand logos. All text must be large, extremely legible on a phone, exact Chinese characters or exact specified English; no additional tiny text or fake code. Use broad visual objects instead of dense tables.
Primary request: An editorial cutaway of three neatly separated but connected layers of project knowledge, like three physical shelves each holding meaningful paper objects. Title exact: “把上下文放回项目”. Top layer a navy rulebook with large label “规则” and smaller but still large exact label “AGENTS.md”. Middle layer a proposal sheet and ruler with label “规格” and smaller exact label “Spec”. Bottom layer a notebook, evidence checklist and bookmark with label “记录” and smaller exact label “learns / handoff”. Broad subtle connector down the left suggests an agent can read these entry points. Not a hierarchy of authority, just organizing different kinds of material; no priority numbers, no formal precedence arrows. Only specified text. Three layers should be instantly distinguishable.
```

## 图 3：03-testing

```text
Use case: illustration-story with sparse educational labels. Asset type: inline editorial illustration for a Chinese WeChat article about the author's Codex software development workflow. Generate a polished landscape image, approximately 1536 x 1024, aspect ratio 3:2. Consistent series art direction: warm ivory lightly textured paper background, deep navy #112b46, restrained burnt orange #e95a24 accents, small muted green accents only for passed checks, tactile layered paper-cut objects with soft shadows, crisp modern editorial composition, lots of breathing room, no photorealistic people, no robots, no neon, no gradients, no watermark, no brand logos. All text must be large, extremely legible on a phone, exact Chinese characters or exact specified English; no additional tiny text or fake code. Use broad visual objects instead of dense tables.
Primary request: Two complementary scales of software testing, clearly separated in two equal spacious panels. Title exact: “开发反馈与阶段验收”. Left panel label exact “tdd”, paper red card with X leading by a navy arrow to green card with checkmark; large caption “一个行为，小步验证”. Right panel label exact “project-testing”, a clipboard of unfilled checklist rows beside a human approval stamp, with one arrow toward an organized report; large caption “先列用例，确认后执行”. Both panels share a thin base strip labeled “预期来自规格”. Do not imply all tests passed; distinguish development feedback from full acceptance. No extra words, no small prose.
```

## 图 4：04-continuation

```text
Use case: illustration-story with sparse educational labels. Asset type: inline editorial illustration for a Chinese WeChat article about the author's Codex software development workflow. Generate a polished landscape image, approximately 1536 x 1024, aspect ratio 3:2. Consistent series art direction: warm ivory lightly textured paper background, deep navy #112b46, restrained burnt orange #e95a24 accents, small muted green accents only for passed checks, tactile layered paper-cut objects with soft shadows, crisp modern editorial composition, lots of breathing room, no photorealistic people, no robots, no neon, no gradients, no watermark, no brand logos. All text must be large, extremely legible on a phone, exact Chinese characters or exact specified English; no additional tiny text or fake code. Use broad visual objects instead of dense tables.
Primary request: Tell the real article's consecutive-development case in a visual that DOES NOT claim successful recovery. Title exact: “继续开发，也要接上证据”. Two large chapter folders linked by a bridge of document pages, left labeled “S2-05”, right labeled “S2-06”. Left folder has a completed checklist and large caption “实现与隔离验证”. Right folder opens into a fork with a small green checked test page labeled “自动检查” and an amber open-circle investigation card labeled “真实验证”. The amber card is visibly unfinished, with a magnifying glass and no green check. Bridge prominently holds an orange bookmark labeled “codex-workflow”. Bottom short caption exact “测试通过 ≠ 真实恢复成功”. No counts, no additional text, no fake screenshots. Maintain sober evidence boundaries and friendly editorial clarity.
```

## 图 5：05-start-small

```text
Use case: illustration-story with sparse educational labels. Asset type: inline editorial illustration for a Chinese WeChat article about the author's Codex software development workflow. Generate a polished landscape image, approximately 1536 x 1024, aspect ratio 3:2. Consistent series art direction: warm ivory lightly textured paper background, deep navy #112b46, restrained burnt orange #e95a24 accents, small muted green accents only for passed checks, tactile layered paper-cut objects with soft shadows, crisp modern editorial composition, lots of breathing room, no photorealistic people, no robots, no neon, no gradients, no watermark, no brand logos. All text must be large, extremely legible on a phone, exact Chinese characters or exact specified English; no additional tiny text or fake code. Use broad visual objects instead of dense tables.
Primary request: Friendly beginning route for a reader to reproduce the open-source tutorial. Title exact: “先跑通一个小功能”. Center three large stepping stones ascending gently from left to right, represented by a project folder with a small rulebook, a single specification page, and a small editor plus checklist. Three exact labels beneath the stones: “打开项目”, “写清需求”, “实现并验证”. On a separate small tray below, several modular paper tools are neatly parked with one collective label “Skills 按需选用”, making optional tools visually separate from the main path. No forced-install funnel, no all-tools-required implication. No Github logo, no QR code, no URL text. Only specified labels.
```

