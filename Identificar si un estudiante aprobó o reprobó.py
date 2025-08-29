#Titulo: Identificar si un estudiante aprobó o reprobó

#Entradas
    # nota: nota que obtuvo el estudiante o aprendiz

#Salidas
    # confirmación de aprobación o reprobación del estudiante

#Proceso
    # el programa determina si el estudiante aprobó o reprobó según la calificación obtenida

nota = int(input("Ingrese la nota del estudiante: "))
if nota >= 60:
    print("El estudiante aprobó")
else:
    print("El estudiante reprobó")