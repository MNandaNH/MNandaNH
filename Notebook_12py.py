# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 22:20:06 2021

@author: franc
"""

temperatura = int(input("Por favor, ingrese la temperatura en ºC: "))
personas = (input("Hay personas? Indique si es Afirmativo, escriba true _ o Negativo_ false_"))
def termostato(temperatura,personas):
    if (temperatura<20 and personas=='true'):
        print("Calefaccion encendida")
    if(temperatura==23 or personas=='false'):
        print("Calefaccion apagada")
    else:
        print("No hacer nada")
termostato(temperatura,personas)


"""

#def smart_thermostat(temp, people_in):

#temperatura = int(input("Por favor, ingrese la temperatura en ºC: "))
#personas = (input("Hay personas? Indique si es Afirmativo, escriba true _ o Negativo_ false_"))
def smart_thermostat(temp,people_in):
    return command

    if smart_thermostat(21,True)
        print("Calefaccion encendida")
    if smart_thermostat(21,False)
        print("Calefaccion apagada")
    else:
        print("No hacer nada")




    if (temp<20 and people_in=='true'):
        print("Calefaccion encendida")
    if(temp==23 or people_in=='false'):
        print("Calefaccion apagada")
    else:
        print("No hacer nada")
"""
smart_thermostat(temp,people_in)
