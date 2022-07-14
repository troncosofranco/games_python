import random
import time #medir tiempo para hacer una tarea

def búsqueda_ingenua(lista, objetivo):
    for i in range(len(lista)):
        #range(len(lista)): 0, 1, 2.... len-1
        if lista[i] == objetivo:
            return i
    return -1 #-1 no es un índice válido

mi_lista = [1, 3, 5, 10, 12]
print(búsqueda_ingenua(mi_lista, 15))

#búsqueda binaria -> La lista debe estar en orden ascendente
def búsqueda_binaria(lista, objetivo, límite_inferior = None, límite_superior = None): #None: valor por defecto
    if límite_inferior is None: #Inicio de la lista
        límite_inferior = 0
    if límite_superior is None:
        límite_superior = len(lista) -1 #Fin de la lista

    if límite_superior < límite_inferior:
        return -1

    punto_medio = (límite_inferior + límite_superior) // 2 #// -> Retorna la parte entera

    if lista[punto_medio] == objetivo:
        return punto_medio
    elif objetivo < lista[punto_medio]:
        return búsqueda_binaria(lista, objetivo,límite_inferior, punto_medio - 1)
    else:
        return búsqueda_binaria(lista, objetivo, punto_medio + 1, límite_superior)


if __name__ == '__main__': #el código no se ejecuta si es llamado por otro módulo

    #Crear una lista ordenada con 100000 elementos
    tamaño = 10000
    conjunto_inicial = set() #conjunto de datos vacíos

    while len(conjunto_inicial) < tamaño:
        conjunto_inicial.add(random.randint(-3*tamaño, 3*tamaño))
        
    lista_ordenada = sorted(list(conjunto_inicial)) #crea el conjunto inicial es una lista

    #sorted -> ordena la lista en orden ascendente

    #Medir el tiempo de búsqueda ingenua
    inicio = time.time()
    for objetivo in lista_ordenada:
        búsqueda_ingenua(lista_ordenada, objetivo)
    fin = time.time()
    print(f"Tiempo de búsqueda ingenua: {fin - inicio} segundos.")
    
    
    #Medir el tiempo de búsqueda ingenua
    inicio = time.time()
    for objetivo in lista_ordenada:
        búsqueda_binaria(lista_ordenada, objetivo)
    fin = time.time()
    print(f"Tiempo de búsqueda binaria: {fin - inicio} segundos.")