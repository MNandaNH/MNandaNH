# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 23:12:52 2021

@author: franc
"""

#L = [i for i in range(-1,-2)]

"""
def fun(x,y):
    if x == y:
        return x
    else:
        return fun(x,y-1)
    print(fun(0,3))
"""
"""
i = 0
while i < i + 2 :
     i += 1
     print("*")
else:
     print("*")
  """
"""
def fun(a,b,c=0)

fun (a=0, b=0) 

"""
"""
z = 0
y = 10

x = y < z and z > y or y > z and z < y
     
"""


dct = {"one":"two", "three":"one", "two":"three" }
v = dct["three"]
for k in range(len(dct)):
    v = dct[v]
print(v)