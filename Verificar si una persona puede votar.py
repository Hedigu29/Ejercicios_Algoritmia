#Titulo: verificar si una persona puede votar

#Entradas
    # edad: edad de la persona que quiere votar
    # nacionalidad: nacionalidad de la persona que quiere votar

#Salidas
    # confirmación de si es apto para votar o no

#Proceso
    # el programa determinará si la persona es apta para votar o no

edad = int(input("Ingrese su edad: "))
nacionalidad = input("Ingrese su nacionalidad: ")
if edad >= 18 and nacionalidad.lower() == "colombiana":
    print("Puede votar")
else:
    print("No puede votar")