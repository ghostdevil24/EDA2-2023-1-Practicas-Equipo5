archivo=open('archivo.txt', 'r')
contenido = archivo.read()
nombre = archivo.name
modo = archivo.mode
encoding = archivo.encoding
archivo.close()

if archivo.closed:
    print("El archivo se ha cerrado correctamente")
else:
    print("El archivo permanece abierto")
print(contenido)
print(nombre)
print(modo)
print(encoding)
