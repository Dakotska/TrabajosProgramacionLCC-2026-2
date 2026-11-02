def Curp(nombre : str, fecha : str, sexo : str, estado : str) -> str:
    """ 
    
        Ingresa nombre completo, fecha de nacimiento, sexo y estado de nacimiento para calcular su CURP.
    
        Parameters:

            nombre (str): Nombre completo de la persona.
            fecha (str): Fecha completa de nacimiento formato (yy-mm-dd)
            sexo (str): Genero de la persona (H/M).
            estado (str): Estado de nacimiento de la persona.

        Returns: 

            str: Devuelve una cadena con los 16 digitos de la CURP.

        Raises: 

            TypeError: Si las cadenas no son un string.

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

    