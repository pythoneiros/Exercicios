#!/usr/bin/python
#-*- coding: utf-8 -*-

def lerImprimeVetor():
  """
   Ler um vetor de 5 números inteiros e imprime na tela.
  """
  vetor = [raw_input('Digite o número %d: ' % i) for i in range(1,6)]

  for i in vetor:
    print i

if __name__ == '__main__':
  lerImprimeVetor()
