#!/usr/bin/python
#-*- coding: utf-8 -*-

def lerNums():
    p = int(input("Quantidade de numeros a serem lidos: "))
    vtr = []
    par, imp = "", ""
    i = 0
    while(i < p):
        vtr.append(int(input("Digite um numero: ")))
	i+=1
    for l in vtr:
	if((l%2) == 0):
	    par += str(l) + " "
	else:
	    imp += str(l) + " "
    print("pares: %s, impares: %s."%(par,imp))
	
if __name__ == '__main__':
    lerNums()
