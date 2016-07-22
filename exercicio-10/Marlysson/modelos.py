# -*- coding : utf-8 -*-

class Mensagem(object):
	def __init__(self,titulo,conteudo):

		from modelos import Data
		from datetime import date

		self.titulo = titulo.title()
		self.conteudo = conteudo.title()
		self.data = Data()

	def to_dict(self):

		atributos = ["titulo","conteudo","data"]
		dados = {}

		# Primeira forma : List Comprehension
		# dados = {atributo:getattr(self,atributo).formatado() \

		# 		if type(getattr(self,atributo)) == Data \
		# 		else getattr(self,atributo) \
		# 		for atributo in atributos}

		# Segunda forma : Foreach
		for atributo in atributos:

			valor_atributo = getattr(self,atributo)

			if type(valor_atributo) == Data:
				dados[atributo] = valor_atributo.formatado()
			else:
				dados[atributo] = valor_atributo

		return dados

	def __repr__(self):
		return "{},{}-{}".format(self.titulo,self.conteudo,self.data)

class Data(object):
	def __init__(self):
		from datetime import date
		self.date = date.today()

	def nativo(self):
		import datetime

		date_string = self.formatado()

		dia , mes , ano = map(int,(date_string.split("/")))

		return datetime.date(ano,mes,dia)

	def formatado(self):
		from datetime import datetime

		return datetime.strftime(self.date,str("%d/%m/%Y"))

	def __repr__(self):
		return "{}".format(self.formatado())


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