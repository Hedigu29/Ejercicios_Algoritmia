#Titulo: determinar si un número es múltiplo de 5

#Entradas
    # número: número que se comprobará si es múltiplo de 5

#Salidas
    # comprobación del número si es múltiplo de 5

#Proceso
    # el programa determina si el número es múltiplo de 5

def multiplo_5():
    numero = int(input("Ingrese un número: "))
    if numero % 5 == 0:
        print("El número es múltiplo de 5")
    else:
        print("El número no es múltiplo de 5")
multiplo_5 ()