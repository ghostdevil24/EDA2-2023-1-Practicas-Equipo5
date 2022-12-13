from tkinter import *

import os

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
            #print("   Vertice "+key+ " El predecesor es "+ str(self.vertices[key].pred))
            #print("   La distancia de inicio a "+ key+" es: "+ str(self.vertices[key].distancia))
     
class Controladora:
    def Destruir(self,ventana):
        for n in ventana.winfo_children():
            n.destroy()
    def GenerarTabla(self,*args):
        Elem=[]
        print(self.tam_var.get())
        if self.tam_var.get()!="":
            for i in range(int(self.tam_var.get())):
                for j in range(int(self.tam_var.get())):
                    self.e=Entry(self.ventana, width=1, fg='blue',font=('Futura',20,'bold'))
                    Elem.append(self.e)
                    self.e.grid(row=i,column=j)
                    
        else:
            for n in Elem:
                n.destroy()
            for n in self.ventana.winfo_children():
                if isinstance(n,Entry):
                    n.destroy()
            tam = Entry(self.ventana, textvariable=self.tam_var,width=20)
            tam.pack()
            tam.place(x=500,y=40)
        
    def Opcion1(self,ventana,A,B):
        self.Destruir(ventana)
        l2=Label(ventana,text = "Escriba la dimensión de la matriz de adyacencia, recuerde que solo son matrices cuadradas")
        l2.pack()
        l2.place(x=500,y=20)
        l3=Label(ventana,text="Su matriz se muestra aquí")
        l3.pack()
        l3.place(x=0,y=0)
        self.tam_var=StringVar(value="0")
        self.tam_var.trace('w', self.GenerarTabla)
        self.GenerarTabla()
        tam = Entry(ventana, textvariable=self.tam_var,width=20)
        tam.pack()
        tam.place(x=500,y=40)
    def Opcion2(self,ventana,A,B):
        self.Destruir(ventana)
        l2=Label(ventana,text = "Escriba la dimensión de la matriz de adyacencia, recuerde que solo son matrices cuadradas")
        l2.pack()
        l2.place(x=500,y=20)
        l3=Label(ventana,text="Su matriz se muestra aquí")
        l3.pack()
        l3.place(x=0,y=0)
        self.tam_var=StringVar(value="0")
        self.tam_var.trace('w', self.GenerarTabla)
        self.GenerarTabla()
        tam = Entry(ventana, textvariable=self.tam_var,width=20) 
        tam.pack()
        tam.place(x=500,y=40)
        
    def main(self):
        self.ventana=Tk()
        self.ventana.geometry("1400x600")
        self.ventana.title("Representacion de grafos")
        l1 = Label(self.ventana,text = "Escoja una opción para representar su grafo")
        A= Button(self.ventana,height=10,width=30,bg="blue", text="Representar con Letras", font=('Futura', 20), command=lambda: self.Opcion1(self.ventana,A,B))
        B= Button(self.ventana,height=10,width=30,bg="green", text="Representar con Números", font=('Futura', 20), command=lambda: self.Opcion2(self.ventana,A,B))
        l1.pack()
        A.pack()
        B.pack()
        A.place(x=800,y=150)
        B.place(x=125, y=150)
        self.ventana.mainloop()
        edges=[]
        g=Grafo()
        n=int(input("Ingresa el numero de filas y columnas de la matriz de adyacencia: "))
        vertical=[]
        for i in range(n):
            vertical.append(str(i))
        print(vertical)
        mat=[[None for x in range(n)] for y in range(n)]
        for i in range(n):
            for j in range(n):
                print("Ingresa para la conexion entre ",i,"y ",j)
                mat[i][j]=int(input("Ingresa un 1 o 0: "))
                while(mat[i][j]!=1 and mat[i][j]!=0):
                      print("Solo se aceptan valores de 1 o 0")
                      print("Ingresa para la conexion entre ",i,"y ",j)
                      mat[i][j]=int(input("Ingresa un 1 o 0: "))
                if(mat[i][j]==1):
                    a=str(i)
                    b=str(j)
                    edges.append(a+b)
        
        #print(edges)
        print(mat)
        for i in range(n):
            print(mat[i])
        
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
        g.imprimeGrafo()
obj=Controladora()
obj.main()