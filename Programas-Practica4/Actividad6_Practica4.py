import math
def BusquedaBinRecursiva(A,x,izquierda,derecha):
    if izquierda>derecha:
        return -1
    medio=math.floor((izquierda+derecha)/2)
   
    if A[medio]==x:
        return medio
    elif A[medio]<x:
        return BusquedaBinRecursiva(A, x, medio+1, derecha)
    else:
        return BusquedaBinRecursiva(A, x, izquierda, medio-1)

A=[1,10,20,30,40,50,60,70,80]
x=70
print(BusquedaBinRecursiva(A,x,0,len(A)-1))
