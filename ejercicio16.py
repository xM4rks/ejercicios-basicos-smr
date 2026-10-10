
saldo = 1000

while True:
    print("\n-- CAJERO AUTOMÁTICO --")
    print("1. Consultar saldo")
    print("2. Ingresar dinero")
    print("3. Retirar dinero")
    print("4. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        print(f"Saldo actual: {saldo} €")
        print("Muchas gracias por utilizar nuestros servicios :)")
        break

    elif opcion == "2":

            cantidad = float(input("Cantidad a ingresar: "))

            if cantidad > 0:
                saldo += cantidad
                print("Ingreso realizado correctamente.")
                print(f"Saldo actual: {saldo} €")
                print("Muchas gracias por utilizar nuestros servicios :)")
                break
            else:
                print("La cantidad debe ser mayor que 0.")
                break

    elif opcion == "3":
            cantidad = float(input("Introduce la cantidad a retirar: "))

            if cantidad <= 0:
                print("La cantidad debe ser mayor que 0.")
                break

            elif cantidad > saldo:
                print("Error. Saldo insuficiente.")
                break

            else:
                saldo -= cantidad
                print("Retirada realizada correctamente.")
                print(f"Saldo actual: {saldo} €")
                print("Muchas gracias por utilizar nuestros servicios :)")
                break

    elif opcion == "4":
        print("Hasta pronto.")
        print("Muchas gracias por utilizar nuestros servicios :)")
        break

    else:
        print("Opción no válida. Inténtalo de nuevo.")
