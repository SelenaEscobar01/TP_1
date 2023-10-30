def cifrado_atbash(cadena):
    """Convierte una cadena con cifrado atbash.
    Creada por: Maita Gustavo
    
    >>> cifrado_atbash("hola")
    SLOZ
    >>> cifrado_atbash("aaaa")
    ZZZZ
    >>> cifrado_atbash("bbbb")
    YYYY
    >>> cifrado_atbash("xxxx")
    CCCC
    >>> cifrado_atbash("AlgoRitmos1")
    zOTLiRGNLH8
    >>> cifrado_atbash("Esto es una Prueba 0")
    vHGL VH FMZ kIFVYZ 9
    >>> cifrado_atbash("Est0 Es Otr@ prueb@")
    vHG9 vH lGI@ KIFVY@
    >>> cifrado_atbash("Alumnos")
    zOFNMLH
    """

    invertido = ""
    
    for caracter in cadena:
        if 'A' <= caracter <= 'Z':
            invertido += chr(ord('Z') - (ord(caracter) - ord('A'))).lower()
            
        elif 'a' <= caracter <= 'z':
            invertido += chr(ord('z') - (ord(caracter) - ord('a'))).upper()
            
        elif "0" <= caracter <= "9":
            invertido +=chr(ord('9') - (ord(caracter) - ord('0')))
        else:
            invertido += caracter
    
    print (invertido)


import doctest
print(doctest.testmod())
        

