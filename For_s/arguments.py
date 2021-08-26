# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 09:26:51 2021

@author: franc
"""

def suma(*args):
    print("", type(args))
    sum=0
    for n in args:
        sum +=n

    print("Suma:", sum)        

suma(3)