def busquedaLineal(A,n,x):
    encontrado=-1
    for k in range(n+1):
        if A[k] == x:
            encontrado=k
            break
    return encontrado

A=[1,4,6,8,12,9,9,11,15,18]
print(busquedaLineal(A,len(A)-1,9))