"""
Nombre del archivo: GenioYFigura.py
Descripción del archivo: Según la selección del usuario, el programa imprimirá cierto tipo de figura ya sea rellena o hueca con una dimension y símbolo establecidos por el usuario.
Autor/es: Ángel Adrián Barragán Ruiz
Fecha: 03 de Noviembre del 2026
"""

# -----Funciones-----

def RelojArena(rellena : bool, dimension : int, simbolo : str) -> bool:
    """
        Dibuja un reloj de arena de forma llena o hueca en la consola.

        Parameters:

            rellena (bool): Indica si el reloj se dibuja lleno (True) o hueco (False).

            dimension (int): Dimensión del reloj, número entero impar entre 5 y 15.

            simbolo (str): Carácter individual con el que se dibuja el reloj.

        Returns:

            bool: Devuelve True si el reloj se dibujó correctamente.

        Raises:

            TypeError: Si rellena no es bool, dimension no es entero o simbolo no es str.

            ValueError: Si dimension no está entre 5 y 15 o es par, o si simbolo no tiene exactamente un carácter.

        Examples:

            >>> RelojArena(True, 5, "*")
            *****
             ***
              *
             ***
            *****
            True
            >>> RelojArena(False, 5, "*")
            *****
             * *
              *
             * *
            *****
            True
            >>> RelojArena(True, 4, "*")
            Traceback (most recent call last):
            ...
            ValueError: La dimensión no está en el rango impar permitido (5-15) o el símbolo no es de longitud 1.
    """

    if not isinstance(rellena, bool) or not isinstance(dimension, int) or not isinstance(simbolo, str):
        raise TypeError("Los tipos de datos de los argumentos no corresponden a los indicados.")

    if not (5 <= dimension <= 15 and dimension % 2 != 0) or len(simbolo) != 1:
        raise ValueError("La dimensión no está en el rango impar permitido (5-15) o el símbolo no es de longitud 1.")

    if rellena == True:
        for j in range(dimension, 0, -2):
            print(f"{j*simbolo:^{dimension}s}".rstrip())

        for i in range(3, dimension+2, 2):
            print(f"{i*simbolo:^{dimension}s}".rstrip())

        return True

    else:
        print(simbolo * dimension)

        for j in range(dimension - 2, 1, -2):
            espacios_izq = (dimension - j) // 2
            espacios_internos = j - 2
            print(" " * espacios_izq + simbolo + " " * espacios_internos + simbolo)

        if dimension % 2 != 0:
            espacios_izq = (dimension - 1) // 2
            print(" " * espacios_izq + simbolo)

        for i in range(3, dimension - 1, 2):
            espacios_izq = (dimension - i) // 2
            espacios_internos = i - 2
            print(" " * espacios_izq + simbolo + " " * espacios_internos + simbolo)

        print(simbolo * dimension)

        return True


def Rombo(rellena : bool, dimension : int, simbolo : str) -> bool:
    """
        Dibuja un rombo de forma llena o hueca en la consola.

        Parameters:

            rellena (bool): Indica si el rombo se dibuja lleno (True) o hueco (False).

            dimension (int): Dimensión del rombo, número entero impar entre 5 y 15.

            simbolo (str): Carácter individual con el que se dibuja el rombo.

        Returns:

            bool: Devuelve True si el rombo se dibujó correctamente.

        Raises:

            TypeError: Si rellena no es bool, dimension no es entero o simbolo no es str.

            ValueError: Si dimension no está entre 5 y 15 o es par, o si simbolo no tiene exactamente un carácter.

        Examples:

            >>> Rombo(True, 5, "*")
              *
             ***
            *****
             ***
              *
            True
            >>> Rombo(False, 5, "*")
              *
             * *
            *   *
             * *
              *
            True
            >>> Rombo(True, 4, "*")
            Traceback (most recent call last):
            ...
            ValueError: La dimensión no está en el rango impar permitido (5-15) o el símbolo no es de longitud 1.
    """

    if not isinstance(rellena, bool) or not isinstance(dimension, int) or not isinstance(simbolo, str):
        raise TypeError("Los tipos de datos de los argumentos no corresponden a los indicados.")

    if not (5 <= dimension <= 15 and dimension % 2 != 0) or len(simbolo) != 1:
        raise ValueError("La dimensión no está en el rango impar permitido (5-15) o el símbolo no es de longitud 1.")

    for ancho in range(1, dimension + 1, 2):
        if rellena:
            texto = simbolo * ancho
        elif ancho == 1:
            texto = simbolo
        else:
            texto = simbolo + " " * (ancho - 2) + simbolo

        print(f"{texto:^{dimension}s}".rstrip())

    for ancho in range(dimension - 2, 0, -2):
        if rellena:
            texto = simbolo * ancho
        elif ancho == 1:
            texto = simbolo
        else:
            texto = simbolo + " " * (ancho - 2) + simbolo

        print(f"{texto:^{dimension}s}".rstrip())

    return True


