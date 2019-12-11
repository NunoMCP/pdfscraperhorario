import requests
import camelot

def main():
    print("downloading pdf")
    url = "http://my.istec.pt/wp-content/uploads/2019/11/3-MUL-D.pdf"
    ficheiro = requests.get(url)

    print("scanning pdf")
    open(r"c:\Users\Nuno\Documents\GitHub\pdfscraperhorario\horario.pdf", "wb").write(ficheiro.content)
    tables = camelot.read_pdf('horario.pdf')

    print("writing json file")
    tables[0].to_json('horario.json')
    
#adicionar timestamp para ver ultimo update ao source file