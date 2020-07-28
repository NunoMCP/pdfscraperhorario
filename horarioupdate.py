import requests
import camelot

def main():
    #obter ficheiro do servidor e fazer download para local
    print("downloading pdf")
    # horário Eng. Multi. 3º ano - 2ºsemestre
    url = "http://my.istec.pt/wp-content/uploads/2020/03/LEM-3-L.pdf"
    # horário Inf. 2º ano - 2º semestre
    # url = "http://my.istec.pt/wp-content/uploads/2020/03/LINF-2-L-1.pdf"
    # horário CTESP Redes e Sistemas Informáticos - 1º semestre
    # url = "http://my.istec.pt/wp-content/uploads/2020/06/Turma-A-2.pdf"
    ficheiro = requests.get(url)

    #abrir ficheiro local e escrever conteudos para variavel
    print("scanning pdf")
    open(r"horario.pdf", "wb").write(ficheiro.content)
    tables = camelot.read_pdf('horario.pdf')

    #converter conteudos do pdf para um ficheiro json
    print("writing json file")
    tables[0].to_json('horario.json')
    tables[1].to_json('horario_sabado.json')