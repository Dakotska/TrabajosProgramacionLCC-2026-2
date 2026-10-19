# #6-PiedraPapeloTijera.py
# Descripción del programa: 
# Autor/es: Ángel Adrián Barragán Ruiz
# Fecha: 2026-10-15

import random as rn

pc = rn.randint(1,3)

print("¡Bienvenido al juego de Piedra Papel o Tijera!")
print("Ingresa un numero del 1 al 3 y juega contra la cpu")
print("Buena suerte")
print("")
print("(1) piedra")
print("(2) papel")
print("(3) tijera")
jugador = int(input("Ingresa tu opción: "))

if jugador >= 1 and jugador <= 3:
    if pc == jugador:
        print("¡Empate!")
    elif pc == 1 and jugador == 2 or pc == 2 and jugador == 3 or pc == 3 and jugador == 1:
        print("¡Ganaste! :)")
    else:
        print("¡Perdiste! :(")
    
    print("")
    print(f"Elegiste: {jugador} y la cpu: {pc}")
else:
    print("Ingresa un numero entre 1 y 3.")