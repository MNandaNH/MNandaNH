# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 11:36:31 2021

@author: franc
"""

def directions(ciudad, barrio, calle):
    print("Su dirección de referencia es:")
    print("Su ciudad es:", ciudad)
    print("el sector es:", barrio)
    print("el sector es:", calle)
    
ci=input("Ingrese la ciudad:")
ba=input("Ingrese el barrio de referencia:")
ca=input("Ingrese la calle para entregar su pedido:")

directions(ci, ba, ca)