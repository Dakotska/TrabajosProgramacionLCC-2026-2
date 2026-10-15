# #10-PromedioWhile.py
# Descripción del programa: 
# Autor/es: Ángel Adrián Barragán Ruiz
# Fecha: 2026-10-15

import sys

print("Bienvenido al sistema de calculo de promedio.")
CalifTotales = int(input("Ingresa el numero de calificaciones a evaluar: "))
while CalifTotales < 1:
    CalifTotales = int(input("Ingresa el numero de calificaciones a evaluar: "))

CalifActual = 1
PromedioTotal = 0.0

while CalifActual <= CalifTotales:
    PromedioActual = float(input(f"Ingresa la calificación {CalifActual} (0-100): "))

    if PromedioActual < 0.0 or PromedioActual > 100.0:
        continue #Reinicia el ciclo

    PromedioTotal += PromedioActual
    CalifActual += 1

PromedioTotal /= CalifTotales

print(f"Tu total de calificaciones es de {CalifTotales}")
print(f"El promedio total es de {PromedioTotal}.")