from telebot import TeleBot, types
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from data.bot_token import TOKEN

bot = TeleBot(TOKEN)

menu_keyboard = ReplyKeyboardMarkup(True, False)
button1 = KeyboardButton('Маленькое')
button2 = KeyboardButton('Большое')
menu_keyboard.row(button1, button2)

answer_keyboard = ReplyKeyboardMarkup(True, False).add(KeyboardButton('Ответ'))
