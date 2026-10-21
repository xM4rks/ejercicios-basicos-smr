
# Generador de facturas

iva = 0.21

def pedir_nombre():
    nombre = input("Introduzca el nombre del producto: ")
    return nombre

def pedir_precio():
    while True:
        try:
            precio = float(input("Introduzca el precio por unidad: "))
            if precio < 0:
                print("Entrada no válida. Vuelva a intentarlo.")
            else:
                return precio
        except ValueError:
            print("Entrada no válida. Vuelva a intentarlo.")

def pedir_cantidad():
    while True:
        try:
            cantidad = int(input("Introduzca la cantidad: "))
            if cantidad <= 0:
                print("La cantidad debe ser mayor que cero.")
            else:
                return cantidad
        except ValueError:
            print("Entrada no válida. Introduzca un número entero.")

nombre = pedir_nombre()
precio = pedir_precio()
cantidad = pedir_cantidad()

subtotal = precio * cantidad
importe_iva = subtotal * iva
total = subtotal + importe_iva

print("\n--- FACTURA ---")
print(f"Producto: {nombre}")
print(f"IVA (21%): {importe_iva:.2f} €")
print(f"Total: {total:.2f} €")
