def cifrar_caracter(caracter):

    """
    >>> cifrado_atbash("Hello, World!")
    'sVOOL, dLIOW!' 
    >>> cifrado_atbash("12345")
    '87654'
    >>> cifrado_atbash("Python")
    'kBGSLM' 
    >>> cifrado_atbash("aBcD 1234")
    'ZyXw 8765'
    >>> cifrado_atbash("Test message with ! and ?")
    'gVHG NVHHZTV DRGS ! ZMW ?'
    >>> cifrado_atbash("The Quick Brown Fox 123")
    'gSV jFRXP yILDM uLC 876'
    >>> cifrado_atbash("This is a Test")
    'gSRH RH Z gVHG'
    >>> cifrado_atbash("9876543210")
    '0123456789'
    >>> cifrado_atbash("Hello, World! 123")
    'sVOOL, dLIOW! 876' 
    >>> cifrado_atbash("ABC xyz 789")
    'zyx CBA 210'
    """

    if caracter.islower():
        cifrado = chr(90 - (ord(caracter) - 97))
    elif caracter.isupper():
        cifrado = chr(122 - (ord(caracter) - 65))
    elif caracter.isnumeric():
        cifrado = str(9 - int(caracter))
    else:
        cifrado = caracter
    return cifrado


def cifrado_atbash(mensaje):
    mensaje_cifrado = ""
    for c in mensaje:
        mensaje_cifrado += cifrar_caracter(c)
    return mensaje_cifrado



def main():
    mensaje = input("Ingrese el mensaje a cifrar: ")
    mensaje_cifrado = cifrado_atbash(mensaje)
    print("Mensaje cifrado:", mensaje_cifrado)


main()

# Pruebas con doctest
import doctest
print(doctest.testmod())
