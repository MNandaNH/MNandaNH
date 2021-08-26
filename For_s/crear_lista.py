# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 09:18:33 2021

@author: franc
"""

def crealista(n):
    lista=[ ]
    for i in range(n):   #tange puede ser(variable inicial, maxima y saltos)
        lista.append(i)
    return lista
resultado=crealista(30) #número de elementos de la lista
print (resultado)
