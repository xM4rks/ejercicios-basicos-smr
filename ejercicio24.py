numero_secreto = 25
intentos = 0
max_intentos = 3


def pedir_solucion():
    while True:
        try:
            solucion = int(input("Adivina el numero secreto: "))
            if solucion < 0:
                print("Entrada no valida. Intentelo de nuevo.")
            else:
                return solucion
        except ValueError:
            print("Entrada no valida. Intentelo de nuevo.")


while intentos < max_intentos:
    intento = pedir_solucion()
    intentos += 1

    if intento < numero_secreto:
        print("Menor que el numero secreto.")
    elif intento > numero_secreto:
        print("Mayor que el numero secreto.")
    else:
        print("Correcto! Has adivinado el numero secreto.")
        break

    if intentos < max_intentos:
        print(f"Te quedan {max_intentos - intentos} intentos.")
    else:
        print("Te has quedado sin intentos socio/a :)")
