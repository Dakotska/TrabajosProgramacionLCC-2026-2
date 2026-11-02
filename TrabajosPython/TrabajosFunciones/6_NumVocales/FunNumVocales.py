def NumVocales(cadena : str) -> int:
    """ 
    
        Recibe una cadena de caracteres y devuelve el numero de vocales que contiene.
    
        Parameters:

            cadena (str): Registra una cadena de caracteres cualesquiera.

        Returns:

            int: Devuelve la cantidad de vocales que contiene la cadena.

        Raises:

            TypeError: Si el argumento cadena no es un str.

        Examples:

            >>> NumVocales("hola")
            2
            >>> NumVocales("hl")
            0
            >>> NumVocales(67)
            Traceback (most recent call last):
            ...
            TypeError: El argumento cadena debe ser un string.

    """

    if not isinstance(cadena, str):
        raise ValueError("El argumento cadena debe ser una cadena de caracteres cualesquiera.")

    lenFrase = len(cadena)
    frase = cadena.upper
    i = 0
    cantVocal = 0

    while i < lenFrase:
        match frase[i]:
            case "A" | "E" | "I" | "O" | "U" | "Á" | "É" | "Í" | "Ó" | "Ú" | "Ü":
                cantVocal += 1
        i += 1

    return cantVocal

print(NumVocales("hóla"))