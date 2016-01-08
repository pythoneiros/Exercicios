#!/usr/bin/python
#-*- coding: utf-8 -*-

def diario():
    file = open("diario.txt", 'w')
    tmp = ""
    print("Para sair dê uma qubra de linha <enter> e digite 'exit'.")
    while(tmp != "exit"):
        tmp = input()
        if(tmp == "exit"):
            file.close()
        else:
            file.write(tmp + '\n')
	
if __name__ == '__main__':
    diario()
