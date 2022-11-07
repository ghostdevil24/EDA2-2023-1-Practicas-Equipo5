class Ordenar:
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
class Vertice :
        def __init__ (self, n):
            self.nombre=n
            self.vecinos= list  ()
        def agregarVecino(self, v):
            if v not in self.vecinos:
                self.vecinos.append(v)
                self.vecinos.sort()
                
class Grafo:
    vertices={}
    def agregarVertice(self, vertice):
        if isinstance(vertice, Vertice) and vertice.nombre not in self.vertices:
            self.vertices[vertice.nombre]=vertice
            return True
        else:
            return False
        
    def agregarArista(self,u,v):
        if u in self.vertices and v in self.vertices:
            for key, value in self.vertices.items():
                if key==u:
                    value.agregarVecino(v)
                if key==v:
                    value.agregarVecino(u)
            return True
        else:
            return False
        
    
    def imprimeGrafo(self):
        for key in sorted(list(self.vertices.keys())):
            print("Vertice "+key+" Sus vecinos son "+str(self.vertices[key].vecinos))
            
class Controladora:
    def main(self):
        g=Grafo()
        a=Vertice('A')
        g.agregarVertice(a)
        edges=['AC','AB','AD','CF','CE','BE','DG','DH','FE','EH']
        Alfabeto=[]
        for i in range(len(edges)):
            for j in range(0,2):
                if ord(edges[i][j]) not in Alfabeto:
                    Alfabeto.append(ord(edges[i][j]))
                    #Alfabeto.append(edges[i][j])
         
        Ordenar.bubbleSort(Alfabeto)
        print(Alfabeto)
        for i in Alfabeto:
            g.agregarVertice(Vertice(chr(i)))
        for edge in edges:
            g.agregarArista(edge[:1], edge[1:])
        g.imprimeGrafo()
obj=Controladora()
obj.main()
