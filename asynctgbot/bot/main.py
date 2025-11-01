import asyncio
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from handlers import start
from config import settings
from db import init_db


async def main():
    await init_db()

    bot = Bot(token=settings.bot_token, parse_mode=ParseMode.HTML)
    dp = Dispatcher()

    dp.include_router(start.router)

    print("🚀 Bot started...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print("❌ Bot stopped.")
