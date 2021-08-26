# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 22:58:08 2021

@author: franc
"""

dct = {}
dct["1"] = (1,2)
dct["2"] = (2,1)
for x in dct.keys():
    print(dct[x][1],end="")
    
# llega al infinito