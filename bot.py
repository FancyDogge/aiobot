from aiogram import executor

from settings.dp import dp
from filters.private_chat import IsPrivate
from handlers.errors import error_handler
from handlers.users import start, admin, help, survey, echo
# from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands


async def on_startup(dispatcher):
    # Устанавливаем дефолтные команды
    await set_default_commands(dispatcher)

    # Уведомляет про запуск
    # await on_startup_notify(dispatcher)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)