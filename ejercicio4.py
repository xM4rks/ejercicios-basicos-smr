## Cambio de celsius a fahrenheit

def pedir_celsius():
    celsius = float(input("Introduce la temperatura en Celsius: "))
    return celsius

celsius = pedir_celsius()

conversion = (float(celsius) * 9 / 5) + 32

print(str(celsius) + " grados Celsius son " + str(conversion) + " en Fahrenheit")