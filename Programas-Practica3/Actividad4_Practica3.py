import math
def countingSort(arr, exp1):
    
    n = len(arr)

	# The output array elements that will have sorted arr
    output = [0] * (n)

	# initialize count array as 0
    count = [0] * (10)
    for i in range(0, n):
        index = arr[i] // exp1
        count[index % 10] += 1
	# Change count[i] so that count[i] now contains actual
	# position of this digit in output arra
    for i in range(1, 10):
        count[i] += count[i - 1]
	# Build the output array
    i = n - 1
    while i >= 0:
        index = arr[i] // exp1
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
	# Copying the output array to arr[],
	# so that arr now contains sorted numbers
    i = 0
    for i in range(0, len(arr)):
        arr[i] = output[i]
        
# Method to do Radix Sort
def radixSort(arr):
    contador=0
    max1 = max(arr)
    temp=[]
    may=[]
    while max1>1:
        max1=max1//10
        contador=contador+1
    exp =int(math.pow(10,contador))
    while exp>=1:
        countingSort(arr, exp)
        for i in reversed(arr):
            if i//exp!=0:
                may.append(i)
                arr.pop()
        countingSort(may, exp)
        contador=0
        temp.insert(contador,may)
        contador+=1
        may=[]
        exp //= 10
    
    p = [item for sublist in temp for item in sublist]
    return p

# Driver code
arr = [170, 45, 75, 90, 802, 24, 2, 66,3,4,1004,1003,100]
print("Lista desordenada: \n",arr)
# Function Call
p=radixSort(arr)
print("Lista ordenada:")
for i in range(len(p)):
	print(p[i],end=",")
