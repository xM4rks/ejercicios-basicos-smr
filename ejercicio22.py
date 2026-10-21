## Orden de menor a mayor de tres numeros con QuickSort

def pedir_numeros():
    contador = 0
    array = []

    while contador < 3:
        try:
            numero = int(input("Introduce un numero: "))

            if numero < 0:
                print("Dígito invalido. Intentelo de nuevo.")
            else:
                array.append(numero)
                contador += 1

        except ValueError:
            print("Digito invalido. Intentelo de nuevo.")

    return array

def quick_sort(array):
    if len(array) <= 1:
        return array

    pivote = array[len(array) // 2]

    menores = [x for x in array if x < pivote]
    iguales = [x for x in array if x == pivote]
    mayores = [x for x in array if x > pivote]

    return quick_sort(menores) + iguales + quick_sort(mayores)

array = pedir_numeros()
array = quick_sort(array)

print("Numero 1: ", array[0])
print("Numero 2: ", array[1])
print("Numero 3: ", array[2])