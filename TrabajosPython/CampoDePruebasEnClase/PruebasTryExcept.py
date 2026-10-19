import sys

try:
    n = int(input("Dame un numero entero: "))

    print("Numero capturado ", n)
except ValueError:
    print("ERROR: No es un numero entero", file=sys.stderr)