def Moño(rellena : bool, dimension : int, simbolo : str) -> bool:
    """
        Dibuja un moño de forma llena o hueca en la consola.

        Parameters:

            rellena (bool): Indica si el moño se dibuja lleno (True) o hueco (False).

            dimension (int): Dimensión del moño, número entero impar entre 5 y 15.

            simbolo (str): Carácter individual con el que se dibuja el moño.

        Returns:

            bool: Devuelve True si el moño se dibujó correctamente.

        Raises:

            TypeError: Si rellena no es bool, dimension no es entero o simbolo no es str.

            ValueError: Si dimension no está entre 5 y 15 o es par, o si simbolo no tiene exactamente un carácter.

        Examples:

            >>> Moño(True, 5, "*")
            *   *
            ** **
            *****
            ** **
            *   *
            True
            >>> Moño(False, 5, "*")
            *   *
            ** **
            * * *
            ** **
            *   *
            True
            >>> Moño(True, 4, "*")
            Traceback (most recent call last):
            ...
            ValueError: La dimensión no está en el rango impar permitido (5-15) o el símbolo no es de longitud 1.
    """

    if not isinstance(rellena, bool) or not isinstance(dimension, int) or not isinstance(simbolo, str):
        raise TypeError("Los tipos de datos de los argumentos no corresponden a los indicados.")

    if not (5 <= dimension <= 15 and dimension % 2 != 0) or len(simbolo) != 1:
        raise ValueError("La dimensión no está en el rango impar permitido (5-15) o el símbolo no es de longitud 1.")

    mitad = (dimension + 1) // 2

    for k in range(1, mitad):
        if rellena:
            lado = simbolo * k
        elif k == 1:
            lado = simbolo
        else:
            lado = simbolo + " " * (k - 2) + simbolo

        print(lado + " " * (dimension - 2 * k) + lado)

    if rellena:
        print(simbolo * dimension)
    else:
        print(simbolo + " " * (mitad - 2) + simbolo + " " * (mitad - 2) + simbolo)

    for k in range(mitad - 1, 0, -1):
        if rellena:
            lado = simbolo * k
        elif k == 1:
            lado = simbolo
        else:
            lado = simbolo + " " * (k - 2) + simbolo

        print(lado + " " * (dimension - 2 * k) + lado)

    return True


