# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 08:05:59 2025

@author: asgun
"""

import random

N = 23

aniversarios = [random.randint(1, 365) for _ in range(N)]

aniversarios.sort()
print(aniversarios)

#Verifica repeticoes
for i in range(N-1):
    if aniversarios[i]==aniversarios[i+1]:
        print("Repetição no dia: ", aniversarios[i])
        break

