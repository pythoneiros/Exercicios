# -*- coding: UTF-8 -*-
from models import *

arquivo = open('../pessoas.csv', 'r')
arquivo.readline()
vetor = []

for linha in arquivo:
    pessoa = linha
    pessoa = pessoa.split(',')
    perfil = Perfil(pessoa[0], pessoa[1], pessoa[2])
    vetor.append(perfil)

arquivo.close()
arquivo_destino = open('estatisticas.csv', 'a')

arquivo_destino.write('Resultados Estatísticos do arquivo lido:\n')
arquivo_destino.write(porcentagem_sexo(vetor))
arquivo_destino.write(conta_idade(vetor))

arquivo_destino.close()