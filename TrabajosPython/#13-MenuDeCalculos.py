# #13-MenuDeCalculos.py
# Descripción del programa: 
# Autor/es: Ángel Adrián Barragán Ruiz
# Fecha: 2026-10-15

import sys
import math
import time

while True:
    print("Opciones a elegir")
    print("(0) Salir del programa")
    print("(1) Area de un triangulo")
    print("(2) Area de un circulo")
    print("(3) Area de un rectángulo")
    opcion = int(input("Ingresa tu opción: "))
    if opcion < 0 or opcion > 3:
        print("")
        print("*Ingresa una opción valida del 0 al 4*", file=sys.stderr)
        continue

    print("")
    match opcion:
        case 0:
            break
        case 1:
            print("Bienvenido a la calculadora de area de un triangulo.")
            base = int(input("Ingresa la base del triangulo: "))
            altura = int(input("Ingresa la altura del triangulo: "))

            print("La area del triangulo es de ", (base*altura)/2, " u² \n")
            time.sleep(1.5)
        case 2:
            print("Bienvenido a la calculadora de area de un circulo.")
            radio = int(input("Ingresa el radio de tu circulo: "))

            print("El area de tu circulo es de ", math.pi * radio ** 2, " u² \n")
            time.sleep(1.5)
        case 3:
            print("Bienvenido a la calculadora de area de un rectángulo.")
            base = int(input("Ingresa la base del triangulo: "))
            altura = int(input("Ingresa la altura del triangulo: "))

            print("El area del rectángulo es de: ", base*altura, " u² \n")
            time.sleep(1.5)