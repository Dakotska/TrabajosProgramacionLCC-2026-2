"""
Nombre del archivo: BlackJack.py
Descripción del programa: Programa que simula el juego de BlackJack o 21, utilizando una librería de interfaz gráfica (sin apuestas).
Autores: Khristo Ricardo Rodriguez Valencia / Ángel Adrián Barragán Ruíz
Fecha: 10/11/2026
Grupo: 7
"""

# incorporación de librerías.

import tkinter as tk
from random import shuffle
import time

# Definición de variables globales.

DENOMINACIONES = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
PALOS = ["♥", "♦", "♣", "♠"]
baraja = []
crupier = []
segundaCartaCrupier = []
puntCrupier = 0
jugador = []
puntJugador = 0

# ╔═══════ ≪ ° <Funcion Iniciar Juego> ° ≫ ═══════╗

def InicioJuego() -> None:
    """
        Inicializa la partida repartiendo dos cartas de manera alternada al crupier y al jugador.
        Limpia la mesa, restablece las variables globales y reparte las manos iniciales.
        Posteriormente, verifica si con la mano inicial hay algún Blackjack y decide al ganador; de lo contrario, sigue el juego normal.

        Globals:
            PALOS (list): Palos predefinidos de las cartas.
            DENOMINACIONES (list): Denominaciones predefinidas de las cartas.
            baraja (list): Baraja completa de 52 combinaciones según los palos y denominaciones.
            crupier (list): Mano del crupier.
            segundaCartaCrupier (list): Segunda carta del crupier, la cual está oculta.
            puntCrupier (int): Puntuación total actual del crupier.
            jugador (list): Mano del jugador.
            puntJugador (int): Puntuación total actual del jugador.
    """
    global PALOS, DENOMINACIONES, baraja, crupier, segundaCartaCrupier, puntCrupier, jugador, puntJugador

    # Se acomodan los botones en la interfaz y se habilitan para el usuario.
    menu.place_forget()
    textoMenu.grid_forget()
    botonInicio.grid_forget()
    botonSalir.grid_forget()
    botonPedir.config(state="normal")
    botonPlantar.config(state="normal")
    for dibujo in marcoManoCrupier.winfo_children():
        dibujo.destroy()
    for dibujo in marcoManoJugador.winfo_children():
        dibujo.destroy()
    barraPuntJugador.config(bg="green")

    # Se restablecen las variables globales para la nueva partida y se baraja el mazo.
    baraja = [(den, palo) for palo in PALOS for den in DENOMINACIONES]
    crupier = []
    segundaCartaCrupier = []
    puntCrupier = 0
    jugador = []
    puntJugador = 0

    shuffle(baraja)

    # Se reparten cuatro cartas de forma alternada: dos para el jugador y dos para el crupier.
    for i in range(2):
        JalarCarta(True)
        JalarCarta(False)

    # Se verifica si algún participante obtuvo Blackjack de manera natural.
    # Si es así, se muestran las cartas del crupier, se determina el ganador y se finaliza la partida.
    estado = VerificarBlackjack()
    if estado != 0:
        hijos = marcoManoCrupier.winfo_children()
        hijos[1].destroy()
        MostrarCarta(segundaCartaCrupier[0], False)
        textoPuntCrupier.configure(text=f"{puntCrupier}/21")
        bordeBarraCrupier.columnconfigure(0, weight=puntCrupier)
        bordeBarraCrupier.columnconfigure(1, weight=(21 - puntCrupier))
        barraPuntCrupier.configure(bg="green")
        if estado == 1:
            MostrarFinJuego(1)
        elif estado == 2:
            MostrarFinJuego(2)
        elif estado == 3:
            MostrarFinJuego(3)

# ╚═══════ ≪ ° </Funcion Iniciar Juego> ° ≫ ═══════╝

# ╔═══════ ≪ ° <Funcion Pedir> ° ≫ ═══════╗

