#coding: utf-8

diario_arquivo = "./diario.txt"
palavra_final = "exit"
ultima_palavra = ""

i = 0	# contar linha

while not palavra_final == ultima_palavra:
	linha = raw_input("%d> " % (i))

	#procurar ultima palavra da linha
	ultima_palavra = linha[len(linha) - len(palavra_final):len(linha)]

	if(ultima_palavra == palavra_final):
		#tirar a palavra final do texto
		linha = linha[0:len(linha) - len(palavra_final)]

	fp = open(diario_arquivo,"a+")
	fp.write(linha)
	fp.close();

	i = i + 1
