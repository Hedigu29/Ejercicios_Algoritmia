#Titulo: determinar si un número es negativo

#Entradas
    # número: el número que se quiere comprobar si es negativo o positivo

#Salidas
    # comprobación de número negativo, positivo o cero

#Proceso
    # el programa determina si el número ingresado es negativo positivo o cero

numero = float (input("Escribe un número: "))
if numero == 0:
    print("Cero")
elif numero < 0:
    print("Negativo")
else:
    print("Positivo")