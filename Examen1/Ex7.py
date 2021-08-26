# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 23:43:12 2021

@author: franc
"""

nativeVLAN = 1
dataVLAN = 100
if nativeVLAN == dataVLAN:
    print("The native VLAN and the data VLAN are the same.")
else:
    print("The native VLAN and the data VLAN are different.")