# #17-FechaOrdenada.py
# Descripción del programa: 
# Autor/es: Ángel Adrián Barragán Ruiz
# Fecha: 2026-10-20

import sys

print("Bienvenido al algoritmo gestor de fechas.")

while True:
    try:
        year = int(input("Ingresa un anio desde 1900 hasta 2026: "))
        while year < 1900 or year > 2026 or len(str(year)) != 4:
            year = int(input("*ERROR: Ingresa un anio desde 1900 hasta 2026*: "))

        month = int(input("Ingresa un mes desde 1 hasta 12: "))
        while month < 1 or month > 12 or (len(str(month)) != 1 and len(str(month)) != 2):
            month = int(input("ERROR: Ingresa un mes desde 1 hasta 12: "))

        match month:
            case 1 | 3 | 5 | 7 | 8 | 10 | 12:
                print("Tu mes tiene 31 Días.")
                monthDays = 31
            case 4 | 6 | 9 | 11:
                print("Tu mes tiene 30 Días")
                monthDays = 30
            case 2:
                if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
                    print("Tu mes tiene 29 Días")
                    monthDays = 29
                else:
                    print("Tu mes tiene 28 Días")
                    monthDays = 28

        day = int(input(f"Ingresa un dia desde 1 hasta {monthDays}: "))
        while day < 1 or day > monthDays or (len(str(day)) != 1 and len(str(day)) != 2):
            day = int(input(f"ERROR: Ingresa un dia desde 1 hasta {monthDays}: "))

    except ValueError as error:
        print(f"*ERROR: {error}*", file=sys.stderr)
        print("*Ingresa números enteros positivos, no se acepta texto ni números flotantes.*")

    except:
        print("*Error general, lea bien las instrucciones del programa.*")

    else:
        print(f"{str(year)[-2:]}{month:>02d}{day:>02d}")
        break