#!/usr/bin/python
#coding: utf-8

print "\n-----------------------------------------------------"
print "\nExercicio 2"
print "Separador de pares e ímpares\n"

numeros = raw_input("Entre com alguns números separados por espaço para \nque eu possa separar os pares dos ímpares\n\n:-) -> ").split( )

# separa numeros
pares = []
impares = []

for numero in numeros:
	if int(numero)%2 == 0:
		pares.append(numero)
	else:
		impares.append(numero)

print "\nNumeros pares: %s"  %(pares);
print "Numeros impares: %s"  %(impares);
