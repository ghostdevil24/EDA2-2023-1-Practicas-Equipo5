import random
from tabulate import tabulate
def GenerarNumeros(Arreglo,filas,columnas):
    for i in range(filas):
        for j in range(columnas):
            Arreglo[i][j]=random.randrange(0,1000)
            
def Bubblesort(Arreglo,filas,columnas,Datos,Tabla):
    tam=filas*columnas
    temp=None
    contador=0
    for i in range(tam):
        for j in range(tam-1):
            indice=i
            Datos.insert(0,indice)
            Datos.insert(1,j)
            Datos.insert(2,Arreglo[j//columnas][j%columnas])
            Datos.insert(3,Arreglo[(j+1)//columnas][(j+1)%columnas])
            if Arreglo[j//columnas][j%columnas]>Arreglo[(j+1)//columnas][(j+1)%columnas]:
                temp=Arreglo[j//columnas][j%columnas]
                Arreglo[j//columnas][j%columnas]=Arreglo[(j+1)//columnas][(j+1)%columnas]
                Arreglo[(j+1)//columnas][(j+1)%columnas]=temp
            Datos.insert(4,temp)
            Datos.insert(5,Arreglo[j//columnas][j%columnas])
            Datos.insert(6,Arreglo[(j+1)//columnas][(j+1)%columnas])
            contador=contador+j
            Tabla.insert(contador+1,Datos)
            Datos=[]
            
            
                

def Imprimir(Arreglo,filas,columnas):
    for i in range(filas):
        for j in range(columnas):
            print("[",Arreglo[i][j],"]",end=" ")
        print()
        
restriccion=True
Tabla=[]
Datos=[]
Titulos=["i","j","Vec[j]","Vec[j+1]","temp","Vec[j](Comparado)","Vec[j+1](Comparado)"]
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
        Tabla.insert(0, Titulos)
        Bubblesort(Arreglo, filas, columnas,Datos,Tabla)
        print("El arreglo ordenado ascendentemente es:\n")
        Imprimir(Arreglo,filas,columnas)
        print(tabulate(Tabla,headers='firstrow',tablefmt='fancy_grid'))
        