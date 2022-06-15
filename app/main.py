import os
from datetime import datetime, timedelta

import telebot
from telebot import types

from app.callback import callback_worker


TOKEN = os.getenv('TELEGRAM_TOKEN')

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def send_keyboard(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=2)  # наша клавиатура
    itembtn1 = types.KeyboardButton('Добавить дело в список') # создадим кнопку
    itembtn2 = types.KeyboardButton('Показать список дел')
    itembtn3 = types.KeyboardButton('Удалить дело из списка')
    itembtn4 = types.KeyboardButton("Удалить все дела из списка")
    itembtn5 = types.KeyboardButton('Другое')
    itembtn6 = types.KeyboardButton('Пока все!')
    keyboard.add(itembtn1, itembtn2) # добавим кнопки 1 и 2 на первый ряд
    keyboard.add(itembtn3, itembtn4, itembtn5, itembtn6) # добавим кнопки 3, 4, 5 на второй ряд
    # но если кнопок слишком много, они пойдут на след ряд автоматически
    d = {}
    d[''] = ...
    # пришлем это все сообщением и запишем выбранный вариант
    msg = bot.send_message(
        message.from_user.id,
        text="Привет, чем я могу тебе помочь?", 
        reply_markup=keyboard,
    )

    # отправим этот вариант в функцию, которая его обработает
    bot.register_next_step_handler(msg, callback_worker, bot=bot)


# @bot.message_handler(commands=['start', 'help'])
# def start(message):

#     bot.send_message(
#         chat_id=message.chat.id, 
#         text='Привет, пользователь!',
#     )

# @bot.message_handler(regexp='^\d{8}$')
# def hand_date(message):

#     date_format = datetime.strptime(message.text, '%Y%m%d')

#     bot.send_message(
#         chat_id=message.chat.id,
#         text=str(date_format.date() + timedelta(days=2))
#     )


# @bot.message_handler(content_types=['text'])
# def reply_same(message):

#     bot.send_message(
#         chat_id=message.chat.id,
#         text=message.text,
#     )


bot.polling(none_stop=True)
