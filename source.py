import os
import telebot
import logging
from telebot import types
import random as rd

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)

game = ['Mobile Legends', 'Free Fire', 'Genshin Impact', 'Final Fantasy', 'Harvest Moon']

@bot.message_handler(commands=['mulai'])
def send_welcome(message):
    bot.reply_to(message, "Masukan nama anda :")

@bot.message_handler(func=lambda message:True)
def echo_all(message):
    bot.reply_to(message, "Hai, " + message.text)
    bot.reply_to(message, "Pasti game kesukaan kamu : " + rd.choice(game))

@bot.message_handler(commands=['reset'])
def handle_reset_command(message):
    bot.reply_to(message, "Reset berhasil!")

bot.infinity_polling()


