import random
from time import time
import matplotlib.pyplot as plt
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
    print(p)
    arr=[]
    arr1=[]
    pos=[]
    
plt.plot(datos,TiempoRS,label="CountingSort",marker="*",color="r")
plt.grid(True)
plt.title("RadixSort")
plt.xlabel("n Datos")
plt.ylabel("Tiempo [s]")
plt.savefig('Figura_RadixSort.png', bbox_inches='tight')
plt.show()
RS="\n".join((str(x) for x in TiempoRS))
with open('RadixSortTiempos.txt', 'w') as f:
    f.write('RadixSort\n')
    f.write(RS)
print(TiempoRS)

