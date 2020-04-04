from model import Pessoa, calc_por


with open("../pessoas.csv", 'r') as file:
    arr = []
    next(file)
    for linha in file:
        nome, idade, sexo = linha.strip().split(',')
        arr.append(Pessoa(nome, idade, sexo))

    result = calc_por(arr)
    cols = [
        'Porcentagem de Homens',
        'Porcentagem de Mulheres',
        'Quantidade de maiores de idade',
        'Quantidade de menores de idade'
    ]
    with open("estatisticas.csv", 'w') as out_file:
        out_file.write('Análise estatistica do arquivo pessoas.csv\n')
        out_file.write(','.join(cols) + '\n')
        out_file.write(','.join(list(map(str, result))) + '\n')
