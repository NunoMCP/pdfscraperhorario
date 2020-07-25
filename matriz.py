from datetime import datetime
import json

def dayCheck():
    with open("horario.json") as file:
        data = json.load(file)
    for i in data[0]:
        for x in range(0, 5):
            if data[0][str(i)] == weekday_switch(x):
                current_date = str(i)
                print(weekday_switch(x))
                print(current_date)

def weekday_switch(argument):
    switch = {
        0: "Seg.",
        1: "Ter.",
        2: "Qua.",
        3: "Qui.",
        4: "Sex.",
    }
    return switch.get(argument)

def check(arg1, arg2):
    print(data[int(arg1)][str(arg2)])
