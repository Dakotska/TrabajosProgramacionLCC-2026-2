def EsPar(n : int) -> bool:
    """ 
    
        Indica si un numero entero es par o no.
    
    
        Parameters: 
    
            n (int): Número entero que se desea saber si es par o no.
    
        Returns: 
    
            bool: True si n es par, False si no lo es.
    
    
        Raises: 
    
            TypeError: Si n no es un entero.
    
    
        Examples: 
    
            >>> EsPar(5) 
            False
            >>> EsPar(4) 
            True
            >>> EsPar(hola) 
            Traceback (most recent call last): 
            ... 
            TypeError: El argumento n debe ser entero. 
    """

    if not isinstance(n,int):
        raise TypeError("El argumento n debe ser entero")

    if n % 2 == 0:
        return True
    else:
        return False