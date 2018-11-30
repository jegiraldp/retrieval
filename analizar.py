from palabra import *

def analizarOcurrencias(la_lista):
    la_lista2=la_lista
    for i in la_lista:
        for j in la_lista2:
            if(i.nombre==j.nombre):
                i.cantidad+=1
    return la_lista

def listaObjetos(listaTexto):
    listaObjetos=[]
    for i in listaTexto:
        listaObjetos.append(palabra(i,0))
    return listaObjetos

def limpiarStopWords(documentText,listaStop):
    listaSinStop=[]
    for w in documentText:
        if w not in listaStop:
            listaSinStop.append(w)
    return listaSinStop

def delRepetidos(listaTexto):
    listaSinRepetidos=[]
    for j in listaTexto:
        if j not in listaSinRepetidos:
            listaSinRepetidos.append(j)
    return listaSinRepetidos

def ranking(listObjOccur, listSinRepe):
    aux=[]
    for j in listSinRepe:
        aux.append(palabra(j,0))

    for jo in aux:
        for jor in listObjOccur:
            if jo.nombre==jor.nombre:
                jo.cantidad =jor.cantidad
    aux.sort(key=lambda x: x.cantidad, reverse=True)
    return aux