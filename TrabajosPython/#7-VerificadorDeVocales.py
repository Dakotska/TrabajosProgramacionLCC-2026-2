# #7-VerificadorDeVocales.py
# Descripción del programa: 
# Autor/es: Ángel Adrián Barragán Ruiz
# Fecha: 2026-10-15

import sys

car = str(input("Ingresa un carácter: ").upper())

# ! No optimizado
"""match car:
    case "a" | "e" | "i" | "o" | "u" | "á" | "é" | "í" | "ó" | "u" | "ü" | "A" | "E" | "I" | "O" | "U" | "Á" | "É" | "Í" | "Ó" | "Ú" | "Ü":
        print("Tu carácter es una vocal.")
    case _: 
        print("Error: Tu carácter no es una vocal", file=sys.stderr)"""

if len(car) == 1:
    match car:
        case "A" | "E" | "I" | "O" | "U" | "Á" | "É" | "Í" | "Ó" | "Ú" | "Ü":
            print("Tu carácter es una vocal.")
        case _:
            print("Tu carácter no es una vocal.", file=sys.stderr)
else:
    print("Ingresa un solo carácter", file=sys.stderr)