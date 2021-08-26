# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 08:33:00 2021

@author: franc
"""
nombre=input("Por favor ingrese sus datos:"))
    print ("Hola!", nombre, "Continua ingresando tus datos_")
apellido=srt(input("Por favor ingrese su apellido"))
localidad=srt(input("Por favor ingrese su dirección"))
edad=int(input ("Ingrese su edad:"))
if edad>=0 and edad<=12:
    print("Es un niño")
elif edad>=13 and edad<=18:
    print("Es un adolescente")
elif edad>=19 and edad<=65:
    print("Es un adulto joven")
elif edad>=66 and edad<=100:
    print("Es un adulto mayor")
else:
    print("Por favor ingrese su edad")
  