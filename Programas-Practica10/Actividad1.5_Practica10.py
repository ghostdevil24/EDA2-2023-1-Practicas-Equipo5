archivo=open("archivo.txt","r")
lista=archivo.readlines()
numlin=0
for linea in lista:
    numlin+=1
    print(numlin,linea)
archivo.close()