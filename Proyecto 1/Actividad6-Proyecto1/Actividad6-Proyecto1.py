import random
from time import time
import matplotlib.pyplot as plt
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
            Mat[i][j]=random.randint(0,1000000)

def bubbleSort(A):
  for i in range(len(A)-1):
    swapped = False
    for j in range(0, len(A) - i - 1):
      if A[j] > A[j + 1]:
        temp = A[j]
        A[j] = A[j+1]
        A[j+1] = temp
        swapped = True
        if not swapped:
            break

def CountingSort(arr):
    maximo = int(max(arr))
    minimo = int(min(arr))
    rango = maximo - minimo + 1
    count = [0 for _ in range(rango)]
    output= [0 for _ in range(len(arr))]
  
    for i in range(0, len(arr)):
        count[arr[i]-minimo] += 1
  
    for i in range(1, len(count)):
        count[i] += count[i-1]
 
    for i in range(len(arr)-1, -1, -1):
        output[count[arr[i] - minimo] - 1] = arr[i]
        count[arr[i] - minimo] -= 1

    for i in range(0, len(arr)):
        arr[i] = output[i]
  

def heapify(arr, n, i):
	largest = i 
	l = 2 * i + 1	
	r = 2 * i + 2	 

	if l < n and arr[largest] < arr[l]:
		largest = l

	if r < n and arr[largest] < arr[r]:
		largest = r

	if largest != i:
		arr[i], arr[largest] = arr[largest], arr[i] 

		heapify(arr, n, largest)


def heapSort(arr):
	n = len(arr)


	for i in range(n//2 - 1, -1, -1):
		heapify(arr, n, i)

	
	for i in range(n-1, 0, -1):
		arr[i], arr[0] = arr[0], arr[i]
		heapify(arr, i, 0)

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        mergeSort(L)
        mergeSort(R)
 
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def intercambia(A,x,y):
    tmp=A[x]
    A[x]=A[y]
    A[y]=tmp
def particionar(A,p,r):
    x=A[r]
    i=p-1
    for j in range(p,r):
        if (A[j]<=x):
            i=i+1
            intercambia(A,i,j)

    intercambia(A,i+1,r)
    return i+1
def Quicksort(A,p,r):
    if(p<r):
        q=particionar(A,p,r)
        Quicksort(A,p,q-1)
        Quicksort(A,q+1,r)

def countingSort(arr, exp1):
	n = len(arr)
	output = [0] * (n)

	count = [0] * (10)

	for i in range(0, n):
		index = arr[i] // exp1
		count[index % 10] += 1

	for i in range(1, 10):
		count[i] += count[i - 1]

	i = n - 1
	while i >= 0:
		index = arr[i] // exp1
		output[count[index % 10] - 1] = arr[i]
		count[index % 10] -= 1
		i -= 1
	i = 0
	for i in range(0, len(arr)):
		arr[i] = output[i]

def radixSort(arr):
	max1 = max(arr)
	exp = 1
	while max1 / exp >= 1:
		countingSort(arr, exp)
		exp *= 10
def Reempacar(Mat,arr,c,d):
    m=0
    for i in range(c):
        for j in range(d):
            Mat[i][j]=arr[m]
            m=m+1
Tiempo=[]
for func in [bubbleSort,CountingSort,heapSort,mergeSort,Quicksort,radixSort]:
    A=GenerarMatriz(125,8)
    IngresarDatos(A, 125,8)
    #ImprimirMatriz(A)
    B=Aplanar(A)
    print(func)
    if func == Quicksort:
        t0=time()
        func(B, 0, len(B)-1)
        Tiempo.append(time()-t0)
        Reempacar(A,B,125,8)
        ImprimirMatriz(A)
    else:
        t0=time()
        func(B)
        Tiempo.append(time()-t0)
        Reempacar(A,B,125,8)
        ImprimirMatriz(A)
print(Tiempo)
funciones=["BubbleSort","CountingSort","HeapSort","MergeSort","QuickSort","RadixSort"]
plt.bar(funciones, Tiempo, color ='maroon',
        width = 0.4)
 
plt.xlabel("Método de ordenamiento")
plt.ylabel("Tiempo en [s]")
plt.title("Comparación de tiempo en métodos de ordenamiento de una matriz de 1000 elementos")
plt.savefig('Figura_GráficaDeBarrasMetodosOrd.png', bbox_inches='tight')
plt.show()
with open('Tiempos.txt', 'w') as f:
    for i in range(6):
        
        f.write(str(funciones[i]))
        f.write('\n')
        f.write(str(Tiempo[i]))
        f.write('\n')

