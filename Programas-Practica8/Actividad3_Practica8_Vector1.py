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

    def inorden(self,nodo):
             if nodo.hijoIzq!=None:
                self.inorden(nodo.hijoIzq)
             
             if (nodo!=None):
                print(str(nodo.val))
             if nodo.hijoDer!=None:
                 self.inorden(nodo.hijoDer)
               
    def imprimeInorden(self):
        if (self.raiz!=None):
            self.inorden(self.raiz)
        
    def preorden(self,nodo):
            if(nodo!=None):
                print(str(nodo.val))
            if nodo.hijoIzq!=None:
                self.preorden(nodo.hijoIzq)
            if nodo.hijoDer!=None:
                self.preorden(nodo.hijoDer)
    def imprimePreorden(self):
        if(self.raiz!=None):
            self.preorden(self.raiz)
            
    def postorden(self,nodo):
            
            if nodo.hijoIzq!=None:
                self.postorden(nodo.hijoIzq)
            if nodo.hijoDer!=None:
                self.postorden(nodo.hijoDer)
            if(nodo!=None):
                print(str(nodo.val))
                
    def imprimePostorden(self):
        if(self.raiz!=None):
            self.postorden(self.raiz)
            
    
class Controladora:
    def main(self):
        nodos=[ 6, 15, 10, 2, 1, 13, 43]
        g=Arbol()
        for i in nodos:
            g.agregar(i)
        print("Lista original")
        print(nodos)
        print("Preorden: ")
        g.imprimePreorden()
        print("Inorden: ")
        g.imprimeInorden()
        print("Postorden: ")
        g.imprimePostorden()
        

obj=Controladora()
obj.main()