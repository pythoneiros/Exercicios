# -*- coding:utf-8 -*_ 

__autor__ = 'https://github.com/Marlysson'

import os
arquivo = open(os.path.join('../','pessoas.csv'),'r')

dados = {
	'homens':0,
	'mulheres':0,
	'adultos':0,
	'adolesc':0
}

# Função para determinar a porcentagem de determinado tipo
def porcentagem(todo,chave):
	#todo: todo o dicionario com os dados
	#chave : chave do dicionario

	if chave in ['homens','mulheres']:
		return todo[chave] / float(( todo['homens'] + todo['mulheres'] ) ) * 100

	if chave in ['adolesc','adultos']:
		return todo[chave] / float( todo['adolesc'] + todo['adultos']) * 100


#passar pela primeira linha
arquivo.readline()

#Fazendo a estatística
for pessoa in arquivo:
	dados_pessoa = pessoa.strip().split(',')
	
	idade = int(dados_pessoa[1])
	sexo = dados_pessoa[2]

	if idade >= 18:
		dados['adultos'] += 1
	else:
		dados['adolesc'] += 1

	if sexo == 'M':
		dados['homens'] += 1
	else:
		dados['mulheres'] += 1


#Variáveis para formatar o CSV das estatísticas
colunas_csv = ['Tipo','Quantidade','Porcentagem']
linhas_csv = ['Homem','Mulher','Adultos','Adolescentes']
chaves_dict = ['homens','mulheres','adultos','adolesc']
dados_csv = []


# Interação para ir pegando os dados do csv e formatando
contador = 0
while contador < len(linhas_csv):
	dados_csv.append(colunas_csv)

	for chave in chaves_dict:
		linha = linhas_csv[contador]

		quantidade = str(dados[chave])

		porcent = '{:.1f}%'.format(porcentagem(dados,chave))
		contador += 1

		dados_csv.append([linha,quantidade,porcent])

# Abrindo o arquivo e usando a variável dados_csv resultante para inserir direto
with open('estatistica.csv','w') as estatistica:
	for dados in dados_csv:
		estatistica.write(','.join(dados)+'\n')