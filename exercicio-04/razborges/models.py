#-*- coding: UTF-8 -*-

class Perfil(object):
    def __init__(self, nome, idade, sexo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo

def porcentagem_sexo(vetor):
        soma_homens = 0
        soma_mulheres = 0

        for i in vetor:
            if 'M' in i.sexo:
                soma_homens+=1
            else:
                soma_mulheres+=1

        soma = soma_homens + soma_mulheres
        porcentagem_homens = 100 * soma_homens/soma
        porcentagem_mulheres = 100 * soma_mulheres/soma
        return "%s%% de homens \n%s%% de mulheres\n" % (porcentagem_homens, porcentagem_mulheres)

def conta_idade(vetor):
        maiores = 0
        menores = 0
        for i in vetor:
            if int(i.idade) < 18:
                menores+=1
            else:
                maiores+=1
        return '%s maiores de idade \n%s menores de idade\n' % (maiores, menores)