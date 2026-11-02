def NumMaximo(num1 : float, num2 : float, num3 : float) -> float:
    """ 
    
        Ingresa 3 números para encontrar el numero mas grande.
    
        Parameters:

            num1 (float): Primer numero real de un conjunto de 3 números.

            num2 (float): Segundo numero real de un conjunto de 3 números.

            num3 (float): Tercer numero real de un conjunto de 3 números.

        Returns: 

            float: Devuelve el numero mayor entre un conjunto de 3 números.

        Raises: 

            TypeError: Si num1, num2 o num3 no es un real.

        Examples: 

            >>> NumMaximo(1, 2, 3)
            3
            >>> NumMaximo(4, 2, 3)
            4
            >>> NumMaximo(4, 5, 3)
            5
            >>> NumMaximo("soy", "un", "string")
            Traceback (most recent call last):
            ...
            TypeError: Los argumentos num1, num2 y num3 deben ser números reales.
    """

    if not isinstance(num1, (int,float)) or not isinstance(num2, (int,float)) or not isinstance(num3, (int,float)):
        raise TypeError("Los argumentos num1, num2 y num3 deben ser números reales.")

    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num1 > num3:
        return num2
    else:
        return num3