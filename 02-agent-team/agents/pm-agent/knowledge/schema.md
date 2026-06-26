---
title: "pm-agent Knowledge Schema"
type: system
created: 2026-06-26
updated: 2026-06-26
---

# Wiki Schema v3.1

## 目錄結構

```
knowledge/
├── raw/          → 所有輸入先進這裡
├── wiki/         → 由 LLM ingest 產出（不可手動寫入）
├── schema.md     → 本文件
├── index.md      → 索引目錄
└── log.md        → 操作日誌（append-only）
```

## Frontmatter（必要）

```yaml
---
title: "頁面標題"
type: concept | entity | source | synthesis | overview
tags: [tag1, tag2]
created: YYYY-MM-DD
updated: YYYY-MM-DD
status: seedling | developing | mature
---
```

## 操作規則

| 規則 | 說明 |
|------|------|
| 所有輸入先進 raw/ | Agent、人類、排程都寫 raw |
| 修改後同步 | 改 wiki → 必須更新 index.md + log.md |
| log append-only | 禁止刪除舊記錄 |
