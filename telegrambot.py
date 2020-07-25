import os
from datetime import datetime
import telebot
import horarioupdate
import jsonchecks

# definir variável com conteudos do api do telegram bot
bot = telebot.TeleBot("1072655287:AAHomNuEsOeevGKkpmsQ0A8iq7WzA0SD48A")

#polling para comando update, realiza horarioupdate.main() e output mensagem de sucesso
@bot.message_handler(commands=["update"])
def send_update(message):
    horarioupdate.main()
    bot.send_message(chat_id=message.chat.id, text="<b>Ficheiro JSON do horário atualizado.</b>", parse_mode="HTML")

#polling para comando get, realiza jsonchecks.main() e versioncheck() e dá output ao utilizador
@bot.message_handler(commands=["obter"])
def send_get(message):
    finalValue = jsonchecks.main()
    bot.send_message(chat_id=message.chat.id, text=finalValue, parse_mode='HTML')
    bot.send_message(chat_id=message.chat.id, text="A última atualização do ficheiro foi desde: <b>" + datetime.fromtimestamp(os.path.getmtime("horario.json")).strftime("%Y-%m-%d %H:%M") + "</b>", parse_mode='HTML')

#este comando é para ficar atento aos inputs do utilizador
print("Running")
bot.polling()