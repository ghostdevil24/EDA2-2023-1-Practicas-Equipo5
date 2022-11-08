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
            self.vecinos = list  ()
            self.distancia=0
            self.color='white'
            self.pred=[None]
            
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
    def bfs(self,vert):
        vert.distancia=0
        vert.color='gris'
        vert.pred=[None]
        q=list()
        q.append(vert.nombre)
        while len(q)>0:
            u=q.pop(0)
            node_u = self.vertices[u]
            for v in node_u.vecinos:
                node_v=self.vertices[v]
                if node_v.color=='white':
                    node_v.color ='gris'
                    node_v.distancia = node_u.distancia+1
                    node_v.pred=node_u.nombre
                    q.append(v)
            self.vertices[u].color='black'

    def imprimeGrafo(self):
        for key in sorted(list(self.vertices.keys())):
            print("Vertice "+key+" Sus vecinos son "+str(self.vertices[key].vecinos))
            print("   Vertice "+key+ " El predecesor es "+ str(self.vertices[key].pred))
            print("   La distancia de inicio a "+ key+" es: "+ str(self.vertices[key].distancia))
    def ObtenDistancia(self):
        P=[]
        for key in sorted(list(self.vertices.keys())):
            P.append(self.vertices[key].distancia)
        return P
    def ObtenNombre(self):
        N=[]
        for key in sorted(list(self.vertices.keys())):
           N.append(key)
        return N
    def ObtenVecinos(self):
        V=[]
        for key in sorted(list(self.vertices.keys())):
            V.append(self.vertices[key].vecinos)
        return V
        
class Controladora:
    def main(self):
        corrida=[]
        g=Grafo()
        a=Vertice('1')
        g.agregarVertice(a)
        edges=['12','14','15','1C','23','26','21','2B','32','34','37','3B','43','41','48','4C','56','59','51','65','62','6A','73','7B','78','8C','87','84','9C','9A','95','AB','A6','A9','BA','B2','B3','B7','BC','CB','C1','C9','C8','C4']
        Alfabeto=[]
        for i in range(len(edges)):
            for j in range(0,2):
                if ord(edges[i][j]) not in Alfabeto:
                    Alfabeto.append(ord(edges[i][j]))
                    #Alfabeto.append(edges[i][j])
 
        for i in Alfabeto:
            g.agregarVertice(Vertice(chr(i)))
        for edge in edges:
            g.agregarArista(edge[:1], edge[1:])
        for i in Alfabeto:
            g.bfs(Vertice(chr(i)))
        P=g.ObtenDistancia()
        N=g.ObtenNombre()
        V=g.ObtenVecinos()
        for i in range(len(P)-1):
          swapped = False
          for j in range(0, len(P) - i - 1):
            if P[j] > P[j + 1]:
              temp = P[j]
              P[j] = P[j+1]
              P[j+1] = temp
              temp1=N[j]
              N[j]=N[j+1]
              N[j+1]=temp1
              temp2=V[j]
              V[j]=V[j+1]
              V[j+1]=temp2
              swapped = True
              if not swapped:
                  break
        print(P)
        print()
        print(N)
        print()
        print(V)
        corrida.append(N[0])
        corrida.extend(V[0])
        for i in range(len(V)):
            for j in range(len(V[i])):
                if V[i][j] not in corrida:
                    corrida.append(V[i][j])
            
        
        g.imprimeGrafo()
        print()
        print("Cola de recorrido: ",corrida)
obj=Controladora()
obj.main()