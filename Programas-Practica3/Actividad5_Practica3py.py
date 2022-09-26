import random
def Mayor(A):
    mayor=0
    for i in range(len(A)):
        if A[i]>mayor:
            mayor=A[i]
    return mayor

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

	max1 = Mayor(arr)

	exp = 1
	while max1 / exp >= 1:
		countingSort(arr, exp)
		exp *= 10


arr1=[]
pos=[]
neg=[]
arr=[]
p=[]
m=int(input("Ingresa el rango inferior: "))
n=int(input("Ingresa el rango superior: "))
k=int(input("Ingresa el tamaño de la lista: "))
arr=random.sample(range(m, n+1), k)
print("La lista desordenada es: \n",arr)
for i in range(len(arr)):
    if arr[i]<0:
        arr1.append(arr[i])
for item in arr:
    if item not in arr1:
        pos.append(item)
for item in arr1:
    if item not in pos:
        neg.append(item)
radixSort(pos)
for i in range(len(neg)):
    neg[i]=neg[i]*-1
radixSort(neg)
neg.reverse()
for i in range(len(neg)):
    neg[i]=neg[i]*-1
p= neg+pos
print("La lista ordenada es:\n",p)
