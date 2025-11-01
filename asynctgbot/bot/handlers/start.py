from aiogram import Router, types, F
from aiogram.filters import Command
from db import add_user, get_user_count
from config import settings

router = Router()


@router.message(Command("start"))
async def cmd_start(message: types.Message):
    user = message.from_user
    await add_user(user.id, user.username, user.first_name, user.last_name)
    await message.answer(f"👋 Hi, {user.first_name} !\n ")


@router.message(Command("users"))
async def cmd_users(message: types.Message):
    if message.from_user.id != settings.admin_id:
        await message.answer("❌ Sizda bu buyruq uchun ruxsat yo‘q.")
        return

    count = await get_user_count()
    await message.answer(f"📊 Jami foydalanuvchilar: {count} ta")
