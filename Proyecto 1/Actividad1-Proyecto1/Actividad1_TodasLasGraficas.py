import random
from time import time
import matplotlib.pyplot as plt

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
  
    return arr

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

B=[]
pos=[]
A=[]
TiempoCS=[]
datos=[500,1000,2000,5000,10000, 20000, 40000, 80000, 100000,
150000, 200000, 250000]
for tam in datos:
    print(tam)
    A=random.choices(range(-1000,1001), weights=None, cum_weights=None,k=tam)
    t0=time()
    B=CountingSort(A)
    TiempoCS.append(round(time()-t0,15))

A=[]
TiempoHS=[]
datos=[500,1000,2000,5000,10000, 20000, 40000, 80000, 100000,
150000, 200000, 250000]
for tam in datos:
    print(tam)
    A=random.choices(range(-1000,1001), weights=None, cum_weights=None,k=tam)
    t0=time()
    heapSort(A)
    TiempoHS.append(round(time()-t0,10))

A=[]
TiempoMS=[]
datos=[500,1000,2000,5000,10000, 20000, 40000, 80000, 100000,
150000, 200000, 250000]
for tam in datos:
    print(tam)
    A=random.choices(range(-1000,1001), weights=None, cum_weights=None,k=tam)
    t0=time()
    mergeSort(A)
    TiempoMS.append(round(time()-t0,10))
    A=[]
A=[]
TiempoQS=[]
datos=[500,1000,2000,5000,10000, 20000, 40000, 80000, 100000,
150000, 200000, 250000]
for tam in datos:
    print(tam)
    A=random.choices(range(-1000,1001), weights=None, cum_weights=None,k=tam)
    t0=time()
    Quicksort(A,0,len(A)-1)
    TiempoQS.append(round(time()-t0,10))
arr1=[]
pos=[]
neg=[]
arr=[]
p=[]
TiempoRS=[]
datos=[500,1000,2000,5000,10000, 20000, 40000, 80000, 100000,
150000, 200000, 250000]
for tam in datos:
    print(tam)
    arr=random.choices(range(-1000,1001), weights=None, cum_weights=None,k=tam)
    for i in arr:
        if i<0:
            arr1.append(i)
        else:
            pos.append(i)
  
    for i in range(len(arr1)):
        arr1[i]=arr1[i]*-1
   
    t0=time()
    radixSort(pos)
    radixSort(arr1)
    TiempoRS.append(round(time()-t0,10))
    arr1.reverse()
    for i in range(len(arr1)):
        arr1[i]=arr1[i]*-1
    p= arr1+pos
    arr=[]
    arr1=[]
    pos=[]
A=[]
TiempoBS=[]
datos=[500,1000,2000,5000,10000, 20000, 40000, 80000, 100000,
150000, 200000, 250000]
for tam in datos:
    print(tam)
    A=random.choices(range(-1000,1001), weights=None, cum_weights=None,k=tam)
    t0=time()
    bubbleSort(A)
    TiempoBS.append(round(time()-t0,10))
    print(A)
    
plt.plot(datos,TiempoCS,label="CountingSort",marker="o",color="b")
plt.plot(datos,TiempoHS,label="HeapSort",marker="o",color="m")
plt.plot(datos,TiempoMS,label="MergeSort",marker="o",color="y")
plt.plot(datos,TiempoQS,label="QuickSort",marker="o",color="g")
plt.plot(datos,TiempoRS,label="RadixSort",marker="o",color="r")
plt.plot(datos,TiempoBS,label="BubbleSort",marker="o",color="c")
plt.legend()
plt.grid(True)
plt.title("Comparación métodos de ordenamiento")
plt.xlabel("n Datos")
plt.ylabel("Tiempo [s]")
plt.savefig('Figura_ComparacionTodas.png', bbox_inches='tight')
plt.show()
BS="\n".join((str(x) for x in TiempoBS))
CS="\n".join((str(x) for x in TiempoCS))
HS="\n".join((str(x) for x in TiempoHS))
MS="\n".join((str(x) for x in TiempoMS))
QS="\n".join((str(x) for x in TiempoQS))
RS="\n".join((str(x) for x in TiempoRS))

with open('Tiempostotales.txt', 'w') as f:
    f.write('BubbleSort\n')
    f.write(BS)
    f.write("\n")
    f.write('CountingSort\n')
    f.write(CS)
    f.write("\n")
    f.write('HeapSort\n')
    f.write(HS)
    f.write("\n")
    f.write('MergeSort\n')
    f.write(MS)
    f.write("\n")
    f.write('QuickSort\n')
    f.write(QS)
    f.write("\n")
    f.write('RadixSort\n')
    f.write(RS)