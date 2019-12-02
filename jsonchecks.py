import json

with open("horario.json") as file:
    data = json.load(file)

print(data[1]["0"])

# segundo elemento da lista tem de ser string
# usar datetime e ifs(?) para criar variaveis com dia e hora