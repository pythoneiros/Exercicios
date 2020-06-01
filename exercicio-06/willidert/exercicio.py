import urllib.request as rq
import re

url = 'http://info.cern.ch'
padrao = '<a.*href="([http: https:]?[\/\/]?.*?)"'

html = rq.urlopen(url).read().decode('UTF-8')
match = re.findall(padrao, html)
file = open('links.txt', 'w')
for i in match:
    file.write(i + '\n')
file.close()
print('Sucess')
