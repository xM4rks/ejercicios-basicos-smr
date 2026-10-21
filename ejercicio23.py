## Conversor de segundos a horas, minutos y segundos

def pedir_segundos():
    while True:
        try:
            segundos = float(input("Introduce los segundos: "))
            if segundos < 0:
                print("Entrada no válida. Intentelo de nuevo.")
            else:
                return segundos

        except ValueError:
            print("Entrada no válida. Intentelo de nuevo.")

segundos = pedir_segundos()

horas = int(segundos // 3600)
minutos = int((segundos % 3600) // 60)
segundos_restantes = int(segundos % 60)

print(f"{horas} horas")
print(f"{minutos} minutos")
print(f"{segundos_restantes} segundos")