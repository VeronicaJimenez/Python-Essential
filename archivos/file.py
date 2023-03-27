# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 19:59:52 2023

@author: Veronica
"""
lista=[]
archivo=open("devices.txt")
for item in archivo:
    item=item.strip()
    lista.append(item)
    print (item)
archivo.close()    
print(lista)