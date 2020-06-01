class Pessoa():
    def __init__(self, nome, idade, sexo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo


def calc_por(arr):
    total_m = 0
    total_f = 0
    id_maior = 0
    id_menor = 0
    for i in arr:
        if i.sexo == 'M':
            total_m += 1
        else:
            total_f += 1
        if int(i.idade) >= 18:
            id_maior += 1
        else:
            id_menor += 1
    return [
        total_m * 100 / len(arr),
        total_f * 100 / len(arr),
        id_maior,
        id_menor]
