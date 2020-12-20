#Algoritmo de porter en español
#Desarrollado por Thomas Sepúlveda Torres
#Fecha 19/12/2020

from tkinter import Tk, Scrollbar
from tkinter.filedialog import askopenfilename
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from stemming import *
import operator
import sys

class ventana:

    def __init__(self):  
        self.texto=""
        self.raiz = Tk()
        self.raiz.resizable(width=False, height=False)
        self.raiz.geometry('500x500')
        self.raiz.config(bg="#49A",bd=5,relief="groove")
        self.raiz.title('Porter')
        self.lsaludo = tk.Label(self.raiz, text="Bienvenido, porfavor examine un archivo txt", bg="#49A", font=("Arial", 15))
        self.lsaludo.pack()
        self.bexaminar = ttk.Button(self.raiz, text='Examinar', command=self.examinar)
        self.bexaminar.place(x=210, y=300)
        self.bpoter = ttk.Button(self.raiz, text="Obetner Resultados", command=self.porter)
        self.bpoter.place(x=190, y=400)
        self.bsalir = ttk.Button(self.raiz, text="SALIR")
        # Vertical (y) Scroll Bar
        self.scroll = Scrollbar(self.raiz)
        self.scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.resultado = tk.Text(self.raiz, height=10, width=50, wrap=None, yscrollcommand=self.scroll.set)
        self.resultado.place(x=40, y=100)
        self.scroll.config(command=self.resultado.yview)
        self.raiz.protocol("WM_DELETE_WINDOW", self.cerrar)
        self.raiz.mainloop()

    def examinar(self): 
        try:
            Tk().withdraw()
            filename = askopenfilename()
            archivo = open(filename, "r")
            self.texto = archivo.read()
        except:
            messagebox.showerror(message="El Arhivo selecionado no es formato txt, ingrese nuevamente", title="Error al selecionar archivo")

    def porter(self): #limpia el texto y extrae la raiz de la palabra
        self.texto=borarBasura(self.texto)
        self.texto=eliminarTildes(self.texto)
        self.texto=eliminarPalabrasInrrelevantes(self.texto)
        self.texto=borrarArticulosYPronombres(self.texto)
        self.texto=borrarSufijos(self.texto)
        self.texto=borrarPrefijos(self.texto)
        self.listaPalabras = self.texto.split()
        self.masRepetidas()
    
    def masRepetidas(self):
        repeticiones = {} #diccionario que guadra la cantidad de veces que se repite una palabra
        for palabra in self.listaPalabras:
            if palabra in repeticiones:
                repeticiones[palabra]+=1
            else:
                repeticiones[palabra]=1
        Top = sorted(repeticiones.items(), key=operator.itemgetter(1), reverse=True) #lista que contiene las repeticiones guardadas
        texto="Lista de palabras ordendas por frecuencia\n"
        self.resultado.insert(tk.INSERT, texto)
        cont=1
        for palabra in enumerate(Top):
            texto = palabra[1][0], "con frecuencia", repeticiones[palabra[1][0]], "\n"
            self.resultado.insert(tk.INSERT, texto)
            cont+=1 
        self.resultado.config(state="disabled")
    
    def cerrar(self): 
        sys.exit()

if __name__ == "__main__":
    app = ventana()
