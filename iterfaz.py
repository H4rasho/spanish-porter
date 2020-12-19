from tkinter import*
from tkinter.filedialog import askopenfilename
import tkinter as tk
from tkinter import ttk
from stemming import *
import operator

class ventana:

    def __init__(self):  
        self.texto=""
        self.raiz = Tk()
        self.raiz.geometry('500x500')
        self.raiz.resizable(width=0, height=False)
        self.raiz.title('Aplicacion')
        self.bexaminar = ttk.Button(self.raiz, text='Examinar', command=self.examinar)
        self.bexaminar.place(x=210, y=400)
        self.bpoter = ttk.Button(self.raiz, text="Iniciar", command=self.porter)
        self.bpoter.place(x=210, y=300)
        self.resultado = tk.Text(self.raiz, height=10, width=50)
        self.resultado.place(x=40, y=100)
        self.raiz.mainloop()


    def examinar(self):  
        try:
            Tk().withdraw()
            filename = askopenfilename()
            archivo = open(filename, "r")
            self.texto = archivo.read()
        except:
            print("error")

    def porter(self):
        self.textotexto=borarBasura(self.texto)
        self.texto=eliminarTildes(self.texto)
        self.texto=eliminarPalabrasInrrelevantes(self.texto)
        self.texto=borrarArticulosYPronombres(self.texto)
        self.texto=borrarSufijos(self.texto)
        self.texto=borrarPrefijos(self.texto)
        self.listaPalabras = self.texto.split()
        self.masRepetidas()
    
    def masRepetidas(self):
        repeticiones = {}
        for palabra in self.listaPalabras:
            if palabra in repeticiones:
                repeticiones[palabra]+=1
            else:
                repeticiones[palabra]=1
        Top = sorted(repeticiones.items(), key=operator.itemgetter(1), reverse=True)
        texto="Lista de palabras ordendas por frecuencia\n"
        self.resultado.insert(tk.INSERT, texto)
        cont=1
        for palabra in enumerate(Top):
            
            texto = palabra[1][0], "con frecuencia", repeticiones[palabra[1][0]], "\n"
            print (texto)
            self.resultado.insert(tk.INSERT, texto)
            cont+=1 
        self.resultado.config(state="disabled")

new = ventana()
new.masRepetidas()