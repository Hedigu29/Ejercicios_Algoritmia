#Titulo: Determinar si un número está entre el rango de -100 a 100

#Entradas
    # numero: numero al que se le hará la comprobacion si está entre el rango

#Salidas
    # comprobacion del numero dentro del rango determinado

#Proceso
    # el programa determinará si el numero ingresado esta dentro del rango -100 a 100

def numero_rango():
    numero = int(input("Ingrese un número: "))
    if numero > 100 or numero < -100:
        print("El número cumple la condición")
    else:
        print("El número no cumple la condición")
numero_rango()