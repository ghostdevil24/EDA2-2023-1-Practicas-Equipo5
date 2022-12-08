try:
    a=None
    a=open("archivo.txt","r")
except:
    print("Error al abrir")
finally:
    if a is not None:
        print("Abrio correctamente")
        a.close()
