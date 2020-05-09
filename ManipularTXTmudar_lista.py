#!/usr/bin/env python
# -*- coding: utf-8 -*-

linha = 5
texto = 'MUDAR LINHA CINCO\n'
linhaparty = linha-1

#Salva todos os dados dentro dee uma lista
with open('arquivo.txt', 'r') as arquivo:
    linhas = arquivo.readlines() #Crir lista
    linhas[linhaparty] = texto   #Salvar novo texto posição lista

#Reescreve  a lista anterior
    with open('arquivo.txt', 'w') as arquivo:
        arquivo.writelines(linhas) #reescreve todo texto
        
