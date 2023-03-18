from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher import FSMContext

from settings.dp import dp
from states.survey_state import Test


# default state = None
@dp.message_handler(Command('survey'))
async def enter_survey(message: types.Message):
    await message.answer('Опрос начинается.\n\n'
                         'Вопрос 1.\n'
                         'Есть 2 стула...')
    
    # coroutine, poetomu await
    await Test.q1.set()

# тут стейт мы уже задаем
@dp.message_handler(state=Test.q1)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text

    # сохраняем введенные данные в словаре стейта с ключом answer1
    await state.update_data(answer1=answer)

    await message.answer('Вопрос 2.\n'
                         'Есть 3 стула...')
    
    # await Test.q2.set() - одно и то же, мы можем захардкодить некст стейт, так и просто сказать переходить
    # к следующему попорядку. Еще есть .previous, для возврата к предыдущему состоянию
    await Test.next()

@dp.message_handler(state=Test.q2)
async def answer_q2(message: types.Message, state: FSMContext):
    # достаем сохраненные в машине состояний ответы
    data = await state.get_data()
    answer1 = data['answer1']
    answer2 = message.text

    await state.update_data(answer2=answer2)
    await message.answer('Спасибо, что прошли опрос!\n'
                         'Вот ваши ответы:')
    await message.answer('Ответ 1:\n'
                         f'{answer1}')
    await message.answer('Ответ 2:\n'
                         f'{answer1}')
    
    # чтобы юзер не оставался в стейте ответа на 2ой вопрос, нужно его сбросить
    await state.finish()
    # await state.reset_state() - same
    # await state.reset_state(with_data=False) - если нужно сбросить состояние, но сохранить данные