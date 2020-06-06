import telebot
import horarioupdate
import jsonchecks

# definir variável com conteudos do api do telegram bot
bot = telebot.TeleBot("922193347:AAHlV79ScsxvFN5IYMkZIXvruucjtJFrzVs")

#user logs
print("Running")

#polling para comando update, realiza horarioupdate.main() e output mensagem de sucesso
@bot.message_handler(commands=["update"])
def send_update(message):
    horarioupdate.main()
    bot.send_message(chat_id=message.chat.id, text="<b>Ficheiro JSON do horário atualizado.</b>", parse_mode="HTML")


#polling para comando get, realiza jsonchecks.main() e versioncheck() e dá output ao utilizador
@bot.message_handler(commands=["get"])
def send_get(message):
    bot.send_message(chat_id=message.chat.id, text="Scanning...")
    finalValue = jsonchecks.main()
    bot.send_message(chat_id=message.chat.id, text=finalValue, parse_mode='HTML')
    lastUpdate = jsonchecks.versionCheck()
    bot.send_message(chat_id=message.chat.id, text=lastUpdate, parse_mode='HTML')

#este comando é para ficar atento aos inputs do utilizador
bot.polling()