# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 10:14:08 2021

@author: franc
"""

lista=[]
file=open("C:\Users\franc\OneDrive\Documents\Mipythhon\D7\devices2.txt","a")
item=1
while True:
    newItem=input("Ingrese item Switch a agregar archivo:a ")
    if "Exit" not in newItem:
        lista.append(item)
        item=item+1
        file.write(newItem+"\n")
    else:
        print ("All done")
        break
file.close()
print(lista)
