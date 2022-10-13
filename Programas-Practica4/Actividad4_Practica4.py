def busquedaLinRecursiva(A,n,x):
    if n<0:
        return -1
    elif A[n]==x:
        return n
    return busquedaLinRecursiva(A, n-1, x)

A=[1,4,6,8,9,11,15,18]
print(busquedaLinRecursiva(A,len(A)-1,8))
