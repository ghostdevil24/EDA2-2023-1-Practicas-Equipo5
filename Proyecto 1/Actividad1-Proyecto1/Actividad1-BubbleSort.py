import random
from time import time
import matplotlib.pyplot as plt

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

plt.plot(datos,TiempoBS,label="BubbleSort",marker="o",color="c")
plt.grid(True)
plt.title("BubbleSort")
plt.xlabel("n Datos")
plt.ylabel("Tiempo [s]")
plt.savefig('Figura_Bubble.png', bbox_inches='tight')
plt.show()
BS="\n".join((str(x) for x in TiempoBS))
with open('BubbleSortTiempos.txt', 'w') as f:
    f.write('BubbleSort\n')
    f.write(BS)
print(TiempoBS)