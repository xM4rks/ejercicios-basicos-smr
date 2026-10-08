## Area del rectangulo

def pedir_base():
    base = int(input("Introduce la base "))
    return base

def pedir_altura():
    altura = int(input("Introduce la altura "))
    return altura

base = pedir_base()
altura = pedir_altura()

area = base * altura

print ("El area del rectangulo es: " + str(area))