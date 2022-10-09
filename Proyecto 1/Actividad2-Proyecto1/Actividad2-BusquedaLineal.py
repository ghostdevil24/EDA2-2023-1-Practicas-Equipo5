import random
from time import time
import matplotlib.pyplot as plt
def busquedaLineal(A,n,x):
	encontrado=-1
	for k in range(n+1):
		if A[k] == x:
			encontrado=k
	return encontrado

A=[]
print()
TiempoBL=[]
datos=[500,1000,2000,5000,10000, 20000, 40000, 80000, 100000,
150000, 200000, 250000]
for tam in datos:
    print(tam)
    A=random.choices(range(-1000,1001), weights=None, cum_weights=None,k=tam)
    x=random.randint(-1000, 1000)
    print("Valor: ",x)
    t0=time()
    busquedaLineal(A,len(A)-1,1000)
    TiempoBL.append(round(time()-t0,16))

plt.plot(datos,TiempoBL,label="Busqueda Lineal",marker="*",color="b")
plt.grid(True)
plt.title("Busqueda Lineal")
plt.xlabel("n Datos")
plt.ylabel("Tiempo [s]")
plt.savefig('Figura_BusquedaLineal.png', bbox_inches='tight')
plt.show()
print(TiempoBL)
BL="\n".join((str(x) for x in TiempoBL))
with open('BusquedaLinealTiempos.txt', 'w') as f:
    f.write('BusquedaLineal\n')
    f.write(BL)
