#!/usr/bin/python
#-*- coding: utf-8 -*-
def lerNums():
    vtr = []
    i = 0
    while(i < 5):
        vtr.append(int(input("Digite um numero: ")))
        i+=1
    for l in vtr:
        print("%d"%l)

if __name__ == '__main__':
    lerNums()
