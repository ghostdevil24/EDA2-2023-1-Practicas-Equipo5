import random
from time import time
def GenerarNumeros(A):
    for i in range(100000):
        A.append(random.randint(0,100000))
def Intercambia(A,x,y):
    tmp=A[x]
    A[x]=A[y]
    A[y]=tmp

def Particionar(A,p,r):
    x=A[p]
    i=p
    for j in range (p+1,r+1):
        if A[j]<=x:
            i=i+1
            Intercambia(A, i, j)
    Intercambia(A,i,p)
    return i

def QuickSort(A,p,r):
    if(p<r):
        q=Particionar(A, p, r)
        QuickSort(A, p, q-1)
        QuickSort(A, q+1, r)
        
A=[]
GenerarNumeros(A)
tiempo0=time()
QuickSort(A, 0, len(A)-1)
tiempof=time()
print(A)
print("\nEl tiempo que tomó ordenar la lista por medio de quick sort fue: %f s" %(tiempof-tiempo0))