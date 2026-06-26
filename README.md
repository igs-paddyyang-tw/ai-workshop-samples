# AI Workshop Samples

> `git clone` → 填 `.env` → `python start.py` → 5 分鐘啟動。

## 使用方式

```bash
git clone https://github.com/igs-paddyyang-tw/ai-workshop-samples.git
cd ai-workshop-samples/{選一個 sample}
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # 填入 Token
python start.py        # 或 start_bot.py
```

## Sample 列表

| # | 目錄 | 功能 | 需要的 Key |
|---|------|------|-----------|
| 01 | [01-ai-bot](01-ai-bot/) | 單一 Bot + 意圖路由 + Gemini 對話 | TG Token + Gemini |
| 02 | [02-agent-team](02-agent-team/) | 5 Agent 團隊 + 任務看板 + Telegram 派工 | TG Token |
| 03 | [03-platform](03-platform/) | API 21 端點 + Web Kanban + 五層架構 | TG Token |
| 04 | [04-skills-demo](04-skills-demo/) | Spec-Driven 開發（拷問→Spec→Skill→驗證） | Kiro CLI |
| 05 | [05-llm-wiki](05-llm-wiki/) | RAG 問答 + 知識圖譜 + Wiki | TG Token + Gemini |

## 前置條件

- Python 3.12+
- Telegram 帳號（01/02/03/05）
- Gemini API Key（01/05，免費：aistudio.google.com）
- Kiro CLI 2.7+（僅 04）

## 與 ai-workshop 教材的關係

| 這個 repo | ai-workshop repo |
|-----------|-----------------|
| 已產出的成品（直接跑） | 教學文件（教你理解怎麼建） |
| 適合「50 分鐘體驗課」 | 適合「從零學習」 |

## 版本

基於 `ark-agent-team-builder v2.1` + `ark-kiro-init v2.1` 產出。
