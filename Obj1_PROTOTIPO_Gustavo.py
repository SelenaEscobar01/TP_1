def cifrado_cesar(cadena,clave):

    """Esta funcion recibe una cadena y la convierte en cifrado césar con la clave
    indicada.
    Creada por: Maita Gustavo"""

    valor2=""

    for caracter in cadena:
        if ord(caracter) == 90 or ord(caracter) == 122:
            valor = ord(caracter) + clave -26

        elif ord(caracter) == 65 or ord(caracter) == 97:
            valor = ord(caracter) + clave +26
            
        elif ord(caracter) == 57:
            valor = ord(caracter) + clave -10
            
        elif ord(caracter) == 32:
            valor= ord(caracter)
            
        else:
            valor = ord(caracter) + clave
            
        valor2+=chr(valor)
            
        
        
    return (valor2)
        
        
