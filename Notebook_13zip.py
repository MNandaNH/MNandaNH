# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 22:44:12 2021

@author: franc
"""

floor_types = ['Parking', 'Shops', 'Food Court', 'Offices']
floor_numbers = range(-1,3)
zipped= zip(floor_types,floor_numbers)
print(tuple(zipped))