def Pedir():
    """
        Función ejecutada por el botón "Pedir".
        Le entrega una carta adicional al jugador y evalúa si este excedió los 21 puntos.
        De ser así, se revela la carta oculta del crupier y la partida termina en victoria para la casa.
    """
    # Llama a la función JalarCarta y asigna una nueva carta al jugador.
    JalarCarta(True)

    # Verifica si el jugador excedió el puntaje máximo. De ser así, muestra las cartas del crupier y finaliza el juego.
    if VerificarSobrepuntaje() == 2:
        hijos = marcoManoCrupier.winfo_children()
        hijos[1].destroy()
        MostrarCarta(segundaCartaCrupier[0], False)
        textoPuntCrupier.configure(text=f"{puntCrupier}/21")
        bordeBarraCrupier.columnconfigure(0, weight=puntCrupier)
        bordeBarraCrupier.columnconfigure(1, weight=(21 - puntCrupier))
        barraPuntCrupier.configure(bg="green")
        MostrarFinJuego(1)

    if VerificarBlackjack() == 2:
        botonPedir.configure(state="disabled")

# ╚═══════ ≪ ° </Funcion Pedir> ° ≫ ═══════╝

# ╔═══════ ≪ ° <Funcion Plantarse> ° ≫ ═══════╗

def Plantarse() -> None:
    """
        Función ejecutada por el botón "Plantar".
        Da por terminado el turno del jugador. Revela la carta oculta del crupier y
        hace que este pida cartas obligatoriamente hasta alcanzar al menos 17 puntos.
        Posteriormente, verifica los puntajes finales y decide al ganador.
    """

    # Se deshabilitan los botones de acción ("Pedir" y "Plantar").
    botonPedir.config(state="disabled")
    botonPlantar.config(state="disabled")

    # Se muestra la segunda carta del crupier en la interfaz.
    hijos = marcoManoCrupier.winfo_children()
    hijos[1].destroy()
    MostrarCarta(segundaCartaCrupier[0], False)

    # El crupier toma cartas adicionales de la baraja mientras su puntuación total sea menor a 17 puntos.
    if puntCrupier >= 17:
        textoPuntCrupier.configure(text=f"{puntCrupier}/21")
        bordeBarraCrupier.columnconfigure(0, weight=puntCrupier)
        bordeBarraCrupier.columnconfigure(1, weight=(21 - puntCrupier))
        barraPuntCrupier.configure(bg="green")
    while puntCrupier < 17:
        JalarCarta(False)

    # Se verifica si el crupier excede los 21 puntos. Posteriormente, se evalúan los puntajes finales
    # para determinar si hubo empate, victoria del jugador o victoria del crupier.
    if VerificarSobrepuntaje() == 1:
        MostrarFinJuego(2)
    estado = VerificarPuntajesFinales()
    if estado == 3:
        MostrarFinJuego(3)
    elif estado == 1:
        MostrarFinJuego(1)
    elif estado == 2:
        MostrarFinJuego(2)

# ╚═══════ ≪ ° </Funcion Plantarse> ° ≫ ═══════╝

# ╔═══════ ≪ ° </> ° ≫ ═══════╗

