import pickle
lista=["algoritmos 1","algoritmos 2","Esctructuras"]
archivo =open("materias.dat","wb")
pickle.dump(lista,archivo)
archivo.close
del lista
archivo= open("materias.dat", "rb")
lista = pickle.load(archivo)
print(lista)
archivo.close
