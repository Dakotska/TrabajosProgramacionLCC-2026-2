# #9-NumerosRomanos.py
# Descripción del programa: 
# Autor/es: Ángel Adrián Barragán Ruiz
# Fecha: 2026-10-15

import sys

num = int(input("Ingresa un numero para convertir a números romanos: "))

if num > 0 & num < 4000:
    Millares = num // 1000
    Centenas = num % 1000 // 100
    Decenas = num % 100 // 10
    Unidades = num % 10

    #print(Millares, Centenas, Decenas, Unidades)

    cadenaRomana = ""

    # ! Caso no optimizado

    """match Millares:
        case 1:
            cadenaRomana = cadenaRomana + "M"
        case 2:
            cadenaRomana = cadenaRomana + "MM"
        case 3:
            cadenaRomana = cadenaRomana + "MMM"""

    cadenaRomana += Millares * "M"

    
else:
    print("Ingresa un numero entre 0 y 4000", file=sys.stderr)