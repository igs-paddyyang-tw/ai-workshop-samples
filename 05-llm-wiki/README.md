# 05 LLM Wiki — RAG 問答 + 知識圖譜

> 5 分鐘啟動，體驗 AI 引用知識庫回答問題。

## 啟動

```bash
cd 05-llm-wiki
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # 填入 GEMINI_API_KEY
python start_bot.py
```

## 預置知識

`knowledge/raw/` 已有 3 篇範例文件：
- `python-async-guide.md` — asyncio 教學
- `agent-design-notes.md` — 五層架構筆記
- `common-errors.md` — 常見問題排查

## 測試

### 在 Telegram 對 Bot 提問

| 你問 | 預期回應 |
|------|---------|
| 什麼是 asyncio？ | 引用 python-async-guide 回答 |
| Agent 五層架構？ | 引用 agent-design-notes 回答 |
| Bot 沒回應怎辦？ | 引用 common-errors 排查表 |

### 進階操作（在 Kiro CLI 觸發）

```
匯入 raw 資料夾的文件到 Wiki     → wiki_ingest
wiki 健康檢查                    → wiki_lint
分析知識圖譜                     → wiki_graph
搜尋：asyncio 超時               → wiki_hybrid_search
```

## 架構

```
使用者問題 → wiki_query（FTS5 搜尋）→ wiki_rag_bridge（注入 context）→ Gemini → 引用回答
```

## 需要的 Key

| Key | 必要 | 取得方式 |
|-----|------|---------|
| TELEGRAM_BOT_TOKEN | ✅ | @BotFather |
| GEMINI_API_KEY | ✅ | aistudio.google.com |
