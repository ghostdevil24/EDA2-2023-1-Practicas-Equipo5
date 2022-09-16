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
		arr[i], arr[0] = arr[0], arr[i]
		heapify(arr, i, 0)
        
arr=[23,20,19,18,13,12,9,7,6,5,4,3,2,1,0]
heapSort(arr)
n = len(arr)
print("El arreglo ordenado es:")
for i in range(n):
	print("%d" % arr[i])