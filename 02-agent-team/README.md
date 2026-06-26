# 02 Agent Team — 多 Agent 協作 + 任務管理

> 5 分鐘啟動 5 人 AI 團隊，體驗 Telegram 派工 + 任務看板。

## 啟動

```bash
cd 02-agent-team
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # 填入 TELEGRAM_BOT_TOKEN + allowed_users Chat ID
python start.py
```

## 測試

| 在 Telegram 發送 | 預期回應 |
|-----------------|---------|
| `/start` | 歡迎訊息 + 團隊成員列表 |
| `/agents` | Agent 列表 + 在線狀態 |
| `/board` | 任務看板摘要 |
| `/assign 建立 REST API` | 建立任務 + 選擇指派對象 |
| `/runtimes` | Runtime 狀態（kiro-cli available） |

## 團隊成員

| Agent | 角色 | 職責 |
|-------|------|------|
| admin-agent | ⚙️ Admin | 服務管理、監控 |
| pm-agent | 🧠 Leader | 需求分析、派工 |
| ai-dev-agent | 🤖 AI Dev | AI 架構、Prompt |
| coder-agent | 💻 Coder | 全端開發 |
| qa-agent | 🧪 QA | 測試、品質 |

## 架構

```
Telegram → Gateway :33333 → Coordinator → A2A Router → Agents
                                 ↓
                          TaskLifecycle（7 狀態機）
```

## 需要的 Key

| Key | 必要 | 取得方式 |
|-----|------|---------|
| TELEGRAM_BOT_TOKEN | ✅ | @BotFather |
