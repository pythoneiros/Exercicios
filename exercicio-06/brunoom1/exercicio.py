import httplib
import HTMLParser
import os

class HTMLParser(HTMLParser.HTMLParser):

	def save(self, file):
		self.file = file

		# cria um novo arquivo
		fp = open(self.file, "w")
		if fp:
			fp.close()


	def handle_starttag(self, tag, attrs):
		self.links = []

		if tag == "a":
			fp = open(self.file, "a")
			if fp:
				fp.write(attrs[0][1] + "\n")
				fp.close()


class Scraping:
	def __init__(self, host):
		self.host = host
		self.content = ""
		self.htmlParser = HTMLParser()

	def save(self, file):
		self.htmlParser.save(file)

	def scan(self, url):
		try:
			httpConn = httplib.HTTPConnection(self.host)
			httpConn.request("GET", url)
			response = httpConn.getresponse()
	
			if response:
				self.content = response.read()
				self.htmlParser.feed(self.content)

		except httplib.HTTPException, e:
			print "ERRO: " + e.message



if __name__ == "__main__":

	# create scrapping 
	scrap = Scraping("guia11.com")

	# define file for save links
	scrap.save(os.curdir + "/links.txt")

	# scrap path
	scrap.scan("/")