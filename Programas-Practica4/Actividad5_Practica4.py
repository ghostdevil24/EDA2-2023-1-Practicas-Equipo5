import math
def BusquedaBinIter(A,x,izquierda,derecha):
  
    while izquierda <= derecha:
        medio=math.floor((izquierda+derecha)/2)
        if (A[medio] == x):
            return medio
        elif (A[medio] < x):
            izquierda = medio+1

        else:
                derecha=medio-1

    return -1


A=[1,10,20,30,40,50,60,70,80]
x=40
print(BusquedaBinIter(A,x,0,len(A)-1))

