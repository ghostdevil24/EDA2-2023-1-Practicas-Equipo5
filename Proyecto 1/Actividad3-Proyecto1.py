from collections import Counter
from itertools import repeat, chain
def GenerarMatriz(a,b):
    Mat=[[None for x in range(b)] for y in range(a)]
    return  Mat

def Aplanar(Mat):
    return [item for sublist in Mat for item in sublist]

def ImprimirMatriz(Mat):
    for fila in range(len(Mat)):
        print(Mat[fila])

def IngresarDatos(Mat,a,b):
    for i in range(a):
        for j in range(b):
            print("Fila %d columna %d"%(i+1,j+1))
            Mat[i][j]=int(input("Ingresa el valor: "))
            print()
            
def Reempacar(Mat,arr,c,d):
    m=0
    for i in range(c):
        for j in range(d):
            Mat[i][j]=arr[m]
            m=m+1

a=int(input("Ingrese el numero de filas de la matriz: "))
print()
b=int(input("Ingrese el numero de columnas de la matriz: "))
matrizI=GenerarMatriz(a, b)
IngresarDatos(matrizI, a, b)
print ("Matriz inicial:")
ImprimirMatriz(matrizI)
matrizInicial=Aplanar(matrizI)
matrizFinal = list(chain.from_iterable(repeat(i, c)
         for i, c in Counter(matrizInicial).most_common()))
Reempacar(matrizI, matrizFinal, a, b)
print("Matriz Final:")
ImprimirMatriz(matrizI)


