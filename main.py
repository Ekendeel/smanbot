
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

import asyncio
import logging
import os

TOKEN = os.getenv("TOKEN")

bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(storage=MemoryStorage())

@dp.message(F.text.in_({'/start', 'start'}))
async def start(message: Message):
    await message.answer(
        "Добро пожаловать в SMANSHOP 👋\n\n"
        "Выберите раздел:\n"
        "🛍 Каталог\n🛒 Корзина\n👤 Профиль"
    )

async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
