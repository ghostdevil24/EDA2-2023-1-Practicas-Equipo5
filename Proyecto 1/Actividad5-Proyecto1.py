def Aplanar(Mat):
    return [item for sublist in Mat for item in sublist]

def ChecarDupicados(Mat,x):
    for i in Mat:
        if i==x:
            return True
    return False

def Interseccion(x,Mat1):
    l=Aplanar(Mat1)
    for i in l:
        if i==x:
            return True
    return False
def IngresarDatos(Mat,a,b):
    for i in range(a):
        for j in range(b):
            print("Fila %d columna %d"%(i+1,j+1))
            Mat[i][j]=int(input("Ingresa el valor: "))
            print()

def IngresarDatosMat2(Mat,a,b,Mat1):
    arr=[]
    for i in range(a):
        for j in range(b):
            r=True
            while r:
                print("Fila %d columna %d"%(i+1,j+1))
                Mat[i][j]=int(input("Ingresa el valor: "))
                dup=ChecarDupicados(arr,Mat[i][j])
                arr.append(Mat[i][j])
                inter=Interseccion(Mat[i][j], Mat1)
                if dup==True:
                    print("No se puede ingresar un valor que esté duplicado")
                    print("Intente nuevamente")
                    arr.pop()
                    
                elif inter==False:
                    print("No se puede ingresar un valor que no esté en la matriz 1")
                    print("Intente nuevamente")
                    arr.pop()
                    
                else:
                    r=False
            print()
        
def GenerarMatriz(a,b):
    Mat=[[None for x in range(b)] for y in range(a)]
    return  Mat

def ImprimirMatriz(Mat):
    for fila in range(len(Mat)):
        print(Mat[fila])

def ObtenerInstancias(x,P):
    contador=0
    for i in range(len(P)):
        if x==P[i]:
            contador=contador+1
    return contador
def ObtenerVariacion(Mat):
    contador=0
    x=[]
    l=Aplanar(Mat)
    for i in l:
        dup=ChecarDupicados(x, i)
        if dup==False:
            x.append(i)
            contador=contador+1
    return contador
def Diseccion(P,frec):
    l3 = [x for x in P if x not in frec]
    return l3

def bubbleSort(A):
   for i in range(len(A)-1):
     swapped = False
     for j in range(0, len(A) - i - 1):
       if A[j] > A[j + 1]:
         temp = A[j]
         A[j] = A[j+1]
         A[j+1] = temp
         swapped = True
         if not swapped:
             break    

def OrdenarFrecuencia(Mat,Mat1,c,d):
    P=Aplanar(Mat)
    S=Aplanar(Mat1)
    T=[]
    Frec=[]
    contador=[]
    Res=[]
    m=0
    for i in S:
        contador.append(ObtenerInstancias(i, P))
    
    for i in range(len(contador)):
        T=[S[i]]*contador[i]
        Frec.extend(T)
        T=[]
   
    resto=Diseccion(P, Frec)
    
    bubbleSort(resto)
    
    Frec.extend(resto)
   
    Res=GenerarMatriz(c, d)
    for i in range(c):
        for j in range(d):
            Res[i][j]=Frec[m]
            m=m+1
    
    return Res        
    
print("Para la primera matriz")
a=int(input("Ingrese el numero de filas de la matriz: "))
print()
b=int(input("Ingrese el numero de columnas de la matriz: "))
c=a
d=b
tam=a*b
A1=GenerarMatriz(a,b)
IngresarDatos(A1,a,b)
ImprimirMatriz(A1)
variacion=ObtenerVariacion(A1)
print("Números diferentes: ",variacion)
print()
print("Asegurese de que el tamaño de la segunda matriz sea menor o igual a la variación de números")
print()
print("Ahora para la segunda matriz")
print()
a=int(input("Ingrese el numero de filas de la matriz: "))
print()
b=int(input("Ingrese el numero de columnas de la matriz: "))
if(a*b>tam):
    print("No se puede sobrepasar el tamaño de la primera matriz")
    print("Intente nuevamente")
elif(a*b>variacion):
    print("No se puede ordenar con tan poca variacion en la matriz 1 y con el tamaño de la matriz 2, los valores no se pueden repetir")
    print("Intente nuevamente")
else:
    A2=GenerarMatriz(a, b)
    IngresarDatosMat2(A2, a, b, A1)
    ImprimirMatriz(A2)
    print()
    A1=OrdenarFrecuencia(A1, A2,c,d)
    print("El resultado es: ")
    ImprimirMatriz(A1)
