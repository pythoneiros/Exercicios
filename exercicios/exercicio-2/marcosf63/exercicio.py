#!/usr/bin python
#-*- coding: utf-8 -*-
"""
O programa pede algumas entradas de numero ao usuário
e imprime nas telas os numeros separados por tipo
Par ou impar.
"""

def pega_numero():
  '''
    Recebe um numero inteiro digitado pelo usuário
  '''
  return int(raw_input('Digite um numero inteiro ou Control + C para sair: '))

def impar(n):
  '''
    Se n for impar retorna Verdadeiro, senão retorna falso.
  '''
  return n % 2

if __name__ == '__main__':

  try:
    lista = []
    pares = []
    impares = []
    while True:
      lista.append(pega_numero())
  except ValueError:
    print "Digite só  número inteiros"
  except KeyboardInterrupt:
    for n in lista:
      if impar(n):
        impares.append(n)
      else:
        pares.append(n)
    print "\nPares: " + str(pares)
    print "Impares: " + str(impares)
    exit(0)
