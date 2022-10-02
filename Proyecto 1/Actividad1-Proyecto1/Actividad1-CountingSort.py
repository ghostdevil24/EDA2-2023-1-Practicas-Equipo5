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
    print(B)

    
plt.plot(datos,TiempoCS,label="CountingSort",marker="*",color="b")
plt.grid(True)
plt.title("CountingSort")
plt.xlabel("n Datos")
plt.ylabel("Tiempo [s]")
plt.savefig('Figura_CountingSort.png', bbox_inches='tight')
plt.show()
print(TiempoCS)
CS="\n".join((str(x) for x in TiempoCS))
with open('CountingSortTiempos.txt', 'w') as f:
    f.write('CountingSort\n')
    f.write(CS)
print(TiempoCS)
