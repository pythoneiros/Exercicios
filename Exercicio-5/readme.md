# Exercício 5

Encontre o problema no exercício abaixo e corrija-o

```python
print "\n-----------------------------------------------------"
print "Separador de pares e ímpares\n"

numeros = raw_input("Insira alguns números separados por espaço para \n que eu possa separar os pares dos ímpares\n\n:-) -> ").split( )

pares = impares = []

for numero in numeros:
	if int(numero)%2 == 0:
		pares.append(numero)
	else:
		impares.append(numero)

print "\nNumeros pares: %s"  %(pares);
print "Numeros impares: %s"  %(impares);

```


## Estrutura 

```
  /Exercicio-5
    /SeuNickGitHub (Pasta com seu username do GitHub)
      - exercicio.py
```
