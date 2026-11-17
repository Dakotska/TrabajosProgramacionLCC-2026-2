#Nombre del archivo: BlackJack.py
#Descripcion: Juego de black jack SIN APUESTAS.
#Autores: Garcia Valenzuela Laura Jazmine, Silva Contreras Sergio Gabriel.
#Fecha: 11/11/2026

"""
JUEGO DE BLACKJACK (un jugador contra la banca)

Como se juega:
    - Al empezar, el jugador y la banca reciben 2 cartas cada uno.
    - El jugador puede "Pedir carta" (recibe otra carta) o "Plantarse".
    - Cuando el jugador se planta, juega la banca: pide cartas mientras
      tenga menos de 17 puntos.
    - Gana quien tenga mas puntos sin pasarse de 21.

Puntos de las cartas:
    - Las cartas 2 a 10 valen su numero.
    - J, Q y K valen 10.
    - El As vale 11 o 1, lo que le convenga a la mano.

Blackjack natural (As + carta de 10 puntos en las dos primeras cartas):
    - Si solo el jugador lo tiene, gana inmediatamente.
    - Si solo la banca lo tiene, gana la banca inmediatamente.
    - Si los dos lo tienen, es empate.

Este juego NO tiene apuestas.

Biblioteca usada:
    - tkinter (viene incluida con Python, no hay que instalar nada)
    - random  (tambien viene incluida, sirve para barajar)

Para ejecutarlo:
    python BlackJack.py
"""

import tkinter as tk
import random

