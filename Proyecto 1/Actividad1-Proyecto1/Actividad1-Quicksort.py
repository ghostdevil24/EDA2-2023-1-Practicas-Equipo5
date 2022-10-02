import random
from time import time
import matplotlib.pyplot as plt
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
    print(A)
    
print(A)
plt.plot(datos,TiempoQS,label="QuickSort",marker="o",color="g")
plt.title("QuickSort")
plt.grid(True)
plt.xlabel("n Datos")
plt.ylabel("Tiempo [s]")
plt.savefig('Figura_QuickSort.png', bbox_inches='tight')
plt.show()
print(TiempoQS)
QS="\n".join((str(x) for x in TiempoQS))
with open('QuickSortTiempos.txt', 'w') as f:
    f.write('QuickSort\n')
    f.write(QS)