def Copa(rellena : bool, dimension : int, simbolo : str) -> bool:
    """
        Dibuja una copa de forma llena o hueca en la consola.

        Parameters:

            rellena (bool): Indica si la copa se dibuja llena (True) o hueca (False).

            dimension (int): Dimensión de la copa, número entero impar entre 5 y 15.

            simbolo (str): Carácter individual con el que se dibuja la copa.

        Returns:

            bool: Devuelve True si la copa se dibujó correctamente.

        Raises:

            TypeError: Si rellena no es bool, dimension no es entero o simbolo no es str.

            ValueError: Si dimension no está entre 5 y 15 o es par, o si simbolo no tiene exactamente un carácter.

        Examples:

            >>> Copa(True, 5, "*")
            *****
             ***
              *
              *
            *****
            True
            >>> Copa(False, 5, "*")
            *****
             * *
              *
              *
            *****
            True
            >>> Copa(True, 4, "*")
            Traceback (most recent call last):
            ...
            ValueError: La dimensión no está en el rango impar permitido (5-15) o el símbolo no es de longitud 1.
    """

    if not isinstance(rellena, bool) or not isinstance(dimension, int) or not isinstance(simbolo, str):
        raise TypeError("Los tipos de datos de los argumentos no corresponden a los indicados.")

    if not (5 <= dimension <= 15 and dimension % 2 != 0) or len(simbolo) != 1:
        raise ValueError("La dimensión no está en el rango impar permitido (5-15) o el símbolo no es de longitud 1.")

    print(simbolo * dimension)

    for ancho in range(dimension - 2, 2, -2):
        if rellena:
            texto = simbolo * ancho
        else:
            texto = simbolo + " " * (ancho - 2) + simbolo

        print(f"{texto:^{dimension}s}".rstrip())

    for _ in range((dimension - 1) // 2):
        print(f"{simbolo:^{dimension}s}".rstrip())

    print(simbolo * dimension)

    return True


# -----Programa Principal-----

## ---Menu Principal---
print("Bienvenido a la impresora de figuras!")
print("Elige del 1 al 5 que tipo de figura quieres imprimir")
print("")
print("-----Menu-----")
print("(0) Salir del programa")
print("(1) Reloj de Arena")
print("(2) Rombo")
print("(3) moño")
print("(4) Copa")
print("(5) Todas las figuras")
print("")

## ---Variables Principales---
"""
figura (int): Proporciona la selección del usuario.
rellena (bool): Proporciona si el usuario quiere la figura llena o hueca.
dimension (int): Proporciona la dimension elegida por el usuario desde 5 hasta 15 en numero impar.
simbolo (str): Proporciona el simbolo utilizado para la impresión de la figuras.
"""

## ---Variables Secundarias---
"""
rellenaAUX (str): Ayuda a conocer la respuesta del usuario para evaluarla en un match y proporcionar el valor de la variable rellena.
"""

## ---Solicitud de valores---

while True:
    # Pide la figura y repite hasta que escriba un número del 0 al 5
    while True:
        try:
            figura = int(input("Ingresa tu figura (0-5): "))
            if 0 <= figura <= 5:
                break
            print("Error: El número debe estar entre 0 y 5.\n")
        except ValueError:
            print("Error: Ingresa únicamente números enteros del 0 al 5.\n")

    # Opción 0: termina el programa
    if figura == 0:
        print("Gracias por usar este programa! :)")
        exit()

    # Las figuras 1 a 4 preguntan si se quieren llenas o huecas
    # La opción 5 no pregunta porque imprime todas llenas y luego todas huecas
    if figura != 5:
        while True:
            try:
                rellenaAUX = str(input("¿La quieres llena? (s/n): ")).strip().lower()
                match rellenaAUX:
                    case "s" | "si" | "sí" | "true" | "1":
                        rellena = True
                        break
                    case "n" | "no" | "false" | "0":
                        rellena = False
                        break
                    case _:
                        raise ValueError("Entrada no reconocida")
            except ValueError:
                print("Error: Ingresa una opción válida (s/n).\n")

    # Dimensión impar entre 5 y 15
    while True:
        try:
            dimension = int(input("Ingresa la dimensión de la figura en numero impar (5-15): "))
            if 5 <= dimension <= 15 and dimension % 2 != 0:
                break
            print("Error: La dimensión debe estar entre 5 y 15 en números impares.\n")
        except ValueError:
            print("Error: Debes ingresar un número entero válido (sin letras ni decimales).\n")

    # Símbolo de un solo carácter
    while True:
        try:
            simbolo = str(input("Ingresa el símbolo a utilizar (ej: * o @): ")).strip()
            if len(simbolo) != 1:
                raise ValueError("Debes ingresar exactamente UN solo carácter.")
            break
        except ValueError as error:
            print(f"Error: {error}\n")

    ## ---Impresión de resultados---

    match figura:
        case 1:
            if RelojArena(rellena, dimension, simbolo):
                print("")
        case 2:
            if Rombo(rellena, dimension, simbolo):
                print("")
        case 3:
            if Moño(rellena, dimension, simbolo):
                print("")
        case 4:
            if Copa(rellena, dimension, simbolo):
                print("")
        case 5:
            # Primero las 4 llenas, una debajo de otra
            if RelojArena(True, dimension, simbolo):
                print("")
            if Rombo(True, dimension, simbolo):
                print("")
            if Moño(True, dimension, simbolo):
                print("")
            if Copa(True, dimension, simbolo):
                print("")

            # Luego las 4 huecas, debajo de las llenas
            if RelojArena(False, dimension, simbolo):
                print("")
            if Rombo(False, dimension, simbolo):
                print("")
            if Moño(False, dimension, simbolo):
                print("")
            if Copa(False, dimension, simbolo):
                print("")