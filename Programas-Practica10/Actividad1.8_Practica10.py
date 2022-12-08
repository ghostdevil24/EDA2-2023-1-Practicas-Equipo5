lista=["lunes","martes","miercoles","jueves","viernes"]
archivo2=open("datos2.txt","w")
archivo2.writelines(lista)
archivo2.close()