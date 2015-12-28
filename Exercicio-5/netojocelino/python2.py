#!/usr/bin/python
#-*- coding: utf-8 -*-
def corrigirSeparador():
    print "\n-----------------------------------------------------"
    print"Separador de pares e impares\n"
    numeros = raw_input("Insira alguns numeros separados por espaco para \n que eu possa separar os pares dos impares\n\n:-) -> ").split( )
    pares = []
    impares = []
    for numero in numeros:
        if int(numero)%2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)
    print "\nNumeros pares: %s"  %(pares)
    print "Numeros impares: %s"  %(impares);

if __name__ == '__main__':
    corrigirSeparador()
