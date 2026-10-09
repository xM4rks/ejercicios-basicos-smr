## calculadora que pide, numeros y operacion deseada

def pedir_numero1():
    numero1 = float(input("Ingrese el primer número: "))
    return numero1

def pedir_numero2():
    numero2 = float(input("Ingrese el segundo número: "))
    return numero2

def pedir_operacion():
    operacion = input("Ingrese el tipo de operacion deseada (+ - * /): ")
    return operacion

numero1 = pedir_numero1()
numero2 = pedir_numero2()
operacion = pedir_operacion()

if operacion == "+":
    resultado = numero1 + numero2
    print("Resultado: ", resultado)

elif operacion == "-":
    resultado = numero1 - numero2
    print("Resultado: ", resultado)

elif operacion == "*":
    resultado = numero1 * numero2
    print("Resultado: ", resultado)

elif operacion == "/":
    resultado = numero1 / numero2
    print("Resultado: ", resultado)

else:
    print("Datos introducidos inválidos")