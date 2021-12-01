#DAY2
def esnum(num):
    if num>="0" and num<="9":
        return True
    else:
        return False
def conv(st):
    string=""
    i=0
    while esnum(st[i])==True:
        string=string+st[i]
        i=i+1
    num = int(string)
    return num

def txt_list():
    archivo=open("lista2.txt","r")
    lista=[]
    for linea in archivo:
        num=conv(linea)
        lista.append(num)
    archivo.close()
    return lista
        
def ame_increases(fnum,snum):
    if fnum>snum:
        return "d" #measurements are larger than the previous measurement
    elif fnum<snum:
        return "i" #measurements are shorter than the previous measurement
    else:
        return "n"

def compa(lista):
    i=0
    suma=0
    while i<len(lista):
        
        meas=ame_increases(lista[i-1],lista[i])
        if meas=="d":
            print(lista[i],"(menor)")
        if meas=="i":
            suma=suma+1
            print(lista[i],"(mayor)")
        i=i+1
    return suma

def Arraymap():
    lista=txt_list()
    i=0
    lista2=[]
    print(lista[i],"none")
    while i<len(lista):
        meas=ame_increases(lista[i-1],lista[i])
        if meas=="d":
            print(lista[i],"(decreased)")
        if meas=="i":
            print(lista[i],"(increased)")
        if meas=="n":
            print(lista[i],"(no change)")
        j=0
        suma=0
        while i<len(lista)-2 and j<3:
            suma=suma+lista[i+j]
            j=j+1
        if suma!=0:
            lista2.append(suma)
        i+=1
        
    rt=compa(lista2)
        
    return rt

def main():
    rt=Arraymap()
    print("measurements are larger than the previous measurement: ",rt)

main()