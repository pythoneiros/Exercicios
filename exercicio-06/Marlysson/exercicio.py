from HTMLParser import HTMLParser
import urllib

class Scraping(HTMLParser):

	def handle_starttag(self,tag,attrs):
		hrefs = []

		if tag == 'a':
			for atributo,valor in attrs:
				if atributo == 'href' and valor != "#":
					hrefs.append(valor)

		with open('links.txt','a') as links:
			for link in hrefs:
				links.write(link+'\n')


scraping = Scraping()
url = urllib.urlopen('http://www.facebook.com').read()
print scraping.feed(url)

