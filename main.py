from stemming import *
texto="extragrande supergrande hiperlocura antifacista, a s d canción televisión. %##$$/"

texto=borarBasura(texto)
texto=eliminarTildes(texto)
texto=eliminarPalabrasInrrelevantes(texto)
texto=borrarArticulosYPronombres(texto)
texto=borrarSufijos(texto)
texto=borrarPrefijos(texto)


print(texto)
