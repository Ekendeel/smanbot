
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

electronics_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Телефоны и смарт-часы", callback_data="sub_Телефоны и смарт-часы")],
    [InlineKeyboardButton(text="Смартфоны", callback_data="sub_Смартфоны")],
    [InlineKeyboardButton(text="Аксессуары для смартфонов и телефонов", callback_data="sub_Аксессуары для смартфонов и телефонов")],
    [InlineKeyboardButton(text="Смарт-часы", callback_data="sub_Смарт-часы")],
    [InlineKeyboardButton(text="Фитнес-браслеты", callback_data="sub_Фитнес-браслеты")],
    [InlineKeyboardButton(text="Ремешки для смарт-часов и фитнес-браслетов", callback_data="sub_Ремешки для смарт-часов и фитнес-браслетов")],
    [InlineKeyboardButton(text="Аксессуары для смарт-часов и фитнес-браслетов", callback_data="sub_Аксессуары для смарт-часов и фитнес-браслетов")],
    [InlineKeyboardButton(text="Мобильные телефоны", callback_data="sub_Мобильные телефоны")],
    [InlineKeyboardButton(text="SIM-карты", callback_data="sub_SIM-карты")],
    [InlineKeyboardButton(text="Запчасти", callback_data="sub_Запчасти")],
    [InlineKeyboardButton(text="Проводные и радиотелефоны", callback_data="sub_Проводные и радиотелефоны")],
    [InlineKeyboardButton(text="Ноутбуки", callback_data="sub_Ноутбуки")],
    [InlineKeyboardButton(text="Игровые ноутбуки", callback_data="sub_Игровые ноутбуки")],
    [InlineKeyboardButton(text="Планшеты", callback_data="sub_Планшеты")],
    [InlineKeyboardButton(text="Электронные книги", callback_data="sub_Электронные книги")],
    [InlineKeyboardButton(text="Графические планшеты", callback_data="sub_Графические планшеты")],
    [InlineKeyboardButton(text="Чехлы и подставки для планшетов", callback_data="sub_Чехлы и подставки для планшетов")],
    [InlineKeyboardButton(text="Стилусы", callback_data="sub_Стилусы")],
    [InlineKeyboardButton(text="Аксессуары для ноутбуков", callback_data="sub_Аксессуары для ноутбуков")],
    [InlineKeyboardButton(text="Запчасти для ноутбуков", callback_data="sub_Запчасти для ноутбуков")],
    [InlineKeyboardButton(text="Аккумуляторы для ноутбуков", callback_data="sub_Аккумуляторы для ноутбуков")],
    [InlineKeyboardButton(text="Зарядные устройства", callback_data="sub_Зарядные устройства")],
    [InlineKeyboardButton(text="Чехлы для электронных книг", callback_data="sub_Чехлы для электронных книг")],
    [InlineKeyboardButton(text="Переводчики и словари", callback_data="sub_Переводчики и словари")],
    [InlineKeyboardButton(text="Телескопы", callback_data="sub_Телескопы")],
    [InlineKeyboardButton(text="Микроскопы", callback_data="sub_Микроскопы")],
    [InlineKeyboardButton(text="Окуляры", callback_data="sub_Окуляры")],
    [InlineKeyboardButton(text="Аксессуары для телескопов", callback_data="sub_Аксессуары для телескопов")],
    [InlineKeyboardButton(text="Аксессуары для микроскопов", callback_data="sub_Аксессуары для микроскопов")],
    [InlineKeyboardButton(text="Наушники", callback_data="sub_Наушники")],
    [InlineKeyboardButton(text="Беспроводные колонки", callback_data="sub_Беспроводные колонки")],
    [InlineKeyboardButton(text="Умные колонки", callback_data="sub_Умные колонки")],
    [InlineKeyboardButton(text="Акустические системы", callback_data="sub_Акустические системы")],
    [InlineKeyboardButton(text="Студийное и сценическое оборудование", callback_data="sub_Студийное и сценическое оборудование")],
    [InlineKeyboardButton(text="Микрофоны", callback_data="sub_Микрофоны")],
    [InlineKeyboardButton(text="Рации и радиостанции", callback_data="sub_Рации и радиостанции")],
    [InlineKeyboardButton(text="Радиоприемники", callback_data="sub_Радиоприемники")],
    [InlineKeyboardButton(text="Виниловые проигрыватели и аксессуары", callback_data="sub_Виниловые проигрыватели и аксессуары")],
    [InlineKeyboardButton(text="Аксессуары для наушников", callback_data="sub_Аксессуары для наушников")],
    [InlineKeyboardButton(text="Аксессуары для аудиотехники", callback_data="sub_Аксессуары для аудиотехники")],
    [InlineKeyboardButton(text="Усилители, ресиверы и ЦАПы", callback_data="sub_Усилители, ресиверы и ЦАПы")],
    [InlineKeyboardButton(text="MP3-плееры", callback_data="sub_MP3-плееры")],
    [InlineKeyboardButton(text="Диктофоны", callback_data="sub_Диктофоны")],
    [InlineKeyboardButton(text="Видеокарты и графические ускорители", callback_data="sub_Видеокарты и графические ускорители")],
    [InlineKeyboardButton(text="Жесткие диски, SSD и сетевые накопители", callback_data="sub_Жесткие диски, SSD и сетевые накопители")],
    [InlineKeyboardButton(text="Процессоры", callback_data="sub_Процессоры")],
    [InlineKeyboardButton(text="Материнские платы", callback_data="sub_Материнские платы")],
    [InlineKeyboardButton(text="Оперативная память", callback_data="sub_Оперативная память")],
    [InlineKeyboardButton(text="Системы охлаждения", callback_data="sub_Системы охлаждения")],
    [InlineKeyboardButton(text="Блоки питания", callback_data="sub_Блоки питания")],
    [InlineKeyboardButton(text="Корпуса", callback_data="sub_Корпуса")],
    [InlineKeyboardButton(text="Звуковые карты", callback_data="sub_Звуковые карты")],
    [InlineKeyboardButton(text="Электронные модули", callback_data="sub_Электронные модули")],
    [InlineKeyboardButton(text="Контроллеры интерфейсов", callback_data="sub_Контроллеры интерфейсов")],
    [InlineKeyboardButton(text="Микроконтроллеры", callback_data="sub_Микроконтроллеры")],
    [InlineKeyboardButton(text="Тестеры для комплектующих", callback_data="sub_Тестеры для комплектующих")],
    [InlineKeyboardButton(text="Мониторы", callback_data="sub_Мониторы")],
    [InlineKeyboardButton(text="Системные блоки", callback_data="sub_Системные блоки")],
    [InlineKeyboardButton(text="Моноблоки", callback_data="sub_Моноблоки")],
    [InlineKeyboardButton(text="Периферия", callback_data="sub_Периферия")],
    [InlineKeyboardButton(text="Сетевое оборудование", callback_data="sub_Сетевое оборудование")],
    [InlineKeyboardButton(text="Неттопы и Мини ПК", callback_data="sub_Неттопы и Мини ПК")],
    [InlineKeyboardButton(text="Майнеры и криптокошельки", callback_data="sub_Майнеры и криптокошельки")],
    [InlineKeyboardButton(text="Микрокомпьютеры и комплектующие", callback_data="sub_Микрокомпьютеры и комплектующие")],
    [InlineKeyboardButton(text="Промышленные компьютеры и серверы", callback_data="sub_Промышленные компьютеры и серверы")],
    [InlineKeyboardButton(text="Запчасти для мониторов", callback_data="sub_Запчасти для мониторов")],
    [InlineKeyboardButton(text="Программное обеспечение", callback_data="sub_Программное обеспечение")],
    [InlineKeyboardButton(text="Экшн-камеры", callback_data="sub_Экшн-камеры")],
    [InlineKeyboardButton(text="Аксессуары для экшн-камер", callback_data="sub_Аксессуары для экшн-камер")],
    [InlineKeyboardButton(text="Видеокамеры", callback_data="sub_Видеокамеры")],
    [InlineKeyboardButton(text="Зеркальные фотоаппараты", callback_data="sub_Зеркальные фотоаппараты")],
    [InlineKeyboardButton(text="Беззеркальные фотоаппараты", callback_data="sub_Беззеркальные фотоаппараты")],
    [InlineKeyboardButton(text="Объективы", callback_data="sub_Объективы")],
    [InlineKeyboardButton(text="Компактные фотоаппараты", callback_data="sub_Компактные фотоаппараты")],
    [InlineKeyboardButton(text="Фотоаппараты мгновенной печати", callback_data="sub_Фотоаппараты мгновенной печати")],
    [InlineKeyboardButton(text="Детские фотоаппараты и видеокамеры", callback_data="sub_Детские фотоаппараты и видеокамеры")],
    [InlineKeyboardButton(text="Аксессуары для фото и видеотехники", callback_data="sub_Аксессуары для фото и видеотехники")],
    [InlineKeyboardButton(text="Фотофоны", callback_data="sub_Фотофоны")],
    [InlineKeyboardButton(text="Студийное оборудование", callback_data="sub_Студийное оборудование")],
    [InlineKeyboardButton(text="Картриджи и фотопленка", callback_data="sub_Картриджи и фотопленка")],
    [InlineKeyboardButton(text="Компактные фотопринтеры", callback_data="sub_Компактные фотопринтеры")],
    [InlineKeyboardButton(text="Цифровые фоторамки", callback_data="sub_Цифровые фоторамки")],
    [InlineKeyboardButton(text="Прочие аксессуары", callback_data="sub_Прочие аксессуары")],
    [InlineKeyboardButton(text="Игровые приставки", callback_data="sub_Игровые приставки")],
    [InlineKeyboardButton(text="Офисная техника", callback_data="sub_Офисная техника")],
    [InlineKeyboardButton(text="МФУ", callback_data="sub_МФУ")],
    [InlineKeyboardButton(text="Принтеры", callback_data="sub_Принтеры")],
    [InlineKeyboardButton(text="Картриджи и расходные материалы", callback_data="sub_Картриджи и расходные материалы")],
    [InlineKeyboardButton(text="Оборудование для торговли", callback_data="sub_Оборудование для торговли")],
    [InlineKeyboardButton(text="3D-оборудование", callback_data="sub_3D-оборудование")],
    [InlineKeyboardButton(text="Запчасти и аксессуары", callback_data="sub_Запчасти и аксессуары")],
    [InlineKeyboardButton(text="Сканеры", callback_data="sub_Сканеры")],
    [InlineKeyboardButton(text="Копировальные аппараты", callback_data="sub_Копировальные аппараты")],
    [InlineKeyboardButton(text="Плоттеры", callback_data="sub_Плоттеры")],
    [InlineKeyboardButton(text="Ламинаторы", callback_data="sub_Ламинаторы")],
    [InlineKeyboardButton(text="Шредеры", callback_data="sub_Шредеры")],
    [InlineKeyboardButton(text="Брошюровщики", callback_data="sub_Брошюровщики")],
    [InlineKeyboardButton(text="Проекторы", callback_data="sub_Проекторы")],
    [InlineKeyboardButton(text="Квадрокоптеры", callback_data="sub_Квадрокоптеры")],
    [InlineKeyboardButton(text="Навигаторы", callback_data="sub_Навигаторы")],
    [InlineKeyboardButton(text="GPS-трекеры и GPS-маяки", callback_data="sub_GPS-трекеры и GPS-маяки")],
    [InlineKeyboardButton(text="Туристические навигаторы", callback_data="sub_Туристические навигаторы")],
    [InlineKeyboardButton(text="Автомобильные навигаторы", callback_data="sub_Автомобильные навигаторы")],
    [InlineKeyboardButton(text="Аксессуары и запчасти", callback_data="sub_Аксессуары и запчасти")],
    [InlineKeyboardButton(text="Умный дом", callback_data="sub_Умный дом")],
    [InlineKeyboardButton(text="Аксессуары для умного дома", callback_data="sub_Аксессуары для умного дома")],
    [InlineKeyboardButton(text="Выключатели и реле", callback_data="sub_Выключатели и реле")],
    [InlineKeyboardButton(text="Датчики и регуляторы", callback_data="sub_Датчики и регуляторы")],
    [InlineKeyboardButton(text="Комплекты умного дома", callback_data="sub_Комплекты умного дома")],
    [InlineKeyboardButton(text="Освещение", callback_data="sub_Освещение")],
    [InlineKeyboardButton(text="Розетки", callback_data="sub_Розетки")],
    [InlineKeyboardButton(text="Устройства безопасности", callback_data="sub_Устройства безопасности")],
    [InlineKeyboardButton(text="Управление умным домом", callback_data="sub_Управление умным домом")],
    [InlineKeyboardButton(text="Электрокарнизы", callback_data="sub_Электрокарнизы")],
    [InlineKeyboardButton(text="Телевизоры", callback_data="sub_Телевизоры")],
    [InlineKeyboardButton(text="ТВ-приставки и медиаплееры", callback_data="sub_ТВ-приставки и медиаплееры")],
    [InlineKeyboardButton(text="Кронштейны и крепления", callback_data="sub_Кронштейны и крепления")],
    [InlineKeyboardButton(text="Цифровое и спутниковое ТВ", callback_data="sub_Цифровое и спутниковое ТВ")],
    [InlineKeyboardButton(text="Онлайн-кинотеатры", callback_data="sub_Онлайн-кинотеатры")],
    [InlineKeyboardButton(text="Пульты ДУ", callback_data="sub_Пульты ДУ")],
    [InlineKeyboardButton(text="Антенны", callback_data="sub_Антенны")],
    [InlineKeyboardButton(text="DVD-плееры", callback_data="sub_DVD-плееры")],
    [InlineKeyboardButton(text="Проекционные экраны", callback_data="sub_Проекционные экраны")],
    [InlineKeyboardButton(text="Интерактивные панели и светодиодные экраны", callback_data="sub_Интерактивные панели и светодиодные экраны")],
    [InlineKeyboardButton(text="Электронные будильники", callback_data="sub_Электронные будильники")],
    [InlineKeyboardButton(text="Радиобудильники", callback_data="sub_Радиобудильники")],
    [InlineKeyboardButton(text="Камеры видеонаблюдения", callback_data="sub_Камеры видеонаблюдения")],
    [InlineKeyboardButton(text="Системы видеонаблюдения", callback_data="sub_Системы видеонаблюдения")],
    [InlineKeyboardButton(text="Автоматика для ворот", callback_data="sub_Автоматика для ворот")],
    [InlineKeyboardButton(text="Домофоны", callback_data="sub_Домофоны")],
    [InlineKeyboardButton(text="Охранное оборудование для дома и дачи", callback_data="sub_Охранное оборудование для дома и дачи")],
    [InlineKeyboardButton(text="Охранные системы для бизнеса", callback_data="sub_Охранные системы для бизнеса")],
    [InlineKeyboardButton(text="Скрытые камеры и персональные видеорегистраторы", callback_data="sub_Скрытые камеры и персональные видеорегистраторы")],
    [InlineKeyboardButton(text="Регистраторы", callback_data="sub_Регистраторы")],
    [InlineKeyboardButton(text="Муляжи камер видеонаблюдения", callback_data="sub_Муляжи камер видеонаблюдения")],
    [InlineKeyboardButton(text="Электронные замки", callback_data="sub_Электронные замки")],
    [InlineKeyboardButton(text="Электронные ключи и карты", callback_data="sub_Электронные ключи и карты")],
    [InlineKeyboardButton(text="Детекторы следящих устройств и антижучки", callback_data="sub_Детекторы следящих устройств и антижучки")],
    [InlineKeyboardButton(text="Установка видеонаблюдения", callback_data="sub_Установка видеонаблюдения")],
    [InlineKeyboardButton(text="Персональные сигнализации", callback_data="sub_Персональные сигнализации")],
    [InlineKeyboardButton(text="Кабели и переходники", callback_data="sub_Кабели и переходники")],
    [InlineKeyboardButton(text="Внешние аккумуляторы", callback_data="sub_Внешние аккумуляторы")],
    [InlineKeyboardButton(text="Батарейки", callback_data="sub_Батарейки")],
    [InlineKeyboardButton(text="Аккумуляторные батарейки", callback_data="sub_Аккумуляторные батарейки")],
    [InlineKeyboardButton(text="Зарядные устройства для аккумуляторов и тестеры батареек", callback_data="sub_Зарядные устройства для аккумуляторов и тестеры батареек")],
    [InlineKeyboardButton(text="Сетевые зарядные устройства", callback_data="sub_Сетевые зарядные устройства")],
    [InlineKeyboardButton(text="Беспроводные зарядные устройства", callback_data="sub_Беспроводные зарядные устройства")],
    [InlineKeyboardButton(text="Автомобильные зарядные устройства", callback_data="sub_Автомобильные зарядные устройства")],
    [InlineKeyboardButton(text="Робототехника", callback_data="sub_Робототехника")],
    [InlineKeyboardButton(text="Дополнительные гарантии", callback_data="sub_Дополнительные гарантии")],
    [InlineKeyboardButton(text="Чистящие средства и салфетки", callback_data="sub_Чистящие средства и салфетки")],
    [InlineKeyboardButton(text="Сетевые блоки питания", callback_data="sub_Сетевые блоки питания")]
])

@dp.message(F.text.in_({'/start', 'start'}))
async def start(message: Message):
    await message.answer("Добро пожаловать в SMANSHOP 👋\n\nВыберите раздел:", reply_markup=main_menu)

@dp.message(F.text == "🛍 Каталог")
async def show_catalog(message: Message):
    await message.answer("📦 Раздел: Электроника\nВыберите подкатегорию:", reply_markup=electronics_keyboard)

@dp.message(F.text == "🛒 Корзина")
async def show_cart(message: Message):
    await message.answer("🛒 Ваша корзина пуста.")

@dp.message(F.text == "👤 Профиль")
async def show_profile(message: Message):
    await message.answer(f"👤 Профиль:\nИмя: {message.from_user.full_name}\nID: {message.from_user.id}")

@dp.callback_query(F.data.startswith("sub_"))
async def subcategory_callback(callback: CallbackQuery):
    subcat = callback.data[4:]
    await callback.message.answer(f"📂 Подкатегория: <b>{subcat}</b>")

async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
