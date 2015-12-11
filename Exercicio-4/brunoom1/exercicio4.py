#coding: utf-8

fp = open("./../pessoas.csv","r")

first_line = fp.readline().split(",")

totalH = 0
totalF = 0
totalMaiores = 0
totalMenores = 0
total = 0

maiorIdadePenal = 18

#retira primeira linha com os campos
while True:

	line = fp.readline()
	print line;
	if not line:
		break

	registro = line.replace("\n","").split(",")
	total = total + 1

	if registro[2] == 'M': 
		totalH = totalH + 1
	else:
		totalF = totalF + 1

	if int(registro[1]) >= maiorIdadePenal:
		totalMaiores = totalMaiores + 1
	else:
		totalMenores = totalMenores + 1 

pH = 100 * totalH / total
pF = 100 * totalF / total

festati = open("estatisticas.txt","w+")
festati.write("+----------------------------------+    \n")
festati.write("| Total de registros      | %5.0d  |    \n" % (total))
festati.write("| Porcentagem de Homes    | %5.2d%% |   \n" % (pH))
festati.write("| Porcentagem de Mulheres | %5.2d%% |   \n" % (pF))
festati.write("| Total de Maiores        | %5.0d  |    \n" % (totalMaiores))
festati.write("| Total de Menores        | %5.0d  |    \n" % (totalMenores))
festati.write("+----------------------------------+    \n")
festati.close();

