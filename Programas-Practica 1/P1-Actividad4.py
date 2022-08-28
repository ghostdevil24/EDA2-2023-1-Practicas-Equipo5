import random
def GenerarNumeros(Arreglo,filas,columnas):
    for i in range(filas):
        for j in range(columnas):
            Arreglo[i][j]=random.randrange(0,1000)
            
def Bubblesort(Arreglo,filas,columnas):
    tam=filas*columnas
    for i in range(tam):
        for j in range(tam-1):
            if Arreglo[j//columnas][j%columnas]>Arreglo[(j+1)//columnas][(j+1)%columnas]:
                temp=Arreglo[j//columnas][j%columnas]
                Arreglo[j//columnas][j%columnas]=Arreglo[(j+1)//columnas][(j+1)%columnas]
                Arreglo[(j+1)//columnas][(j+1)%columnas]=temp

def Imprimir(Arreglo,filas,columnas):
    for i in range(filas):
        for j in range(columnas):
            print("[",Arreglo[i][j],"]",end=" ")
        print()
        
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
        Bubblesort(Arreglo, filas, columnas)
        print("El arreglo ordenado ascendentemente es:\n")
        Imprimir(Arreglo,filas,columnas)


