file = open('../lista_ips.txt')

ips_validos = []
ips_invalidos = []

for linha in file:
    linha = linha.strip().split('.')
    if len(linha) != 4:
        ips_invalidos.append(linha)
    else:
        try:
            ip = [int(i) for i in linha]
            if all([ip[0] <= 255, ip[1] <= 255, ip[2] <= 255, ip[3] <= 255]):
                ips_validos.append(linha)
            else:
                ips_invalidos.append(linha)
        except ValueError:
            print('ip inválido:' + '.'.join(linha))
file.close()
out = open('ips_validos.txt', 'w')
for i in ips_validos:
    out.write('.'.join(i) + '\n')
out.close()

out = open('ips_invalidos.txt', 'w')
for i in ips_invalidos:
    out.write('.'.join(i) + '\n')
out.close()
