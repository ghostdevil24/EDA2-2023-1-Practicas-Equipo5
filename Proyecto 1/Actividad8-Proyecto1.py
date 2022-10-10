import numpy as np
def GenerarMatriz(a,b):
    Mat=[[None for x in range(b)] for y in range(a)]
    return  Mat
def ImprimirMatriz(Mat):
    for fila in range(len(Mat)):
        print(Mat[fila])
        
def Aplanar(Mat):
    return [item for sublist in Mat for item in sublist]

def bubbleSort(A):
   for i in range(len(A)-1):
     swapped = False
     for j in range(0, len(A) - i - 1):
       if A[j] < A[j + 1]:
         temp = A[j]
         A[j] = A[j+1]
         A[j+1] = temp
         swapped = True
         if not swapped:
             break    
def Reempacar(F,fil,col):
    Res=GenerarMatriz(fil, col)
    m=0
    for i in range(fil):
        for j in range(col):
            Res[i][j]=F[m]
            m=m+1
    return Res
fil= int(input("Introduce el numero de filas que desees para tus matrices: "))
col= int(input("Introduce el numero de columnas que desees para tus matrices: "))

if fil<=10 and col<=10 :
    matriz1=[]
    matriz2=[]
    print ('\n')
    print ('----Ingrese los datos de la matriz 1----')
    for i in range (fil):
        matriz1.append([])
        for j in range(col):
            val = int(input("Fila {} , Columna {} : ".format (i+1, j+1)))
            matriz1[i].append(val)
   
    F=Aplanar(matriz1)
    bubbleSort(F)
    matriz1=Reempacar(F, fil, col)
    print("Matriz 1 Ordenada decrecientemente")
    ImprimirMatriz(matriz1)
    print ('----Ingrese los datos de la matriz numero 2----')   
    for i in range (fil):
        matriz2.append([])
        for j in range(col):
            val = int(input("Fila {} , Columna {} : ".format (i+1, j+1)))
            matriz2[i].append(val)
    F=Aplanar(matriz2)
    bubbleSort(F)
    matriz2=Reempacar(F, fil, col)
    print("Matriz 2 Ordenada decrecientemente")
    ImprimirMatriz(matriz2)
    print("Ambas matrices:")
    print("Matriz 1")
    ImprimirMatriz(matriz1)
    print("Matriz 2")
    ImprimirMatriz(matriz2)
    c = np.intersect1d(matriz1,matriz2)
    print ('\nMatriz 1')  
   
    print("\tLos elementos comunes entre la matriz 1 y 2 son:",c)
else:
    print("El tamaño de las matrices debe de ser menor o igual a 10x10")