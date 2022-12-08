archivo=open("archivo.txt","r")
archivo.seek(5)
cadena1=archivo.read(5)
print(cadena1)
print(archivo.tell())
archivo.close
