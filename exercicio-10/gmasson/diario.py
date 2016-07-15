# -*- coding:utf-8 -*-

banco_de_dados = "bd.json"

while True:
  with open(caminho_chat,'a') as chat:

    texto = raw_input('Querido Diário: ')

    while not texto:
      print '\n Ei.. digite algo! \n'
      texto = raw_input('Querido Diário: ')

    if texto in comandos_sair:
      print '\n Você saiu do chat, sua conversa foi salva em: '+caminho_chat+' \n'
      break
    else:
      chat.write('  "'+texto+'" \n')
