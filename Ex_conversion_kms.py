# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 10:21:06 2021

@author: franc
"""

def l100kmtompg(liters):
   miles=100*1000/1609.344
   galons=liters/3.785411784 
   return miles/galons
   

def mpgtol100km(miles):
    liters=3.785411784 
    kilometers=miles*1609.344/1000
    km100=kilometers/100
    return liters/km100


print(l100kmtompg(3.9))
print(l100kmtompg(7.5))
print(l100kmtompg(10.))
print(mpgtol100km(60.3))
print(mpgtol100km(31.4))
print(mpgtol100km(23.5))



"""
def listafun(lista):
    for i in lista:
        print("Hola", i)
    print ("\n"*2)
    
listafun(["Juan"])
listafun(["Juan", "Carlos"])
listafun(["Juan", "Carlos", "Ana"])
listafun(["Juan", "Carlos", "Ana", "Ali"])
"""