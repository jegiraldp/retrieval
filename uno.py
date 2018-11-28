from docx import Document
from palabra import *
from analizar import analizarOcurrencias

###Captura texto
docu = Document('archivo.docx')
texto=""
for i in docu.paragraphs:
    texto+=i.text.lower()+" "
####

#### guarda palabras en list
words = texto.split()
lista = []
for w in words:
    lista.append(palabra(w,0,0))
####
analizarOcurrencias(lista)
########
"""print ('\n'+'Resultados del análisis\n+++++++++++++++++++++++')
for j in listaF:
    print (j.nombre+'-'+str(j.cantidad)+'-'+str(j.aparicion))
    """



