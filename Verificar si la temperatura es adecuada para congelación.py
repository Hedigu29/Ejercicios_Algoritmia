#Titulo: Verificar si la temperatura es adecuada para congelación

#Entradas
    # temperatura: temperatura que determinaá si es valida para el punto de congelación 

#Salidas
    # confirmación si la temperatura es adecuada para congelación 

#Proceso
    # el programa determinara si la temperatura ingresada es adecuada para congelación o no

def congelacion():
    temperatura = float(input("Ingrese la temperatura: "))
    if temperatura <= 0:
        print("La temperatura es adecuada para congelación")
    else:
        print("No es adecuada para congelación")
congelacion ()