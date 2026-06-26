# 04 Skills Demo — Spec-Driven 開發完整迴圈

> 體驗：拷問設計 → 產出 Spec → 建 Skill → 驗證一致性。

## 使用方式

本 sample 搭配 Kiro CLI 使用（在聊天框輸入指令觸發 Skill）。

### 流程 A：拷問設計

```
拷問我的設計：每日科技新聞日報 Skill
```

→ AI 問 8-15 個問題，走完決策樹，產出決策摘要。

### 流程 B：產出 Spec

```
根據以上決策摘要，幫我寫 spec
```

→ 產出 `docs/specs/` 下的標準規格文件。

### 流程 C：建 Skill

```
建立新 Skill：每日科技新聞日報，根據 spec 實作
```

→ 產出 `.kiro/skills/my-daily-news/` 完整結構。

### 流程 D：驗證 Spec ↔ Code

```
驗證 code 跟 spec 一致嗎
```

→ 產出 Drift Report（4 維度 0-100 評分）。

## 已安裝的 Skills

| Skill | 功能 | 觸發詞 |
|-------|------|--------|
| `ark-grill-me` | 拷問設計 | 「拷問」「grill me」 |
| `ark-superpowers` | 產出 Spec/Design/Plan | 「寫 spec」「設計文件」 |
| `ark-code-spec-validator` | 驗證一致性 | 「驗證 spec」「drift」 |

## 範例 Spec

已預置：`docs/specs/example-spec.md`（可作為驗證範例）

## 需要的工具

| 工具 | 必要 |
|------|------|
| Kiro CLI 2.7+ | ✅ |
| Python 3.12+ | ✅ |
