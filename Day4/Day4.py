import numpy

#carga de archivo
archivoB="Bingo.txt"

def esnum(num):
    if num>="0" and num<="9":
        return True
    else:
        return False
def listnum(lista):
    listanum=[]
    i=0
    while len(lista)>i:
        string=""
        while len(lista)>i and esnum(lista[i])==True:
            string=string+lista[i]
            i=i+1
        if string!='\n' and len(string)>0:
            listanum.append(int(string))
                
        while len(lista)>i and esnum(lista[i])==False:
            i=i+1
    return listanum

def numerosBingo():
    archivo=open(archivoB,"r")
    lista=[]
    for linea in archivo:
        if linea=="\n":
            break 
        lista.append(linea)
    archivo.close()
    #paso los num de bingo a numeros
    lista=lista[0]
    listaNum=listnum(lista)
    return listaNum
            
def listBoard():
    archivo=open(archivoB,"r")
    lista=[]
    band=False
    for linea in archivo:
        if band==True and linea!="\n":
            lista.append(linea)
        if linea=="\n":
            band=True
    archivo.close()
    #archivocargado
    lista1=[]
    i=0
    while i<len(lista):
        cont=1
        listaMatr=[]
        while cont%6!=0:
            lista[i]=listnum(lista[i])
            listaMatr.append(lista[i])
            i=i+1
            cont=cont+1
        if len(listaMatr)>0:
            lista1.append(listaMatr)
    return lista1
#-------------------------------------------------------------------------------------------------------------------------------------------
#carga de archivo hasta aca
def buscarEnLista(lista,num):
    band=False
    i=0
    while i<len(lista) and band==False:
        if lista[i]==num:
            band=True
        i=i+1
    return band
    
def listabingo():
    listaBing=numerosBingo()
    listaBoard=listBoard()
    listaBoard2=listBoard()
    win=False
    winpos=0
    listaNum=[]#agregoNumerosqueSalen en bingo
    cant=4
    listaNum.append(listaBing[0])
    listaNum.append(listaBing[1])
    listaNum.append(listaBing[2])
    listaNum.append(listaBing[3])
    listaNum.append(listaBing[4])
    
    while win==False:
        if searchWinRow(listaBoard2,listaBing,cant)!="nada":
            win=True
            winpos=listaBing[cant]
            posBoard=searchWinRow(listaBoard2,listaBing,cant)
        elif searchWinColumn(listaBoard,listaBing,cant)!="nada":
            win=True
            winpos=listaBing[cant]
            posBoard=searchWinColumn(listaBoard,listaBing,cant)
        if cant!=4:
            listaNum.append(listaBing[cant])
        cant=cant+1
    #busco que num no salieron en la tabla
    suma=0
    winBoard=listaBoard[posBoard]
    
    for f in range(len(winBoard)):
        for c in range(len(winBoard[f])):
          if not winBoard[f][c] in listaNum:
              suma=suma+winBoard[f][c]
    total=suma*listaNum[-1]
    print("total es:",total)
        
def searchWinRow(boards,numeros,cant):
    band=False
    posWin="nada"
    for i in range(len(boards)):
        num=0
        for f in range(len(boards[i])):
            cont=0
            num=0
            for n in range(len(numeros)):
                if (numeros[n] in boards[i][f])==True:
                    cont=cont+1
                if n>=cant or cont==5:
                    break
            if cont==5:
                break
        if cont==5:
            band=True
            posWin=i
            break
    return posWin

                
def searchWinColumn(board,numeros,cant):
    
    band=False
    posWin="nada"
    for i in range(len(board)):
        board[i]=numpy.transpose(board[i])
        for f in range(len(board[i])):
            cont=0
            num=0
            for n in range(len(numeros)):
                if (numeros[n] in board[i][f])==True:
                    cont=cont+1
                if n>=cant or cont==5:
                    break
            '''while num<cant and (numeros[num] in boards[i][f])==True:
                cont=cont+1
                num=num+1
            while num<cant and (numeros[num] in boards[i][f])==False:
                num=num+1'''
            
        if cont>5:
            band=True
            posWin=i
    return posWin
    
listabingo()    