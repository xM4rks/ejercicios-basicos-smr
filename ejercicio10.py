## Pide una nota entre 0 y 10 y muestra la calificación correspondiente:

def pedir_nota():
    nota = float(input("Introduce la nota que has sacado (0-10): "))
    return nota

nota = pedir_nota()

if nota < 0 or nota <4.99:
    print("Suspenso")
elif nota >=5 and nota <5.99:
    print("Suficiente")
elif nota >=6 and nota <6.99:
    print("Bien")
elif nota >=7 and nota <8.99:
    print("Notable")
elif nota >=9 and nota <=10:
    print("Sobresaliente")
else:
    print("Nota no válida")