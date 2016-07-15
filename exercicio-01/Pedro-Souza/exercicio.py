#!/usr/bin/env python 
#_*_ coding:utf-8 _*_

from os import name, system

nmr = []

def Main():
	Sistema()
	PegarNum()
	Apresenta()

def Sistema():
	if name == 'nt':
		system("cls")
	else:
		system("clear")

def PegarNum():
	global nmr
	cnt = 0
	while cnt <= 4:
		nmr.append(int(input("Digite um numero inteiro: ")))
		cnt += 1

def Apresenta():
	global nmr
	for i in nmr:
		print(i)
Main()