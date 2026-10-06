def pedir_numero1():
    numero1 = int(input("Introduce el primer número: "))
    return numero1

def pedir_numero2():
    numero2 = int(input("Introduce el segundo número: "))
    return numero2

suma = pedir_numero1() + pedir_numero2()
resta = pedir_numero1() - pedir_numero2()
multiplicacion = pedir_numero1() * pedir_numero2()
division = pedir_numero1() / pedir_numero2()

print("suma: " + str(suma))
print("resta: " + str(resta))
print("multiplicación: " + str(multiplicacion))
print("división: " + str(division))