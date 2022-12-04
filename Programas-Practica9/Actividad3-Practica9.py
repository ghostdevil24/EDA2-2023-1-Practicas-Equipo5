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
        for i in range(1, 2+self.t, 1):
            if (nodo.llaves[i] != None):
                print(nodo.llaves[i])


class Controladora:
    def main(self):
        BT = ArbolB(2)

        actual = BT.CrearArbolb()

        print("Se insertara B")
        BT.InsertarArbolb(actual, ord("B"))

        print("Se insertara T")
        BT.InsertarArbolb(actual, ord("T"))

        print("Se insertara H")
        BT.InsertarArbolb(actual, ord("H"))

        print("Imprime raiz")
        BT.imprimirNodo(BT.raiz)

        print("Se insertara M")
        BT.InsertarArbolb(actual, ord("M"))

        print("Imprime raiz llaves")
        print(BT.raiz.llaves)

        print("Imprime hijo1 llaves")
        print(BT.raiz.hijos[1].llaves)
        print("Imprime hijo2 llaves")
        print(BT.raiz.hijos[2].llaves)

        print("Se insertara O")
        BT.InsertarArbolb(actual, ord("O"))

        print("Se insertara C")
        BT.InsertarArbolb(actual, ord("C"))

        print("-------------------")
        print("Imprime raiz llaves")
        print(BT.raiz.llaves)

        print("Imprime hijo1 llaves")
        print(BT.raiz.hijos[1].llaves)
        print("Imprime hijo2 llaves")
        print(BT.raiz.hijos[2].llaves)

        print("Se insertara Z")
        BT.InsertarArbolb(actual, ord("Z"))

        print("-------------------")
        print("Imprime raiz llaves")
        print(BT.raiz.llaves)

        print("Imprime hijo1 llaves")
        print(BT.raiz.hijos[1].llaves)
        print("Imprime hijo2 llaves")
        print(BT.raiz.hijos[2].llaves)
        print("Imprime hijo3 llaves")
        print(BT.raiz.hijos[3].llaves)

        print("Se insertara G")
        BT.InsertarArbolb(actual, ord("G"))

        print("Se insertara L")
        BT.InsertarArbolb(actual, ord("L"))

        print("Se insertara E")
        BT.InsertarArbolb(actual, ord("E"))

        print("Se insertara N")
        BT.InsertarArbolb(actual, ord("N"))

        print("Se insertara P")
        BT.InsertarArbolb(actual, ord("P"))

        print("Se insertara R")
        BT.InsertarArbolb(actual, ord("R"))

        print("Se insertara D")
        BT.InsertarArbolb(actual, ord("D"))

        print("Se insertara J")
        BT.InsertarArbolb(actual, ord("J"))

        print("Se insertara Q")
        BT.InsertarArbolb(actual, ord("Q"))

        print("Se insertara F")
        BT.InsertarArbolb(actual, ord("F"))

        print("Se insertara W")
        BT.InsertarArbolb(actual, ord("W"))

        print("Se insertara X")
        BT.InsertarArbolb(actual, ord("X"))

        print("-------------------")
        print("Imprime raiz llaves")
        BT.imprimirNodo(BT.raiz)
        print(len(BT.raiz.hijos))

        print("Imprime hijos 1")
        BT.imprimirNodo(BT.raiz.hijos[1])
        print("Imprime hijos 2")
        BT.imprimirNodo(BT.raiz.hijos[2])
        print("Imprime hijos 3")
        BT.imprimirNodo(BT.raiz.hijos[3])
        print("Imprime hijos 4")
        BT.imprimirNodo(BT.raiz.hijos[3].hijos[2])


obj = Controladora()
obj.main()