def JalarCarta(esJugador: bool):
    """
        Agrega una carta de la baraja a la mano del jugador o del crupier.

        Actualiza las variables globales correspondientes (`jugador` o `crupier`),
        ajusta el puntaje y renderiza la barra de progreso en la interfaz.

        Parameters:
            esJugador (bool): `True` si el que pide la carta es el jugador, `False` si es el crupier.

        Raises:
            TypeError: Si el argumento `esJugador` no es un valor booleano.

        Examples:
            >>> JalarCarta(True)
            >>> JalarCarta(False)
    """
    # Manejo de excepciones para validar el tipo de dato.
    if not isinstance(esJugador, bool):
        raise TypeError("ERROR: El argumento 'esJugador' no es un valor booleano.")

    # Definición de variables globales.
    global crupier, jugador, puntCrupier, puntJugador

    # Evalúa si la carta solicitada es para el jugador o para el crupier.
    if esJugador:
        # Se extrae una carta de la baraja, se agrega a la mano del jugador y se renderiza en la interfaz.
        carta = baraja.pop()
        jugador.append(carta)
        MostrarCarta(carta, True)

        # Si la carta es un As, Jota, Reina o Rey, se llama a la función ArreglarValores para ajustar
        # su valor antes de sumarlo a la puntuación del jugador.
        if carta[0] in "AJQK":
            jugador.pop()
            jugador.append(ArreglarValores(True, carta))

        puntJugador += int(jugador[-1][0])
        textoPuntJugador.configure(text=f"{puntJugador}/21")

        # Se ajusta el color y progreso de la barra de puntuación dependiendo de si el jugador superó los 21 puntos.
        if puntJugador <= 21:
            bordeBarraJugador.columnconfigure(0, weight=puntJugador)
            bordeBarraJugador.columnconfigure(1, weight=(21 - puntJugador))
        else:
            bordeBarraJugador.columnconfigure(0, weight=21)
            bordeBarraJugador.columnconfigure(1, weight=0)
            barraPuntJugador.configure(bg="red")
    else:
        # Se extrae una carta de la baraja, se agrega a la mano del crupier y se renderiza en la interfaz.
        carta = baraja.pop()
        crupier.append(carta)
        MostrarCarta(carta, False)

        # Si la carta es un As, Jota, Reina o Rey, se llama a la función ArreglarValores para ajustar
        # su valor antes de sumarlo a la puntuación del crupier.
        if carta[0] in "AJQK":
            crupier.pop()
            crupier.append(ArreglarValores(False, carta))

        puntCrupier += int(crupier[-1][0])

        # Si el jugador aún no se ha plantado, se oculta la puntuación total del crupier.
        # De lo contrario, se muestra su puntaje actual y se actualiza el estado de su barra de puntuación.
        if len(crupier) <= 2:
            textoPuntCrupier.configure(text=f"?/21")
            puntCrupierConocida = int(crupier[0][0])
            bordeBarraCrupier.columnconfigure(0, weight=puntCrupierConocida)
            bordeBarraCrupier.columnconfigure(1, weight=(21 - puntCrupierConocida))
            barraPuntCrupier.configure(bg="yellow")
        else:
            textoPuntCrupier.configure(text=f"{puntCrupier}/21")
            if puntCrupier <= 21:
                bordeBarraCrupier.columnconfigure(0, weight=puntCrupier)
                bordeBarraCrupier.columnconfigure(1, weight=(21 - puntCrupier))
                barraPuntCrupier.configure(bg="green")
            else:
                bordeBarraCrupier.columnconfigure(0, weight=21)
                bordeBarraCrupier.columnconfigure(1, weight=0)
                barraPuntCrupier.configure(bg="red")

# ╚═══════ ≪ ° </> ° ≫ ═══════╝

# ╔═══════ ≪ ° </> ° ≫ ═══════╗

def VerificarBlackjack() -> int:
    """
        Evalúa si el puntaje del crupier o del jugador es exactamente de 21 puntos.

        Returns:
            int: Devuelve `0` si nadie tiene 21 (el juego sigue), `1` si el crupier tiene 21,
            `2` si el jugador tiene 21, y `3` si ambos tienen 21 (empate).

        Examples:
            >>> puntJugador = 21
            >>> puntCrupier = 17
            >>> VerificarBlackjack()
            2
    """
    # Definición de variables globales.
    global puntJugador, puntCrupier

    # Se evalúa si hubo un empate por Blackjack natural, o victoria de alguna de las partes por la misma vía.
    # Si no ocurre ninguno de estos escenarios, se devuelve 0.
    if puntCrupier == 21 and puntJugador == 21:
        return 3
    elif puntJugador == 21:
        return 2
    elif puntCrupier == 21:
        return 1
    else:
        return 0

# ╚═══════ ≪ ° </> ° ≫ ═══════╝

# ╔═══════ ≪ ° </> ° ≫ ═══════╗

def VerificarSobrepuntaje() -> int:
    """
        Evalúa si el puntaje del crupier o del jugador superó los 21 puntos.

        Returns:
            int: Devuelve `0` si nadie se ha pasado, `1` si el crupier se pasó de 21,
            `2` si el jugador se pasó de 21.
    """
    # Definición de variables globales.
    global puntJugador, puntCrupier

    # Evalúa si el crupier o el jugador excedieron los 21 puntos. En caso contrario, se devuelve 0.
    if puntCrupier > 21:
        return 1
    elif puntJugador > 21:
        return 2
    return 0

# ╚═══════ ≪ ° </> ° ≫ ═══════╝

# ╔═══════ ≪ ° </> ° ≫ ═══════╗

