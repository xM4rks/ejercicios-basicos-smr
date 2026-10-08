## Datos personales

def pedir_nombre():
    nombre = input("Introduce tu nombre: ")
    return nombre

def pedir_edad():
    edad = input("Introduce tu edad: ")
    return edad

def pedir_ciudad():
    ciudad = input("Introduce tu ciudad: ")
    return ciudad

nombre = pedir_nombre()
edad = pedir_edad()
ciudad = pedir_ciudad()

print("Hola, me llamo " + nombre + " tengo " + edad + " años y vivo en " + ciudad)