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
        minlist=[]
        for num in range(len(linea)):
            if linea[num]!="\n":
                print(int(linea[num]),end=" ")
                minlist.append((linea[num]))
        lista.append(lista)
    archivo.close()
    return lista

def bits():
    #transpuesta
    lista=txt_list()
    print(lista)
    cont=0
    f=0
    c=0
    while f < (len(lista)) :
        #ve que nums se repiten mas
        for c in range(len(lista[f])):
            print(lista[f][c],end=" ")
        print("\n")
        f=f+1
bits()
               
    #pasar a decimal
'''num=0
    i=0
    while bit>0:
        dec=bit%10
        bit=bit//10
        num=num+(dec*(2**i))
        i+=1
    print(num)'''
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
                