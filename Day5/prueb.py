listap=[[5, 2], [3, 9], [2, 8], [5, 5]]
p1=[5,5]
p2=[8,2]
def generarPuntos(p1,p2,listap):
    lista=[]
    listap.append(p1)
    lista.append(p1)
    lista.append(p2)
    listap.append(p2)
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
    if p1[0]==p2[1]:
        cont=cont+1
    if p1[1]==p2[1]:
        cont=cont+1
    elif cont==2:
        return 2
    return cont

def cuantasvecesSalio():
    lista=generarPuntos(p1,p2,listap)
    for i in range(len(lista)):
        punto=lista[i]
        cont=0
        for j in range(len(lista)):
            if compararPuntos(lista[i],lista[j])==2:
                cont=cont+1
        print("el punto {} se repite {} veces".format(lista[i],cont))
    
print("vemos cuantas veces salio cada uno: ")
#cuantasvecesSalio()
def imprimir():
    matrf=[]
    for f in range(10):
        matrc=[]
        for c in range(10):
            matrc.append(0)
            print("0",end=",")
        print("\n")
        matrf.append(matrc)
imprimir()
    
                    
        
    
    
    
    