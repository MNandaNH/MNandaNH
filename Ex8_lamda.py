# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 21:58:50 2021

@author: franc
"""

#print(chr(ord("p") + 2))

def o(p):

      def q():

         return "*" * p

      return q

r = o(1)

s = o(2)

print(r() + s())
