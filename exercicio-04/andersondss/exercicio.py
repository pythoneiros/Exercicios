# !/usr/bin/python
# -*- coding: utf-8 -*-
'''
@author: Anderson Santos
@email: anderson.bcc.uag@gmail.com
@github: https://github.com/andersondss
'''

maiores_idade = 0
menores_idade = 0
output_sexo = {"M": 0, "F": 0}
with open('../pessoas.csv', 'r') as diario:
    lines = diario.readlines()[1:]
for line in lines:
    nome, idade, sexo = line.rstrip().split(",")
    output_sexo[sexo] += 1
    if int(idade) >= 18:
        maiores_idade += 1
    else:
        menores_idade += 1

espaco_amostral = 100/float(len(lines))
string_save = """
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    %                                        %
    %    Porcentagem de homens: {0}%        %
    %    Porcentagem de mulheres: {1}%      %
    %    Quantidade de maiores de Idade: {2}   %
    %    Quantidade de menores de idade: {3}   %
    %                                        %
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
""".format(output_sexo["M"]*espaco_amostral, output_sexo["F"]*espaco_amostral,
           maiores_idade, menores_idade)

with open("estatísticas.txt", "w") as estatistica:
    estatistica.write(string_save)
