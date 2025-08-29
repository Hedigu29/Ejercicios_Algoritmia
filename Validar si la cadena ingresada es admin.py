#Titulo: Validar si el usuario es admin

#Entradas
    # usuario: se ingresa el nombre de usuario

#Salidas
    # confirmación si el usuario está registrado correctamente

#Proceso
    # el programa determinará si el usuario coincide con el preestablecido

def validar_admin():
    usuario = input("Ingrese usuario: ")
    if usuario.lower() == "admin":
        print("Acceso permitido")
    else:
        print("Acceso denegado")
validar_admin ()