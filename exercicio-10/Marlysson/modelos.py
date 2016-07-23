# -*- coding : utf-8 -*-

class Mensagem(object):
	def __init__(self,titulo,conteudo):

		from datetime import date

		self.titulo = titulo.title()
		self.conteudo = conteudo.title()
		self.data = date.strftime(date.today(),str("%d/%m/%Y"))

	def to_dict(self):
		return self.__dict__

	def __repr__(self):
		return "{},{}-{}".format(self.titulo,self.conteudo,self.data)


class Json(object):

	def __init__(self,arquivo):
		self.arquivo = arquivo

	def carregar(self):
		import json

		try:

			with open(self.arquivo,"r") as arquivo:
				arquivo_encodado = json.load(arquivo)

		except:

			arquivo_encodado = json.loads('[]')

		return arquivo_encodado

	def gravar(self,objeto):
		import json

		arquivo_atual = self.carregar()

		arquivo_atual.append(objeto)		

		conteudo_pythonico = json.dumps(arquivo_atual)

		with open(self.arquivo,"w") as arquivo:
			arquivo.write(conteudo_pythonico)
		

	def __repr__(self):
		return "{}".format(self.arquivo)
