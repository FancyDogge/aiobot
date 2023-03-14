from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

from settings.dp import dp


class IsPrivate(BoundFilter):
    """
    класс, выполняющий проверку приватен ли чат
    """
    async def check(self, message: types.Message) -> bool:
        return message.chat.type == types.ChatType.PRIVATE
    
dp.filters_factory.bind(IsPrivate)