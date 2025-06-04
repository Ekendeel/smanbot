
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

PAGES = [['Телефоны и смарт-часы', 'Смартфоны', 'Аксессуары для смартфонов и телефонов', 'Смарт-часы', 'Фитнес-браслеты', 'Ремешки для смарт-часов и фитнес-браслетов', 'Аксессуары для смарт-часов и фитнес-браслетов', 'Мобильные телефоны', 'SIM-карты', 'Запчасти', 'Проводные и радиотелефоны', 'Ноутбуки'], ['Игровые ноутбуки', 'Планшеты', 'Электронные книги', 'Графические планшеты', 'Чехлы и подставки для планшетов', 'Стилусы', 'Аксессуары для ноутбуков', 'Запчасти для ноутбуков', 'Аккумуляторы для ноутбуков', 'Зарядные устройства', 'Чехлы для электронных книг', 'Переводчики и словари'], ['Телескопы', 'Микроскопы', 'Окуляры', 'Аксессуары для телескопов', 'Аксессуары для микроскопов', 'Наушники', 'Беспроводные колонки', 'Умные колонки', 'Акустические системы', 'Студийное и сценическое оборудование', 'Микрофоны', 'Рации и радиостанции'], ['Радиоприемники', 'Виниловые проигрыватели и аксессуары', 'Аксессуары для наушников', 'Аксессуары для аудиотехники', 'Усилители, ресиверы и ЦАПы', 'MP3-плееры', 'Диктофоны', 'Видеокарты и графические ускорители', 'Жесткие диски, SSD и сетевые накопители', 'Процессоры', 'Материнские платы', 'Оперативная память'], ['Системы охлаждения', 'Блоки питания', 'Корпуса', 'Звуковые карты', 'Электронные модули', 'Контроллеры интерфейсов', 'Микроконтроллеры', 'Тестеры для комплектующих']]
PAGE_SIZE = 12


def get_catalog_page(page_index: int):
    page = PAGES[page_index]
    buttons = [[InlineKeyboardButton(text=name, callback_data=f"sub_{name}")] for name in page]
    nav_buttons = []
    if page_index > 0:
        nav_buttons.append(InlineKeyboardButton(text="⬅️ Назад", callback_data=f"page_{page_index - 1}"))
    if page_index < len(PAGES) - 1:
        nav_buttons.append(InlineKeyboardButton(text="➡️ Далее", callback_data=f"page_{page_index + 1}"))
    if nav_buttons:
        buttons.append(nav_buttons)
    return InlineKeyboardMarkup(inline_keyboard=buttons)

@dp.message(F.text.in_({'/start', 'start'}))
async def start(message: Message):
    await message.answer("Добро пожаловать в SMANSHOP 👋\n\nВыберите раздел:", reply_markup=main_menu)

@dp.message(F.text == "🛍 Каталог")
async def show_catalog(message: Message):
    await message.answer("📦 Раздел: Электроника\nВыберите подкатегорию:", reply_markup=get_catalog_page(0))

@dp.callback_query(F.data.startswith("page_"))
async def paginate(callback: CallbackQuery):
    page_index = int(callback.data.split("_")[1])
    await callback.message.edit_reply_markup(reply_markup=get_catalog_page(page_index))

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
