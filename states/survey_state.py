from aiogram.dispatcher.filters.state import StatesGroup, State


class Test(StatesGroup):
    """
    q1 и q1 будут нашими состояниями и машина состояний запомнит выбор,
    на котором юзер остановился и введенные им данные
    """
    q1 = State()
    q2 = State()