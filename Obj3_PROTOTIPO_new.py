from tkinter import*
from tkinter import messagebox
def ventana_principal(): 
    raiz = Tk()
    raiz.iconbitmap("uba.ico")
    raiz.title("TP Grupal Parte 1 - Grupo: PROTOTIPO")
    raiz.resizable(0,0)
    raiz.config(bg="grey")

    miFrame = Frame(raiz,width=430, height=200,bg="grey")
    miFrame.pack()
    
    Label(miFrame, bg="grey", text = ("Construido por:\n Gustavo Alfredo Maita\n Agostina Armando\n Selena Escobar\n Guido Tiscornia\n")).place(x=140, y=95)
    Label(miFrame, text = ("Bienvenido a la aplicación de mensajes secretos del grupo PROTOTIPO.\n Para continuar presione continuar, de lo contrario cierre la ventana")).place(x=20,y=20)
    
    botonContinuar =Button(raiz,text="Continuar", command= lambda: ventana_continuar())
    botonContinuar.place(x=170 , y=65)
    
    raiz.mainloop()
   
def ventana_continuar():  
    raiz = Tk()
    raiz.iconbitmap("uba.ico")
    raiz.title("TP Grupal Parte 1 - Grupo: PROTOTIPO")
    miFrame = Frame(raiz,width=430, height=150)

    miFrame.pack()

    Label(raiz, text = ("Ingrese mensaje:")).place(x=20,y=20)
    cuadroUsuario = Entry(miFrame)
    cuadroUsuario.place(x=160, y=20)

    Label(miFrame, text = ("Clave:")).place(x=20,y=40)
    cuadroClave = Entry(miFrame)
    cuadroClave.place(x=160, y=40)
    cuadroClave.config()

    botonAgregar = Button(raiz,text="Cifrar mensaje\n César", command= lambda: cifrado_cesar(cuadroUsuario,cuadroClave))
    botonAgregar.place(x=8,y=62)

    botonAgregar = Button(raiz,text="Cifrar mensaje\n Atbash", command= lambda: cifrado_atbash(cuadroUsuario))
    botonAgregar.place(x=106,y=62)

    botonAgregar = Button(raiz,text="Descifrar mensaje\n César", command= lambda: cifrado_cesar(cuadroUsuario,cuadroClave))
    botonAgregar.place(x=206,y=62)

    botonAgregar = Button(raiz,text="Descifrar mensaje\n Atbash", command= lambda: cifrado_atbash(cuadroUsuario))
    botonAgregar.place(x=320,y=62)

    raiz.mainloop()


def cifrado_cesar(cuadroUsuario,cuadroClave):    
    texto = cuadroUsuario.get()
    clave = cuadroClave.get()
    if not texto or not clave: 
        messagebox.showwarning("", "Debe ingresar un mensaje y una clave")
    else:        
        desplazamiento = int(clave)
        cifrado=""    
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
            
    return messagebox.showinfo("El mensaje cifrado es:",cifrado )

def cifrado_atbash(cuadroUsuario):
    texto = cuadroUsuario.get()
    cifrado = []
    cifrado = list(texto) #conversion a lista para acceso a elementos
    contador = 0    
    if not texto: 
        messagebox.showwarning("", "Debe ingresar un mensaje")
    else:
        for contador in range(len(cifrado)): 
            elem = cifrado[contador] 
            if elem.isnumeric(): 
                cifrado[contador] = str(9 - int(elem))

            elif elem.isalpha(): 
                if elem.isupper():
                    minus = chr(90 - (ord(elem)-65)) #pasaje de letra mayuscula a minuscula
                    cifrado[contador] = minus.lower()
                else:
                    mayus = chr(122 - (ord(elem)-97)) #pasaje de letra minuscula a mayuscula
                    cifrado[contador] = mayus.upper()
            else:
                cifrado[contador] = elem  #el elemento no es caracter ni numero, se deja igual 
                contador +=1 #aumento del indice de la lista para acceder y reemplazar al elemento siguiente
        cifrado = "".join(cifrado)               
    return messagebox.showinfo("El mensaje cifrado es:",cifrado)

ventana_principal()