# Diccionario con el valor de cada carta.
# La llave es el numero o letra de la carta, y el valor es cuantos puntos vale.
# El As aparece como 11, pero mas abajo se convierte en 1 si la mano se pasa de 21.
valores = {"A": 11, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
           "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10}

# Los cuatro palos de la baraja: picas, corazones, diamantes y treboles.
palos = ["♠", "♥", "♦", "♣"]

# Variables globales: guardan el estado del juego mientras se juega.
mazo = []        # lista de cartas que quedan por repartir
jugador = []     # cartas que tiene el jugador
dealer = []      # cartas que tiene la banca
tapada = True    # True = la segunda carta de la banca esta boca abajo
mensaje = ""     # texto del resultado que se muestra en pantalla

def sumar(mano):
    """
    Calcula los puntos de una mano de cartas.

    Recibe:   una lista de cartas, por ejemplo ["K♠", "5♥"]
    Devuelve: el total de puntos (un numero entero)

    Los Ases valen 11, pero si la mano se pasa de 21 se van
    cambiando a 1 punto (uno por uno) hasta que ya no se pase.
    """
    total = 0
    ases = 0  # cuenta cuantos Ases hay en la mano

    for carta in mano:
        # carta[:-1] es la carta sin el ultimo caracter (el palo).
        # Por ejemplo, de "10♠" se queda con "10", y de "K♥" con "K".
        numero = carta[:-1]
        total = total + valores[numero]
        if numero == "A":
            ases = ases + 1

    # Si nos pasamos de 21 y hay Ases, cada As pasa de valer 11 a valer 1
    # (por eso se restan 10).
    while total > 21 and ases > 0:
        total = total - 10
        ases = ases - 1

    return total

def dibujar_carta(target_canvas, x, y, carta, tapar):
    """
    Dibuja una carta en la pantalla.

    Recibe:
        target_canvas - el lienzo donde se dibujara
        x, y          - posicion de la esquina de arriba a la izquierda de la carta
        carta         - el texto de la carta, por ejemplo "K♠"
        tapar         - True si la carta va boca abajo, False si se ve

    Cada carta mide 70 de ancho y 100 de alto.
    """
    ancho_carta = 80
    alto_carta = 110

    # Si la carta va tapada, se dibuja un rectangulo oscuro con un signo "?".
    if tapar:
        target_canvas.create_rectangle(x, y, x + ancho_carta, y + alto_carta, fill="#0e3a1f", outline="white", width=2)
        target_canvas.create_text(x + ancho_carta / 2, y + alto_carta / 2, text="?", font=("Arial", 24, "bold"), fill="white")
        return  # terminamos aqui, no hay que dibujar nada mas

    # Separamos la carta en numero y palo. Ejemplo: "K♠" -> "K" y "♠"
    numero = carta[:-1]   # todo menos el ultimo caracter
    palo = carta[-1]      # solo el ultimo caracter

    # Corazones y diamantes se dibujan en rojo; los demas en negro.
    color = "black"
    if palo == "♥" or palo == "♦":
        color = "red"

    # Fondo blanco de la carta con borde sutil.
    target_canvas.create_rectangle(x, y, x + ancho_carta, y + alto_carta, fill="white", outline="#bdc3c7", width=2)

    # Numero o letra en la esquina de arriba a la izquierda.
    target_canvas.create_text(x + 8, y + 10, text=numero, anchor="nw", font=("Arial", 12, "bold"), fill=color)

    # Palo grande en el centro de la carta.
    target_canvas.create_text(x + ancho_carta / 2, y + alto_carta / 2 + 2, text=palo, font=("Arial", 28), fill=color)

    # Numero o letra en la esquina de abajo a la derecha.
    target_canvas.create_text(x + ancho_carta - 8, y + alto_carta - 10, text=numero, anchor="se", font=("Arial", 12, "bold"), fill=color)


def actualizar():
    """
    Borra la pantalla y vuelve a dibujar todo:
    las cartas de la banca, el mensaje, y las cartas del jugador.

    Se llama cada vez que algo cambia (se reparte, se pide carta, etc.).
    """
    canvas_dealer.delete("all")  # borra lo del dealer
    canvas_jugador.delete("all") # borra lo del jugador

    # Banca (arriba)
    # Mientras la carta esta tapada no se muestran los puntos de la banca.
    if tapada:
        puntos = "?"
    else:
        puntos = str(sumar(dealer))
    label_dealer_puntos.config(text="Banca (Dealer)                                                   Puntos: " + puntos)

    # Dibujamos cada carta de la banca, una al lado de la otra.
    for i in range(len(dealer)):
        # Solo la segunda carta (posicion 1) va tapada, y solo si tapada es True.
        tapar = tapada and i == 1
        dibujar_carta(canvas_dealer, 10 + i * 85, 10, dealer[i], tapar)

    # Mensaje del resultado (en medio, grande y animado)
    label_estado.config(text=mensaje)

    # Jugador (abajo)
    label_jugador_puntos.config(text="Jugador                                                             Puntos: " + str(sumar(jugador)))
    for i in range(len(jugador)):
        dibujar_carta(canvas_jugador, 10 + i * 85, 10, jugador[i], False)

def terminar(texto):
    """
    Termina la partida.

    Recibe:   el mensaje del resultado, por ejemplo "Ganaste!"
    Hace:     destapa la carta de la banca, muestra el mensaje y
              desactiva los botones de "Pedir carta" y "Plantarse".
    """
    global tapada, mensaje  # "global" permite cambiar las variables de arriba
    tapada = False          # ahora se ve la carta de la banca
    mensaje = texto
    actualizar()
    boton_pedir.config(state="disabled")
    boton_plantarse.config(state="disabled")


def nueva():
    """
    Empieza una partida nueva.
    
    Crea y baraja el mazo, reparte 2 cartas al jugador y 2 a la banca,
    y revisa si alguien tiene blackjack natural.
    """
    global mazo, jugador, dealer, tapada, mensaje

    # Creamos el mazo: una carta por cada combinacion de numero y palo (52 cartas).
    mazo = []
    for n in valores:
        for p in palos:
         mazo.append(n + p)   # por ejemplo "K" + "♠" = "K♠"
    random.shuffle(mazo)         # barajamos

    # Repartimos. pop() saca la ultima carta del mazo y nos la da.
    jugador = [mazo.pop(), mazo.pop()]
    dealer = [mazo.pop(), mazo.pop()]

    # Reiniciamos el estado y activamos los botones.
    tapada = True
    mensaje = ""
    boton_pedir.config(state="normal")
    boton_plantarse.config(state="normal")
    actualizar()

    # Revisamos si hay blackjack natural.
    # Con solo 2 cartas, tener 21 puntos significa que es As + carta de 10.
    if sumar(jugador) == 21 and sumar(dealer) == 21:
        terminar("Empate, los dos tienen BlackJack ._.")
    elif sumar(jugador) == 21:
        terminar("BlackJack, ganaste :D ")
    elif sumar(dealer) == 21:
        terminar("La banca tiene BlackJack, perdiste :( ")

def pedir():
    """
    Se ejecuta al presionar "Pedir carta".

    El jugador recibe una carta mas. Si se pasa de 21, pierde.
    """
    jugador.append(mazo.pop())   # agregamos una carta a la mano del jugador
    actualizar()
    if sumar(jugador) > 21:
        terminar("Te pasaste, perdiste :(")


def plantarse():
    """
    Se ejecuta al presionar "Plantarse".

    Ahora juega la banca: pide cartas mientras tenga menos de 17 puntos.
    Despues se comparan los puntos para saber quien gano.
    """
    # La banca esta obligada a pedir mientras tenga menos de 17.
    while sumar(dealer) < 17:
        dealer.append(mazo.pop())

    # Comparamos resultados.
    if sumar(dealer) > 21:
        terminar("La banca se paso, ganaste :p")
    elif sumar(jugador) > sumar(dealer):
        terminar("Ganaste :D")
    elif sumar(jugador) < sumar(dealer):
        terminar("Perdiste :(")
    else:
        terminar("Empate ._.")

# Creamos la ventana principal.
ventana = tk.Tk()
ventana.title("BlackJack")
ventana.geometry("580x520")
ventana.config(bg="#145a32")
 
# Titulo del juego
titulo = tk.Label( ventana, text="♠ BLACKJACK ♣",  font=("Arial", 24, "bold"), bg="#145a32",  fg="#f1c40f")
titulo.pack(pady=10) 
    
# Zona de la banca
frame_dealer = tk.Frame(ventana, bg="#145a32")
frame_dealer.pack(fill="x", padx=20, pady=5)
label_dealer_puntos = tk.Label(frame_dealer, text="BANCA   Puntos: ?", font=("Arial", 14, "bold"), bg="#145a32", fg="white")
label_dealer_puntos.pack(anchor="w", pady=2)
canvas_dealer = tk.Canvas(frame_dealer, width=540, height=120, bg="#145a32", highlightthickness=0)
canvas_dealer.pack()

# Mensaje central
label_estado = tk.Label(ventana, text="", font=("Arial", 18, "bold"), bg="#145a32", fg="#f1c40f")
label_estado.pack(pady=5)

# Linea de separacion
tk.Frame(ventana, height=2, bg="#1e8449").pack(fill="x", padx=25, pady=5)

# Zona del jugador
frame_jugador = tk.Frame(ventana, bg="#145a32")
frame_jugador.pack(fill="x", padx=20, pady=5)
label_jugador_puntos = tk.Label(frame_jugador, text="JUGADOR   Puntos: 0", font=("Arial", 14, "bold"), bg="#145a32", fg="white")
label_jugador_puntos.pack(anchor="w", pady=2)
canvas_jugador = tk.Canvas(frame_jugador, width=540, height=120, bg="#145a32", highlightthickness=0)
canvas_jugador.pack()

# Botones
botones = tk.Frame(ventana, bg="#145a32")
botones.pack(pady=15)

# Cada boton ejecuta una funcion de arriba cuando se le da clic (command=...).
boton_pedir = tk.Button(botones, text="Pedir carta", font=("Arial", 11), command=pedir, width=12)
boton_pedir.pack(side="left", padx=10)
boton_plantarse = tk.Button(botones, text="Plantarse", font=("Arial", 11), command=plantarse, width=12)
boton_plantarse.pack(side="left", padx=10)
tk.Button(botones, text="Nueva partida", font=("Arial", 11), command=nueva, width=12, bg="#d4ac0d", fg="black").pack(side="left", padx=10)

# Empezamos la primera partida automaticamente al abrir el programa.
nueva()

# mainloop() mantiene la ventana abierta esperando a que el usuario haga clic.
ventana.mainloop()