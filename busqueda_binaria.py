#lista_ordenada = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

def busqueda_binaria(lista, x):
    izq = 0
    der = len(lista)-1
    pasos = 0 # Cantidad de pasos necesarios para obtener el valor buscado

    while izq <= der:
        medio = (izq+der)//2
        pasos = pasos + 1
        print("DEBUG:", "izq: ", izq, "der:", der, "medio: ", medio, "Pasos: ", pasos)

        if lista[medio] == x:
            return medio
        
        elif lista[medio] > x:
            der = medio - 1

        else:
            izq = medio + 1

    return -1


lista = input("Dame los elementos de una lista ordenada: ").split()

while lista != []:

    x = input("Valor Buscado?: ")
    resultado = busqueda_binaria(lista, x)

    print("### ------ Resultado Busqueda Binaria ------- ###\n")

    if resultado != -1:
        print("El elemento", x, "se encuentra en la posición: ", resultado, "de la lista: ", lista)

    else:
        print("El elemento: ", x ,"no se encuetra en la lista!!!", resultado,)

    print("\n")
    lista = input("Dame los elementos de una lista ordenada: ").split()
