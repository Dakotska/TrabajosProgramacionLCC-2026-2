def Grados(gradosF : float) -> float:
    """ 
    
        Ingresa grados farenheit y los convierte a celcius.
    
        Parameters:

            gradosF (float): Numero real que representa grados farenheit.

        Returns:

            float: Devuelve un numero real que representa grados celcius.

        Raises:

            TypeError: Si el num no es un numero real.

        Examples:

            >>> Grados(77)
            25
            >>> Grados(67.78)
            19.87
            >>> NumPrimo("soy")
            Traceback (most recent call last):
            ...
            TypeError: El argumento gradosF debe ser real.

    """

    if not isinstance(gradosF, (int, float)):
        raise ValueError("El argumento gradosF debe ser real.")

    return (gradosF - 32) * 5/9