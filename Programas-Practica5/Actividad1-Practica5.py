def formaArreglo(tamano):
    Arr=[None]*tamano
    return Arr

def obtenerLlaveNumerica(llave):
    hash=0
    for char in str(llave):
        hash+=ord(char)
    return hash

def H(llaveN):
    return llaveN%5
def Completo(map):
    for i in range(len(map)):
        if map[i]==None:
            return False
    return True

def agregar(llave,valor,map,tamano):
    llave_hash=H(obtenerLlaveNumerica(llave))
    ParllaveValor=[llave,valor]
    
    if map[llave_hash] is None:
        map[llave_hash]=list([ParllaveValor])
        return True
    else:
        g=0
        for j in range(tamano+1):
            llaveh=(llave_hash+j)%13
            if g!=0:
                llaveh=(llave_hash+g)%13
                g=g+1
            if Completo(map)==True:
                print("Tabla llena",llave_hash)
                break
            elif Completo(map)==False and llaveh==len(map):
                p=j-len(map)
                g=p
                llaveh=(llave_hash+g)%1
            elif map[llaveh] is None:
                map[llaveh]=list([ParllaveValor])
                return True
               
            
def buscar(llave,tamano):
    res=[]

    llave_hash=H(obtenerLlaveNumerica(llave))
    if map[llave_hash] is not None:
       x=list(map)
       lista=[item[0] for item in x]
       x=[item[0] for item in lista]
       for i in range(len(map)):
            if llave==x[i]:
                pares=map[i]
                g=[item[1] for item in pares]
                res.extend(g)
       if len(res)==0:
           return None
       else:
           return res
   

map=formaArreglo(10);

agregar("Hola6",12213299,map,10)
agregar("Hola4",12213214,map,10)
agregar("Hola1",1221321,map,10)
agregar("Hola2",1221322,map,10)
agregar("Hola3",1221323,map,10)
agregar("Hola5",1221325,map,10)
agregar("Hola6",1221326,map,10)
agregar("Hola7",1221327,map,10)
agregar("Hola1",1221328,map,10)
agregar("Hola1",1221310,map,10)
print(map)

print("\nLLAVE\s DE  1: ",buscar("Hola1",10))
