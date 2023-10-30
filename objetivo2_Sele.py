#objetivo 2 ---- cifrado atbash

import doctest

def cifrar_Atbash(texto):
    """
    >>> cifrar_Atbash("hola mundo")
    SLOZ ÑFNWL
    >>> cifrar_Atbash("HOLA MUNDO")
    sloz ñfnwl
    
    """    
    
    original = "abcdefghijklmnñopqrstuvwxyz"
    clave = "ZYXWVUTSRQPOÑNMLKJIHGFEDCBA"
    cifrado = ""
    lower = texto.lower()
    for i in lower:
        if i in original:
                cifrado += clave[original.index(i)]
        else:
                cifrado +=i
    if texto.isupper():
        print(cifrado.lower())
    else:
        print(cifrado)     
           

def main():
    texto = input("mensaje: ")
    cifrar_Atbash(texto)
main()


#-----------pruebas con doctest ------------#

import doctest 

print(doctest.testmod())


