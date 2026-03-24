from aiogram.fsm.state import State, StatesGroup

class RegistrationProfile(StatesGroup):
    waiting_name = State('waiting_name')
    # waiting_email = State('waiting_email')
    waiting_age = State('waiting_age')
    waiting_city = State('waiting_city')