# -*- coding:utf-8 -*-

import sqlite3
from time import gmtime, strftime

conexao = sqlite3.connect("exercicio.db")

def setup():
	conexao.execute("CREATE TABLE IF NOT EXISTS diario (texto text, data text, hora text );")
	conexao.commit()

def diario():
	texto = raw_input('Querido Diário: ')
	data = strftime("%d-%m-%Y", gmtime())
	hora = strftime("%H:%M:%S", gmtime())
	try:
		conexao.execute("INSERT INTO diario VALUES ('{}', '{}', '{}');".format(texto, data, hora))
		conexao.commit()
		print("Frase salva com sucesso!")
	except Exception as erro:
		print("Erro: {}".format(erro))

if __name__ == '__main__':
	setup()
	diario()
	conexao.close()