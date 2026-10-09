## Comprobar si la contraseña proporcionada es correcta

def pedir_contraseña():
    contraseña = input("Ingrese la contraseña:")
    return contraseña

contraseña_correcta = "1234"

contraseña_ingresada = pedir_contraseña()

if contraseña_ingresada == contraseña_correcta:
    print("Acceso permitido")
else:
    print("Acceso denegado")