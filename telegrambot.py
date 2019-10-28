import telebot

import camelot

tables = camelot.read_pdf('horario.pdf')

bot = telebot.TeleBot("922193347:AAHlV79ScsxvFN5IYMkZIXvruucjtJFrzVs")

@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
    bot.reply_to(message, tables[0])

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()