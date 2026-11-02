# #20-Minimo&Maximo.py
# Descripción del programa: 
# Autor/es: Ángel Adrián Barragán Ruiz
# Fecha: 2026-10-22

import sys

print("Programa que encuentre el mínimo y máximo en un conjunto.")

min = 0
max = 0

while True:
    try:
        cantElementos = int(input("Ingresa el numero de elementos: "))
        while cantElementos < 2:
            cantElementos = int(input("Ingresa el numero de elementos: "))

        for i in range(0, cantElementos):
            num = float(input(f"Ingresa el elemento {i+1}: "))

            if i != 0:
                if num < min:
                    min = num
                elif num > max:
                    max = num
            else:
                min = num
                max = num

    except ValueError as error:
        print(f"ERROR: {error}")

    else:
        print(f"El mínimo es {min}")
        print(f"El máximo es {max}")
    finally:
        min = 0
        max = 0