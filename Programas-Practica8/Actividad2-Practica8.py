class Nodo:
     def __init__(self, valor):
         self.hijoIzq=None
         self.hijoDer=None
         self.val=valor

class Arbol:
    def __init__(self):
        self.raiz=None
    
    def obtenerRaiz(self):
        return self.raiz
    
    def agregar(self,val):
        if(self.raiz==None):
            self.raiz=Nodo(val)
        else:
            self.agregarNodo(val,self.raiz)
    
    def agregarNodo(self,val,nodo):
        if (val<nodo.val):
            if(nodo.hijoIzq!=None):
                self.agregarNodo(val, nodo.hijoIzq)
            else:
                nodo.hijoIzq=Nodo(val)
        else:
            if(nodo.hijoDer!=None):
                self.agregarNodo(val, nodo.hijoDer)
            else:
                nodo.hijoDer=Nodo(val)
    def preorden(self,nodo,x):
        if(nodo!=None):
            print(str(nodo.val))
            x.append(int(nodo.val))
            if nodo.hijoIzq!=None:
                self.preorden(nodo.hijoIzq,x)
            if nodo.hijoDer!=None:
                self.preorden(nodo.hijoDer,x)
        return x
    def imprimePreorden(self):
        x=[]
        if(self.raiz!=None):
            x=self.preorden(self.raiz,x)
        return x
    def buscar(self,x,busqueda):
       if(busqueda in x):
           print("Valor encontrado")
       else:
           print("Valor no encontrado")
class Controladora:
    def main(self):
        nodos=[8,3,10,1,6,14,4,7,13]
        g=Arbol()
        for i in nodos:
            g.agregar(i)
        x=g.imprimePreorden()
        busqueda=int(input("Ingrese un valor a buscar en el arbol: "))
        g.buscar(x,busqueda)
obj=Controladora()
obj.main()