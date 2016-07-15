# -*- coding:utf8 -*-

from modelo import IPValidator , WriterFile

arquivo_leitura = open("../lista_ips.txt","r")
ips_valids     = open("ips_validos.txt","w")
ips_invalids   = open("ips_invalidos.txt","w")

validator = IPValidator()

writer_valids = WriterFile(ips_valids)
writer_invalids = WriterFile(ips_invalids)

lista_ips = [ip.strip() for ip in arquivo_leitura.readlines()]

for ip in lista_ips:
	if validator.validate(ip):
		writer_valids.write(ip)
	else:
		writer_invalids.write(ip)

writer_valids.close()
writer_invalids.close()

print("Gravado com sucesso")