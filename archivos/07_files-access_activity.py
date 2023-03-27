# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 18:32:57 2023

@author: Veronica
"""
file=open("devices.txt","a")
while True:
    newitem=input("Ingrese un nuevo item: ")
    if newitem == 'exit':
        break
    file.write(newitem + "\n")   
print('All done')
