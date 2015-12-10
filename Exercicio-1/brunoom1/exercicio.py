#coding: utf-8

numeros = raw_input("Digite 5 numeros separados por espacos: ").split()

if len(numeros) == 5:
	for numero in numeros:
		print numero
else:
	print "Sao necessarios exatamente 5 numeros por favor."

