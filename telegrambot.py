import telebot
import horarioupdate
import jsonchecks

bot = telebot.TeleBot("922193347:AAHlV79ScsxvFN5IYMkZIXvruucjtJFrzVs")

@bot.message_handler(commands=["update"])
def send_update(message):
    horarioupdate.main()
    bot.send_message(chat_id=message.chat.id, text="Ficheiro *JSON* do horário atualizado.", parse_mode="Markdown")
    lastUpdate = jsonchecks.versionCheck()
    bot.send_message(chat_id=message.chat.id, text=lastUpdate, parse_mode="Markdown")


@bot.message_handler(commands=["get"])
def send_get(message):
    bot.send_message(chat_id=message.chat.id, text="Scanning...")
    finalValue = jsonchecks.main()
    bot.send_message(chat_id=message.chat.id, text=finalValue, parse_mode="Markdown")

bot.polling()