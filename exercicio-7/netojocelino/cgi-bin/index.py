#!/usr/bin/python
#-*- coding: utf-8 -*-
from wsgiref.handlers import CGIHandler

def show(env, resp):
    resp('200 OK', [('Content-Type', 'text/html')])
    response = frases('Frase 001', 'Frase 002', 'Frase 003', 'Frase 004')
    return response

def frases(*frase):
    vetor = []
    for arg in frase:
        vetor.append('<p>'+arg+'</p>')
    return vetor
if __name__ == '__main__':
    CGIHandler().run(show)
