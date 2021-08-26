# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 23:52:32 2021

@author: franc
"""

lst = [[x for x in range(3)] for y in range(3)]
for r in range(3):
    for c in range(3):
        if lst[r][c] % 2 != 0:
            print("#")