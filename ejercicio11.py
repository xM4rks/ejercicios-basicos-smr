## Aplicar descuento del 10% si el precio del producto es mayor a 100

def pedir_precio():
    precio = float(input("Ingrese el precio del producto: "))
    return precio

precio = pedir_precio()

if precio > 100:
    descuento = precio * 0.10
    precio_final = precio - descuento
    print("Se le ha aplicado un descuento del 10%. Precio final:", precio_final)

else:
    print("No alcanza el mínimo para aplicar descuento. Precio final: ", precio)