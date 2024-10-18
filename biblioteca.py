import random

#funcion para generar una lista de 50 numeros enteros aleatorios entre 1 y 100

'''Generar una lista de números enteros aleatorios: Desarrollar una función que genere de manera aleatoria una lista de 50 números enteros positivos entre 1 y 100.'''

def generar_lista_numeros():
    """Esta funcion genera una lista de numeros enteros aleatorios entre 1 y 100"""
    return [random.randint(1, 100)]

#Funcion para generar una matriz de 6x15 caracteres alphanumericos

def generar_matriz_caracteres():
    '''Esta funcion va a generar una matriz de 6 filas y 15 columnas compuestas de alphanumericos'''
    matriz = []
    for i in range(6):
        fila = [random.choice() for _ in range(15)]
        matriz.append(fila)
    return matriz

#funcion para ordenar una lista de numteros

def ordenar_lista(lista, criterio="ASC"):
    '''Esta funcion nos va a devolver una lista de numeros enteros en orden ascendente o decendente'''
    numero = len(lista)
    
    for i in range(numero):
        for j in range(0, numero - i - 1):
            if (criterio == "ASC" and lista[j] > lista[j + 1]) or criterio == "DESC" and lista[j] < lista[j + 1]: 
                #Intercambiamos los elementos si no estan en el orden deseado
                lista[j], lista[j + 1] = lista[j + 1], lista[j]              
    return lista

def validar_cadena_alphanumerica(cadena):
    '''Esta funcion valida si una cadena contiene solo caracteres alphanumericos'''
    return cadena.isalnum()

def contar_numeros_en_rango(lista, inicio, fin):
    '''Cuenta cuantos numeros en la lista estan dentro de un rango dado'''
    return [num for num in lista if inicio <= num <= fin]