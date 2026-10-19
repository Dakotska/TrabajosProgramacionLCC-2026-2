# #15-NumeroMagico.py
# Descripción del programa: 
# Autor/es: Ángel Adrián Barragán Ruiz
# Fecha: 2026-10-19

import random

print("¡Bienvenido al juego del numero mágico!")
print("Ingresa un numero entre los intervalos hasta encontrar el numero oculto.")

numR = random.randint(1,100)
completado = False
intervaloMin = 0
intervaloMax = 101
intentos = 0

while completado == False:
    print(f"Tus intervalos son: [{intervaloMin + 1}, {intervaloMax - 1}]")
    print(f"Tu intento actual es el {intentos}")
    num = int(input("Ingresa un numero: "))
    print("")

    if num > intervaloMin and num < intervaloMax:
        intentos += 1
        if num == numR:
            completado = True
        elif num > numR:
            intervaloMax = num
        elif num < numR:
            intervaloMin = num
    else:
        print("ERROR: leé bien tus intervalos.")
        continue

print("FELICIDADES GANASTE!!!")
print(f"El numero oculto es: {numR}")
print(f"Tus intentos totales fueron: {intentos}")