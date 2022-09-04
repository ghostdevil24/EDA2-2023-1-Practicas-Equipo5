import random
def bubbleSort(A):
    pasadas=0
    for i in range(1,len(A)+1):
        pasadas=pasadas+1
        for j in range(len(A)-1):
            if A[j]>A[j+1]:
                temp=A[j]
                A[j]=A[j+1]
                A[j+1]=temp
        print(pasadas)
        
    print(pasadas)
    return pasadas
                
def bubbleSort2(A):
    bandera=True
    pasada=0
    while pasada<len(A)-1 and bandera:
        bandera=False
        for j in range(len(A)-1-pasada):
            if(A[j]>A[j+1]):
                bandera=True
                temp=A[j]
                A[j]=A[j+1]
                A[j+1]=temp
        pasada=pasada+1
    return pasada
def GenerarNumeros(A):
    for i in range(10):
            A.append(random.randrange(0,2001))
A=[]
GenerarNumeros(A)
pasadas1=bubbleSort(A)
print("El arreglo de bubbleSort es:")
print(A,"\nEl número de pasadas para bubbleSort es: ",pasadas1) #siempre 10 pasadas
A=[]
GenerarNumeros(A)
pasadas2=bubbleSort2(A)
print("\nEl arreglo de bubbleSort2 es:")
print(A,"\nEl número de pasadas para bubbleSort2 es: ",pasadas2) #pasadas variables



