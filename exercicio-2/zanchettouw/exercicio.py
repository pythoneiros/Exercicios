N = int(input("Informe a quantidade de numeros que serao analisados: "))
i = 0
vetorGeral = []

while N > i:
   vetorGeral.append(int(input("Digite um valor: ")))
   i = i + 1


vetorPar = []
vetorImpar = []

for x in vetorGeral:
   if x%2 == 0:
	vetorPar.append(x)
   else:
        vetorImpar.append(x)

print("Valores Pares: ")
for y in vetorPar:
    print(y)

print("Valores Impares: ")
for z in vetorImpar:
    print z
