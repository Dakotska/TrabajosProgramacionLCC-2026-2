# #11-PrimoCompuesto.py
# Descripción del programa: 
# Autor/es: Ángel Adrián Barragán Ruiz
# Fecha: 2026-10-15

import math

NumEntPos = int(input("Ingresa un numero entero positivo (>1): "))
while NumEntPos <= 1:
    NumEntPos = int(input("Ingresa un numero entero positivo(>1): "))

NumRaiz = math.ceil(math.sqrt(NumEntPos))
Contador = 1
Residuos = 0

while Contador <= NumRaiz:
    if math.remainder(NumEntPos, Contador) == 0:
        Residuos += 1
    Contador += 1

if Residuos > 2:
    print("El numero es compuesto")
else:
    print("El numero es primo")
