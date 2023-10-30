import doctest

def descifrar_mensaje(texto,desplazamiento):
    """
    >>> descifrar_mensaje("hola mundo", 3)
    'krod pxqgr'
    >>> descifrar_mensaje("CASA", 2)
    'ECUC'
    >>> descifrar_mensaje("BIENVENIDOS", 4)
    'FMIRZIRMHSW'
    >>> descifrar_mensaje("argentina vota", 1)
    'bshfoujob wpub'
    >>> descifrar_mensaje("PASO", 2)
    'RCUQ'
    >>> descifrar_mensaje("este es un mensaje", 5)
    'jxyj jx zs rjsxfoj'
    >>> descifrar_mensaje("elecciones", 2)
    'gngeekqpgu'
 
    
    """
   
    if texto == texto.upper():
        #para las mayusculas
        abc="ABCDEFGHIJKLMNOPQRSTUVWXYZ" 
    else:
        #para las minusculas
        abc="abcdefghijklmnopqrstuvwxyz" 
    cifrado= ""
    
    for i in texto:
        if i in abc:
            cifrado += abc[(abc.index(i)+ desplazamiento)%(len(abc))]
        else:
            cifrado +=i
    return cifrado

def mostrar_mensaje(texto_revelado):
    
    return print("mensaje cifrado: ", texto_revelado)


def main():
    texto = input("mensaje: ")
   
        
    desplazamiento = int(input("valor del desplazamiento: "))
    texto_revelado= descifrar_mensaje(texto,desplazamiento)
    mostrar_mensaje(texto_revelado)


    
main()

#-----------pruebas con doctest ------------#

import doctest 

print(doctest.testmod())
