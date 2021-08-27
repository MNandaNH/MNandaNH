# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 23:12:26 2021

@author: franc
"""

l1 = [1,2]

for v in range(2):

   l1.insert(-1,l1[v])

print(l1)