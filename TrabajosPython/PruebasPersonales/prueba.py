"""
Nombre del archivo: GenioYFigura.py
Descripción del archivo: Según la selección del usuario, el programa imprimirá cierto tipo de figura ya sea rellena o hueca con una dimension maxima establecida.
Autores: Ángel Adrián Barragán Ruiz y Khristo Ricardo Rodríguez Valencia
Fecha: 03 de Noviembre del 2026
"""

# -----Constantes-----

DIMENSION_MINIMA = 5
DIMENSION_MAXIMA = 15  # Con 15 como máximo, las figuras caben en una terminal de 80 columnas.

# -----Funciones auxiliares-----

def _validar_argumentos(rellena: bool, dimension: int, simbolo: str) -> None:
    """
    Revisa los argumentos de las figuras.

    Raises:
        TypeError: Si los tipos de datos no corresponden a los indicados.
        ValueError: Si la dimensión no es impar entre 5 y 15, o si el símbolo no es de longitud 1.
    """
    if (not isinstance(rellena, bool) or not isinstance(dimension, int)
            or isinstance(dimension, bool) or not isinstance(simbolo, str)):
        raise TypeError("Los tipos de datos de los argumentos no corresponden a los indicados.")
    if not (DIMENSION_MINIMA <= dimension <= DIMENSION_MAXIMA) or dimension % 2 == 0:
        raise ValueError("La dimensión debe ser un número impar entre 5 y 15.")
    if len(simbolo) != 1:
        raise ValueError("El símbolo debe tener longitud 1.")


def _rejilla_vacia(dimension: int) -> list:
    """Crea una rejilla cuadrada de dimension x dimension sin celdas marcadas."""
    return [[False] * dimension for _ in range(dimension)]


def _llenar_segmento(rejilla: list, fila: int, ancho: int) -> None:
    """Marca en la fila indicada una franja centrada de 'ancho' celdas."""
    inicio = (len(rejilla) - ancho) // 2
    for columna in range(inicio, inicio + ancho):
        rejilla[fila][columna] = True


def _es_borde(rejilla: list, fila: int, columna: int) -> bool:
    """Indica si una celda llena toca una celda vacía o queda en el borde de la rejilla."""
    for df, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        f, c = fila + df, columna + dc
        if not (0 <= f < len(rejilla) and 0 <= c < len(rejilla)) or not rejilla[f][c]:
            return True
    return False


def _lineas(rejilla: list, rellena: bool, simbolo: str) -> list:
    """Convierte la rejilla en texto. Si la figura es hueca, sólo se dibuja su contorno."""
    lineas = []
    for fila in range(len(rejilla)):
        linea = ""
        for columna in range(len(rejilla)):
            if rejilla[fila][columna] and (rellena or _es_borde(rejilla, fila, columna)):
                linea += simbolo
            else:
                linea += " "
        lineas.append(linea)
    return lineas


def _imprimir(rejilla: list, rellena: bool, simbolo: str) -> None:
    for linea in _lineas(rejilla, rellena, simbolo):
        print(linea.rstrip())


# -----Máscaras de cada figura-----

def _mascara_reloj_arena(dimension: int) -> list:
    rejilla = _rejilla_vacia(dimension)
    for fila in range(dimension):
        mitad = min(fila, dimension - 1 - fila)
        _llenar_segmento(rejilla, fila, dimension - 2 * mitad)
    return rejilla


def _mascara_rombo(dimension: int) -> list:
    rejilla = _rejilla_vacia(dimension)
    centro = (dimension - 1) // 2
    for fila in range(dimension):
        mitad = centro - abs(fila - centro)
        _llenar_segmento(rejilla, fila, 2 * mitad + 1)
    return rejilla


def _mascara_moño(dimension: int) -> list:
    rejilla = _rejilla_vacia(dimension)
    centro = (dimension - 1) // 2
    for fila in range(dimension):
        if fila == centro:
            _llenar_segmento(rejilla, fila, dimension)  # El nudo del moño
        else:
            ala = centro - abs(fila - centro) + 1
            for columna in range(ala):
                rejilla[fila][columna] = True
                rejilla[fila][dimension - 1 - columna] = True
    return rejilla


