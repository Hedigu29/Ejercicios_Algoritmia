#Titulo: determinar el tipo de triángulo

#Entradas
    # lado1: se ingresa el lado 1 del triángulo
    # lado2: se ingresa el lado 2 del triángulo
    # lado3: se ingresa el lado 3 del triángulo

#Salidas
    # confirmación del tipo de triangulo ingresado dependiendo de los lados del mismo

#Proceso
    # el programa determinara si los lados ingresados corresponden a un triángulo equilátero, isóceles o escaleno

def tipo_triangulo():
    lado1 = float(input("Ingrese lado 1: "))
    lado2 = float(input("Ingrese lado 2: "))
    lado3 = float(input("Ingrese lado 3: "))
    if lado1 == lado2 == lado3:
        print("El triángulo es equilátero")
    elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
        print("El triángulo es isósceles")
    else:
        print("El triángulo es escaleno")
tipo_triangulo()