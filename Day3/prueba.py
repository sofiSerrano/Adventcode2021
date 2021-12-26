'''def automion(num):
    suma=0
    for i in range(num+1):
        suma=suma+i
    return suma


def main():
    ing=int(input("ingresar num:"))
    print(automion(ing))
main()'''
 
'''   
def larga(string):
    lar=[]
    for i in range(len(string)):
        if string[i] not in lar:
            lar.append(string[i])
    return lar

def caracterComun(string):
    may=0
    lista=larga(string)
    let=""
    for i in range(len(lista)):
        cont=0
        for j in range(len(string)):
            if string[j]==string[i]:
                cont=cont+1
        if cont>may:
            may=cont
            let=lista[i]
    print("lest:",let,"num_",may)
caracterComun('llllllllloooadmfnnejsn')'''

def listaAgregar(string):
    lista=[]
    for i in range(len(string)):
        if string[i] not in lista:
            lista.append(string[i])
    return lista

def listaAgregar(string):
    lista=[]
    for i in range(len(string)):
        if string[i] not in lista:
            lista.append(string[i])
    return lista

'''def caracterMascomun(string):
    cmay=0
    lmay=string[0]
    listaletr=listaAgregar(string)
    for i in range(len(listaletr)):
        cont=0
        let=string[i]
        for j in range(len(string)):
            if string[j]==listaletr[i]:
                cont=cont+1
        if cont>=cmay:
            cmay=cont
            lmay=listaletr[i]
    print(lmay)
caracterMascomun('ferrocarril')
'''
def normalizar(string):
    pal=string.lower()
    return pal
    
def palindromo(string):
    band=0
    pal=normalizar(string)
    for i in range(len(pal)):
        if pal[i]!=pal[(len(pal)-1)-i]:
            band=1
    if band==0:
        print(True)
    else:
        print(False)
palindromo('anilina')