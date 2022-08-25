import math
def Triangulo():
    print("Ingresa la magnitud de la base\n")
    base=float(input())
    print("Ingresa la magnitud de la altura\n")
    altura=float(input())
    resultado=(base*altura)/2
    print("El resultado es: ",resultado,"u²")
def Rectangulo():
    print("Ingresa la magnitud de la base\n")
    base=float(input())
    print("Ingresa la magnitud de la altura\n")
    altura=float(input())
    resultado=base*altura
    print("El resultado es: ",resultado,"u²")
def Circulo():
    print("Ingresa la magnitud del radio\n")
    radio=float(input())
    resultado=math.pi*math.pow(radio,2)
    print("El resultado es: ",resultado,"u²")
def error():
    print("Error")
switch={
     1: Triangulo,
     2: Rectangulo,
     3: Circulo
    }
print("Buen día\nIngrese la figura la cual quiere calcular su área\n1. Triángulo\n2. Rectangulo\n3. Círculo\n->")
Figura=int(input())
switch.get(Figura,error)()