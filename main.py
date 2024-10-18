import biblioteca

def menu():
    lista_numeros = []
    while True:
        print("\n---Menu de Opciones---")
        print("1. Generar lista de numeros enteros aleatorios")
        print("2. Ordenar lista de numeros")
        print("3. Contar numeros en un rango")
        print("4. Mostrar el maximo y el minimo de un rango")
        print("5. Generar una matriz de caracteres alphanumericos")
        print("6. Salir")
        
        opcion = int(input("Seleccione una opcion: "))
        
        if opcion == 1:
            #Genera una lista de numeros enteros aleatorios
            lista_numeros = biblioteca.generar_lista_numeros()
            print(f"Lista generada: {lista_numeros}")
            
        elif opcion == 2:
            #Ordenar lista de numero
            if lista_numeros:
                criterio = input("Ingrese el criterio de ordenamiento (ASC o DESC): ")
                try:
                    lista_ordenada = biblioteca.ordenar_lista(lista_numeros, criterio)
                    print("Lista ordenada", lista_ordenada)
                except ValueError:
                    print("")
            else:
                print("Primero debe generar una lista de numeros (opcion 1).")
                
        elif opcion == 3:
            #Cuenta los numeros de un rango
            if lista_numeros:
                try:
                    inicio = int(input("Ingrese el valor inicial del rango: "))
                    fin = int(input("Ingrese el valor final del rango: "))
                    numeros_en_rango = biblioteca.contar_numeros_en_rango(lista_numeros, inicio, fin)
                    print(f"CANTIDAD DE NUMEROS EN EL RANGO [{inicio}-{fin}]: {len(numeros_en_rango)}")
                except ValueError:
                    print("Por favor, ingrese valores numericos validos.")
                    
        elif opcion == 4:
            #Mostrar maximo y minimo en un rango
            if lista_numeros:
                try:
                    inicio = int(input("Ingrese el valor inicial del rango: "))
                    fin = int(input("Ingrese el valor final del rango: "))
                    numeros_en_rango = biblioteca.contar_numeros_en_rango(lista_numeros, inicio, fin)
                    if numeros_en_rango:
                        print(f"numero maximo en el rango: {max(numeros_en_rango)}")
                        print(f"Numero minimo en el rango: {min(numeros_en_rango)}")
                    else:
                        print(f"No hay numero en el rango [{inicio}-{fin}]")
                except ValueError:
                    print("Primero debe generar una lista de numeros (opcio 1).")
            else:
                print("Primero debe generar una lista de numeros (opcion 1).")
                        
        elif opcion == 5:
            #Generar matriz de caracteres alphanumericos
            matriz = biblioteca.generar_matriz_caracteres()
            print("Matriz Generada: ")
            for fila in matriz:
                print(fila)
                
        elif opcion == 6:
            #salir del programa
            print("Saliendo del programa...")
            break
        
        else:
            print("Opcopn no valida. Por Favor, elija una opcopn correcta.")
            
if __name__ == "__main__":
    menu()