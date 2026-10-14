## Cálculo de descuento en el envío a domicilio dependiendo del importe de la compra

def pedir_importe():
    while True:
        try:
            importe = float(input("Introduzca el importe de la compra: "))
            if importe < 0:
                print("Importe inválido. Por favor, introduzca un importe positivo.")

            else:
                return importe
        except ValueError:
            print("Importe inválido. Por favor, introduzca un número válido.")

importe_compra = pedir_importe()

if importe_compra < 50:
    gastos_envio = 5
    print("Gastos de envio: 5 €")
    print("Total:", importe_compra + gastos_envio, "€")

elif 50 <= importe_compra < 99.99:
    gastos_envio = 2
    print("Gastos de envio: 2 €")
    print("Total:", importe_compra + gastos_envio, "€")

else: 
    gastos_envio = 0
    print("Gastos de envio: 0 €")
    print("Total:", importe_compra + gastos_envio, "€")