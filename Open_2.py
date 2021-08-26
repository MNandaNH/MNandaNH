# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 13:04:00 2021

@author: franc
"""


file=open("devices2.txt")
for i in file:
    i=i.strip()
    print(i)
file.close()
