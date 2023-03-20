import logging

from aiogram import types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware

from settings.config import banned_users


class TestMdlw(BaseMiddleware):
    async def on_pre_process_update(self, update: types.Update, data: dict):
        logging.info('Апдейт:')
        logging.info('1) pre process update')
        logging.info('Следующая точка: Process Update')
        data['middleware_data'] = 'Эти данные дойдут до on_post_process_update'
        if update.message:
            user = update.message.from_user.id
        elif update.callback_query:
            user = update.callback_query.from_user.id
        else:
            return
        
        if user in banned_users:
            raise CancelHandler()
        
    async def on_post_process_update(self, update: types.Update, data: dict):
        logging.info(f'2) process update: {data}')
        logging.info('Следующая точка: Pre Process Msg')

    async def on_pre_process_message(self, update: types.Update, data: dict):
        logging.info(f'3) Pre Process Msg: {data}')
        logging.info('Следующая точка: Filters, Process Msg')
        data['middleware_data'] = 'Эти данные дойдут до on_process_message'