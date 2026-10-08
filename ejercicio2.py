## Operaciones matemáticas básicas

def pedir_numero1():
    numero1 = int(input("Introduce el primer número: "))
    return numero1

def pedir_numero2():
    numero2 = int(input("Introduce el segundo número: "))
    return numero2

numero1= pedir_numero1()
numero2= pedir_numero2()

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2

print("suma: " + str(suma))
print("resta: " + str(resta))
print("multiplicación: " + str(multiplicacion))
print("división: " + str(division))