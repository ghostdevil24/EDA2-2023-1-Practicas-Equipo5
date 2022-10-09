import math
import random
from time import time
import matplotlib.pyplot as plt
def BusquedaBinIter(A,x,izquierda,derecha):
  
    while izquierda <= derecha:
        medio=math.floor((izquierda+derecha)/2)
        if (A[medio] == x):
            return medio
        elif (A[medio] < x):
            izquierda = medio+1

        else:
                derecha=medio-1
    return -1
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

A=[]
B=[]
print()
TiempoBB=[]
datos=[500,1000,2000,5000,10000, 20000, 40000, 80000, 100000,
150000, 200000, 250000]
for tam in datos:
    print(tam)
    B=random.choices(range(-1000,1001), weights=None, cum_weights=None,k=tam)
    x=random.randint(-1000, 1000)
    print("Valor: ",x)
    derecha=len(A)-1
    A=CountingSort(B)
    t0=time()
    h=BusquedaBinIter(A, x, 0, derecha)
    TiempoBB.append(round(time()-t0,16))
    print(h)

plt.plot(datos,TiempoBB,label="Busqueda Binaria",marker="*",color="b")
plt.grid(True)
plt.title("Busqueda Binaria")
plt.xlabel("n Datos")
plt.ylabel("Tiempo [s]")
plt.savefig('Figura_BusquedaBinaria.png', bbox_inches='tight')
plt.show()
print(TiempoBB)
BB="\n".join((str(x) for x in TiempoBB))
with open('BusquedaBinariaTiempos.txt', 'w') as f:
    f.write('BusquedaBinaria\n')
    f.write(BB)