def cifrar_atabash(lista_1):
    cifrado = []
    i = 0
    for i in range(len(lista_1)): 
        l= lista_1[i]
        i +=1
        numero = ord(l)
        valor = 122 - (numero-65)
        cifrado += chr(valor)
    s = cifrado.index('\x9b')
    cifrado[s]= " "
    return cifrado

def main():
    texto = input("mensaje: ")
    lista_1 = list(texto.lower())
    Str = cifrar_atabash(lista_1)
    Str = "".join(Str)
    if texto.isupper():
        print(Str.lower())
    else:
        print(Str)
    
main()
