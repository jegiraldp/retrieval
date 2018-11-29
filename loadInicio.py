from docx import Document

def stopwords():
    f = open('archivos/stopwords.txt','r')
    txt = f.read()
    words = []
    for i in txt:
        words = txt.split("\n")
    return words

def leerDocumento():
    docu = Document('archivos/archivo.docx')
    texto = ""
    words=[]
    lista=[]

    for i in docu.paragraphs:
        texto += i.text.lower() + " "
        words=texto.split()
    return words