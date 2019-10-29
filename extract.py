import json
import camelot
import pprint

tables = camelot.read_pdf('horario.pdf')
# tables.export("horario.html", f="html")

tables[0].to_json('foo.json')
# if sábado, use tables[1] for file e depois usar o algoritmo