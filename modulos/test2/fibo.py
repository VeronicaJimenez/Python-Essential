""" intento fallido 
for i in range(0,16):
    
    if i==0:
        return 0
           
    elif i==1:
        return 1
   
    else:  
        return (i-2 + i-1)
    
    print(i)  """ 
    

def Fibonacci(n):
    a, b = 0,1
    while a <= n:
        print(a, end=' ')
        c=a+b
        a=b
        b=c
        #a, b = b, a+b
    print()
    
"""Fibonacci(20)"""    