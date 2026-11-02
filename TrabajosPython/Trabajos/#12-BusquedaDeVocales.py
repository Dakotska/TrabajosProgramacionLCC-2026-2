# #12-BusquedaDeVocales.py
# Descripción del programa: 
# Autor/es: Ángel Adrián Barragán Ruiz
# Fecha: 2026-10-15

print("Bienvenido al buscador de vocales!")
frase = str(input("Ingresa una frase para verificar si hay alguna vocal: ").upper())
lenFrase = len(frase)

i = 0 
cA = ""
Find = False

while i < lenFrase: 
    cA = frase[i]
    match cA:
        case "A" | "E" | "I" | "O" | "U" | "Á" | "É" | "Í" | "Ó" | "Ú" | "Ü":
            Find = True
            break
    i += 1

if Find == True:
    print(f"La primer vocal de tu frase es: {cA}")
else:
    print("Tu frase no tiene vocales")