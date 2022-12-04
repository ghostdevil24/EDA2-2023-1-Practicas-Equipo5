class Nodo:
    def __init__(self, t):
        self.hijos = list()
        self.llaves = list()
        self.hoja = 1
        self.n = 0
        for k in range(2*t):
            self.llaves.append([None])
        for k in range(2*t+1):
            self.hijos.append([None])


class ArbolB:
    def __init__(self, gradoMinimo):
        self.t = gradoMinimo
        self.raiz = None

    def CrearArbolb(self):
        if (self.raiz == None):
            self.raiz = Nodo(self.t)
        return self.raiz

    def DividirArbolb(self, x, i):
        z = Nodo(self.t)
        y = x.hijos[i]
        z.hoja = y.hoja
        z.n = self.t-1

        for j in range(1, self.t):
            z.llaves[j] = y.llaves[j+self.t]
            y.llaves[j+self.t] = None

        if y.hoja == 0:
            for j in range(1, self.t+1):
                z.hijos[j] = y.hijos[j+self.t]
                y.hijos[j+self.t] = None
        y.n = self.t-1
        for j in range(x.n+1, i-1, -1):
            x.hijos[j+1] = x.hijos[j]

        x.hijos[i+1] = z

        for j in range(x.n, i-1, -1):
            x.llaves[j+1] = x.llaves[j]
        x.llaves[i] = y.llaves[self.t]
        y.llaves[self.t] = None
        x.n = x.n+1

    def ArbolbNolleno(self, x, k):
        i = x.n
        if x.hoja == 1:
            while (i >= 1) and (k < x.llaves[i]):
                x.llaves[i+1] = x.llaves[i]
                i = i-1
            x.llaves[i+1] = k
            x.n = x.n+1
        else:
            while (i >= 1) and (k < x.llaves[i]):
                i = i-1
            i = i+1

            if x.hijos[i].n == 2*self.t-1:
                self.DividirArbolb(x, i)
                if k > x.llaves[i]:
                    i = i+1
            self.ArbolbNolleno(x.hijos[i], k)

    def InsertarArbolb(self, nodo, k):
        r = self.raiz
        if r.n == 2*self.t-1:
            s = Nodo(self.t)
            self.raiz = s
            s.hoja = 0
            s.n = 0
            s.hijos[1] = r
            self.DividirArbolb(s, 1)
            self.ArbolbNolleno(s, k)
        else:
            self.ArbolbNolleno(r, k)

    def imprimirNodo(self, nodo):
        for i in range(1,2+self.t, 1):
            if (nodo.llaves[i] != None):
                print(nodo.llaves[i])

class Controladora:
    def main(self):
        contador=0
        BT = ArbolB(2)
        actual = BT.CrearArbolb()
        vector= [5,1,6,2,8,3]
        for i in vector:
            print("Se insertara ",i)
            BT.InsertarArbolb(actual,i)
            contador=contador+1
            if contador==3:
                print("Imprime raiz")
                BT.imprimirNodo(BT.raiz)
            if contador==6:
                print("Imprime raiz")
                BT.imprimirNodo(BT.raiz)
                print("Imprime hijo1 llaves")
                print(BT.raiz.hijos[1].llaves)
                print("Imprime hijo2 llaves")
                print(BT.raiz.hijos[2].llaves)
            if contador==6:
                print("Imprime raiz")
                BT.imprimirNodo(BT.raiz)
                print("Imprime hijo1 llaves")
                print(BT.raiz.hijos[1].llaves)
                print("Imprime hijo2 llaves")
                print(BT.raiz.hijos[2].llaves)
            if contador==6:
                print("Imprime raiz")
                BT.imprimirNodo(BT.raiz)
                print("Imprime hijo1 llaves")
                print(BT.raiz.hijos[1].llaves)
                print("Imprime hijo2 llaves")
                print(BT.raiz.hijos[2].llaves)
            if contador==7:
                print("Imprime raiz")
                BT.imprimirNodo(BT.raiz)
                print("Imprime hijo1 llaves")
                print(BT.raiz.hijos[1].llaves)
                print("Imprime hijo2 llaves")
                print(BT.raiz.hijos[2].llaves)
                




obj = Controladora()
obj.main()
