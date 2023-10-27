import datetime

import telebot
import requests
import json

bot = telebot.TeleBot('6563652362:AAEOYpOGq5PJBb6Evcd0M5sqFHuTb9Hzr-c')
API = 'fbadafcb1eda3d2aff01e0ba3dd81f92'

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Hello!')

@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')

    if res.status_code == 200:
        data = json.loads(res.text)
        sunrise = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        bot.reply_to(message, f'Now Weather in {city} is:\n'
                              f'tempereture: {data["main"]["temp"]}\n'
                              f'sunrise is: {sunrise}')

    else:
        bot.reply_to(message, f'The city is specified incorrectly')


bot.polling(none_stop=True)