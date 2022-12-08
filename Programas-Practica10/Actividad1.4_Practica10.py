a3=open("archivo.txt","r")
while True:
    linea=a3.readline()
    if not linea:
        break
    print(linea)
a3.close()
