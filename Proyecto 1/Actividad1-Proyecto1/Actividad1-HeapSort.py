import random
from time import time
import matplotlib.pyplot as plt
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
    print(A)
plt.plot(datos,TiempoHS,label="HeapSort",marker="o",color="m")
plt.grid(True)
plt.title("HeapSort")
plt.xlabel("n Datos")
plt.ylabel("Tiempo [s]")
plt.savefig('Figura_HeapSort.png', bbox_inches='tight')
plt.show()
HS="\n".join((str(x) for x in TiempoHS))
with open('HeapSortTiempos.txt', 'w') as f:
    f.write('HeapSort\n')
    f.write(HS)
print(TiempoHS)