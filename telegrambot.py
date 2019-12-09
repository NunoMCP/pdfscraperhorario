import telebot
import horarioupdate
import jsonchecks

bot = telebot.TeleBot("922193347:AAHlV79ScsxvFN5IYMkZIXvruucjtJFrzVs")



@bot.message_handler(commands=["update"])
def send_update(message):
    bot.send_message(chat_id=message.chat.id, text="Updating...")
    horarioupdate.main()
    bot.send_message(chat_id=message.chat.id, text="Ficheiro JSON do horário atualizado.")

@bot.message_handler(commands=["get"])
def send_get(message):
    bot.send_message(chat_id=message.chat.id, text="Scanning...")
    finalValue = jsonchecks.main()
    bot.send_message(chat_id=message.chat.id, text=finalValue)

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()