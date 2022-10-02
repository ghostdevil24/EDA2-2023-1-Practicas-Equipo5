import random
from time import time
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
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
    print(A)
    A=[]

  
plt.plot(datos,TiempoMS,label="MergeSort",marker="o",color="b")
plt.grid(True)
plt.title("MergeSort")
plt.xlabel("n Datos")
plt.ylabel("Tiempo [s]")
plt.savefig('Figura_MergeSort.png', bbox_inches='tight')
plt.show()
print(TiempoMS)
MS="\n".join((str(x) for x in TiempoMS))
with open('MergeSortTiempos.txt', 'w') as f:
    f.write('MergeSort\n')
    f.write(MS)