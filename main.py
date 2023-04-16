import datetime
import random
from typing import Union
from translate import Translator
import os
from num2words import num2words
from telebot.types import Message
from src.create_bot import bot, menu_keyboard, answer_keyboard
import pandas as pd

translator = Translator(to_lang='kk')

@bot.message_handler(commands=['start'])
def start_message(message: Message):
    msg = bot.send_message(message.chat.id, 'Приятной тренировки! <3', reply_markup=menu_keyboard)
    bot.register_next_step_handler(msg, menu)


@bot.message_handler(content_types=['text'])
def menu(message: Message):
    if message.text == 'Маленькое':
        num = random.randint(10, 99)
        action = bot.send_message(message.chat.id, f'{num}', reply_markup=answer_keyboard)
        bot.register_next_step_handler(action, cardinal, num)
        write_log(message)
    elif message.text == 'Большое':
        num = random.randint(99, 9999)
        action = bot.send_message(message.chat.id, f'{num}', reply_markup=answer_keyboard)
        bot.register_next_step_handler(action, cardinal, num)
        write_log(message)


@bot.message_handler(content_types=['text'])
def cardinal(message: Message, num: Union[int, float]):
    reply = translator.translate(num2words(num))
    action = bot.send_message(message.chat.id, f'{reply}', reply_markup=menu_keyboard)
    bot.register_next_step_handler(action, menu)


def write_log(message: Message):
    new_log = pd.DataFrame({'create_dttm': [datetime.datetime.now()],
                            'user_id': [message.from_user.id],
                            'number': [message.text]
                            })
    path_to_csv = 'data/logs.csv'
    header = not os.path.exists(path_to_csv)
    new_log.to_csv(path_to_csv, mode='a', index=False, header=header)


if __name__ == '__main__':
    bot.infinity_polling()
