#Ejercicio 10 Actividad 1 - crear un directorio
import os
def crear_directorio(ruta):
    try:
        os.makedirs(ruta)
    except OSError:
        print("Error o el directorio ya fue creado")
        pass
    os.chdir(ruta)
principal=os.getcwd()
directorio='Nuevo'
ruta = os.path.join(principal, directorio)
crear_directorio(ruta)
