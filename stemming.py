#aqui estan las funciones que limpiaran el texto y extraearn la raiz
from libreria import *
import re, string

def borarBasura(texto):
    texto=re.sub('[%s]' % re.escape(string.punctuation), ' ', texto)
    texto=re.sub(SIMBOLOS,"",texto)
    texto=re.sub(DIGITOS,"",texto)
    BASURA=ESPACIO+"[a-z][a-z]?"+ESPACIO
    re.sub(BASURA,"",texto)
    texto=re.sub("\\b[a-z]{1,3}\\b","",texto)
    texto=re.sub(" * "," ",texto) #espacios consecutivos
    return texto

def eliminarTildes(texto):
    texto=re.sub(TILDE_A, "a", texto)
    texto=re.sub(TILDE_E, "e", texto)
    texto=re.sub(TILDE_I, "i", texto)
    texto=re.sub(TILDE_O, "o", texto)
    texto=re.sub(TILDE_U, "u", texto)
    return texto
def eliminarPalabrasInrrelevantes(texto):
    INRRELEVANTES=ESPACIO+"que|del|por"+ESPACIO
    texto=re.sub(INRRELEVANTES,"",texto)
    return texto

def borrarPrefijos(texto):
    texto = re.sub(PREFIJO1, "", texto)
    texto = re.sub(PREFIJO2, "", texto)
    texto = re.sub(PREFIJO3, "", texto)
    texto = re.sub(PREFIJO4, "", texto)
    texto = re.sub(PREFIJO5, "", texto)
    texto = re.sub(PREFIJO6, "", texto)
    texto = re.sub(PREFIJO7, "", texto)
    texto = re.sub(PREFIJO8, "", texto)
    texto = re.sub(PREFIJO9, "", texto)
    texto = re.sub(PREFIJO10, "", texto)
    texto = re.sub(PREFIJO11, "", texto)
    texto = re.sub(PREFIJO12, "", texto)
    texto = re.sub(PREFIJO13, "", texto)
    texto = re.sub(PREFIJO14, "", texto)
    return texto

def borrarSufijos(texto):
    #adjetivos
    texto= re.sub(ADJETIVO1,"",texto)
    texto= re.sub(ADJETIVO2,"",texto)
    texto= re.sub(ADJETIVO3,"",texto)
    texto= re.sub(ADJETIVO4,"",texto)
    texto= re.sub(ADJETIVO5,"",texto)
    texto= re.sub(ADJETIVO6,"",texto)
    texto= re.sub(ADJETIVO7,"",texto)
    texto= re.sub(ADJETIVO8,"",texto)
    texto= re.sub(ADJETIVO9,"",texto)
    texto= re.sub(ADJETIVO10,"",texto)
    texto= re.sub(ADJETIVO11,"",texto)
    #sustativos
    texto=re.sub(SUSTANTIVO1,"",texto)
    texto=re.sub(SUSTANTIVO2,"",texto)
    texto=re.sub(SUSTANTIVO3,"",texto)
    texto=re.sub(SUSTANTIVO4,"",texto)
    texto=re.sub(SUSTANTIVO5,"",texto)
    texto=re.sub(SUSTANTIVO6,"",texto)
    texto=re.sub(SUSTANTIVO7,"",texto)
    texto=re.sub(SUSTANTIVO8,"",texto)
    texto=re.sub(SUSTANTIVO9,"",texto)
    texto=re.sub(SUSTANTIVO10,"",texto)
    texto=re.sub(SUSTANTIVO11,"",texto)
    #aumentativos
    texto=re.sub(AUMENTATIVO1,"",texto)
    texto=re.sub(AUMENTATIVO2,"",texto)
    texto=re.sub(AUMENTATIVO3,"",texto)
    #disminutivos
    texto=re.sub(DISMINUTIVO1,"",texto)
    texto=re.sub(DISMINUTIVO2,"",texto)
    texto=re.sub(DISMINUTIVO3,"",texto)
    #despetivos
    texto=re.sub(DESPECTIVO1,"",texto)
    texto=re.sub(DESPECTIVO2,"",texto)
    texto=re.sub(DESPECTIVO3,"",texto)
    texto=re.sub(DESPECTIVO4,"",texto)
    texto=re.sub(DESPECTIVO5,"",texto)
    #verbo1
    texto=re.sub(VERBO1,"",texto)
    texto=re.sub(VERBO2,"",texto)
    texto=re.sub(VERBO3,"",texto)
    return texto

def borrarArticulosYPronombres(texto):
    #articulos
    texto=re.sub(ARTICULO1,"",texto)
    texto=re.sub(ARTICULO2,"",texto)
    texto=re.sub(ARTICULO3,"",texto)
    texto=re.sub(ARTICULO4,"",texto)
    texto=re.sub(ARTICULO5,"",texto)
    texto=re.sub(ARTICULO6,"",texto)
    texto=re.sub(ARTICULO7,"",texto)
    #pronombres
    texto=re.sub(PRONOMBRE1,"",texto)
    texto=re.sub(PRONOMBRE2,"",texto)
    texto=re.sub(PRONOMBRE3,"",texto)
    texto=re.sub(PRONOMBRE4,"",texto)
    texto=re.sub(PRONOMBRE5,"",texto)
    texto=re.sub(PRONOMBRE6,"",texto)
    texto=re.sub(PRONOMBRE7,"",texto)
    texto=re.sub(PRONOMBRE8,"",texto)
    texto=re.sub(PRONOMBRE9,"",texto)
    texto=re.sub(PRONOMBRE10,"",texto)
    texto=re.sub(PRONOMBRE11,"",texto)
    texto=re.sub(PRONOMBRE12,"",texto)
    texto=re.sub(PRONOMBRE13,"",texto)
    texto=re.sub(PRONOMBRE14,"",texto)
    texto=re.sub(PRONOMBRE15,"",texto)
    texto=re.sub(PRONOMBRE16,"",texto)
    texto=re.sub(PRONOMBRE17,"",texto)
    texto=re.sub(PRONOMBRE18,"",texto)
    texto=re.sub(PRONOMBRE19,"",texto)
    texto=re.sub(PRONOMBRE20,"",texto)
    texto=re.sub(PRONOMBRE21,"",texto)
    texto=re.sub(PRONOMBRE22,"",texto)
    texto=re.sub(PRONOMBRE23,"",texto)
    texto=re.sub(PRONOMBRE24,"",texto)
    texto=re.sub(PRONOMBRE25,"",texto)
    texto=re.sub(PRONOMBRE26,"",texto)
    texto=re.sub(PRONOMBRE27,"",texto)
    texto=re.sub(PRONOMBRE28,"",texto)
    texto=re.sub(PRONOMBRE29,"",texto)
    texto=re.sub(PRONOMBRE30,"",texto)
    texto=re.sub(PRONOMBRE31,"",texto)
    texto=re.sub(PRONOMBRE32,"",texto)
    texto=re.sub(PRONOMBRE33,"",texto)
    texto=re.sub(PRONOMBRE34,"",texto)
    texto=re.sub(PRONOMBRE35,"",texto)
    texto=re.sub(PRONOMBRE36,"",texto)
    texto=re.sub(PRONOMBRE37,"",texto)
    texto=re.sub(PRONOMBRE38,"",texto)
    texto=re.sub(PRONOMBRE40,"",texto)
    return texto



