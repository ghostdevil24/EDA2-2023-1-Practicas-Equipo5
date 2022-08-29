from time import time
import random
def GenerarNumeros(A):
    for i in range(2000):
            A.append(random.randrange(0,2001))
def CrearSubArreglo(A,indIzq,indDer):
    return A[indIzq:indDer+1]

def Merge(A,p,q,r):
    Izq=CrearSubArreglo(A, p, q)
    Der=CrearSubArreglo(A, q+1, r)
    i=0
    j=0
    for k in range(p,r+1):
        if(j>=len(Der))or(i<len(Izq) and Izq[i] <Der[j]):
            A[k]=Izq[i]
            i=i+1
        else:
            A[k]=Der[j]
            j=j+1

def MergeSort(A,p,r):
    if r-p>0:
        q=int(((p+r)/2))
        MergeSort(A, p, q)
        MergeSort(A, q+1, r)
        Merge(A,p,q,r)
        
A=[]
GenerarNumeros(A)
print("El arreglo desordenado:\n",A)
Ti=time()
MergeSort(A, 0, len(A)-1)
Tiempo=time()-Ti
print("El arreglo ordenado:\n",A)
print("\nEl tiempo en ordenar fue de: ",Tiempo,"s")