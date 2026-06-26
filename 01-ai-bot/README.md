# 01 AI Bot — 單一 Agent 對話 + 意圖路由

> 5 分鐘啟動，體驗 AI Bot 的意圖路由 + Gemini 即時對話。

## 啟動

```bash
cd 01-ai-bot
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # 填入 TELEGRAM_BOT_TOKEN + GEMINI_API_KEY
python start_bot.py
```

## 測試

| 在 Telegram 發送 | 預期回應 |
|-----------------|---------|
| `/start` | 歡迎訊息 |
| `什麼是 Python？` | Gemini AI 回答 |
| `今天新聞` | News Skill 觸發 |

## 架構

```
使用者訊息 → Planner（意圖分類）→ Gemini Chat / News Skill / 指令 Handler
```

## 需要的 Key

| Key | 必要 | 取得方式 |
|-----|------|---------|
| TELEGRAM_BOT_TOKEN | ✅ | @BotFather |
| GEMINI_API_KEY | 選用 | aistudio.google.com |
