from datetime import datetime
import os
import json

def weekday_switch(argument):
    switch = {
        0: "Seg.",
        1: "Ter.",
        2: "Qua.",
        3: "Qui.",
        4: "Sex."
    }
    return switch.get(argument)

def versionCheck():
    timeStamp = datetime.fromtimestamp(os.path.getmtime("horario.json")).strftime("%Y-%m-%d %H:%M")
    return "A última atualização do ficheiro foi desde: *" + timeStamp + "*"

def main():
    with open("horario.json") as file:
        data = json.load(file)
    
    current_weekday = weekday_switch(datetime.now().weekday())


    for i in data[0]:
        if data[0][str(i)] == current_weekday:
            current_date = str(i)
            break
        else:
            current_date = 5


    current_hour = int(datetime.now().strftime("%H")) - 7
    current_room = int(current_date) + 1

    if current_date != 5:
        if current_hour >= 1 and current_hour <= 11:
            if data[current_hour][current_date] == "":
                finalString = "Não estás a ter aulas neste momento."
            else:
                finalString = "A aula é: *" + data[current_hour][current_date] + "* e a sala é: *" + data[current_hour][str(current_room)] + "*"
                print(data[current_hour][current_date])
                print(data[current_hour][str(current_room)])
        else:
            finalString = "Só há aulas das 8h às 18h."
        return finalString
    else:
        finalString = "Não há aulas ao fim de semana."
        return finalString