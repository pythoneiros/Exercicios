#!/usr/bin/python
#-*- coding: utf-8 -*-

def estatisticas():
    file = open('pessoas.csv', 'r')
    file.readline()
    linhas = []
    idades = []
    sexos = []
    old, young, masc, fem = 0, 0, 0, 0
    for ln in file:
        idades = int(str(str(ln)[:-1].split(',')[1]))
        sexos = str(str(ln)[:-1].split(',')[2])
        if (sexos == 'M'):
            masc += 1
        elif(sexos == 'F'):
            fem += 1
        if(idades > 17):
            old += 1
        elif(idades < 18):
            young += 1
    perMasc = (masc * ((masc + fem) / 100) * 100)
    perFem = (fem * ((masc + fem) / 100) * 100)
    perOld = (old * ((old + young) / 100) * 100)
    perYoung = (young * ((old + young) / 100) * 100)
    print("Temos %d%% de homens e %d%% de mulheres, sendo %d maiores de 18 anos e %d menores de 18 anos."%(perMasc, perFem, old, young))
    file.close()
    file = open('estatisticas.csv', 'w')
    file.write("Homens (%), Mulheres (%), Adultos (%), Jovens (%)\n")
    file.write("%d (%d%%), %d (%d%%), %d(%d%%), %d(%d%%)"%(masc,perMasc,fem,perFem,old,perOld,young,perYoung))
    file.close()
	
if __name__ == '__main__':
    estatisticas()
