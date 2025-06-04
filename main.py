
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
import asyncio
import logging
import os

TOKEN = os.getenv("TOKEN")
bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(storage=MemoryStorage())

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🛍 Каталог"), KeyboardButton(text="🛒 Корзина")],
        [KeyboardButton(text="👤 Профиль")],
    ],
    resize_keyboard=True
)

catalog_page_0 = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Смартфоны", callback_data="sub_Смартфоны")],
        [InlineKeyboardButton(text="Смарт-часы", callback_data="sub_Смарт-часы")],
        [InlineKeyboardButton(text="Наушники", callback_data="sub_Наушники")],
        [InlineKeyboardButton(text="Ноутбуки", callback_data="sub_Ноутбуки")],
        [InlineKeyboardButton(text="Фотоаппараты", callback_data="sub_Фотоаппараты")],
        [InlineKeyboardButton(text="Игровые приставки", callback_data="sub_Игровые приставки")],
        [InlineKeyboardButton(text="Принтеры", callback_data="sub_Принтеры")],
        [InlineKeyboardButton(text="Квадрокоптеры", callback_data="sub_Квадрокоптеры")],
        [InlineKeyboardButton(text="Умный дом", callback_data="sub_Умный дом")],
        [InlineKeyboardButton(text="Телевизоры", callback_data="sub_Телевизоры")],
    ]
)

@dp.message(F.text.in_({'/start', 'start'}))
async def start(message: Message):
    await message.answer("Добро пожаловать в SMANSHOP 👋\n\nВыберите раздел:", reply_markup=main_menu)

@dp.message(F.text == "🛍 Каталог")
async def show_catalog(message: Message):
    await message.answer("📦 Электроника — выбери подкатегорию:", reply_markup=catalog_page_0)

@dp.callback_query(F.data.startswith("sub_"))
async def subcategory_callback(callback: CallbackQuery):
    subcat = callback.data[4:]
    await callback.message.answer(f"📂 Подкатегория: <b>{subcat}</b>")

@dp.message(F.text == "🛒 Корзина")
async def show_cart(message: Message):
    await message.answer("🛒 Ваша корзина пуста.")

@dp.message(F.text == "👤 Профиль")
async def show_profile(message: Message):
    await message.answer(f"👤 Профиль:\nИмя: {message.from_user.full_name}\nID: {message.from_user.id}")

async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
