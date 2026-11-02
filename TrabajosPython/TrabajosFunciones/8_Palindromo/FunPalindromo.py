def Palindromo(cadena : str) -> bool:
    """ 
    
        Ingresa una cadena y devuelve True si es un palindromo y False si no lo es.
    
        Parameters:

            cadena (str): cadena de caracteres cualesquiera.

        Returns: 

            bool: Devuelve True si la cadena es un palindromo y False si no lo es.

        Raises: 

            TypeError: Si la cadena no es un string.

        Examples: 

            >>> CadenaInvertida("hola")
            aloh
            >>> CadenaInvertida("Alumno LCC")
            CCL onmulA
            >>> CadenaInvertida(26)
            Traceback (most recent call last):
            ...
            TypeError: El argumento cadena debe ser un string.

    """

    if not isinstance(cadena, str):
        raise TypeError("El argumento cadena debe ser un string.")

    cadenaSE = ""
    cadenaR = ""
    cadenita = cadena.lower()

    for i in cadenita:
        if i not in(" ", ",", "á", "é", "í", "ó", "ú", "ü"):
            cadenaSE += i
        elif i == "á":
            cadenaSE += "a"
        elif i == "é":
            cadenaSE += "e"
        elif i == "í":
            cadenaSE += "i"
        elif i == "ó":
            cadenaSE += "o"
        elif i == "ú" or i == "ü":
            cadenaSE += "u"
        else:
            cadenaSE += ""

    for j in range(len(cadenaSE), 0, -1):
        cadenaR += cadenaSE[j-1]

    if cadenaSE == cadenaR:
        return True
    else:
        return False

print(Palindromo("A mamá, Roma le aviva el amor a papá, y a papá, Roma le aviva el amor a mamá"))
print(Palindromo("dábale arroz a la zorra el abad"))
print(Palindromo("hola"))
# print(Palindromo(26))