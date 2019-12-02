import telebot
import camelot

tables = camelot.read_pdf('horario.pdf')

bot = telebot.TeleBot("922193347:AAHlV79ScsxvFN5IYMkZIXvruucjtJFrzVs")

@bot.message_handler(commands=["sexta"])
def send_sexta(message):
    bot.reply_to(message, "Rapaz, você se dá conta que é sexta feira quando você acorda com a sua pica com mais disposição que você mermão, quando sua pica tá em alta, a minha pica aqui tá parecendo um gol de futebol americano que quando vê uma buceta grita : TOUCHDOWN, TOUCHDOWN DISGRAÇA.Rapaz e pra piorar eu abro a porta do quarto e do de cara com a diarista olha pra ela, ela olho pra mim. Ela 45 anos de idade e eu a minha mãe vo libera hj não. Hoje é sexta feira chupa minha pica. Vem lustrar minha pica com óleo de peroba sua disgraça. Vem botar cheirinho no meu ovo aqui pra ele ficar tinino DISGRAÇA rapaz. ela olha e me respeite eu vou dá queixa de vc. Vai dá queixa na casa da desgraça. Vai dar queixa quando eu vou esfolar teu cu ai vc vai ter motivo pra dar queixa Maria da penha sua puta. Aí quando chega o final do dia ela quer pagamento. Pagamento é PIROCARD disgraça dentro da sua boca saía daqui sua puta. BORA FUDER CAMBADA DE DISGRAÇA. QUE HJ É SEXTA FEIRA PORRA")

@bot.message_handler(commands=["flamengo"])
def send_flamengo(message):
    audio = open("flamengo.mp3", "rb")
    bot.send_audio(message.chat.id, audio)

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()