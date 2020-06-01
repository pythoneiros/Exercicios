#!/usr/bin/python
# -*- coding: utf-8 -*-

from wsgiref.handlers import CGIHandler


def app(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    reposta = get_html()
    return reposta


def get_html():
    arr = [
        'Amor Proprio',
        'Amei uma pessoa que se foi',
        'Chorei por alguém especial demais',
        'Os dias que se seguiram, foram tristes',
        'Mas assim teve que ser para que ela pudesse sorrir.'
    ]

    return ['<p>' + i + '</p>' for i in arr]


CGIHandler().run(app)
