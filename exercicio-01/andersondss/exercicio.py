# !/usr/bin/python
# -*- coding: utf-8 -*-
'''
@author: Anderson Santos
@email: anderson.bcc.uag@gmail.com
@github: https://github.com/andersondss
'''

vetor = []
while len(vetor) < 5:
    try:
        inteiro = input("Digite o {}º número inteiro: ".format(len(vetor)+1))
        vetor.append(inteiro)
    except NameError:
        pass
print vetor
