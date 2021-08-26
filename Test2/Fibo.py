# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 09:40:29 2021

@author: franc
"""

def fibonacci(n):
    x,y = 0,1 # Si x=0 y y=1, 
#x=0
#y=1
    while x < n:
        print(x, end=" ")
         
        """
         z=x+y
        x=y
        y=z
        """
        x, y = y, x+y
       
    print()

#fibonacci(8)

