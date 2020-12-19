from tkinter import*
from tkinter.filedialog import askopenfilename
import tkinter as tk
from tkinter import ttk
from stemming import *
from collections import Counter
class ventana:

    def __init__(self):  
        self.texto=""
        self.raiz = Tk()
        self.raiz.geometry('500x500')
        self.raiz.resizable(width=False, height=False)
        self.raiz.title('Aplicacion')
        self.bexaminar = ttk.Button(self.raiz, text='Examinar', command=self.examinar)
        self.bexaminar.place(x=210, y=400)
        self.bpoter = ttk.Button(self.raiz, text="Iniciar", command=self.porter)
        self.bpoter.place(x=210, y=300)
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
        self.frecuencia = Counter(self.listaPalabras)
        print(self.frecuencia)
 

new = ventana()
new.masRepetidas()