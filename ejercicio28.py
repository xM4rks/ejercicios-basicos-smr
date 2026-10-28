## Retirada de dinero en cajero indicando billetes
## Cabe recalcar que para la resolución de este ejercicio se ha usado ayuda de IA

def pedir_cantidad():
    while True:
        try:
            cantidad = int(input("Introduzca la cantidad a retirar (€): "))

            if cantidad <= 0:
                print("Cantidad no válida. Inténtelo de nuevo.")
            elif cantidad % 5 != 0:
                print("La cantidad debe ser múltiplo de 5 €.")
            else:
                return cantidad

        except ValueError:
            print("Entrada no válida. Introduzca un número entero.")


def calcular_billetes(cantidad):
    billetes_50 = cantidad // 50
    cantidad = cantidad % 50

    billetes_20 = cantidad // 20
    cantidad = cantidad % 20

    billetes_10 = cantidad // 10
    cantidad = cantidad % 10

    billetes_5 = cantidad // 5

    print("\nBilletes que debe entregar:")

    print(f"{billetes_50} billetes de 50 €")
    print(f"{billetes_20} billetes de 20 €")
    print(f"{billetes_10} billetes de 10 €")
    print(f"{billetes_5} billetes de 5 €")


# Programa principal
cantidad = pedir_cantidad()
calcular_billetes(cantidad)
