import numpy

archiv="prueb.txt"

def esnum(num):
    if num>="0" and num<="9":
        return True
    else:
        return False

#guarda las coordenadas en un array ([x1,y1],[x2,y2])
def coordenadasArray(linea):
    lista=[]
    p1=[]
    p2=[]
    x1=0
    x2=0
    j=0
    i=0
    y1=0
    y2=0
    while i<len(linea):
        num=""
        y1=0
        y2=0
        while esnum(linea[i])!=False:
            num=num+linea[i]
            i=i+1
        
        #p1
        if len(num)!=0 and j==0:
            num=int(num)
            x1=num
            j=j+1
            p1.append(x1)
        elif len(num)!=0 and j==1:
            num=int(num)
            y1=num
            j=j+1
            p1.append(y1)
            #print("punto1: ",p1)
            lista.append(p1)
        #p2
        elif len(num)!=0 and j==2:
            num=int(num)
            x2=num
            j=j+1
            p2.append(x2)
        elif len(num)!=0 and j==3:
            num=int(num)
            y2=num
            j=j+1
            p2.append(y2)
            #print("punto2: ",p2)
            lista.append(p2)
        i=i+1
    return lista
            
def SegmentArray():
    archivo=open(archiv,"r")
    listaSeg=[] #se guardan desde tal segmento a tal seg
    for linea in archivo:
        seg=[]
        seg=coordenadasArray(linea)
        #print("segmento: ",seg)
        listaSeg.append(seg)
    return listaSeg

#busca punto x max
def pxmax(listaseg):
    mayx=listaseg[0][0][0]
    for seg in range(len(listaseg)):
        punto=listaseg[seg]
        for punt in range(len(punto)):
            num=listaseg[seg][punt][0]
            if num>mayx:
                mayx=num
    print(mayx)
    return mayx

#busca punto y maximo
def pymax(listaseg):
    mayy=listaseg[0][0][1]
    for seg in range(len(listaseg)):
        punto=listaseg[seg]
        for punt in range(len(punto)):
            num=listaseg[seg][punt][1]
            if num>mayy:
                mayy=num
    return mayy

'------------------------------------------------------------------------'
#en esta parte genera los puntos y  muestras cuantas veces salia
def generarPuntos(p1,p2,listap):
    lista=[]
    listap.append(p1)
    lista.append(p1)
    lista.append(p2)
    listap.append(p2)
    print("punto:",p1)
    print("punto:",p2)
    mayx=p2[0]
    menx=p1[0]
    if p1[0]>p2[0]:
        mayx=p1[0]
        menx=p2[0]
    
    mayy=p2[1]
    meny=p1[1]
    if p1[1]>p2[1]:
        mayy=p1[1]
        meny=p2[1]
    rtx=mayx-menx #cant de px que faltan 2
    rty=mayy-meny#cant de py que faltan 0
    #encontrpuntomen en donde va a empeza a contar
    pini=p2
    pfin=p1
    if abs(p1[0]-p1[1])<abs(p2[0]-p2[1]):
        pini=p1
        pfin=p2
    dist=((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)**(1/2)
    i=0
    ptx=pini[0]
    pty=pini[1]
    xcont=0
    ycont=0
    #averigua si x de punto inicial < o may que el final
    bandx="men"
    bandy="men"
    if pini[0]>pfin[0]:
        bandx="may"
    if pini[1]>pfin[1]:
        bandy="may"
        
    while i<dist:
        punt=[]
        if xcont<rtx:
            if bandx=="men":
                ptx=ptx+1
            else:
                ptx=ptx-1
            xcont=xcont+1
        punt.append(ptx)
        if ycont<rty:
            if bandy=="men":
                pty=pty+1
            else:
                pty=pty-1
            ycont=ycont+1
        punt.append(pty)
        
        if not punt in lista:
            listap.append(punt)
            lista.append(punt)
            print("punto:",punt)
        i=i+1
    return listap


def compararPuntos(p1,p2):
    cont=0
    if p1[0]==p2[0]:
        cont=cont+1
    if p1[1]==p2[1]:
        cont=cont+1
    elif cont==2:
        return True
    return False

def cuantasvecesSalio(listacomp,punto):
    #me cuenta cuantas veces salio num en la listade Punts
    '''for i in range(len(lista)):
        punto=lista[i]
        cont=0
        for j in range(len(lista)):
            if compararPuntos(lista[i],lista[j])==True: #son iguales
                cont=cont+1'''
        #print("el punto {} se repite {} veces".format(lista[i],cont))
    cont=0
    for i in range(len(listacomp)):
        if  compararPuntos(listacomp[i],punto)==True:
            cont=cont+1
    return cont
'------------------------------------------------------------------------'

def diagram():
    listaseg=SegmentArray()
    print("punto x may es :", pxmax(listaseg))
    print("punto y may es :", pymax(listaseg))
    #imprecion de diagram de 0
    xmax=pxmax(listaseg)
    ymax=pymax(listaseg)
    matrf=[]
    for f in range(ymax):
        matrc=[]
        for c in range(xmax):
            matrc.append(".")
        print(matrc)
        matrf.append(matrc)
    
    print('---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    #junta en una lista todos los puntos intermedios
    listaPunts=[]
    for i in range(len(listaseg)):
        p1=listaseg[i][0]
        p2=listaseg[i][1]
        listaPunts=generarPuntos(p1,p2,listaPunts)
        print("-------------------------------")
    #los analizo en la matriz de 0
    for f1 in range(len(matrf)):
        for c1 in range(len(matrf[f1])):
            punto=[c1,f1]#posicion de puntos
            if punto in listaPunts:
                cont=cuantasvecesSalio(listaPunts,punto)
                if cont>0:
                    matrf[f1][c1]=str(cont)
            print(matrf[f1][c1],end=", ")
        print("\n")
    
diagram()