"""一鍵啟動 Bot。"""
from __future__ import annotations
import asyncio, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent / "src"))
from dotenv import load_dotenv
load_dotenv()
from bot.main import main

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nBot 已停止。")
