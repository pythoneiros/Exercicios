#-*- coding: utf-8 -*-

class ValidarIp():
    def __init__( self, ips ):
        print("Validar IPs IPv4.")
        for ip in ips:
            if( self.__validar__( ip ) is 200 ):
                print("IPv4 válido.")
        

    def __validar__( self, ip ):
        retorno = ip.split(".")
        if( len( retorno ) != 4 ):
            return -1
        else:
            for num in retorno:
                if not num.isdigit() and int(num) < 0 or int(num) > 255:
                    return -1
            self.insert( ip )
            return 200

    def insert (self, data ):
        fName="ips_validos.txt"
        try:
            file = open(fName, "r")
            if( data in file ):
                return
        except:
            open(fName,"w").close()
        file = open(fName, "a")
        file.write("%s\n"%data)
        file.close()
            
f = open("lista_ips.txt","r")
txt = f.read()
f.close()

ValidarIp( txt.split("\n") )
