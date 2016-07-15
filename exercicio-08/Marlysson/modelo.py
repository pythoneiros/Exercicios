# -*- coding : utf8 -*-

class IPValidator(object):
	
	def quantidade_octetos(self,ip):
		if len(ip) != 4:
			return False
		return True

	def valida_intervalo(self,octeto):
		if ( int(octeto) < 0) or ( int(octeto) > 255 ):
			return False
		return True

	def consistencia_octeto(self,octeto):
		if ( octeto.startswith("0") and len(octeto) > 1 ):
			return False
		return True

	def validate(self, ip):
		octetos = ip.split(".")
		
		if self.quantidade_octetos(octetos):
			for octeto in octetos:
				if not octeto.isdigit() or not self.consistencia_octeto(octeto) or not self.valida_intervalo(octeto):
					return False
			return True

		return False
			

class WriterFile(object):
	def __init__(self,file):
		self.target = file

	def write(self,ip):
		self.target.write(ip+"\n")

	def close(self):
		self.target.close()
