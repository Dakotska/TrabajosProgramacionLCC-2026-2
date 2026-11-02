# #16-EnteroFactorial.py
# Descripción del programa: 
# Autor/es: Ángel Adrián Barragán Ruiz
# Fecha: 2026-10-19

import sys

i = 1
factorial = 1

while True:
    try:
        num = int(input("Ingresa un numero entero positivo: "))
        while num < 1:
            num = int(input("Ingresa un numero entero positivo: "))
    except ValueError as error:
        print(f"**Error: {error}", file=sys.stderr)
        print("**Ingresa un numero entero, no se aceptan cadenas o números con decimal.")
    else:
        while i < num:
            i += 1
            factorial = factorial * i
        #print(factorial)
        print(factorial, file=sys.set_int_max_str_digits(100000))
