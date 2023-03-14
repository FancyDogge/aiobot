from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from settings.dp import dp
from filters.private_chat import IsPrivate


@dp.message_handler(CommandStart(deep_link='Doggo'), IsPrivate())
async def bot_start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}, ты передал аргумент Doggo!")

# Для любого аргумента, кстати можно настроить регулярки
@dp.message_handler(CommandStart(), IsPrivate())
async def bot_start(message: types.Message):
# достаем аргумент из message и проверяем существует ли он
    arg = message.get_args()
    if arg:
        await message.answer(f"Привет, {message.from_user.full_name}, ты передал аргумент {arg}!")
    else:
        await message.answer(f"Привет, {message.from_user.full_name}, ты запустил бота без аргумента.")
