def Intercambia(A,x,y):
    tmp=A[x]
    A[x]=A[y]
    A[y]=tmp

def Particionar(A,p,r):
    print(A)
    x=A[p]
    print(x)
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

A=[23,20,19,18,13,12,9,7,6,5,4,3,2,1,0]
for i in range(len(A)):
    print(i,": ",A[i])
seleccion=int(input("Ingresa el índice del valor que quieres como pivote: "))
if seleccion>=0 and seleccion<=len(A)-1:
    B=A[0:seleccion]
    QuickSort(B, 0, len(B)-1)
    C=A[seleccion:len(A)]
    print(C)
    QuickSort(C, 0, len(C)-1)
    A=C+B
    print("El arreglo ordenado es: ")
    print(A)
else: 
    print("Escoge un índice válido")
