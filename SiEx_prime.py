# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 11:20:37 2021

@author: franc
"""

def is_prime(x):
    if x < 2:
       
        return False
    elif x == 2:
        return True
    
    for n in range (2, x):
        if x % n ==0:
            return False
    
    return True
    


for i in range(1,20,1):
    if is_prime(i + 1): #condicionc correcta de numero para entregar resultado y entega condicion de verdad para la conidion.
        print (i+ 1, end=" ")
print() 

   