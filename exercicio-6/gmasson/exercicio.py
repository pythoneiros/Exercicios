#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2

t = urllib2.urlopen('https://www.youtube.com.br/').read()

# TAG
tags = t.split('<a')[1:]
tags = [ tag.split('</a>')[0].split('>',1)[1] for tag in tags ]

for i in tags:
  grava = open('links.txt','a')
  grava.write('\n'+i+'\n')

print 'OK'