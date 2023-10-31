def cifrar_atbash(texto):
    mensaje = texto
    lista_1 = list(mensaje.lower())
    cifrado = []
    i = 0
    for i in range(len(lista_1)): 
        l= lista_1[i]
        i +=1
        if l.isnumeric():            
            numero = 9 - int(l)
            cifrado += str(numero)            
        else: 
            numero = ord(l)
            valor = 122 - (numero-65)
            cifrado += chr(valor)
    if '\x9b' in cifrado:  
        s = cifrado.index('\x9b')
        cifrado[s]= " "
    else:
        cifrado
        
    cifrado = "".join(cifrado)
    if texto.isupper():   
        Str = cifrado.lower()
    else:
        Str = cifrado
    Str = mostrar_texto(Str, texto)
    
    return Str


def mostrar_texto(Str, texto):
    j = 0
    last=[]
    for j in range(len(Str)):
        if texto[j].isupper():
            l = Str[j]
            last.append(l.lower())
        else:
            l = Str[j]
            last.append(l)
        j += 1
 
        
    mensaje_final = "".join(last)   
    return(mensaje_final)