def _mascara_copa(dimension: int) -> list:
    rejilla = _rejilla_vacia(dimension)
    anchos = [dimension]                                                        # Borde superior
    anchos += [dimension - 2 * i for i in range(1, (dimension - 3) // 2 + 1)]  # Copa
    anchos += [1] * ((dimension - 1) // 2)                                      # Tallo
    anchos += [dimension]                                                       # Base
    for fila, ancho in enumerate(anchos):
        _llenar_segmento(rejilla, fila, ancho)
    return rejilla


# -----Figuras-----

def RelojArena(rellena: bool, dimension: int, simbolo: str) -> bool:
    """
    Dibuja un reloj de arena lleno o hueco en la consola.

    Parameters:
        rellena (bool): True para figura llena, False para hueca.
        dimension (int): Número impar entre 5 y 15.
        simbolo (str): Carácter individual con el que se imprime la figura.

    Examples:
        >>> RelojArena(True, 5, "*")
        *****
         ***
          *
         ***
        *****
        True
    """
    _validar_argumentos(rellena, dimension, simbolo)
    _imprimir(_mascara_reloj_arena(dimension), rellena, simbolo)
    return True


def Rombo(rellena: bool, dimension: int, simbolo: str) -> bool:
    """Dibuja un rombo lleno o hueco en la consola."""
    _validar_argumentos(rellena, dimension, simbolo)
    _imprimir(_mascara_rombo(dimension), rellena, simbolo)
    return True


def Moño(rellena: bool, dimension: int, simbolo: str) -> bool:
    """Dibuja un moño lleno o hueco en la consola."""
    _validar_argumentos(rellena, dimension, simbolo)
    _imprimir(_mascara_moño(dimension), rellena, simbolo)
    return True


def Copa(rellena: bool, dimension: int, simbolo: str) -> bool:
    """Dibuja una copa llena o hueca en la consola."""
    _validar_argumentos(rellena, dimension, simbolo)
    _imprimir(_mascara_copa(dimension), rellena, simbolo)
    return True


def TodasLasFiguras(rellena: bool, dimension: int, simbolo: str) -> bool:
    """Dibuja las cuatro figuras una al lado de la otra, todas llenas o todas huecas."""
    _validar_argumentos(rellena, dimension, simbolo)
    columnas = [
        _lineas(_mascara_reloj_arena(dimension), rellena, simbolo),
        _lineas(_mascara_rombo(dimension), rellena, simbolo),
        _lineas(_mascara_moño(dimension), rellena, simbolo),
        _lineas(_mascara_copa(dimension), rellena, simbolo),
    ]
    for fila in range(dimension):
        print("    ".join(columna[fila] for columna in columnas).rstrip())
    return True


# -----Menú y peticiones de datos-----

FIGURAS = {
    1: ("Reloj de Arena", RelojArena),
    2: ("Rombo", Rombo),
    3: ("Moño", Moño),
    4: ("Copa", Copa),
    5: ("Todas las figuras", TodasLasFiguras),
}


def MostrarMenu() -> None:
    print("Elige del 1 al 5 qué tipo de figura quieres imprimir")
    print("")
    print("-----Menu-----")
    print("(0) Salir del programa")
    for numero, (nombre, _) in FIGURAS.items():
        print(f"({numero}) {nombre}")
    print("")


def PedirFigura() -> int:
    while True:
        try:
            figura = int(input("Ingresa tu figura (0-5): "))
        except ValueError:
            print("Error: Ingresa únicamente números enteros del 0 al 5.\n")
            continue
        if 0 <= figura <= 5:
            return figura
        print("Error: El número debe estar entre 0 y 5.\n")


def PedirRellena() -> bool:
    while True:
        respuesta = input("¿La quieres llena? (s/n): ").strip().lower()
        if respuesta in ("s", "si", "sí", "true", "1"):
            return True
        if respuesta in ("n", "no", "false", "0"):
            return False
        print("Error: Ingresa una opción válida (s/n).\n")


def PedirDimension() -> int:
    while True:
        try:
            dimension = int(input(
                f"Ingresa la dimensión de la figura en número impar ({DIMENSION_MINIMA}-{DIMENSION_MAXIMA}): "
            ))
        except ValueError:
            print("Error: Debes ingresar un número entero válido (sin letras ni decimales).\n")
            continue
        if DIMENSION_MINIMA <= dimension <= DIMENSION_MAXIMA and dimension % 2 != 0:
            return dimension
        print(f"Error: La dimensión debe ser impar y estar entre {DIMENSION_MINIMA} y {DIMENSION_MAXIMA}.\n")


def PedirSimbolo() -> str:
    while True:
        simbolo = input("Ingresa el símbolo a utilizar (ej: * o @): ").strip()
        if len(simbolo) == 1:
            return simbolo
        print("Error: Debes ingresar exactamente UN solo carácter.\n")


# -----Programa principal-----

def main() -> None:
    print("Bienvenido a la impresora de figuras!")
    print("")
    while True:
        MostrarMenu()
        figura = PedirFigura()
        if figura == 0:
            print("Gracias por usar nuestro programa! :)")
            break

        rellena = PedirRellena()
        dimension = PedirDimension()
        simbolo = PedirSimbolo()

        print("")
        _, funcion = FIGURAS[figura]
        funcion(rellena, dimension, simbolo)
        print("")


if __name__ == "__main__":
    main()