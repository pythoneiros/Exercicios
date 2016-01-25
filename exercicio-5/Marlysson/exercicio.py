# -*- coding: utf8 -*-

'''
CORREÇÕES:

- Retirada da atribuição de lista, pois da forma que estava (a = b = []) estava associando
o valor de referência da lista "a" à lista "b" e assim qualquer mudança que ocorresse em
"a" ocorreria em "b".

Forma correta: a,b = [],[]

- Retirada de ";"" no final do print,pois em python não há ";" :p

'''

print "\n-----------------------------------------------------"
print "Separador de pares e ímpares\n"

numeros = raw_input("Insira alguns números separados por espaço para \n que eu possa separar os pares dos ímpares\n\n:-) -> ").split( )

pares,impares = [],[]

for numero in numeros:
	if int(numero)%2 == 0:
		pares.append(numero)
	else:
		impares.append(numero)

print "\nNumeros pares: %s"  %(pares)
print "Numeros impares: %s"  %(impares)