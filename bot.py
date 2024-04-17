import logging
import asyncio
from api import get_info
from aiogram.types import Message
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from config import TOKEN


logger = logging.getLogger(__name__)

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def start_cmd(message: types.Message):
    await message.answer(
        "Привет! Введите номер телефона, который Вы хотите проверить\n"
        "Например: 81234567890 или 71234567890"
    )


@dp.message(F.text)
async def number_info(message: Message):
    info = get_info(message.text)
    if not isinstance(info, Exception) and info:
        await message.answer(
            f'Телефон: {info["phone"]}\n'
            f'Тип: {info["phone_type"]}\n'
            f'Регион: {info["phone_region"]}\n'
            f'Страна: {info["country"]}\n'
            f'Код страны: {info["country_code"]}\n'
            f'Префикс страны: {info["country_prefix"]}\n'
            f'Оператор: {info["carrier"]}'
        )
    else:
        await message.answer('Некорректный ввод')


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
