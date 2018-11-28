
def analizarOcurrencias(la_lista):
    la_lista2=la_lista
    for i in range(len(la_lista)):
        for j in range(len(la_lista2)):
            if la_lista[i].nombre==la_lista2[j].nombre:
                la_lista[i].cantidad+=1
                #print(la_lista[i].nombre+"--"+str(la_lista[i].cantidad))
    print (la_lista[0].nombre+"--"+str(la_lista[0].cantidad))