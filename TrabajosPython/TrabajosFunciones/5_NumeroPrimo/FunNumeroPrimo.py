from math import sqrt

def NumeroPrimo(num : int) -> bool:
    """ 
    
        Ingresa un numero entero mayor que 1 y devuelve si es primo o no.
    
        Parameters:

            num (int): Numero entero positivo mayor que 1.

        Returns: 

            bool: Devuelve si el numero es primo o no.

        Raises: 
            ValueError: Si el numero es menor o igual 1.
            TypeError: Si el num no es entero.

        Examples: 

            >>> NumPrimo(5)
            True
            >>> NumPrimo(3301)
            True
            >>> NumPrimo(4)
            False
            >>> NumPrimo("soy")
            Traceback (most recent call last):
            ...
            TypeError: El argumento num debe ser entero.
            >>> NumPrimo(4.2)
            Traceback (most recent call last):
            ...
            TypeError: El argumento num debe ser entero.
            >>> NumPrimo(1)
            Traceback (most recent call last):
            ...
            ValueError: Ningún argumento debe ser menor o igual a 1.
            >>> NumPrimo(-1)
            Traceback (most recent call last):
            ...
            ValueError: Ningún argumento debe ser menor o igual a 1.

    """

    if not isinstance(num, int):
        raise TypeError("El argumento num debe ser entero.")
    if num <= 1:
        raise ValueError("Ningún argumento debe ser menor o igual a 1.")

    Contador = 2
    raizNum = int(sqrt(num))

    while Contador <= raizNum:
        if num % Contador == 0:
            return False
        Contador += 1

    return True

print(NumeroPrimo(5))
print(NumeroPrimo(3301))
print(NumeroPrimo(4))
# print(NumeroPrimo(-25))
# print(NumeroPrimo("hola"))