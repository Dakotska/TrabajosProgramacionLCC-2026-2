# #8-NumeroDeDias.py
# Descripción del programa: 
# Autor/es: Ángel Adrián Barragán Ruiz
# Fecha: 2026-10-15

import sys

month = int(input("Ingresa un mes entre el 1 y el 12 (enero, ..., diciembre)"))

match month:
    case 1:
        print("Enero, 31 días.")
    case 2:
        year = int(input("Ingresa un año mayor a 1582: "))
        
        if year > 1582:
            if year % 400 == 0 | year % 4 == 0 & year % 100 != 0:
                print("Febrero, 29 días")
            else:
                print("Febrero, 28 días")
        else:
            print("Ingresa un año mayor a 1582.")
    case 3:
        print("Marzo, 31 días")
    case 4:
        print("Abril, 30 días")
    case 5:
        print("Mayo, 31 días")
    case 6:
        print("Junio, 30 días")
    case 7:
        print("Julio, 31 días")
    case 8:
        print("Agosto, 31 días")
    case 9:
        print("Septiembre, 30 días")
    case 10:
        print("Octubre, 31 días")
    case 11:
        print("Noviembre, 30 días")
    case 12:
        print("Diciembre, 31 días")
    case _:
        print("Ingresa un valor entre 1 y 12 según el numero de mes.", file=sys.stderr)