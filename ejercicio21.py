## Cálculo de impuestos a pagar según salario

def pedir_salario():
    while True:
        try:
            salario = float(input("Introduzca su salario mensual: "))
            if salario < 0:
                print("Dígito inválido. Inténtelo de nuevo.")
            else:
                return salario
        except ValueError:
            print("Dígito inválido. Inténtelo de nuevo.")

salario = pedir_salario()

if salario <= 1000:
    impuesto = 0
    print("Salario bruto: ${:.2f}".format(salario))
    print("Porcentaje de impuestos: 0%")
    print("Cantidad descontada: ${:.2f}".format(impuesto))
    print("Salario neto: ${:.2f}".format(salario - impuesto))

elif salario <= 2000:
    impuesto = salario *  0.10
    print("Salario bruto: ${:.2f}".format(salario))
    print("Porcentaje de impuestos: 10%")
    print("Cantidad descontada: ${:.2f}".format(impuesto))
    print("Salario neto: ${:.2f}".format(salario - impuesto))

else:
    impuesto = salario * 0.20
    print("Salario bruto: ${:.2f}".format(salario))
    print("Porcentaje de impuestos: 20%")
    print("Cantidad descontada: ${:.2f}".format(impuesto))
    print("Salario neto: ${:.2f}".format(salario - impuesto))