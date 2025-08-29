#Titulo: determinar permisos de administrador con código

#Entradas
    # código: código de acceso

#Salidas
    # permiso concedido o denegado dependiendo del código de acceso

#Proceso
    # el programa otorga el acceso a un usuario si el código es correcto 

def permiso_codigo():
    codigo = int(input("Ingrese el código de administrador: "))
    if codigo == 12345:
        print("Acceso concedido")
    else:
        print("Acceso denegado")
permiso_codigo()