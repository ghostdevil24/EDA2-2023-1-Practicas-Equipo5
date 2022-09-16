import math
def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1	 
    r = 2 * i + 2
    if l < n and arr[largest] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
    
def heapSort(arr):
	n = len(arr)
	for i in range(n//2 - 1, -1, -1):
		heapify(arr, n, i)
	for i in range(n-1, 0, -1):
		arr[0], arr[i] = arr[i], arr[0]
		heapify(arr, i, 0)
        
arr=[5,4,3,2,1,0,9,8,1]
heapSort(arr)
n = len(arr)
j=0
contador=0

print("El arreglo ordenado es:")

for i in range(n):
    print("\t\t   ",end="")
    if j!=0:
        while contador<2+i:
            print("\b",end="")
            contador=contador+1
        contador=0
    for j in range(n):
        if j<math.pow(2,i) and j+math.pow(2,i)<n+1:
            print("[%d]"%arr[j+int(math.pow(2,i)-1)],end="\t")
    print() 