#!/usr/bin/env python
# -*- coding: utf-8 -*-

arquivo = open("arquivo.txt","w")
linhas = []
linhas.append('LINHA  NUMERO 1\n')
linhas.append('LINHA  NUMERO 2\n')
linhas.append('LINHA  NUMERO 3\n')
linhas.append('LINHA  NUMERO 4\n')
linhas.append('LINHA  NUMERO 5\n')
linhas.append('LINHA  NUMERO 6\n')
linhas.append('LINHA  NUMERO 7\n')
linhas.append('LINHA  NUMERO 8\n')
arquivo.writelines(linhas)
arquivo.close()

