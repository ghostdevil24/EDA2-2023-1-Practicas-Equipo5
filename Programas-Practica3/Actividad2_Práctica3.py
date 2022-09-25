import random
def Mayor(A):
    mayor=0
    for i in range(len(A)):
        if A[i]>mayor:
            mayor=A[i]
    return mayor
def GenerarNumeros(A,k):
    for i in range(k-1):
        A.append(random.randint(0, k))

def CountingSort(A,k): # A es la lista y k es el valor máximo de la lista
   C=[0 for _ in range(k+1)]
   for i in A:
       C[i]+=1
   i=0
   for j in range (k,-1,-1):
      for k in range(C[j]):
          A[i]=j
          i+=1
    
   return A 
   
Condicion=True
while Condicion:
    k=int(input("Ingresa el rango superior de la lista: "))
    if k>10 and k<30:
        A=[]
        GenerarNumeros(A, k)
        print("El valor maximo de la lista o k es: ",max(A))
        print("El valor minimo de la lista es: ",min(A))
        print("El valor maximo de k es ",Mayor(A))##Otra forma sin usar max
        print(A)
        A=CountingSort(A,k)
        print(A)
        Condicion=False
    else:
        print("Ingresa valores mayor a 10 y menores a 30")
