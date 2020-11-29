import telebot
from telebot import types
import os

#Настройки бота

TOKEN=os.environ['TOKEN']
bot = telebot.TeleBot(TOKEN)
GROUP_SCAN_ID=os.environ['GROUP_SCAN_ID']
GROUP_FRW_ID=os.environ['GROUP_FRW_ID']
SEARCH_LIST=eval(os.environ['SEARCH_LIST'])
HELLO_MSG=os.environ['HELLO_MSG']

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, HELLO_MSG)

@bot.message_handler(commands=['id'])
def id(message):
    bot.reply_to(message,message.chat.id)

@bot.message_handler(func=lambda message: True, content_types=['text'])
def all_messages(message):
    if str(message.chat.id) == str(GROUP_SCAN_ID):
        for search in SEARCH_LIST:
            if search.upper() in message.text.upper():
                bot.forward_message(GROUP_FRW_ID, message.chat.id, message.message_id)

if __name__ == '__main__':
    try:
        bot.polling(none_stop=True)
    except:
        print('ошибка')