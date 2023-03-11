import os
import logging

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types


load_dotenv()

# logging to see any errors or messages from your bot
logging.basicConfig(level=logging.INFO)

# Initialize the Bot and Dispatcher objects
bot = Bot(token=os.getenv('BOT_TOKEN'))
dp = Dispatcher(bot)


# A command handler that will respond to the /start command
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply("Yo mate!")


# Starts the bot
if __name__ == '__main__':
    executor.start_polling(dp)