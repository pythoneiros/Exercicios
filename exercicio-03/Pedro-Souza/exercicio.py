#!/usr/bin/env python
#_*_ coding:utf-8 _*_

from os import name, system

diario = open("diario.txt", "w")

def Main():
	Sistema()
	Verificar()

def Sistema():
	if name == 'nt':
	    system("cls")
	else:
		system("clear")

def Verificar():
	global diario
	while True:
		texto = raw_input("Digite o texto: ") 
		if texto == "exit":
			quit()
		else:
			diario.write(texto+"\n")
Main()