def VerificarPuntajesFinales() -> int:
    """
        Evalúa el puntaje final del crupier y del jugador para determinar al ganador.

        Esta función asume que ninguno de los participantes se ha pasado de los 21 puntos.

        Returns:
            int: Devuelve `1` si el crupier ganó, `2` si el jugador ganó,
            y `3` si fue un empate.
    """
    # Definición de variables globales.
    global puntJugador, puntCrupier

    # Evalúa los puntajes finales válidos (menores o iguales a 21) para determinar al ganador o un posible empate.
    # Si no se cumple ninguna condición, se devuelve 0.
    if (puntJugador == puntCrupier) and (puntJugador <= 21 and puntCrupier <= 21):
        return 3
    elif (puntJugador > puntCrupier) and puntJugador <= 21:
        return 2
    elif (puntCrupier > puntJugador) and puntCrupier <= 21:
        return 1
    else:
        return 0

# ╚═══════ ≪ ° </> ° ≫ ═══════╝

# ╔═══════ ≪ ° </> ° ≫ ═══════╗

def ArreglarValores(esJugador: bool, carta: tuple) -> tuple:
    """
        Asigna el valor numérico correspondiente a una carta especial ("A", "J", "Q", "K").

        Si la carta es un As ("A"), evalúa si su valor debe ser 1 u 11, dependiendo de si
        la puntuación total superaría los 21 puntos.

        Parameters:
            esJugador (bool): `True` si se evalúa la carta del jugador, `False` si es del crupier.
            carta (tuple): Tupla que contiene la carta a evaluar.

        Returns:
            tuple: Nueva tupla con el valor numérico ajustado y el mismo palo.
    """
    # Evalúa si se está ajustando el valor para el jugador o para el crupier.
    if esJugador:
        # Si la carta es Jota, Reina o Rey, devuelve un valor numérico de 10.
        if carta[0] in "JQK":
            return (10,carta[1])
        # Si es un As, devuelve el valor que más le conviene al jugador (1 u 11) para evitar superar los 21 puntos.
        else:
            if 11 + puntJugador > 21:
                return (1,carta[1])
            else:
                return (11,carta[1])
    else:
        # Si la carta es Jota, Reina o Rey, devuelve un valor numérico de 10.
        if carta[0] in "JQK":
            return (10,carta[1])
        # Si es un As, devuelve el valor que más le conviene al crupier (1 u 11) para evitar superar los 21 puntos.
        else:
            if 11 + puntCrupier > 21:
                return (1,carta[1])
            else:
                return (11,carta[1])

# ╚═══════ ≪ ° </> ° ≫ ═══════╝

# ╔═══════ ≪ ° </> ° ≫ ═══════╗

