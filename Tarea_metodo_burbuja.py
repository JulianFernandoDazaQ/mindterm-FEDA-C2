
def burbuja(lista):
    # La funcion len: nos quiere decir que de los 10 elementos nos recorra hasta el 9 elemento y por eso le ponemos el -1
    length = len(lista) - 1
     # En un bucle for queremos que inicie en un rango de 0 hasta el 9 y tambien se encarga de dar las pasadas que hay en el algoritmo
    for i in range(0, length):
        print(f"pasada # {i + 1}") # El print nos imprime cuantas pasadas esta haciendo el sistema para llegar ala ordenacion
        # Este segubdo for se encarga de las comparaciones
        for j in range(0, length - i):
            if lista[j] > lista[j + 1]:
                # Con la variable aux es una forma de cambiar el valor para no perderlo para darle valor al indise 1 al indice 0
                aux = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = aux
                
    return lista

puntos = [10, 8, 9, 6, 5, 2, 7, 3, 1]
print("antes de ordenar: ")
print(puntos)
print("despues de ordenar: ")
print(burbuja(puntos))