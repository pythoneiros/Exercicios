# John Owl
# 29/06/2016

def printNumbers(numbers):
    for n in numbers:
        print(n, end=" ")


entradas = []

for i in range(10):
    n = input("Digite um número: ")
    entradas.append(n)

pares = []
impares = []

for e in entradas:
    if int(e) % 2 == 0:
        pares.append(e)
    else:
        impares.append(e)


print("Números pares: ", end="");
printNumbers(pares)
print("")
print("Números ímpares: ", end="");
printNumbers(impares)



