def CadenaInvertida(cadena : str) -> str:
    """ 
    
        Ingresa una cadena y devuelve la misma cadena pero invertida.
    
        Parameters:

            cadena (str): cadena de caracteres cualesquiera.

        Returns: 

            str: Devuelve la cadena pero invertida.

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

    cadenaR = ""

    for j in range(len(cadena), 0, -1):
        cadenaR += cadena[j-1]

    return cadenaR

print(CadenaInvertida("hola"))
print(CadenaInvertida("Alumno LCC"))
# print(CadenaInvertida(26))