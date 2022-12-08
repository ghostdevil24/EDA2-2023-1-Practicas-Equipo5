cadena1="Datos"
cadena2="Secretos"
archivo2=open("datos2.txt","w")
print(cadena1+"\n")
archivo2.write(cadena1+"\n")
archivo2.write("hola")
archivo2.write(cadena2)
archivo2.close