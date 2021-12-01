#DAY1
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
    archivo=open("lista.txt","r")
    lista=[]
    for linea in archivo:
        num=conv(linea)
        print(num)
        lista.append(num)
    archivo.close()
    return lista
        
def ame_increases(fnum,snum):
    if fnum>snum:
        return "d" #measurements are larger than the previous measurement
    else:
        return "i" #measurements are shorter than the previous measurement
    
def Arraymap():
    lista=txt_list()
    inc=0
    i=1
    print(lista[i],"none")
    while i<len(lista):
        meas=ame_increases(lista[i-1],lista[i])
        if meas=="d":
            print(lista[i],"(decreased)")
        if meas=="i":
            inc=inc+1
            print(lista[i],"(increased)")
        i+=1
        
    return inc

def main():
    rt=Arraymap()
    print("measurements are larger than the previous measurement: ",rt)

main()