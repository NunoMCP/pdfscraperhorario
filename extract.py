import camelot
tables = camelot.read_pdf('horario.pdf')
# tables.export("horario.html", f="html",)
print(tables[0][1])
print(tables[1])