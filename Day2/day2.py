
def txt_list():
    archivo=open("lista3.txt","r")
    lista=[]
    for linea in archivo:
        num=List(linea)
        lista.append(num)
    archivo.close()
    return lista
#esltra
def esltra(l):
    if ("A"<=l and "Z">=l) or ("a"<=l and "z">=l):
        return True
    else:
        return False
#numero
def esnum(num):
    if num>="0" and num<="9":
        return True
    else:
        return False
def List(linea):
    lista=[]
    i=0
    while i<len(linea):
        string=""
        num=""
        while i<len(linea) and True==(esltra(linea[i])):
            string=string+linea[i]
            i=i+1
        if string!=" " and True!=(esnum(linea[i])):
            lista.append(string)
        while i<len(linea) and True==(esnum(linea[i])):
            num=num+linea[i]
            i+=1
        if esnum(num)==True:
            lista.append(int(num))
        i=i+1
    return lista
#parte1
'''def profun():
    lista=txt_list()
    hp=0# horizontal position
    d=0 # depth
    for i in range(len(lista)):
        if lista[i][0]=="forward":
            hp=hp+lista[i][1]
        elif lista[i][0]=="down":
            d=d+lista[i][1]
        elif lista[i][0]=="up":
            d=d-lista[i][1]
            
    print("depth:",d,"hp:",hp)
    print("val total: ",d*hp)'''
def profun():
    lista=txt_list()
    hp=0# horizontal position
    d=0 # depth
    aim=0
    for i in range(len(lista)):
        if lista[i][0]=="forward":
            hp=hp+lista[i][1]
            if aim!=0:
                d=d+(lista[i][1]*aim)

        elif lista[i][0]=="down":
            aim=aim+lista[i][1]
            
        elif lista[i][0]=="up":
            aim=aim-lista[i][1]
            
    print("depth:",d,"hp:",hp)
    print("val total: ",d*hp)
    
profun()
    