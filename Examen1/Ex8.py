# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 00:22:02 2021

@author: franc
"""

lst = [[x for x in range(3)] for y in range(3)]   #EL simbolo de los corchetes separa 2 componentes para esta función
for r in range(3):
    for c in range(3):
        if lst [r][c] % 2 != 0:
            print("#")


