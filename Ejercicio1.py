#programa para obtener las iniciales en mayusculas

#Entradas

    #Nombre Nombre de la persona,
    #Apellido Apellido de la persona

#Salidas
    #Iniciales en Mayusculas

#Proceso
    #Pide el nombre de la persona, extrae el primer caracter de cada nombre e imprime en mayusculas las iniciales

#pedir nombre y apellido
nombre = input("ingresa tu nombre: ")
apellido = input("ingresa tu apellido: ")
#tomar la primera letra de cada uno y ponerlo en mayusculas
iniciales= nombre [0] .upper () + apellido [0].upper ()
#Mostrar resultados
print("tus iniciales son: ", iniciales)