import json
from time import localtime


def carregar_json():
    flag = False
    try:
        with open('diario.json', 'r') as file:
            arq_json = json.load(file)
            flag = True
    except FileNotFoundError:
        file =  open('diario.json', 'w')
        arq_json = json.loads('[]')

    return arq_json, flag

def escrever_json(lista):
    dic, flag = carregar_json()
    chave = '-'.join([str(i) for i in localtime()[:6]])
    if flag:
        dic[chave] = lista
    else:
        dic = {
            chave: lista
        }
    with open('diario.json', 'w') as file:
        json.dump(dic, file, indent=4)
    print('sucess')


if __name__ == '__main__':
    dic = {
        'titulo': input(),
        'msg': input()
    }

    escrever_json(dic)
    out = carregar_json()[0]

    print(out)

    
