from aiogram import types
from misc import dp, bot


ADMIN_ID_1 = 494588959 #Cаня
ADMIN_ID_2 = 44520977 #Коля
ADMIN_ID_3 = 1489359560 #Менеджер

ADMIN_ID =[ADMIN_ID_1,ADMIN_ID_2,ADMIN_ID_3]

@dp.message_handler(commands=['admin'])
async def admin_ka(message: types.Message):
    id = message.from_user.id
    if id in ADMIN_ID:
        markup = types.InlineKeyboardMarkup()
        bat_a = types.InlineKeyboardButton(text='Анализ', callback_data='admin_1')
        bat_b = types.InlineKeyboardButton(text='Участники', callback_data='admin_2')

        markup.add(bat_a, bat_b)
        await bot.send_message(message.chat.id,'Добро пожаловать в Админ панель',reply_markup=markup)
