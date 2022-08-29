import random

def Arreglar(A,filas,columnas,B):
    contador=0
    for i in range(filas):
        for j in range(columnas):
            B[i][j]=A[contador]
            contador=contador+1
    return B
def GenerarNumeros(Arreglo,filas,columnas):
    for i in range(filas):
        for j in range(columnas):
            Arreglo[i][j]=random.randrange(0,1001)

def Imprimir(Arreglo,filas,columnas):
    for i in range(filas):
        for j in range(columnas):
            print("[",Arreglo[i][j],"]",end=" ")
        print()
   
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

restriccion=True
while restriccion:
    filas=int(input("Ingresa el numero de filas: "))
    columnas=int(input("Ingresa el numero de columnas: "))
    if filas>10 or columnas>10:
        print("Intenta usar un arreglo menor a 10x10\n")
        restriccion=False
    else:
        restriccion=False
        Arreglo=[[None for i in range(columnas)]for j in range(filas)]
        GenerarNumeros(Arreglo,filas,columnas)
        print("El arreglo desordenado es:\n")
        Imprimir(Arreglo,filas,columnas)
        ArregloTransformado=[item for sublist in Arreglo for item in sublist]
        MergeSort(ArregloTransformado,0,filas*columnas-1)
        print("El arreglo ordenado ascendentemente es:\n")
        Arreglo=Arreglar(ArregloTransformado,filas, columnas,Arreglo)
        Imprimir(Arreglo,filas,columnas)