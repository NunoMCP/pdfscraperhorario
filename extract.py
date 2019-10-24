import camelot
tables = camelot.read_pdf('horario.pdf')
tables.export("horario.html", f="html", compress=True)