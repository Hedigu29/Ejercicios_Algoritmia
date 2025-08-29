#Titulo: Comprobar si un año es bisiesto

#Entradas
    #año: año que se quiere comprobar

#Salidas
    #comprobación de año bisiesto

#Proceso
    #el programa determinará si el año ingresado es bisiesto o no 

def año_bisiesto():
    año = int(input("Ingrese un año: "))
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        print("El año es bisiesto")
    else:
        print("El año no es bisiesto")
año_bisiesto()
