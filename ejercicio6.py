def pedir_edad():
    edad = int(input("Introduce tu edad: "))
    return edad

edad = pedir_edad()

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")