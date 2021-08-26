# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 11:40:22 2021

@author: franc
"""
print("Inicio")
try:
    x=int(input("Enter a number"))
    y= 1 / x
  # print(y)

"""
except ZeroDivisionError:
    print ("You cannot divide by zero, sorry")
except ValueError:
    print ("You must enter an integer value")
"""

except: 
    print("Oh dear, something went wrong")
print("Fin")



"""
Nota:
Para poder activar el tercer mensaje, se debe
terminar el código presionando CTRL+C
Existe 63 tipos de errores identificados básicos en Python

"""