#!/usr/bin/env python
#_*_ coding:utf-8 _*_

feminino, masculino, maior, menor = 0, 0, 0, 0

a = open("pessoas.csv", "r").readlines()
for i in a:
    spl = i.split(',')
    if spl[1] == 'Idade':
    	pass
    elif int(spl[1]) >= 18:
    	maior += 1
    else:
    	menor += 1
    if spl[2] == "M\n":
    	masculino += 1
    else:
    	feminino += 1

porcentH = (100 * masculino) / (masculino + feminino)
porcentF = (100 * feminino) / (masculino+feminino)

festati = open("estatisticas.txt","w+")
festati.write("+----------------------------------+    \n")
festati.write("| Porcentagem de Homes    | %5.2d%% |   \n" % (porcentH))
festati.write("| Porcentagem de Mulheres | %5.2d%% |   \n" % (porcentF))
festati.write("| Total de Maiores        | %5.0d  |    \n" % (maior))
festati.write("| Total de Menores        | %5.0d  |    \n" % (menor))
festati.write("+----------------------------------+    \n")
festati.close();

