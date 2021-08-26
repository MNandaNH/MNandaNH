# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 23:48:07 2021

@author: franc
"""

x = int (input ())
y = int (input ())
3x = x % y
x = x % y
y = y % x
print (y)