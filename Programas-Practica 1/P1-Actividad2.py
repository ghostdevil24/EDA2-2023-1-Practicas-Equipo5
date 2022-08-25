from random import seed 
from random import randint
def bubbleSortDescendiente(A):
    for i in range(1,len(A)+1):
        for j in range(len(A)-1):
            if A[j]>A[j+1]:
                temp=A[j]
                A[j]=A[j+1]
                A[j+1]=temp

def bubbleSortAscendiente(A):
    for i in range(1,len(A)+1):
        for j in range(len(A)-1):
            if A[j]<A[j+1]:
                temp=A[j]
                A[j]=A[j+1]
                A[j+1]=temp
                
def numerosAleatorios(i):
    seed(i)
    return randint(0,1500)

A=[]
for i in range(1500):
   A.append(numerosAleatorios(i))
print("Los numeros generados son: \n")
print(A)
seleccion=int(input("Cómo desea ordenar el arreglo: \n1) Ascendente \n2) Descendente\n-> "))
if seleccion==1:
    bubbleSortDescendiente(A)
elif seleccion==2:
    bubbleSortAscendiente(A)
else:
    print("error")

print(A)
