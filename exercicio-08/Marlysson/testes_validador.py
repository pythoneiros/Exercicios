# -*- coding:utf8 -*-

import unittest
from modelo import IPValidator

class TestIPValidator(unittest.TestCase):

    def setUp(self):
        self.validator = IPValidator()
    
    def iterar_sobre_lista(self,ips):

        for ip in ips:
            validade = self.validator.validate(ip)

            if validade:
                self.assertTrue(validade)
            else:
                self.assertFalse(validade)
    
    def test_deve_retornar_se_octeto_esta_inconsistente_ou_nao(self):
        octeto_correto = self.validator.consistencia_octeto("0")
        octeto_correto2 = self.validator.consistencia_octeto("123")
        octeto_errado = self.validator.consistencia_octeto("01")

        self.assertTrue(octeto_correto)
        self.assertTrue(octeto_correto2)
        self.assertFalse(octeto_errado)

    def test_caracteres_precisam_ser_numeros(self):
        
        valido = self.validator.validate("1.1.1.1")
        valido = self.validator.validate("255.13.34.1")
        invalido = self.validator.validate("e.r.t.y")

        self.assertTrue(valido)
        self.assertTrue(valido)
        self.assertFalse(invalido)

    def test_numeros_devem_estar_no_intervalo_permitido_de_IP(self):

        valido = self.validator.validate("123.123.123.123")
        invalido = self.validator.validate("132.312.903.3")

        self.assertTrue(valido)
        self.assertFalse(invalido)

    def test_ip_passado_deve_ter_quatro_octetos(self):
        
        valido = self.validator.validate("123.123.123.123")
        invalido = self.validator.validate("123.123.123.123.123")

        self.assertTrue(valido)
        self.assertFalse(invalido)
    
    def test_caracteres_estranhos_devem_invalidar_o_ip(self):
        
        invalido = self.validator.validate("123.123.123.12..!")

        self.assertFalse(invalido)

    def test_arquivo_aberto_precisa_retornar_lista_de_strings(self):
        
        arquivo = open("../lista_ips.txt","r")
        
        self.assertEqual(list,type(arquivo.readlines()))
        arquivo.close()

    def test_lista_de_ips_vindas_de_arquivos_devem_ser_validadas(self):

        lista_ips = [ip.strip() for ip in open("../lista_ips.txt","r").readlines()]

        self.iterar_sobre_lista(lista_ips)


if __name__ == "__main__":
    unittest.main(warnings="ignore",verbosity=1)
