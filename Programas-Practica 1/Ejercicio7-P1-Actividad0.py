Tienda={
        "Yogurt": 10,
        "Coca cola": 20,
        "Leche": 15,
        "Kilos de huevo": 36,
        "Galletas": 15,
        "Jugo": 13,
}
def Imprimir():
    print("\nProducto\t Precio\n")
    for key, value in Tienda.items():
        print(key,"\b:\t","$",value)
    return True
def Ingresar():
    Nombre=str(input("Ingresa el nombre del Producto:"))
    Tienda[Nombre]=int(input("Ingresa el precio del producto: "))
    Imprimir()
    print("Hecho\n")
    return True
def Modificar():
    Imprimir()
    Nombre=str(input("Ingresa el nombre del producto a modificar: "))
    Tienda[Nombre]=int(input("Ingresa el nuevo precio del producto: "))
    Imprimir()
    print("Hecho\n")
    return True
def Salir():
    return False
def error():
    print("error")
switch={
        1: Imprimir,
        2: Ingresar,
        3: Modificar,
        4: Salir
        }
a=True
while a==True:
    seleccion=int(input("Ingresa una opción:\n1) Imprimir inventario\n2) Agregar un producto\n3) Modificar un precio\n4) Salir\n->"))
    a=switch.get(seleccion,error)()


    
    