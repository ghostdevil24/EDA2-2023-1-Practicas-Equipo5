from tabulate import tabulate
Tabla=[]
def heapify(arr, n, i):
    Datos=[]
    largest = i
    l = 2 * i + 1	 
    r = 2 * i + 2
    if l < n and arr[largest] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        Datos.append(arr[:])
        Datos.append(n)
        Datos.append(i)
        Datos.append(largest)
        Datos.append(l)
        Datos.append(r)
        Tabla.append(Datos)
        Datos=[]
        heapify(arr, n, largest)
    Datos.append(arr[:])
    Datos.append(n)
    Datos.append(i)
    Datos.append(largest)
    Datos.append(l)
    Datos.append(r)
    Tabla.append(Datos)
    Datos=[]
def heapSort(arr):
	n = len(arr)
	for i in range(n//2 - 1, -1, -1):
		heapify(arr, n, i)
	for i in range(n-1, 0, -1):
		arr[0], arr[i] = arr[i], arr[0]
		heapify(arr, i, 0)
        
arr=[5,4,3,2,1,0]
heapSort(arr)
n = len(arr)
print("El arreglo ordenado es:")
for i in range(n):
	print("%d" % arr[i])
print(tabulate(Tabla,headers=["arr","n","i","largest","l","r"],tablefmt="fancy_grid"))
#Arr,n,i,largest,l,r