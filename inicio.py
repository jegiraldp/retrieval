import time
from analizar import *
from loadInicio import stopwords, leerDocumento
tiempo=0
############################-----inicia-----############################
print("\n\n------------- Super_Analizador T2018 -------------\n")
#######
print('Document Analysing...(in progress)')
stopw_list=stopwords()
documentText=leerDocumento()
time.sleep(tiempo)
print('Document Analysing...(done)')
##########
listSinStop=limpiarStopWords(documentText, stopw_list)
print('Cleaning stop-words...(in progress)')
time.sleep(tiempo)
print('Cleaning stop-words...(done)')
##########
listSinRepe=delRepetidos(listSinStop)
print('Cleaning duplicate-words...(in progress)')
time.sleep(tiempo)
print('Cleaning duplicate-words...(done)')
##########
listObj=listaObjetos(documentText)
listObjOccur=analizarOcurrencias(listObj)
print('Defining occurrences...(in progress)')
time.sleep(tiempo)
print('Defining occurrences...(done)')
##########
lf=ranking(listObjOccur,listSinRepe)
print('Ranking...(in progress)')
time.sleep(tiempo)
print('Ranking...(done)')
print ("\n*********************************\n")

for ll in lf:
    print (ll.nombre+":"+str(ll.cantidad))