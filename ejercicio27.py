## dar descuentos dependiendo de importe y tarjeta de socio

def pedir_importe():
    while True:
        try:
            importe = float(input("Introduzca el importe de su compra: "))
            if importe < 0:
                print("El importe introducido no es válido. Inténtelo de nuevo.")
            else:
                return importe
        except ValueError:
            print("Entrada introducida no válida. Inténtelo de nuevo.")

def pedir_tarjeta():
    while True:
        try:
            tarjeta = float(input("¿Tiene tarjeta de socio? Yes(1) No(2): "))
            if tarjeta < 0:
                print("Entrada no válida. Inténtelo de nuevo.")
            elif tarjeta > 2:
                print("Entrada no válida. Inténtelo de nuevo.")
            else:
                return tarjeta
        except ValueError:
            print("Entrada no válida. Inténtelo de nuevo")


def calcular_total(importe):
    descuento = 0

    if importe > 500:
        tarjeta = pedir_tarjeta()

        if tarjeta == "1":
            descuento = importe * 0.15

        else:
            descuento = importe * 0.05

    total = importe - descuento

    print("\n--- RESUMEN DE LA COMPRA ---")
    print(f"Subtotal: {importe:.2f} €")
    print(f"Descuento: {descuento:.2f} €")
    print(f"Precio final: {total:.2f} €")

importe = pedir_importe()
calcular_total(importe)