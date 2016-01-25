# -*- coding: UTF-8 -*-

arquivo = open('diario.txt', 'a')

texto = ''

while texto != 'exit':
    print 'Digite o texto de hoje do diário:'
    texto = raw_input()
    if texto == 'exit':
        arquivo.close()
    else:
        arquivo.write(texto + '\n')