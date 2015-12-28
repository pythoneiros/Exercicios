#!/usr/bin/python
#-*- coding: utf-8 -*-

def webScraping():
    import urllib.request
    html = urllib.request.urlopen('http://jocelinoalves.url.ph').read()
    i, tag = 0, "href="
    tam = len(tag)
    arq = open('links.txt', 'w')
    print('Carregando...')
    while (i < len(html)) and (html[i:i+len('</html>')] != "</html>"):
        if(html[i:i+len('</html>')] != '</html>'):
            while (str(html)[i:i+tam] != tag) and (html[i:i+len('</html>')] != '</html>'):
                i += 1
            i += len(tag)+1
            asp = i
            while (str(html)[asp] != '"') and (str(html)[asp] != '"') and (html[i:i+len('</html>')] != '</html>'):
                asp += 1
            tmp = str(html)[i:asp]+ '\n'
            arq.write(tmp)
            #
    arq.close()
    print('Done.')
    
if __name__ == '__main__':
    webScraping()
