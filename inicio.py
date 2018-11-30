import time
from analizar import *
from loadInicio import stopwords, leerDocumento,getDocumento
tiempo=0
############################-----inicia-----############################
print("\n\n------------- Analizer T-2018 -------------\n")
#######
tinicio='init:'+str(time.ctime())
print('Document Analysing... -- ('+getDocumento()+') (in progress...)')
stopw_list=stopwords()
documentText=leerDocumento()
time.sleep(tiempo)
print('Document Analysing...'+':(words:'+str(len(documentText))+') -- no specials characters')
##########
listSinStop=limpiarStopWords(documentText, stopw_list)
time.sleep(tiempo)
print('Cleaning stop-words...')
##########
##########
print('Defining occurrences...')
listObj=listaObjetos(documentText)
listObjOccur=analizarOcurrencias(listObj)
time.sleep(tiempo)
###########
print('Cleaning duplicate-words...')
listSinRepe=delRepetidos(listSinStop)
time.sleep(tiempo)
##########
##########
print('Ranking...')
lf=ranking(listObjOccur,listSinRepe)
time.sleep(tiempo)

#####
print ('+++')
print (tinicio)
print ('end:'+str(time.ctime()))
print ("*************Resultados********************")
###
info=""
for ll in lf[:30]:
    info+=ll.nombre+":"+str(ll.cantidad)+"  "
print (info)