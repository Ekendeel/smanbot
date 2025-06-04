from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
import asyncio
import logging
import os

TOKEN = os.getenv("TOKEN")

bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher(storage=MemoryStorage())

# Главное меню
main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🛍 Каталог"), KeyboardButton(text="🛒 Корзина")],
        [KeyboardButton(text="👤 Профиль")],
    ],
    resize_keyboard=True
)

# Категории каталога (как у Ozon)
catalog_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="📱 Электроника", callback_data="cat_электроника")],
    [InlineKeyboardButton(text="👕 Одежда", callback_data="cat_одежда")],
    [InlineKeyboardButton(text="👟 Обувь", callback_data="cat_обувь")],
    [InlineKeyboardButton(text="🏡 Дом и сад", callback_data="cat_домисад")],
    [InlineKeyboardButton(text="🧸 Детские товары", callback_data="cat_детское")],
    [InlineKeyboardButton(text="💄 Красота и здоровье", callback_data="cat_красота")],
    [InlineKeyboardButton(text="📺 Бытовая техника", callback_data="cat_техника")],
    [InlineKeyboardButton(text="🏕 Спорт и отдых", callback_data="cat_спорт")],
    [InlineKeyboardButton(text="🛠 Строительство и ремонт", callback_data="cat_ремонт")],
    [InlineKeyboardButton(text="🍎 Продукты питания", callback_data="cat_еда")],
    [InlineKeyboardButton(text="💊 Аптека", callback_data="cat_аптека")],
    [InlineKeyboardButton(text="🐶 Товары для животных", callback_data="cat_животные")],
    [InlineKeyboardButton(text="📚 Книги", callback_data="cat_книги")],
    [InlineKeyboardButton(text="🎣 Туризм, рыбалка, охота", callback_data="cat_туризм")],
    [InlineKeyboardButton(text="🚗 Автотовары", callback_data="cat_авто")],
    [InlineKeyboardButton(text="🪑 Мебель", callback_data="cat_мебель")],
    [InlineKeyboardButton(text="🎨 Хобби и творчество", callback_data="cat_хобби")],
    [InlineKeyboardButton(text="💍 Ювелирные украшения", callback_data="cat_ювелирка")],
    [InlineKeyboardButton(text="🎮 Игры и консоли", callback_data="cat_игры")],
    [InlineKeyboardButton(text="🖊 Канцелярия", callback_data="cat_канцелярия")],
    [InlineKeyboardButton(text="🔞 Товары для взрослых", callback_data="cat_18")],
    [InlineKeyboardButton(text="📀 Цифровые товары", callback_data="cat_цифра")],
    [InlineKeyboardButton(text="🧼 Бытовая химия", callback_data="cat_химия")],
    [InlineKeyboardButton(text="🎵 Музыка и видео", callback_data="cat_музыка")],
    [InlineKeyboardButton(text="🚘 Автомобили", callback_data="cat_авто2")],
])

# Команды

@dp.message(F.text.in_({'/start', 'start'}))
async def start(message: Message):
    await message.answer(
        "Добро пожаловать в SMANSHOP 👋\n\nВыберите раздел:",
        reply_markup=main_menu
    )

@dp.message(F.text == "🛍 Каталог")
async def show_catalog(message: Message):
    await message.answer("Выберите категорию:", reply_markup=catalog_keyboard)

@dp.message(F.text == "🛒 Корзина")
async def show_cart(message: Message):
    await message.answer("🛒 Ваша корзина пуста.")

@dp.message(F.text == "👤 Профиль")
async def show_profile(message: Message):
    await message.answer(f"👤 Профиль:\nИмя: {message.from_user.full_name}\nID: {message.from_user.id}")

# Обработка нажатий по категориям
@dp.callback_query(F.data.startswith("cat_"))
async def category_callback(callback):
    category = callback.data[4:]
    await callback.message.answer(f"🔍 Вы выбрали категорию: <b>{category.capitalize()}</b>")

async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
