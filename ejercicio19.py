## Información del podio de una carrera

def pedir_1():
    while True:
        corredor_uno = float(input("Introduce el tiempo del primer puesto: "))
        if corredor_uno < 0:
            print("Tiempo no válido.")

        else: 
            return corredor_uno
def pedir_2():
     while True:
        corredor_dos = float(input("Introduce el tiempo del segundo puesto: "))
        if corredor_dos < 0:
                 print("Tiempo no válido.")
    
        else: 
                 return corredor_dos

def pedir_3():
     while True:
        corredor_tres = float(input("Introduce el tiempo del tercer puesto: "))
        if corredor_tres < 0:
                 print("Tiempo no válido.")
    
        else: 
                 return corredor_tres

corredor_uno = pedir_1()
corredor_dos = pedir_2()
corredor_tres = pedir_3()

if corredor_uno < corredor_dos and corredor_uno < corredor_tres:
      print("Ganador: Corredor 1")
elif corredor_dos < corredor_uno and corredor_dos < corredor_tres:
      print("Ganador: Corredor 2")
else:
      print("Ganador: Corredor 3")