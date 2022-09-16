def heapify(arr, n, i):
	minimo = i
	l = 2 * i + 1	 
	r = 2 * i + 2
	if l < n and arr[minimo]>arr[l]:
		minimo = l
	if r < n and arr[minimo]>arr[r]:
		minimo = r
	if minimo != i:
		arr[i], arr[minimo] = arr[minimo], arr[i] 
		heapify(arr, n, minimo)

def heapSort(arr):
	n = len(arr)
	for i in range(n//2 - 1, -1, -1):
		heapify(arr, n, i)
	for i in range(n-1, -1, -1):
		arr[0], arr[i] = arr[i], arr[0]
		heapify(arr, i, 0)
        
arr=[23,20,19,18,13,12,9,7,6,5,4,3,2,1,0]
heapSort(arr)
n = len(arr)
print("El arreglo ordenado es:")
for i in range(n):
	print("%d" % arr[i])