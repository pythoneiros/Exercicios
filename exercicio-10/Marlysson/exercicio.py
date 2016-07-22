#-*- coding:utf-8 -*-

from modelos import Mensagem, Json

print("--- Olá , Bem-vindo ao diário ---\n")


def menu():

	opcoes_menu = [
		(1,"Listar mensagens"),
		(2,"Inserir mensagem"),
		(3,"Sair do diário")
	]

	for opcao, acao in opcoes_menu:
		print(opcao,"-",acao)

while True:
	import sys

	menu()

	arquivo = Json("diario.json")

	opcao = str(input("O que deseja fazer? "))

	if opcao == "1":
		conteudo = arquivo.carregar()

		if not conteudo:
			print("\nAinda não há conteúdo\n")
		else:
			print("\nConteúdo do diário: \n")
			for mensagem in conteudo:
				print("Título: "+mensagem["titulo"])
				print("Conteúdo: "+mensagem["conteudo"])
				print("Data: "+mensagem["data"]+"\n")

	if opcao == "2":

		titulo = str(input("Título da mensagem: "))
		conteudo = str(input("Conteúdo da mensagem: "))

		while titulo == "" or conteudo == "":
			print("\nDigite novamente")

			titulo = str(input("Título da mensagem: "))
			conteudo = str(input("Conteúdo da mensagem: "))

		mensagem = Mensagem(titulo,conteudo)

		arquivo.gravar(mensagem.to_dict())

		print("Gravado com sucesso\n")

	if opcao == "3":
		print("Até mais :D ...")
		break