import requests
import camelot

url = "http://my.istec.pt/wp-content/uploads/2019/11/3-MUL-D.pdf"
ficheiro = requests.get(url)
open(r"c:\Users\Nuno\Documents\GitHub\pdfscraperhorario\horario.pdf", "wb").write(ficheiro.content)

tables = camelot.read_pdf('horario.pdf')
tables[0].to_json('horario.json')


#adicionar timestamp para ver ultimo update ao source file