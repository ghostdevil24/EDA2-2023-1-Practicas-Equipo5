from tabulate import tabulate
Tabla=[]
def Intercambia(A,x,y):
    tmp=A[x]
    A[x]=A[y]
    A[y]=tmp

def Particionar(A,p,r):
    Datos=[]
    print(A)
    x=A[p]
    print(x)
    i=p
    for j in range (p+1,r+1):
        if A[j]<=x:
            i=i+1
            Intercambia(A, i, j)
            Datos.append(A[:])
            Datos.append(p)
            Datos.append(r)
            Datos.append(x)
            Datos.append(i)
            Datos.append(j)
            Datos.append(None)
            Datos.append(A[i])
            Datos.append(A[j])
            Tabla.append(Datos)
            Datos=[]
    Intercambia(A,i,p)
    Datos.append(A[:])
    Datos.append(p)
    Datos.append(r)
    Datos.append(x)
    Datos.append(i)
    Datos.append(j)
    Datos.append(i)
    Datos.append(A[i])
    Datos.append(A[p])
    Tabla.append(Datos)
    Datos=[]
    return i

def QuickSort(A,p,r):
    if(p<r):
        q=Particionar(A, p, r)
        QuickSort(A, p, q-1)
        QuickSort(A, q+1, r)
        
A=[5,4,3,2,1,0]
QuickSort(A, 0,len(A)-1)
print(A)
Tabla.insert(0,[[5,4,3,2,1,0],0,5,5,0,1,None,None,None])
print(tabulate(Tabla,headers=["A","p","r","pivote","i","j","q","A[x]","A[y]"],tablefmt="fancy_grid"))
#A,p,r,pivote,i,j,q