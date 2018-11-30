from docx import Document

def stopwords():
    f = open('archivos/stopwords.txt','r')
    txt = f.read()
    words = []
    for i in txt:
        words = txt.split("\n")
    return words

def leerDocumento():
    docu = Document('archivos/capitulo.docx')
    texto = ""
    words=[]

    for i in docu.paragraphs:
        texto += i.text.lower() + " "
        texto=especiales(texto)
        words=texto.split()
    return words

def especiales(texto):
    texto=texto.replace('(','')
    texto = texto.replace(')', '')
    texto = texto.replace('+', '')
    texto = texto.replace('-', '')
    texto = texto.replace('*', '')
    texto = texto.replace('%', '')
    texto = texto.replace('#', '')
    texto = texto.replace('$', '')
    texto = texto.replace('\&', '')
    texto = texto.replace('?', '')
    texto = texto.replace('¿', '')
    texto = texto.replace(';', '')
    texto = texto.replace(',', '')
    texto = texto.replace('~', '')
    texto = texto.replace('{','')
    texto = texto.replace('}','')
    texto = texto.replace('[','')
    texto = texto.replace(']','')
    return texto