import os
from telegram import Bot
import asyncio

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

async def main():
    bot = Bot(token=TOKEN)
    await bot.send_message(
        chat_id=CHAT_ID,
        text="✅ StockPKM est maintenant en ligne sur Railway !"
    )

if __name__ == "__main__":
    asyncio.run(main())
