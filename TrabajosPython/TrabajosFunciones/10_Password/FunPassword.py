def Segura(cadena : str) -> bool:
    """ 
    
        Ingresa una cadena de una contraseña y devuelve True si es una contraseña segura y False si no lo es.
    
        Parameters:

            cadena (str): cadena de caracteres cualesquiera de una contraseña.

        Returns: 

            bool: Devuelve True si la cadena es una contraseña segura y False si no lo es.

        Raises: 

            TypeError: Si la cadena no es un string.

        Examples: 

            >>> Segura("ABCDE")
            False
            >>> Segura("Hola@LCC26")
            True
            >>> Segura(26)
            Traceback (most recent call last):
            ...
            TypeError: El argumento cadena debe ser un string.

    """

    if not isinstance(cadena, str):
        raise TypeError("El argumento cadena debe ser un string.")

    minus = 0
    mayus = 0
    num = 0
    carEsp = "!@#$%^&*()_+-=[]{}|;:,.<>?/~`'\"\\ "
    esp = 0

    if len(cadena) < 5:
        return False
    
    for i in cadena:
        match i:
            case _ if i.islower():
                minus += 1
            case _ if i.isupper():
                mayus += 1
            case "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" | "0":
                num += 1
            case _ if i in carEsp:
                esp += 1

    return minus > 0 and mayus > 0 and num > 0 and esp > 0

print(Segura("abc"))
print(Segura("Abc1 "))
print(Segura("ABCDE"))
print(Segura("abcde1"))
print(Segura("Ab1!"))
print(Segura("Hola\\LCC26"))