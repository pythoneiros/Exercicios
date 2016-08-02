# !/usr/bin/python
# -*- coding: utf-8 -*-
'''
@author: Anderson Santos
@email: anderson.bcc.uag@gmail.com
@github: https://github.com/andersondss
'''

n_inteiros = 5
pares = []
impares = []
# Obtendo os inteiros
while len(pares) + len(impares) < n_inteiros:
    try:
        inteiro = input("Digite o {}º número inteiro: ".format(len(pares) +
                                                               len(impares)+1))
    except NameError:
        continue
    if inteiro % 2:
        impares.append(inteiro)
    else:
        pares.append(inteiro)

print "Pares: {}\n".format(pares.__str__())
print "Impares: {}\n".format(impares)
