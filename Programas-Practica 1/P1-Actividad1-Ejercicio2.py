import random
def crearSubArreglo(A, indIzq, indDer):
	 return A[indIzq:indDer+1]
def Merge(A,p,q,r):
	Izq = crearSubArreglo(A,p,q)
	Der = crearSubArreglo(A,q+1,r)
	i=0
	j=0
	for k in range(p,r+1):
		if(j>=len(Der)) or (i < len (Izq)and Izq[i] and Izq[i] < Der[j]):
			A[k]=Izq[i]
			print("lista Izquierda",Izq)
			i=i+1
		else:
			A[k]=Der[j]
			print("lista Derecha",Der)
			j=j+1
def MergeSort(A,p,r):
	if r - p > 0:
		q = int((p+r)/2)
		MergeSort(A,p,q)
		MergeSort(A,q+1,r)
		Merge(A,p,q,r)

def GenerarNumeros(A):
    for i in range(6):
            A.append(random.randrange(0,2001))
A=[]
GenerarNumeros(A)
print("\nLista desordenada: ")
print(A,"\n")
MergeSort(A,0,len(A)-1)
print("\nLista ordenada: ")
print(A)