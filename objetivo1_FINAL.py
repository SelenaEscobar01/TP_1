def cifrar_mensaje(texto, desplazamiento):
    """
    Cifra un mensaje utilizando el cifrado de César.

    >>> cifrar_mensaje("hola mundo", 3)
    'krod pxqgr'
    >>> cifrar_mensaje("CASA", 2)
    'ECUC'
    >>> cifrar_mensaje("BIENVENIDOS", 4)
    'FMIRZIRMHSW'
    >>> cifrar_mensaje("argentina vota", 1)
    'bshfoujob wpub'
    >>> cifrar_mensaje("PASO", 2)
    'RCUQ'
    >>> cifrar_mensaje("este es un mensaje", 5)
    'jxyj jx zs rjsxfoj'
    >>> cifrar_mensaje("elecciones", 2)
    'gngeekqpgu'
    """
   
    cifrado = ""

    for i in texto:
        if i.isalpha():
            # Cifrar letras
            mayuscula = i.isupper()
            i = i.lower()
            desplazamiento_letra = (ord(i) - ord('a') + desplazamiento) % 26
            letra_cifrada = chr(ord('a') + desplazamiento_letra)
            if mayuscula:
                letra_cifrada = letra_cifrada.upper()
            cifrado += letra_cifrada
        elif i.isnumeric():
            # Cifrar dígitos numéricos
            d = int(i)
            d_cifrado = (d + desplazamiento) % 10
            cifrado += str(d_cifrado)
        else:
            # Mantener otros caracteres sin cifrar
            cifrado += i

    return cifrado

def mostrar_mensaje(texto_cifrado):
    return print("Mensaje cifrado: ", texto_cifrado)

def main():
    texto = input("Ingrese el mensaje que será cifrado: ")
    desplazamiento = int(input("valor del desplazamiento: "))
    texto_cifrado = cifrar_mensaje(texto, desplazamiento)
    mostrar_mensaje(texto_cifrado)

main()

# Pruebas con doctest
import doctest
print(doctest.testmod())
