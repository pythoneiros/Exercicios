#!/usr/bin/env python
#_*_ coding:utf-8 _*_

from os import system, name 

nmr, par, impa = [], [], []

def Main():
	Sistema()
	PegarNum()
	VerificarNum()
	Apresenta()

def Sistema():
	if name == 'nt':
		system("cls")
	else:
		system("clear")

def PegarNum():
	global nmr 
	ctn = 0 
	while ctn <= 19:
		nmr.append(int(input("Digite um numero: ")))
		ctn += 1

def VerificarNum():
	global nmr, impa, par
	for i in nmr:
		if (i%2) == 0:
			par.append(i)
		else:
			impa.append(i)

def Apresenta():
	global impa, par
	print "Numeros pares."
	for i in par:
		print i,
	print "\nNmeros impares"
	for i in impa:
		print i,

Main()