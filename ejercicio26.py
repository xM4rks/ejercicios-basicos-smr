## Pide un año y determina si es bisiesto


def año_bisiesto(año):
    if año % 4 == 0:
        print("Tu año es bisiesto")
    elif año % 100 == 0 and año % 400 == 0:
        print("Tu año es bisiesto")
    else:
        print("Tu año NO es bisiesto")

def pedir_año():
    while True:
        try:
            año = int(input("Introduce un año: "))
            if año < 0:
                print("Año inválido. Inténtelo de nuevo.")
            else:
                return año
        except ValueError:
            print("Entrada no válida. Inténtelo de nuevo.")

año_bisiesto(pedir_año())

