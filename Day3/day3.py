import numpy
#esltra
#numero
def esnum(num):
    if num>="0" and num<="9":
        return True
    else:
        return False

def txt_list():
    archivo=open("lista3.txt","r")
    lista=[]
    for linea in archivo:
        lista.append(linea)
    archivo.close()
    return lista

def pasarMatric(lista):
    listart=[]
    for f in range(len(lista)):
        minlist=[]
        i=0
        for c in range(len(lista[f])):
            if lista[f][i]!="\n":
                minlist.append(int(lista[f][i]))
            i=i+1
        listart.append(minlist)
    return listart
def conv(bit): #convierte num a bit
    num=0
    i=0
    while bit>0:
        dec=bit%10
        bit=bit//10
        num=num+(dec*(2**i))
        i+=1
    return num
def compsac(lista,num,pos):
    f=0
    while f<len(lista):
        c=0
        band=0
        while c <len(lista[f]) and band==0:
            if c==pos-1 and lista[f][c]!=num: #llego hasta la pos
                band=1 #llego pero no cumple
            c+=1
        if band==1:
            lista.pop(f)
        else:
            f+=1
            
        
        
def bites():
    #transpuesta
    normlist=pasarMatric(txt_list()) #pasa string a matriz y a entero 
    lista=numpy.transpose(normlist)   #invierte matriz
    co2=normlist
    ox=pasarMatric(txt_list())
    f=0
    
    while f < (len(lista)) and len(co2)>1:
        #ve que nums se repiten mas
        cero=0
        uno=0
        for c in range(len(lista[f])):
            if lista[f][c]==1:
                uno=uno+1
            elif lista[f][c]==0:
                cero=cero+1   
        f=f+1
        if cero<uno:
            compsac(co2,1,f)
        elif uno<=cero:
            compsac(co2,0,f)
    print("oc2",co2[0])
    
    f1=0
    while f1 < len(lista) and len(ox)>1:
        cero1=0
        uno1=0
        for c1 in range(len(lista[f1])):
            if lista[f1][c1]==1:
                uno1=uno1+1
            elif lista[f1][c1]==0:
                cero1=cero1+1
        f1+=1
        if cero1<uno1:
            compsac(ox,0,f1)
        elif uno1<cero1:
            compsac(ox,1,f1)
    print("ox",ox[0])
    
            #combits=combits+"1"
            #menbit=menbit+"0"
'''if cero>uno:
            combits=combits+"0" #no me acuerdo como juntar binarios ahorita XD
            menbit=menbit+"1"
        elif uno>cero:
            combits=combits+"1"
            menbit=menbit+"0"
    print("comun bin de columanas es :",combits)
    combits=int(combits)        
    print(conv(combits))
    print("menos comun bin de columanas es :",menbit)
    menbit=int(menbit)
    print(conv(menbit))
    print("total: ",conv(menbit)*conv(combits))'''
    
bites()
                