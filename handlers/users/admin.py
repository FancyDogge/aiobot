from aiogram import types

from settings.dp import dp
from filters.private_chat import IsPrivate


@dp.message_handler(IsPrivate(), user_id=['415304682',], text='admin')
async def secret_admin_msg(message: types.Message):
    await message.answer('Это сообщение вызвано админом по ключевому слову')