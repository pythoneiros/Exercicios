# !/usr/bin/python
# -*- coding: utf-8 -*-
'''
@author: Anderson Santos
@email: anderson.bcc.uag@gmail.com
@github: https://github.com/andersondss
'''

with open('diario.txt', 'a') as diario:
    while True:
        texto = raw_input('Digite o texto: ')
        if texto != 'exit':
            diario.write(texto)
            continue
        break
