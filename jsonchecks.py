from datetime import datetime
import os
import json

#switch para obter dias da semana correspondentes
def weekday_switch(argument):
    switch = {
        0: "Seg.",
        1: "Ter.",
        2: "Qua.",
        3: "Qui.",
        4: "Sex.",
    }
    return switch.get(argument)
#
def main():
    #verifica se é sabado ou nao e abre o ficheiro correspondente
    if datetime.now().weekday() == 5:
        current_date = 5
        with open("horario_sabado.json") as file:
            data = json.load(file)
    else:
        with open("horario.json") as file:
            data = json.load(file)
        for i in data[0]:
            if data[0][str(i)] == weekday_switch(datetime.now().weekday()):
                current_date = str(i)
                break
            else:
                current_date = 6

    #verificar se é sábado
    if current_date == 5:
        current_hour = int(datetime.now().strftime("%H")) - 7
        if current_hour >= 1 and current_hour <= 7:
            current_date = "1"
            current_room = "2"
            if data[current_hour][current_date] == "":
                finalString = "Não estás a ter aulas neste momento."
                return finalString
            else:
                finalString = "A aula é: <b>" + data[current_hour][current_date] + "</b> e a sala é: <b>" + data[current_hour][str(current_room)] + "</b>"
                return finalString
        else:
            finalString = "Só há aulas das 8h às 15h aos sábados."
            return finalString
    #verificar se dia da semana 
    elif current_date != 6:
        current_hour = int(datetime.now().strftime("%H")) - 7
        if current_hour >= 1 and current_hour <= 10:
            current_room = int(current_date) + 1
            if data[current_hour][current_date] == "":
                finalString = "Não estás a ter aulas neste momento."
            else:
                finalString = "A aula é: <b>" + data[current_hour][current_date] + "</b> e a sala é: <b>" + data[current_hour][str(current_room)] + "</b>"

        else:
            finalString = "Só há aulas das 8h às 18h em dias de semana."
        return finalString
    else:
        finalString = "Não há aulas ao domingo."
        return finalString