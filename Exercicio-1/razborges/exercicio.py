# -*- coding: UTF-8 -*-

i = 0
vetor = []

while i < 5:
    print 'Digite um número inteiro:'
    numero = raw_input()
    vetor.append(numero)
    i+=1

for num in vetor:
    print num