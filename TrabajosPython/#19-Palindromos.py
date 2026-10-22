# #19-Palindromos.py
# Descripción del programa: 
# Autor/es: Ángel Adrián Barragán Ruiz
# Fecha: 2026-10-22

import sys

print("Bienvenido a la calculadora de palíndromos")

cadenaR = ""
cadenaSE = ""

while True:
    try:
        cadena = str(input("Ingresa una cadena de caracteres: ").lower())
        while len(cadena) < 1 :
            cadena = str(input("Ingresa una cadena de caracteres: ").lower())

        print(len(cadena))
    except ValueError as error:
        print("Ingresa una cadena de caracteres.")

    else:
        for i in cadena:
            if i not in(" ", ",", "á", "é", "í", "ó", "ú", "ü"):
                cadenaSE += i
            elif i == "á":
                cadenaSE += "a"
            elif i == "é":
                cadenaSE += "e"
            elif i == "í":
                cadenaSE += "i"
            elif i == "ó":
                cadenaSE += "o"
            elif i == "ú" or i == "ü":
                cadenaSE += "u"
            else:
                cadenaSE += ""

            print(cadenaSE)

        for j in range(len(cadenaSE), 0, -1):
            cadenaR += cadenaSE[j-1]

        if cadenaSE == cadenaR:
            print(f"'{cadena}' es un palíndromo.")
        else:
            print(f"'{cadena}' no es un palíndromo.")

    finally:
        cadenaSE == ""
        cadenaR == ""
        cadena == ""