import os
import logging

from aiogram import Dispatcher
from dotenv import load_dotenv


load_dotenv()


async def on_startup_notify(dp: Dispatcher):
    for admin in list(os.getenv('ADMINS')):
        try:
            await dp.bot.send_message(admin, "Бот Запущен")

        except Exception as err:
            logging.exception(err)