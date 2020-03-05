import telebot
import horarioupdate
import jsonchecks

bot = telebot.TeleBot("922193347:AAHlV79ScsxvFN5IYMkZIXvruucjtJFrzVs")

print("Running")

@bot.message_handler(commands=["update"])
def send_update(message):
    horarioupdate.main()
    bot.send_message(chat_id=message.chat.id, text="<b>Ficheiro JSON do horário atualizado.</b>", parse_mode="HTML")


@bot.message_handler(commands=["get"])
def send_get(message):
    bot.send_message(chat_id=message.chat.id, text="Scanning...")
    finalValue = jsonchecks.main()
    bot.send_message(chat_id=message.chat.id, text=finalValue, parse_mode='HTML')
    lastUpdate = jsonchecks.versionCheck()
    bot.send_message(chat_id=message.chat.id, text=lastUpdate, parse_mode='HTML')

bot.polling()