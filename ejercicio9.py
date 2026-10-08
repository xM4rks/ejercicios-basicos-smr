## El mayor de 2 numeros

def pedir_numero():
    numero=int(input("Introduce un numero: "))
    return numero

numero1 = pedir_numero()
numero2 = pedir_numero()

if numero1 > numero2:
    print("El numero mayor es:", numero1)
else:
    print("El numero mayor es:", numero2)