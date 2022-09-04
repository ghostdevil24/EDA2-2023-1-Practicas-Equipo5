A=[]
Nombre=str(input("Ingresa tu nombre completo empezando por apellidos: "))
print("Tu nombre completo:")
print(Nombre)
tam=len(Nombre)
for i in range(len(Nombre)):
    if Nombre[i]==" ":
      A.append(i)  
print("Nombre de pila:")
print(Nombre[A[1]+1:tam])
print("Apellido Paterno:")
print(Nombre[0:A[0]])
print("Apellido Materno:")
print(Nombre[A[0]+1:A[1]])
print("Iniciales por apellidos:")
print("%s%s%s"%(Nombre[0],Nombre[A[0]+1],Nombre[A[1]+1]))
