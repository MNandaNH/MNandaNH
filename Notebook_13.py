# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 22:48:05 2021

@author: franc
"""

floor_types = ['Estacionamiento', 'Negocios', 'Area de restaurantes', 'Oficinas']
floor_numbers = range(-1,3)
zipped = zip (floor_types,floor_numbers) 
print(tuple(zipped))