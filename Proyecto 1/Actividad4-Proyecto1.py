def GenerarMatriz(a,b):
    Mat=[[None for x in range(b)] for y in range(a)]
    return  Mat

def IngresarDatos(Mat,a,b):
    for i in range(a):
        for j in range(b):
            print("Fila %d columna %d"%(i+1,j+1))
            Mat[i][j]=int(input("Ingresa el valor: "))
            print()
            
def Aplanar(Mat):
    return [item for sublist in Mat for item in sublist]

def Reempacar(Mat,arr,c,d):
    m=0
    for i in range(c):
        for j in range(d):
            Mat[i][j]=arr[m]
            m=m+1

def ImprimirMatriz(Mat):
    for fila in range(len(Mat)):
        print(Mat[fila])

def Diseccion(P,frec):
    l3 = [x for x in P if x not in frec]
    return l3

def ChecarPares(Mat):
    pares=[]
    for i in Mat:
        if i%2==0:
            pares.append(i)
    return pares
def ChecarDiferencias(Mat,k,pares):
    res=[]
    num=[]
    suma=[]
    for i in pares:
        for j in Mat:
            if j-i==k or i-j==k:
                num=[]
                num.append(i)
                num.append(j)
                if sum(num) not in suma:
                    res.append(num)
                    suma.append(sum(num))
    return res

    
print("Para la matriz")
a=int(input("Ingrese el numero de filas de la matriz: "))
print()
b=int(input("Ingrese el numero de columnas de la matriz: "))
A1=GenerarMatriz(a,b)
IngresarDatos(A1,a,b)
ImprimirMatriz(A1)
B=Aplanar(A1)
print()
k=int(input("Ingrese la diferencia k de los numeros pares: "))
while k<0:
    print("K debe de ser positivo\nIntente nuevamente")
    k=int(input("Ingrese la diferencia k de los numeros pares: "))
pares=ChecarPares(B)
res=ChecarDiferencias(B, k, pares)

ImprimirMatriz(A1)
print("Hay",len(res),"pares con una diferencia de",k,"\b, los pares son: ")
for i in range(len(res)):
    print(res[i],end=",")