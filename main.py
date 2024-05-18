from telebot.async_telebot import AsyncTeleBot
import datetime
import asyncio
import time
TOKEN = ''

bot= AsyncTeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start'])
async def func(message):
  await while True:
    current_datetime = datetime.datetime.now().hour
    if datetime.date.weekday() == 5 or datetime.date.weekday() == 6:
      if current_datetime == 10:
        bot.reply_to(message, "Сделаешь 20 отжиманий? nya~")
        time.sleep(20)
        bot.reply_to(message, "Сделаешь 20 приседаний? nya~")
      time.sleep(600)
      
    else:
      if current_datetime == 7:
        bot.reply_to(message, "Сделаешь 20 отжиманий? nya~")
        time.sleep(20)
        bot.reply_to(message, "Сделаешь 20 приседаний? nya~")
      time.sleep(600)
bot.infinity_polling()      
