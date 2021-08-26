# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 09:22:18 2021

@author: franc
"""

lista1=[]
lista2=[]
lista=["R1","R2","R3", "S1", "S3","L1"]
for i in lista:
    if "R" in i: 
        lista1.append(i)
    print (lista1)
for i in lista:
    if "S" in i: 
        lista2.append(i)
    print (lista2)