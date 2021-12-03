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
def conv(bit):
    num=0
    i=0
    while bit>0:
        dec=bit%10
        bit=bit//10
        num=num+(dec*(2**i))
        i+=1
    return num
def bites():
    #transpuesta
    txtlist=pasarMatric(txt_list()) #pasa string a matriz y a entero 
    lista=numpy.transpose(txtlist)    
    cont=0
    f=0
    combits=""
    menbit=""
    while f < (len(lista)) :
        #ve que nums se repiten mas
        cero=0
        uno=0
        for c in range(len(lista[f])):
            if lista[f][c]==1:
                uno=uno+1
            elif lista[f][c]==0:
                cero=cero+1   
        f=f+1
        if cero>uno:
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
    print("total: ",conv(menbit)*conv(combits))
    
bites()
'''def main(bit):
    num=0
    i=0
    while bit>0:
        dec=bit%10
        bit=bit//10
        num=num+(dec*(2**i))
        i+=1
    print(num)
main(10011011)'''
                