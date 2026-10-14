## Cálculo de la entrada de cine dependiendo de la edad

def pedir_edad():
    while True:
        try:
            edad = float(input("Introduzca la edad del espectador: "))
            if edad < 0:
                print("Edad inválida. Por favor, introduzca una edad positiva.")

            else:
                return edad
        except ValueError:
            print("Edad inválida. Por favor, introduzca una edad válida.")

edad_espectador = pedir_edad()

if edad_espectador < 5:
    precio = 0
    print("Total:", precio, "€")

elif 5 <= edad_espectador < 17:
    precio = 5
    print("Total:", precio, "€")

elif 18 <= edad_espectador < 64:
    precio = 10
    print("Total:", precio, "€")

else: 
    precio = 6
    print("Total:", precio, "€")