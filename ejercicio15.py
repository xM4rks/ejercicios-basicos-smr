## Numeros y meses

def pedir_numero():
    numero = int(input("Introduzca un numero de mes: "))
    return numero

numero = pedir_numero()

if numero == 1:
    print("Enero tiene 31 dias.")
elif numero == 2:
    print("Febrero tiene 28 dias.")
elif numero == 3:
    print("Marzo tiene 31 dias.")
elif numero == 4:
    print("Abril tiene 30 dias.")
elif numero == 5:
    print("Mayo tiene 31 dias.")
elif numero == 6:
    print("Junio tiene 30 dias.")
elif numero == 7:
    print("Julio tiene 31 dias.")
elif numero == 8:
    print("Agosto tiene 31 dias.")
elif numero == 9:
    print("Septiembre tiene 30 dias.")
elif numero == 10:
    print("Octubre tiene 31 dias.")
elif numero == 11:
    print("Noviembre tiene 30 dias.")
elif numero == 12:
    print("Diciembre tiene 31 dias.")
else:
    print("Numero invalido.")