def MostrarCarta(carta: tuple, esJugador: bool):
    """
        Genera y coloca gráficamente una carta en la interfaz (Tkinter).

        Si es la segunda carta del crupier en el turno inicial, se imprime boca abajo
        (oculta) hasta que sea el turno de revelarla.

        Parameters:
            carta (tuple): Tupla que representa la carta (valor, palo).
            esJugador (bool): `True` si la carta pertenece al jugador, `False` al crupier.

        Raises:
            TypeError: Si `carta` no es una tupla o `esJugador` no es un valor booleano.
            ValueError: Si el formato de la carta es inválido.
    """
    # Manejo de excepciones para validar los tipos de datos de entrada.
    if not isinstance(carta, tuple) or not isinstance(esJugador, bool):
        raise TypeError("El argumento 'carta' debe ser una tupla y el argumento 'esJugador' debe ser un valor booleano.")
    if not len(carta) == 2:
        raise ValueError("El argumento 'carta' debe tener 2 elementos dentro de la tupla.")
    if not 1 <= len(carta[0]) <= 2 or not carta[1] in PALOS:
        raise ValueError("El primer elemento del argumento 'carta' debe tener 1 o 2 caracteres, y el segundo elemento debe estar en la constante PALOS.")
    if len(carta[0]) == 2 and not carta[0] == "10":
        raise ValueError("El primer elemento del argumento 'carta' que tiene 2 caracteres debe ser la cadena '10'.")

    # Definición de variables globales.
    global crupier, jugador, segundaCartaCrupier

    # Asignación del valor y palo de la carta a variables locales.
    valor = carta[0]
    palo = carta[1]

    # Renderizado adaptado para cartas cuyo valor es de un solo carácter.
    if len(valor) == 1:
        textoCarta = (
            f"┌───────┐\n"
            f"│{valor}      │\n"
            f"│       │\n"
            f"│   {palo}   │\n"
            f"│       │\n"
            f"│      {valor}│\n"
            f"└───────┘"
        )
    # Renderizado adaptado para cartas cuyo valor es de dos caracteres.
    else:
        textoCarta = (
            f"┌───────┐\n"
            f"│{valor}     │\n"
            f"│       │\n"
            f"│   {palo}   │\n"
            f"│       │\n"
            f"│     {valor}│\n"
            f"└───────┘"
        )

    # Evalúa si la carta a mostrar pertenece al jugador o al crupier.
    if esJugador:
        # Renderiza y configura la carta del jugador de forma visible.
        dibujoCarta = tk.Label(marcoManoJugador, text=textoCarta, font=("Courier New", 11, "bold"), bg="white")
        dibujoCarta.grid(column=jugador.index(carta), row=0, sticky="w")
    else:
        # Determina si es la primera o la segunda carta del crupier.
        # La primera se muestra normalmente, mientras que la segunda se oculta temporalmente.
        if len(segundaCartaCrupier) != 0 and carta == segundaCartaCrupier[0]:
            dibujoCarta = tk.Label(marcoManoCrupier, text=textoCarta, font=("Courier New", 11, "bold"), bg="white")
            dibujoCarta.grid(column=4, row=0, sticky="e")
        else:
            if len(crupier) == 2 and crupier.index(carta) == 1:
                textoCarta = (
                    f"┌───────┐\n"
                    f"│ ▓▓▓▓▓ │\n"
                    f"│ ▓▓▓▓▓ │\n"
                    f"│ ▓▓▓▓▓ │\n"
                    f"│ ▓▓▓▓▓ │\n"
                    f"│ ▓▓▓▓▓ │\n"
                    f"└───────┘"
                )
                segundaCartaCrupier.append(carta)

            dibujoCarta = tk.Label(marcoManoCrupier, text=textoCarta, font=("Courier New", 11, "bold"), bg="white")
            if len(segundaCartaCrupier) != 0 and carta in segundaCartaCrupier:
                dibujoCarta.grid(column=4, row=0, sticky="e")
            else:
                columna_pos = 5 - (len(crupier) - 1)
                dibujoCarta.grid(column=columna_pos, row=0, sticky="e")

# ╚═══════ ≪ ° </> ° ≫ ═══════╝

# ╔═══════ ≪ ° </> ° ≫ ═══════╗

def MostrarFinJuego(estado: int):
    """
        Muestra la interfaz de final de partida.

        Despliega un menú superpuesto anunciando al ganador, desactiva los botones
        de acción y muestra las opciones de "REINICIAR" o "SALIR".

        Parameters:
            estado (int): Representa el resultado (1 = Gana crupier, 2 = Gana jugador, 3 = Empate).

        Raises:
            TypeError: Si el `estado` proporcionado no es un número entero.
            ValueError: Si el `estado` no está en el rango válido (1, 2, 3).
    """
    # Manejo de excepciones para validar que el estado sea válido.
    if not isinstance(estado, int):
        raise TypeError("El argumento 'estado' debe ser un número entero.")
    if not 1 <= estado <= 3:
        raise ValueError("El argumento 'estado' debe ser un número entero de 1 a 3.")

    # Se deshabilitan los botones de acción y se despliega el menú de fin de juego.
    botonPedir.config(state="disabled")
    botonPlantar.config(state="disabled")

    menu.place(width=app.winfo_width(), height=180, y=(app.winfo_height()-180))
    menu.rowconfigure((0, 1), weight=1)
    menu.columnconfigure(0, weight=1)

    # Evalúa el estado final para determinar si ganó el crupier, ganó el jugador o hubo empate.
    if estado == 1:
        textoEstado = "Gana CRUPIER!"
    elif estado == 2:
        textoEstado = "Gana JUGADOR!"
    else:
        textoEstado = "EMPATE!"

    # Renderiza el mensaje final y muestra los botones con las opciones de reiniciar la partida o salir del programa.
    textoMenu.config(text=textoEstado, font=("OCR A EXTENDED", 50, "bold"), bg="#58101b")
    textoMenu.grid(column=0, row=0, sticky="n", pady=(15, 0))

    botonInicio.config(text="REINICIAR", font=("Courier New", 20, "bold"), bg="green", command=InicioJuego)
    botonSalir.config(text="SALIR", font=("Courier New", 20, "bold"), bg="red", command=exit)

    botonInicio.grid(column=0, row=1, sticky="s", pady=(0,15), padx=(0, 200))
    botonSalir.grid(column=0, row=1, sticky="s", pady=(0,15), padx=(200, 0))

