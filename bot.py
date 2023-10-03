import os
import telebot
from telebot.types import Message
from func import fract
from dotenv import load_dotenv
load_dotenv()
API_TOKEN = os.getenv('API_TOKEN')

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, 'Привет. Присылай дробь!')


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message: Message):
    bot.send_message(message.chat.id, fract(message.text))


bot.infinity_polling()
