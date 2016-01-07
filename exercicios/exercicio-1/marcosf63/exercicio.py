#!/usr/bin/python
#-*- coding: utf-8 -*-

def lerImprimeVetor():
  """
   Ler um vetor de 5 números inteiros e imprime na tela.
  """
  try:
   vetor = [int(raw_input('Digite o número %d: ' % i)) for i in range(1,6)]

   for i in vetor:
     print i
  except ValueError:
    print "O valor digitado dever ser inteiro"

if __name__ == '__main__':
  lerImprimeVetor()
