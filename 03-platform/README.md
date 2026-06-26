# 03 Platform — API + Web Dashboard + 五層架構

> 體驗 21 個 API 端點 + Kanban Web UI + 五層架構全貌。

## 啟動

```bash
cd 03-platform
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # 填入 TELEGRAM_BOT_TOKEN
python start.py
```

## 測試

### API（curl）

```bash
curl http://localhost:33333/api/health
curl http://localhost:33333/api/board
curl http://localhost:33333/api/runtimes
curl http://localhost:33333/api/agents
```

### Web Kanban Board

瀏覽器開啟：`http://localhost:33333/board`

### Telegram

| 指令 | 功能 |
|------|------|
| `/board` | 任務看板 |
| `/assign 描述` | 建立任務 |
| `/unblock <id>` | 解除阻礙 |
| `/retry <id>` | 重試失敗任務 |
| `/runtimes` | Runtime 狀態 |

## 五層架構

```
L1 Entry        → API :33333 + Telegram + Web Board
L2 OS           → TaskLifecycle + Autopilot + EventBus
L3 Collaboration→ A2A Router + TaskGraph + Discovery
L4 Execution    → RuntimeRegistry (kiro-cli/claude/codex/multica)
L5 Knowledge    → Wiki Engine + raw→ingest→wiki
```

## 需要的 Key

| Key | 必要 |
|-----|------|
| TELEGRAM_BOT_TOKEN | ✅ |
