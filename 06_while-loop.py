# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 19:24:21 2023

@author: Veronica
"""

num_con=input('Ingrese el # al que debo contar:')
num_con=int(num_con)
contador=1
while(contador<=num_con):
    print(contador)
    contador+=1 
    """que es igual a: contador=contador+1"""
    
num_con=input('Ingrese el # al que debo contar:')
num_con=int(num_con)
contador=1
print("antes del while")
while(True):
    print(contador)
    contador+=1 
    if contador>num_con:
        break
    print("dentro del bucle")
print("fuera del bucle")    