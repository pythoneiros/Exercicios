vetor = []

def escrever(texto):
    print(texto, end=" ")

for i in range(0, 5):
    n = int(input('\nDigite um número:\t'))
    vetor.append(n)

for num in vetor:
    escrever(num)

