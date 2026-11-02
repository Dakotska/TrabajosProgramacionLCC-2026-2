def AreaTriangulo(b : float, h : float) -> float:
    """ 
    
        Ingresa el valor de la base y altura de un triangulo para calcular su area.
    
        Parameters:

            b (int): Numero real positivo de la base de un triangulo.

            h (int): Numero real positivo de la altura de un triangulo.

        Returns: 

            float: Devuelve el area de un triangulo en un numero real positivo.

        Raises: 

            ValueError: Si b o h es un negativo.
            TypeError: Si b o h no es un real.

        Examples: 

            >>> AreaTriangulo(5, 10)
            25.0
            >>> AreaTriangulo(2.2, 20.25)
            22.275000000000002
            >>> AreaTriangulo(hola, asd)
            Traceback (most recent call last):
            ...
            TypeError: Los argumentos b y h deben ser reales.
            >>> AreaTriangulo(-20, 50)
            Traceback (most recent call last):
            ...
            ValueError: Ningún argumento debe ser negativo.
    """

    if not isinstance(b, (int,float)) or not isinstance(h, (int,float)):
        raise TypeError("Los argumentos b y h deben ser reales.")
    if b < 0 or h < 0:
        raise ValueError("Ningún argumento debe ser negativo.")

    return (b * h) / 2

print(AreaTriangulo(5,10))
print(AreaTriangulo(2.2, 20.25))
# print(AreaTriangulo(-20 , 7))
# print(AreaTriangulo("asd, hola"))