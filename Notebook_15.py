# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 22:50:50 2021

@author: franc
"""

floor_types = ['Estacionamiento', 'Negocios', 'Area de restaurantes', 'Oficinas']
floor_numbers = range(-1,3)
elevator_dict = dict(zip(floor_types,floor_numbers))
print("Los diversos pisos y espacios se muestran a continuación:", elevator_dict)

elevator_dict[-1]