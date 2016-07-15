#-*- coding:utf-8-*_
quant_numeros = raw_input('Quantidade de números: ')

while not quant_numeros.isdigit():
	print 'Insira uma quantidade inteira.'
	quant_numeros = raw_input('Quantidade de números: ')

numeros = []

for i in range(int(quant_numeros)):
	numero = int(input('Número: '))
	numeros.append(numero)

'''
FILTER = aplica uma função em uma determinada lista,
no caso uma função anônima que dado um número como argumento
retorna o número do argumento caso a função seja True.
'''

pares = filter(lambda x: x%2 == 0,numeros)
impares = filter(lambda x: x%2 == 1,numeros)

print 'PARES:'
for i in pares:
	print i,

print '\n'

print 'ÍMPARES:'
for i in impares:
	print i,
