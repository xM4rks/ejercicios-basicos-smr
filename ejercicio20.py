## Tipo de triangulo

def pedir_lado1():
    while True:
        try:
            lado1 = float(input("Introduce el primer lado del triángulo: "))
            if lado1 <= 0:
                print("Dato no válido. Inténtelo de nuevo.")

            else:
                return lado1
        except ValueError:
            print("Dato no válido. Inténtelo de nuevo.")

def pedir_lado2():
    while True:
        try:
            lado2 = float(input("Introduce el segundo lado del triángulo: "))
            if lado2 <= 0:
                print("Dato no válido. Inténtelo de nuevo.")

            else:
                return lado2
        except ValueError:
            print("Dato no válido. Inténtelo de nuevo.")

def pedir_lado3():
    while True:
        try:
            lado3 = float(input("Introduce el tercer lado del triángulo: "))
            if lado3 <= 0:
                print("Dato no válido. Inténtelo de nuevo.")

            else:
                return lado3
        except ValueError:
            print("Dato no válido. Inténtelo de nuevo.")

lado1 = pedir_lado1()
lado2 = pedir_lado2()
lado3 = pedir_lado3()

if lado1 == lado2 and lado2 ==lado3:
    print("El triángulo es equilátero.")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("El triángulo es isósceles.")
else:
    print("El triángulo es escaleno.")