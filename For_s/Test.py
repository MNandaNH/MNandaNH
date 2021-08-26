# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 22:52:49 2021

@author: fer
"""

print("Comienzo")
for i in range(0,30,1):
    print("Hola ", end=" ")
print()
print("Final")


for a in "AMIGO":
    print("Dame una", {a})
print("¡AMIGO!")

veces = int(input("¿Cuántas veces quiere que le salude? "))
for i in range(1,veces+1,1):
    print("Holis ", end="")
print()
print("Adiós")