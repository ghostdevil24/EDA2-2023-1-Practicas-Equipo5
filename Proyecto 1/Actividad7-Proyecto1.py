#Actividad 7
matriz = [
    [1,1,2,3],
    [3,4,4,5],
    [6,9,9,9],
    [10,10,12,14]
    ]
def ImprimirMatriz(Mat):
    for fila in range(len(Mat)):
        print(Mat[fila])
    
print("Matriz:")
ImprimirMatriz(matriz)
x = 9
print("Valor a buscar: ",x)
output = sum([i.count(x) for i in matriz])  #Contabiliza los elementos fila por fila
print("El número de veces que '"+ str(x) +"' aparece en la matriz son: "+str(output))