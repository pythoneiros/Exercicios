#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Web Scraping que navega em um site e salva os links num arquivo links.txt
  -h, --help mostra mensagem de ajuda e sai

Uso: exercico.py <site>
  site - site alvo no formato http://www.sitealvo.com.br
"""
import urllib2
from bs4 import BeautifulSoup
import sys	

def pega_link():
  """
    Extrai os links de uma página
  """
  try:
    html_doc = urllib2.urlopen(sys.argv[1]).read()

    soup = BeautifulSoup(html_doc, 'html.parser')

    links =  soup.find_all('a')

    links_file = open('links.txt', 'a')
  
    for link in links:
      links_file.write(str(link.get('href')) + '\n')

   
    links_file.close()

  except IndexError:
    print __doc__
  except ValueError:
    print __doc__
   
if __name__ == '__main__':
  pega_link()
