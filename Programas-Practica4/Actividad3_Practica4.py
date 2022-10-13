def BusquedaLinealCentinela(A,n,x):
    tmp=A[n]
    A[n]=x
    k=0
    while A[k]!=x:
        k=k+1
    A[n]=tmp
    if k<n or A[n]==x:
        return k
    else:
        return -1

A=[1,4,6,8,9,11,15,18]
print(BusquedaLinealCentinela(A,len(A)-1,18))