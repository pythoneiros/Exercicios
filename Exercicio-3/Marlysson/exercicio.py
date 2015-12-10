#-*- coding:utf-8 -*-

while True:
	with open('diario.txt','a') as diario:

		texto = raw_input('Digite o texto: ')

		while not texto:
			print 'Digite algo..'
			texto = raw_input('Digite o texto: ')

		if texto == 'exit':
			print 'Concluído com sucesso.'
			break
		else:
			diario.write(texto+'\n')