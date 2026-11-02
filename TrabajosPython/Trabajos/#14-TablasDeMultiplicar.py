# #14-TablasDeMultiplicar.py
# Descripción del programa: 
# Autor/es: Ángel Adrián Barragán Ruiz
# Fecha: 2026-10-19

print("Bienvenido a la calculadora de tablas de multiplicar desde 1 al 10.")
numT = int(input("Ingresa el numero a multiplicar (cualquier natural): "))

if numT > 0:
    i = 1

    while i <= 10:
        print(f"{numT} * {i} = {numT * i}")
        i += 1