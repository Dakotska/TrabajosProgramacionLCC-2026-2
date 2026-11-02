def Factorial(n: int, mostrarPasos: bool = False) -> int: 

    """ 

    Calcula el factorial de un número entero no negativo. 


    Parameters: 

        n (int): Número entero no negativo cuyo factorial se desea calcular. 

        mostrarPasos (bool, opcional): Si es True, imprime los pasos intermedios del cálculo (por defecto False). 


    Returns: 


        int: El Factorial de n. 


    Raises: 

        ValueError: Si n es negativo. 

        TypeError: Si n no es un entero. 


    Examples: 

        >>> Factorial(5) 

        120 

        >>> Factorial(0) 

        1 

        >>> Factorial(-3) 

        Traceback (most recent call last): 

        ... 

        ValueError: El argumento n debe ser un entero no negativo 

        >>> Factorial(4, mostrarPasos=True)      # También puede ser: Factorial(4,True) 

        Paso 1: 1 

        Paso 2: 2 

        Paso 3: 6 

        Paso 4: 24 

        24 

        >>> Factorial(mostrarPasos=True , n=3) 

        Paso 1: 1 

        Paso 2: 2 

        Paso 3: 6 

        6 

    """ 

    if not isinstance(n, int): 

        raise TypeError("El argumento n debe ser un entero") 

    if n < 0: 

        raise ValueError("El argumento n debe ser un entero no negativo") 

    fact = 1 

    for i in range(1, n + 1): 

        fact *= i 

        if mostrarPasos: 

            print(f"Paso {i}: {fact}") 

    return fact

print(Factorial(5, True))