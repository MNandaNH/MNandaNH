# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 23:06:23 2021

@author: franc
"""

l1 = [1,2]

for v in range(2):

   l1.insert(-1,l1[v])

print(l1)