# ╚═══════ ≪ ° </> ° ≫ ═══════╝

# ================== Programa Principal ==================

if __name__ == "__main__":

    app = tk.Tk()
    app.title("BlackJack LCC")
    app.geometry("900x600")
    app.resizable(False, False)

    marcoPrincipal = tk.Frame(app, bg="pale green", highlightbackground="brown", highlightthickness=20)
    marcoPrincipal.pack(fill="both", expand=True)
    marcoPrincipal.rowconfigure(0, weight=4)
    marcoPrincipal.rowconfigure(1, weight=1)
    marcoPrincipal.columnconfigure(0, weight=1)

    marcoManos = tk.Frame(marcoPrincipal, bg="pale green")
    marcoManos.grid(row=0, column=0, sticky="nsew", padx=20, pady=(20, 10))
    marcoManos.rowconfigure(0, weight=1)
    marcoManos.rowconfigure(1, weight=1)
    marcoManos.columnconfigure(0, weight=1)

    marcoCrupier = tk.Frame(marcoManos, bg="pale green")
    marcoCrupier.grid(row=0, column=0, sticky="nsew", pady=(0, 5))
    marcoCrupier.columnconfigure(0, weight=1)
    marcoCrupier.columnconfigure(1, weight=3)
    marcoCrupier.rowconfigure(0, weight=1)

    marcoPuntCrupier = tk.Frame(marcoCrupier, bg="snow", highlightbackground="goldenrod3", highlightthickness=5)
    marcoPuntCrupier.grid(row=0, column=0, sticky="nsew", padx=(0, 10), pady=10)
    marcoPuntCrupier.rowconfigure((0, 1, 2), weight=1)
    marcoPuntCrupier.columnconfigure(0, weight=1)
    marcoPuntCrupier.grid_propagate(False)

    nombreCrupier = tk.Label(marcoPuntCrupier, text="CRUPIER", font=("Small Fonts", 20, "bold"), bg="snow")
    nombreCrupier.grid(row=0, column=0, sticky="n", pady=(15, 0))

    bordeBarraCrupier = tk.Frame(marcoPuntCrupier, bg="white", highlightbackground="black", highlightthickness=5, width=160, height=25)
    bordeBarraCrupier.grid(row=1, column=0, sticky="n", pady=(20,0))
    bordeBarraCrupier.columnconfigure(0, weight=0)
    bordeBarraCrupier.columnconfigure(1, weight=21)
    bordeBarraCrupier.rowconfigure(0, weight=1)
    bordeBarraCrupier.grid_propagate(False)

    barraPuntCrupier = tk.Frame(bordeBarraCrupier, bg="light green")
    barraPuntCrupier.grid(row=0, column=0, sticky="nsew")

    barraNoPuntCrupier = tk.Frame(bordeBarraCrupier, bg="white")
    barraNoPuntCrupier.grid(row=0, column=1, sticky="nsew")

    textoPuntCrupier = tk.Label(marcoPuntCrupier, text="0/21", font=("Small Fonts", 20), bg="snow")
    textoPuntCrupier.grid(row=2, column=0, sticky="sw", pady=10, padx=(15, 0))

    marcoManoCrupier = tk.Frame(marcoCrupier, bg="pale green")
    marcoManoCrupier.grid(row=0, column=1, sticky="nsew", padx=(10, 0), pady=20)
    marcoManoCrupier.grid_propagate(False)
    marcoManoCrupier.rowconfigure(0, weight=1)
    marcoManoCrupier.columnconfigure((0, 1, 2, 3, 4, 5), weight=1)

    marcoJugador = tk.Frame(marcoManos, bg="pale green")
    marcoJugador.grid(row=1, column=0, sticky="nsew", pady=(5, 0))
    marcoJugador.columnconfigure(0, weight=3)
    marcoJugador.columnconfigure(1, weight=1)
    marcoJugador.rowconfigure(0, weight=1)

    marcoManoJugador = tk.Frame(marcoJugador, bg="pale green")
    marcoManoJugador.grid(row=0, column=0, sticky="nsew", padx=(0, 10), pady=20)
    marcoManoJugador.grid_propagate(False)
    marcoManoJugador.rowconfigure(0, weight=1)
    marcoManoJugador.columnconfigure((0, 1, 2, 3, 4, 5), weight=1)

    marcoPuntJugador = tk.Frame(marcoJugador, bg="snow", highlightbackground="goldenrod3", highlightthickness=5)
    marcoPuntJugador.grid(row=0, column=1, sticky="nsew", padx=(10, 0), pady=10)
    marcoPuntJugador.rowconfigure((0, 1, 2), weight=1)
    marcoPuntJugador.columnconfigure(0, weight=1)
    marcoPuntJugador.grid_propagate(False)

    nombreJugador = tk.Label(marcoPuntJugador, text="JUGADOR", font=("Small Fonts", 20, "bold"), bg="snow")
    nombreJugador.grid(row=0, column=0, sticky="n", pady=(15, 0))

    bordeBarraJugador = tk.Frame(marcoPuntJugador, bg="white", highlightbackground="black", highlightthickness=5, width=160, height=25)
    bordeBarraJugador.grid(row=1, column=0, sticky="n", pady=(20,0))
    bordeBarraJugador.columnconfigure(0, weight=0)
    bordeBarraJugador.columnconfigure(1, weight=21)
    bordeBarraJugador.rowconfigure(0, weight=1)
    bordeBarraJugador.grid_propagate(False)

    barraPuntJugador = tk.Frame(bordeBarraJugador, bg="green")
    barraPuntJugador.grid(row=0, column=0, sticky="nsew")

    barraNoPuntJugador = tk.Frame(bordeBarraJugador, bg="white")
    barraNoPuntJugador.grid(row=0, column=1, sticky="nsew")

    textoPuntJugador = tk.Label(marcoPuntJugador, text="0/21", font=("Small Fonts", 20), bg="snow")
    textoPuntJugador.grid(row=2, column=0, sticky="se", pady=10, padx=(0, 15))

    marcoBotones = tk.Frame(marcoPrincipal, bg="pale green")
    marcoBotones.grid(row=1, column=0, sticky="nsew", padx=20, pady=(10, 20))
    marcoBotones.columnconfigure((0, 1), weight=1)
    marcoBotones.rowconfigure(0, weight=1)

    botonPedir = tk.Button(marcoBotones, text="Pedir", width=20, font=("Courier New", 16, "bold"), command=Pedir)
    botonPlantar = tk.Button(marcoBotones, text="Plantar", width=20, font=("Courier New", 16, "bold"), command=Plantarse)

    botonPedir.configure(bg="green", bd=5, relief=tk.RAISED, state="disabled")
    botonPlantar.configure(bg="indian red", bd=5, relief=tk.RAISED, state="disabled")

    botonPedir.grid(row=0, column=0, sticky="w", padx=(80, 0))
    botonPlantar.grid(row=0, column=1, sticky="e", padx=(0, 80))

    menu = tk.Frame(app, bg="#58101b", highlightbackground="gold", highlightthickness="10")
    menu.place(relwidth=app.winfo_width(), height=250, y=125)
    menu.rowconfigure((0,1), weight=1)
    menu.columnconfigure(0, weight=1)

    textoMenu = tk.Label(menu, text="BLACKJACK", font=("OCR A EXTENDED", 50, "bold"), bg="#58101b", fg="gold")
    textoMenu.grid(column=0, row=0, sticky="n", pady=(30, 0))

    botonInicio = tk.Button(menu, text="INICIAR", font=("Courier New", 20, "bold"), bg="green", command=InicioJuego)
    botonSalir = tk.Button(menu, text="SALIR", font=("Courier New", 20, "bold"), bg="red", command=exit)

    botonInicio.grid(column=0, row=1, sticky="s", pady=(0,30), padx=(0, 200))
    botonSalir.grid(column=0, row=1, sticky="s", pady=(0,30), padx=(200, 0))

    app.mainloop()