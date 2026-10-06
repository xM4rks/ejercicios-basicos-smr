def pedir_numero():
    numero = int(input ("Introduce un numero: "))
    return numero

numero = pedir_numero()

if numero > 0:
    print("El numero es positivo")
elif numero < 0:
    print("El numero es negativo")
else:
    print("El numero es 0")