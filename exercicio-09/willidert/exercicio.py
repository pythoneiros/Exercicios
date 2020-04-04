import sqlite3
import time


class Banco():
    def __init__(self):
        self.con = sqlite3.connect('exercicio.db')
        self.cursor = self.con.cursor()
        self.__criar()

    def __criar(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS diario (texto text, data text, hora text)")

    def inserir(self, texto, data, hora):
        self.cursor.execute("INSERT INTO diario (texto, data, hora) VALUES (?, ?, ?)", (texto, data, hora))
        self.con.commit()

    def read(self):
        consulta = self.cursor.execute("SELECT * FROM diario")
        return consulta.fetchall()


def get_data_hour():
    localtime = [str(i) for i in list(time.localtime())[:6]]
    data = '/'.join(localtime[:3])
    hora = ':'.join(localtime[3:])
    return data, hora


def exibir_registro(consulta):
    for registro in consulta:
        print(' '.join(registro))


if __name__ == '__main__':
    db = Banco()
    print('Hello, how are you? [exit p/ sair]')
    entrada = input()
    while entrada != 'exit':
        if entrada == 'ler':
            consulta = db.read()
            exibir_registro(consulta)
        else:
            data, hora = get_data_hour()
            db.inserir(entrada, data, hora)
        entrada = input()
    print('Até mais!')
