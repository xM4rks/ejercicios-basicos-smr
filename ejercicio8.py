## Definir si un numero es par o impar

def pedir_numero():
    numero=int(input("Introduce un numero: "))
    return numero

numero = pedir_numero()

if numero % 2 == 0:
    print("El numero es par")
else:
    print("El numero es impar")