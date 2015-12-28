#-*- coding: UTF-8 -*-

i = 0
vetor = []
vetor_par = []
vetor_impar = []

while i < 10:
    print 'Digite um número inteiro:'
    numero = raw_input()
    vetor.append(numero)
    i = i + 1

for num in vetor:
    if int(num) % 2 == 0:
        vetor_par.append(num)
    else:
        vetor_impar.append(num)

print "Números pares: %s" % (vetor_par)
print "Números ímpares: %s" % (vetor_impar)